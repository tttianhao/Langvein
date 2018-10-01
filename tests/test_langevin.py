#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for ` package."""
import numpy as np
import unittest
import pytest
import langevin.langevin as langevin
import langevin 
import langevin.langevin
import langevin.langevin as langevin
import scipy.stats as ss
import random
import matplotlib
matplotlib.use('Agg')

class Testworkshop(unittest.TestCase):

    def test_dragForce(self):
        '''
        unit test for drag force calculator
        '''
        dampingCoef = 0.1
        velocity = 10
        result = langevin.dragForce(dampingCoef,velocity)
        self.assertEquals(result,-1)


    def test_randomForceGenerator(self):
        '''
        unit test for random force generator

        generate random force for 2000 times and perform statistical test on the resulting array
        '''
        randomForces = []
        temperature = 298
        dampingCoef = 0.1
        for i in range(5000):
            randomForce = langevin.randomForceGenerator(temperature,dampingCoef)
            randomForces.append(randomForce)
        _ , pValue = ss.shapiro(randomForces)
        mean = np.mean(randomForces)
        var = np.var(randomForces)
        #perform shapiro-wilk test and see if p value is greater or equal to 0.05 which indicates the array is possiblity from normal distribution
        self.assertLessEqual(0.05,pValue)
        #test if the mean is almost equal to 0
        self.assertTrue(mean<= 0.5 or mean >= -0.5)
        #test if the variance is almost equal to the expected variance (with 5% difference)
        self.assertTrue(var>=2*temperature*dampingCoef*(.95) or var<=2*temperature*dampingCoef*(1.05))
    
    def test_checkwall(self):
        '''
        unit test for checkwall function with different edge case
        '''
        randomPosition = random.random()*5
        if randomPosition != 0:
            self.assertTrue(langevin.checkWall(randomPosition))
        randomPosition = random.random()*(-5)
        if randomPosition != 0:
            self.assertTrue(langevin.checkWall(randomPosition))
        self.assertFalse(langevin.checkWall(-5))
        self.assertFalse(langevin.checkWall(5))
        self.assertFalse(langevin.checkWall(9))
        self.assertFalse(langevin.checkWall(-10))
     
    def test_initialStatus(self):
        defaultCase = langevin.status(0,0,300,0.1,0.1,1000)
        self.assertEquals(defaultCase.initial_position,0)
        self.assertEquals(defaultCase.initial_velocity,0)
        self.assertEquals(defaultCase.temperature,300)
        self.assertEquals(defaultCase.damping_coefficient,0.1)
        self.assertEquals(defaultCase.time_step,0.1)
        self.assertEquals(defaultCase.total_time,1000)

    def test_euler(self):
        initialposition = random.random()*5
        initialVelocity = random.random()*5
        time_step = random.random()
        total_time = random.random()*999+1
        damping_coefficient = random.random()
        temperature = random.random()*1000
        time,velocity,position = langevin.eulerIntegration(initialposition,time_step,total_time,initialVelocity,damping_coefficient,temperature)
        self.assertEquals(len(time),len(position))
        self.assertEquals(len(time),len(velocity))
        self.assertLessEqual(len(time),int(total_time/time_step+1))
        self.assertEquals(time[0],0)
        self.assertEquals(velocity[0],initialVelocity)
        self.assertEquals(position[0],initialposition)
        self.assertLessEqual(position[-2],5)
        self.assertLessEqual(-5,position[-2])

    def test_outPut(self):
        time = np.zeros(5)
        position = np.zeros(5)
        velocity = np.zeros(5)
        langevin.outPut(time,position,velocity)
        with open('Langvein_dynamics_output.txt') as f:
            first_line = f.readline()
            self.assertEquals(first_line,'index  time  position  velocity \n')

    def test_main(self):
        defaultCase = langevin.status(0,0,300,0.1,0.1,1000)
        langevin.main(defaultCase)
        with open('Langvein_dynamics_output.txt') as f:
            first_line = f.readline()
            self.assertEquals(first_line,'index  time  position  velocity \n')


if __name__ == '__main__':
    unittest.main()