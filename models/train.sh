#!/bin/bash

# 定義工作目錄
HOME=$(pwd)

# 查看 GPU 的狀態
nvidia-smi

# 檢查 YOLOv8 環境
python -c "import ultralytics; ultralytics.checks()"

# 建立資料集目錄並進入
mkdir -p "$HOME/datasets"
cd "$HOME/datasets"

# 初始化 Roboflow 並下載資料集
python - <<END
from roboflow import Roboflow
rf = Roboflow(api_key="vQpY4GwAhAtrSZQTm2J0")
project = rf.workspace("david-lee-d0rhs").project("american-sign-language-letters")
dataset = project.version(1).download("yolov5")
END

# 使用 YOLOv8 進行訓練
yolo device=0,1 task=detect mode=train model=yolov8l.pt optimizer="auto" batch=32 data={dataset.location}/data.yaml epochs=50 imgsz=800
