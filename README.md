# Ducks in a Circular Pond

This program was created for a project for my statistics class in which we had to write a program that would numerically verify the relative frequency of success in the ducks in a circular pond problem.
Discription of project from instructor:
>There is a circular pond with n (n ≥2) ducks randomly distributed across the top. Each duck
can be modeled as a point. What is the probability that all of the n ducks are in the same half of the circular
pond. Note here that we can draw the half way line on any diameter; they can go at any angle.

My program uses Python with the Tkinter library to first create a GUI which will be used to gather user inputs for running the simulation. The inputs are the number of ducks that will be placed in the pond, the number of iterations that the simulation will run, and the sector at which it iwss checking the points to be in which is base case 180 degrees or half the pond, but can be anything between 1 degree to 359 degrees. When the button is clicked to run the simulation it will create a new window that shows the simulation of the ducks in the pond with updating variables that shows the number of successes, the current iteration through the simulation, and the relative frequency of successes. The simulation has a button at the bottom labeled next which will allow you to itterate through the trials of the simulation. 

Credit to Colby0506 for helping me with figuring out parts of the math and simulation.
