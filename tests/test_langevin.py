#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for langevin package."""
import numpy as np
import unittest
import pytest
import langevin.langevin as langevin
import scipy.stats as ss
import random
import matplotlib
import os
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
        self.assertTrue(langevin.checkWall(randomPosition))
        self.assertFalse(langevin.checkWall(0))
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
        '''
        test for euler integration output is valid array with reasonable position, time and velocity
        '''
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
        self.assertLessEqual(position[-1],5)
        self.assertLessEqual(0,position[-1])

    def test_outPut(self):
        '''
        test output function and assert if a text file is being created
        '''
        time = np.zeros(5)
        position = np.zeros(5)
        velocity = np.zeros(5)
        langevin.outPut(time,position,velocity)
        with open('Langvein_dynamics_output.txt') as f:
            first_line = f.readline()
            self.assertEquals(first_line,'index  time  position  velocity \n')

    def test_Parser(self):
        '''
        test parser function and assert if a value can be passed in
        '''
        args = langevin.getParser()
        self.assertEquals(args.initial_position,0)
        self.assertEquals(args.temperature,298)

    def test_figure(self):
        '''
        test figure function and assert if figures are being created
        '''
        timeWall = [0,0,1,2,3,4]
        time = np.linspace(0,10,11)
        position = np.linspace(0,10,11)
        langevin.figure(timeWall,time,position)
        self.assertTrue(os.path.isfile('histogram.png'))
        self.assertTrue(os.path.isfile('trajectory.png'))

    def test_checkInput(self):
        '''
        unit test for check input function
        '''
        valid = langevin.status(0,0,300,0.1,0.1,1000)
        self.assertFalse(langevin.checkInput(valid))

        arg1 = langevin.status(10,0,300,0.1,0.1,1000)
        self.assertTrue(langevin.checkInput(arg1))
        arg2 = langevin.status(0,0,-10,0.1,0.1,1000)
        self.assertTrue(langevin.checkInput(arg2))
        arg3 = langevin.status(0,0,300,-10,0.1,1000)
        self.assertTrue(langevin.checkInput(arg3))
        arg4 = langevin.status(0,0,300,0.1,-10,1000)
        self.assertTrue(langevin.checkInput(arg4))
        arg5 = langevin.status(0,0,300,0.1,0.1,-10)
        self.assertTrue(langevin.checkInput(arg5))

    def test_secondLargest(self):
        '''
        test secondLargest function and assert if the output is desired output
        '''
        list1 = [1,5,3,2,43,6,2]
        self.assertEquals(langevin.secondLargest(list1,43),6)
        list1 = [1,1,1,1,1,1,1]
        self.assertEquals(langevin.secondLargest(list1,1),1)
        list3 = [2,2,2,10]
        self.assertEquals(langevin.secondLargest(list3,10),2)

    def test_main(self):
        '''
        test main function and assert a file is createdß
        '''
        #defaultCase = langevin.status(0,0,300,0.1,0.1,1000)
        langevin.main()
        with open('Langvein_dynamics_output.txt') as f:
            first_line = f.readline()
            self.assertEquals(first_line,'index  time  position  velocity \n')


if __name__ == '__main__':
    unittest.main()