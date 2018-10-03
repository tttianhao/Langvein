========
Langevin
========


.. image:: https://img.shields.io/travis/tttianhao/langevin.svg
        :target: https://travis-ci.org/tttianhao/langevin


.. image:: https://coveralls.io/repos/github/tttianhao/langevin/badge.svg?branch=master
        :target: https://coveralls.io/github/tttianhao/langevin?branch=master



Overview
--------

This project is a Langevin Dynamics simulator that simulates the movment of a particle in 1 dimension. 
This project uses frictional force and random force to calculate acceration of the particle. 
This simulator uses Euler's integration to simulate the position and velocity of the particle from the previous instance.
The potential energy in this program is assumed to be zero.
User input includes the initial postion, initial velocity, temperature, damping coefficient, time step and total time.

Installation
------------

To install the simulator simply copy and paste the following command line:

``git clone https://github.com/tttianhao/langevin.git``

Usage
-----

To run the simulator simply copy and paste the following command line in the project directory:

``python langevin/langevin.py --initial_position 0 --initial_velocity 0 --temperature 300 
--total_time 1000 --time_step 0.01 --damping_coefficient 0.1``

Input value of the program should make physical senses. e.g. Temperature should always be a positive number.
The output files are one text file with time, position and velocity information and two figures.

* Free software: MIT license


Features
--------

* Produce histagram from 100 runs
* Produce a nice trajectory of the position
* Produce a neatly formatted txt file with information including time, position and velocity

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
