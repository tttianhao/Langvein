# -*- coding: utf-8 -*-

"""Main module."""

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

class status:

    '''This class initialize the initial status of the particle'''

    def __init__(self,position,velocity, temperature, dampingCoef,timeStep,totalTime,mass=1):
        self.postion = position
        self.velocity = velocity
        self.temperature = temperature
        self.dampingCoef = dampingCoef
        self.timeStep = timeStep
        self.totalTime = totalTime
        self.mass = mass

def dragForce(dampingCoef,velocity):
    '''
    This function calculates drage force from given damping coefficient and velocity

    Args:
        dampingCoef: damping coefficient gamma
        velocity: velocity at a certain time
    
    returns:
        drag force (frictional force)
    '''

    return -dampingCoef*velocity



def randomForceGenerator(temperature,dampingCoef,kB =1,delta=1):

    '''
    This function generate a random number from a normal distribution, whose mean is zero and variance is determined by 'variance' function.

    returns:
        Xi: the random force at a certain instance
    '''

    mu = 0
    var = 2*temperature*dampingCoef*kB*delta
    sigma = np.sqrt(var)
    Xi = np.random.normal(mu,sigma)
    return Xi

class langvein:
    def __init__(self):
        pass

def main(status):
    xi = randomForceGenerator(status.temperature,status.dampingCoef)
    print('The random force Xi is {}'.format(xi))


if __name__ == '__main__':
    testCase = status(2,1,298,1,2,60)
    main(testCase)
