#!/usr/bin/env python
# coding: utf-8

import os
import subprocess
from roboflow import Roboflow
import ultralytics
from ultralytics import YOLO
from yaml_parser import update_data_yaml

API_KEY = "UMHEdNtxcnwY7uVP60Lh"
WORKSPACE = "david-lee-d0rhs"
PROJECT = "american-sign-language-letters"
VERSION = 1
FORMAT = "yolov5"
# https://universe.roboflow.com/david-lee-d0rhs/american-sign-language-letters

EPOCH = 10
IMGSZ = 800
BATCH = 32


# ----------------------------------------------------------------------


def print_section_head(txt, divider=('-', 100)):
    print('\n' + divider[0] * divider[1] + '\n' + txt)


# Define the working directory
MODEL_DIR = os.getcwd()
print('Working directory: ', MODEL_DIR)


# Check GPU status
print_section_head('Checking GPU status')
subprocess.run(['nvidia-smi'])


# Check ultralytics and environment
print_section_head('Checking ultralytics and environment')
ultralytics.checks()


# Create datasets directory and navigate into it
datasets_dir = os.path.join(MODEL_DIR, 'datasets')
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


# Ensure `path: .` is at the end of the dataset configuration file
config_path = os.path.join(f'{dataset.location}', 'data.yaml')# 替換為你實際的 yaml 文件路徑
update_data_yaml(config_path)
os.chdir(MODEL_DIR)


# Initialize the YOLO pre-trained model
print_section_head('Initialize YOLO model')
# Our choice: YOLOv8 Large
model = YOLO('yolov8l.pt')


# # Congifure hyperparameters and start model training
print_section_head('Start training...')
model.train(
    data=config_path,       # dataset configuration file
    epochs=EPOCH,           # number of training epochs
    imgsz=IMGSZ,            # image size
    batch=BATCH,            # batch size
    optimizer="auto",       # optimizer
    save_dir=MODEL_DIR      # saving directory
)
