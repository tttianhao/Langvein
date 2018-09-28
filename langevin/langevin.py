# -*- coding: utf-8 -*-

"""Main module."""

import numpy as np
import scipy.stats as ss

class initial:
    '''This class initialize the initial status of the particle'''
    def __init__(self,position,velocity, temperature, dampingCoef,timeStep,totalTime):
        self.postion = position
        self.velocity = velocity
        self.temperature = temperature
        self.dampingCoef = dampingCoef
        self.timeStep = timeStep
        self.totalTime = totalTime

class dragForce:
    def __init__(self):
        pass

class randomForce:
    @staticmethod
    def variance(temperature,dampingCoef,kB=1,delta=1):

        '''
        This function calculates the variance of random force

        Args: 
            temperature: float
            dampingCoef: float
            kB = 1
            delta = 1
        
        return: 
            variance of the normal distribution
        '''

        var = 2*temperature*dampingCoef*kB*delta
        return var

    @staticmethod
    def randomForceGenerator(temperature,dampingCoef):

        '''
        This function generate a random number from a normal distribution, whose mean is zero and variance is determined by 'variance' function.

        returns:
            Xi: the random force at a certain instance
        '''

        mu = 0
        sigma = np.sqrt(randomForce.variance(temperature,dampingCoef))
        Xi = np.random.normal(mu,sigma)
        return Xi

class langvein:
    def __init__(self):
        pass

def main(initial):
    xi = randomForce.randomForceGenerator(initial.temperature,initial.dampingCoef)
    print('The random force Xi is {}'.format(xi))

if __name__ == '__main__':
    testCase = initial(2,1,298,1,2,60)
    main(testCase)
