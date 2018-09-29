========
Langevin
========


.. image:: https://img.shields.io/pypi/v/langevin.svg
        :target: https://pypi.python.org/pypi/langevin

.. image:: https://img.shields.io/travis/tttianhao/langevin.svg
        :target: https://travis-ci.org/tttianhao/langevin

.. image:: https://readthedocs.org/projects/langevin/badge/?version=latest
        :target: https://langevin.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/tttianhao/langevin/badge.svg?branch=master
        :target: https://coveralls.io/github/tttianhao/langevin?branch=master

.. image:: https://pyup.io/repos/github/tttianhao/langevin/shield.svg
     :target: https://pyup.io/repos/github/tttianhao/langevin/
     :alt: Updates



Langevin Dynamics project for CHE477

This project is a Langevin Dynamics simulator that simulates the movment of a particle. 
This project uses frictional force and random force to calculate acceration of the particle based on the previous time instance.
User input including the initial postion, initial velocity, temperature, damping coefficient, time step and total time.
To run this simulator, please use the following command:

`python langevin/langevin.py --initial_position 0 --initial_velocity 0 --temperature 300 --total_time 1000 --time_step 0.01 --damping_coefficient 0.1`

The output files are one txt file with time, position and velocity and two figures.

* Free software: MIT license
* Documentation: https://langevin.readthedocs.io.


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
