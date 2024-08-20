#!/usr/bin/env python
# coding: utf-8

import os
import subprocess
from roboflow import Roboflow
import ultralytics
from ultralytics import YOLO

API_KEY = "UMHEdNtxcnwY7uVP60Lh"
WORKSPACE = "david-lee-d0rhs"
PROJECT = "american-sign-language-letters"
VERSION = 1
FORMAT = "yolov8"
# https://universe.roboflow.com/david-lee-d0rhs/american-sign-language-letters

EPOCH = 10
IMGSZ = 800
BATCH = 32


# ----------------------------------------------------------------------


def print_section_head(txt):
    print('\n' + '-' * 8+ '\n' + txt)


# Define the working directory
HOME = os.getcwd()
print('Working directory: ', HOME)


# Check GPU status
print_section_head('Checking GPU status')
subprocess.run(['nvidia-smi'])


# Check ultralytics and environment
print_section_head('Checking ultralytics and environment')
ultralytics.checks()


# Create datasets directory and navigate into it
datasets_dir = os.path.join(HOME, 'datasets')
os.makedirs(datasets_dir, exist_ok=True)
os.chdir(datasets_dir)
print('Dataset directory: ', datasets_dir)


# Initialize Roboflow and download the dataset
print_section_head('Initialize Roboflow and download the dataset')
rf = Roboflow(api_key=API_KEY)
workspace = rf.workspace(WORKSPACE)
project = workspace.project(PROJECT)
version = project.version(VERSION)
dataset = version.download(FORMAT)


# Add a new line `path: .` at the end of the dataset configuration file
os.chdir(dataset.location)
with open('data.yaml', 'a') as file:
    file.write('\npath: .\n')
os.chdir(HOME)


# Initialize the YOLO pre-trained model
print_section_head('Initialize YOLO model')
# Our choice: YOLOv8 Large
model = YOLO('yolov8l.pt')


# Congifure hyperparameters and start model training
print_section_head('Start training...')
model.train(
    data=f'{dataset.location}/data.yaml',  # Dataset configuration file
    epochs=EPOCH,                          # Number of training epochs
    imgsz=IMGSZ,                           # Image size
    batch=BATCH,                           # Batch size
    optimizer="auto"                       # Optimizer
)
