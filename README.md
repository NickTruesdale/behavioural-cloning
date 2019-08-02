## Autonomous Driving Learning
The field of autonomous driving is one of the more interesting applications for
machine learning and neural networks. Currently, hundreds of companies are trying
to get their foot in the door, and this is leading to a wealth of demand for
engineers, as well as a lot of open source materials and programs to help train
said engineers. 

## Behavioural Cloning
This repo aims to implement a version of NVIDIA's PilotNet Convolutional Neural
Network (CNN). We will train the network on images taken from the Udacity driving
simulator, with the training label being the inverse of steering angle. This will
allow the model to run in real time with the simulator, taking in images and 
returning a steering angle in order to drive the vehicle.

## Server
The model runs within a fastapi server in order to communicate with the simulator.
In order to run this, a .env file is required in the module directory, with the
following structure:

```
UVICORN_PORT=8080
UVICORN_HOST=127.0.0.1
```

## Useful Links
Udacity self-driving car nanodegree 
- https://eu.udacity.com/course/self-driving-car-engineer-nanodegree--nd013

Udacity's self-driving car simulator
- https://github.com/udacity/self-driving-car-sim

Siraj Raval - How to Simulate a Self-Driving Car
- https://www.youtube.com/watch?v=EaY5QiZwSP4
- https://github.com/llSourcell/How_to_simulate_a_self_driving_car

NVidia CNN Paper:
- https://devblogs.nvidia.com/deep-learning-self-driving-cars/
