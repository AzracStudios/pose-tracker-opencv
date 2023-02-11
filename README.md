# Pose Tracker

## Introduction
This is a simple application, built with python and opencv, making use of the mediapipe framework. 

## Mediapipe 
MediaPipe is a cross-platform pipeline framework to build custom machine learning solutions for live and streaming media. It is extremely powerful in both the datasets and the performance. This app makes use of the pose estimation, facial mesh tessellation and the hand mesh tessalation models, to track the movement of a person.

## Run the application
- Clone or download the github repository
- Install requirements
- Run

`$ git clone git@github.com:AzracStudios/pose_tracker_opencv`

`$ cd pose_tracker_opencv`

`$ pip install -r requirements.txt`

`$ python3 main.py`


## Resources
Mediapipe home: https://google.github.io/

Mediapipe hands: https://google.github.io/mediapipe/solutions/hands#python-solution-api

Mediapipe face: https://google.github.io/mediapipe/solutions/face_mesh#python-solution-api

Mediapipe pose: https://google.github.io/mediapipe/solutions/pose#python-solution-api

Opencv documentation: https://opencv24-python-tutorials.readthedocs.io/en/latest/
