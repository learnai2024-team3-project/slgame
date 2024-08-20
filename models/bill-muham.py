#!/usr/bin/env python
# coding: utf-8

import os
import subprocess
from roboflow import Roboflow
import ultralytics

# 定義工作目錄
HOME = os.getcwd()

# 查看 GPU 狀態
subprocess.run(['nvidia-smi'])

# 檢查 ultralytics 並環境
ultralytics.checks()

# 建立資料集目錄並進入
datasets_dir = os.path.join(HOME, 'datasets')
os.makedirs(datasets_dir, exist_ok=True)
os.chdir(datasets_dir)

# 初始化 Roboflow 並下載資料集
rf = Roboflow(api_key="vQpY4GwAhAtrSZQTm2J0")
ws = "david-lee-d0rhs"
pj = "american-sign-language-letters"
dataset = rf.workspace(ws).project(pj).version(1).download("yolov5")

# # 執行 YOLOv8 的訓練 (示範)
# # 這裡需要確保你的 YOLOv8 模型和配置正確
# subprocess.run(['yolo',
#                 'task=detect',
#                 'mode=train',
#                 f'data={dataset.location}/data.yaml',
#                 'epochs=50',
#                 'batch=32']
#                )
