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
    # draw a random number from a normal distribution with mean=0 and std=sqrt(var)
    Xi = np.random.normal(mu,sigma)
    return Xi

def eulerIntegration(timeStep,totalTime,initialVelocity,dampingCoef,temperature):
    '''
    This function uses euler method to calculate

    Args:
        timeStep: the time interval between two times
        totalTime: the total runtime of the integration
        initialVelocity: the input velocity at t=0
        dampingCoef: damping coefficient
        temperature: the input temperature
    
    returns:
        time: time profile 
        velocity: velocity at time t
        accerlation: the derivative of velocity at time t
    '''
    n = totalTime/timeStep+1
    time = np.linspace(0,totalTime,n)
    #initialize velocity and accerlation
    velocity = np.zeros(n)
    accerlation = np.zeros(n)
    #set initial velocity and accerlation
    velocity[0] = initialVelocity
    accerlation[0] = accerlationCalculator(dampingCoef,velocity[0],temperature)
    for i in range(1,n):
        randomForce = randomForceGenerator(temperature,dampingCoef)
        #apply euler equation to estimate y(i) from y(i-1)
        #equation used is : y_i = dx(f(y_i-1,x_i-1)) + y_i-1
        velocity[i] = timeStep*(dragForce(dampingCoef,velocity[i-1])+randomForce)+velocity[i-1]
        accerlation[i] = accerlationCalculator(dampingCoef,velocity[i-1],temperature)
    return time,velocity,accerlation

def accerlationCalculator(dampingCoef,velocity,temperature):
    accerlation = dragForce(dampingCoef,velocity)+randomForceGenerator(temperature,dampingCoef)
    return accerlation

def checkWall(position):
    '''
    This function checks if the position of the particle is still in the two walls
    
    returns:
        true if particle in the wall and false if not.
    '''

    if position > 0 and position < 5:
        return True
    else:
        return False

def main(status):
    xi = randomForceGenerator(status.temperature,status.dampingCoef)
    print('The random force Xi is {}'.format(xi))
    time,velocity,accerlation = eulerIntegration(status.timeStep,status.totalTime,status.velocity,status.dampingCoef,status.temperature)
    plt.plot(time,velocity,label='velocity')
    plt.plot(time,accerlation,label='accerlation')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    testCase = status(2,1,298,0.1,1,100)
    main(testCase)
