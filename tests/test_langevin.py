#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for ` package."""
import numpy as np
import unittest
import pytest
from langevin import *
import scipy.stats as ss
import random

class Testworkshop(unittest.TestCase):

    def test_dragForce(self):
        '''
        unit test for drag force calculator
        '''
        dampingCoef = 0.1
        velocity = 10
        result = dragForce(dampingCoef,velocity)
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
            randomForce = randomForceGenerator(temperature,dampingCoef)
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
            self.assertTrue(checkWall(randomPosition))
        randomPosition = random.random()*(-5)
        if randomPosition != 0:
            self.assertTrue(checkWall(randomPosition))
        self.assertFalse(checkWall(-5))
        self.assertFalse(checkWall(5))
        self.assertFalse(checkWall(9))
        self.assertFalse(checkWall(-10))
     
    def test_initialStatus(self):
        defaultCase = status(0,0,300,0.1,0.1,1000)
        self.assertEquals(defaultCase.initial_position,0)
        self.assertEquals(defaultCase.initial_velocity,0)
        self.assertEquals(defaultCase.temperature,300)
        self.assertEquals(defaultCase.damping_coefficient,0.1)
        self.assertEquals(defaultCase.time_step,0.1)
        self.assertEquals(defaultCase.total_time,1000)
if __name__ == '__main__':
    unittest.main()