# -*- coding: utf-8 -*-

"""Main module."""

import argparse
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

class status:

    '''This class initialize the initial status of the particle'''

    def __init__(self,initial_position,initial_velocity, temperature, damping_coefficient,time_step,total_time,mass=1):
        self.initial_position = initial_position
        self.initial_velocity = initial_velocity
        self.temperature = temperature
        self.damping_coefficient = damping_coefficient
        self.time_step = time_step
        self.total_time = total_time
        self.mass = mass

def dragForce(damping_coefficient,velocity):
    '''
    This function calculates drage force from given damping coefficient and velocity

    Args:
        damping_coefficient: damping coefficient gamma
        velocity: velocity at a certain time
    
    returns:
        drag force (frictional force)
    '''

    return -damping_coefficient*velocity



def randomForceGenerator(temperature,damping_coefficient,kB =1,delta=1):

    '''
    This function generate a random number from a normal distribution, whose mean is zero and variance is determined by 'variance' function.

    returns:
        Xi: the random force at a certain instance
    '''

    mu = 0
    var = 2*temperature*damping_coefficient*kB*delta
    sigma = np.sqrt(var)
    # draw a random number from a normal distribution with mean=0 and std=sqrt(var)
    Xi = np.random.normal(mu,sigma)
    return Xi

def eulerIntegration(initialposition,time_step,total_time,initialVelocity,damping_coefficient,temperature):
    '''
    This function uses euler method to calculate

    Args:
        initialpositon: the input position at t=0
        time_step: the time interval between two times
        total_time: the total runtime of the integration
        initialVelocity: the input velocity at t=0
        damping_coefficient: damping coefficient
        temperature: the input temperature
    
    returns:
        time: time profile 
        velocity: velocity at time t
        accerlation: the derivative of velocity at time t
        position: the position of particle at time t
    '''
    #set up the indext of total possible times
    n = int(total_time/time_step+1)
    time = np.linspace(0,total_time,n)
    #initialize velocity and position
    velocity = np.zeros(n)
    position = np.zeros(n)
    #set initial velocity and position
    velocity[0] = initialVelocity
    position[0] = initialposition
    #apply euler equation to estimate y(i) from y(i-1)
    for i in range(1,n):
        randomForce = randomForceGenerator(temperature,damping_coefficient)
        #Euler equation used is : y_i = dx(f(y_i-1,x_i-1)) + y_i-1
        accerlation = dragForce(damping_coefficient,velocity[i-1])+randomForce
        velocity[i] = time_step*accerlation+velocity[i-1]
        #use equation x = x + dt*v
        position[i] = position[i-1] + time_step*velocity[i-1]
        # check if the particle hits the wall
        if not checkWall(position[i]):
            break
    #return the time, velocity and postion at each time.
    #trumed becasue the particle stops when it hits the wall.
    return time[0:i+1],velocity[0:i+1],position[0:i+1]


def checkWall(position):
    '''
    This function checks if the position of the particle is still in the two walls
    
    returns:
        true if particle in the wall and false if not.
    '''

    if position > -5 and position < 5:
        return True
    else:
        return False

def outPut(time,position,velocity):
    '''
    This function writes the output to a new text file with information incluting index, time, velocity and positon
    '''

    #write output to a new text file named 'langvein_dynamics_output.txt'
    file = open('Langvein_dynamics_output.txt','w+')
    file.write('index  time  position  velocity \n')
    for i in np.arange(0,len(time)):
        file.write('{:5.0f}  {:4.2f}  {:8.2f}  {:8.2f} \n'.format(i,time[i],position[i],velocity[i]))
    file.close()

def main(status):
    '''
    main function, only run when directly used
    '''
    at = []
    ap = []
    av = []
    #run 100 times and collect the time that particle hits the wall
    timeWall = np.zeros(100)
    for i in range(100):
        time,velocity,position = eulerIntegration(status.initial_position,status.time_step,status.total_time,status.initial_velocity,status.damping_coefficient,status.temperature)
        timeWall[i] = time[-1]
        at.append(time)
        ap.append(position)
        av.append(velocity)
    
    #choose the longest run
    maxIndex = np.argmax(timeWall)
    time = at[maxIndex]
    position = ap[maxIndex]
    velocity = av[maxIndex]

    #write output to new file
    outPut(time,position,velocity)
    #first figure is the histogram of 100 runs
    plt.figure(0)
    plt.hist(timeWall,bins=20)
    plt.title('histogram of 100 runs')
    plt.savefig('histogram.png')
    #second figure is the trjectory of the postion of particle in one run
    plt.figure(1)
    plt.plot(time,position)
    plt.title('trajectory')
    plt.savefig('trajectory.png')

if __name__ == '__main__':

    #Using parser to take in user in put form termial.
    #The default command is:
    #langevin/langevin.py --initial_position 0 --initial_velocity 0 --temperature 300 --total_time 1000 --time_step 0.01 --damping_coefficient 0.1
    parser = argparse.ArgumentParser()
    parser.add_argument('--initial_position', type = float, default = 0, help = 'Initial position of the particle, default = 0' )
    parser.add_argument('--initial_velocity', type = float, default = 0, help = 'Initial velocity of the particle, default = 0' )
    parser.add_argument('--temperature', type = float, default = 298, help = 'Temperature of the molecule, default = 298' )
    parser.add_argument('--damping_coefficient', type = float, default = 0.1, help = 'Damping Coefficient of the molecule, default = 0.1' )
    parser.add_argument('--time_step', type = float, default = 0.01, help = 'Time interval of the simulation, default = 0.01' )
    parser.add_argument('--total_time', type = float, default = 1000, help = 'Total time of the simulation, default = 1000' )
    args = parser.parse_args()
    main(args)
