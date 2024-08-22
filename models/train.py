import os
from roboflow import Roboflow
from ultralytics import YOLO
from util import check_all, print_section_head, update_data_yaml
from decouple import config

ROBOFLOW_API_KEY = config('ROBOFLOW_API_KEY')
WORKSPACE = "david-lee-d0rhs"
PROJECT = "american-sign-language-letters"
VERSION = 1
FORMAT = "yolov5"
# https://universe.roboflow.com/david-lee-d0rhs/american-sign-language-letters

EPOCH = 10
IMGSZ = 800
BATCH = 9


# ----------------------------------------------------------------------


if __name__ == '__main__':
    # Define the working directory
    MODEL_DIR = os.getcwd()
    print('Working directory: ', MODEL_DIR)

    check_all()

    # Create datasets directory and navigate into it
    datasets_dir = os.path.join(MODEL_DIR, 'datasets')
    os.makedirs(datasets_dir, exist_ok=True)
    os.chdir(datasets_dir)
    print('Dataset directory: ', datasets_dir)

    # Initialize Roboflow and download the dataset
    print_section_head('Initialize Roboflow and download the dataset')
    rf = Roboflow(api_key=ROBOFLOW_API_KEY)
    workspace = rf.workspace(WORKSPACE)
    project = workspace.project(PROJECT)
    version = project.version(VERSION)
    dataset = version.download(FORMAT)

    # Ensure `path: .` is at the end of the dataset configuration file
    config_path = os.path.join(f'{dataset.location}', 'data.yaml')
    update_data_yaml(config_path)
    os.chdir(MODEL_DIR)

    # Initialize the YOLO pre-trained model
    print_section_head('Initialize YOLO model')
    # Our choice: YOLOv8 Large
    model = YOLO('yolov8l.pt')

    # # # Congifure hyperparameters and start model training
    # print_section_head('Start training...')
    # model.train(
    #     device=0,               # GPU
    #     data=config_path,       # dataset configuration file
    #     epochs=EPOCH,           # number of training epochs
    #     imgsz=IMGSZ,            # image size
    #     batch=BATCH,            # batch size
    #     optimizer="auto",       # optimizer
    #     workers=0               # saving directory
    # )
