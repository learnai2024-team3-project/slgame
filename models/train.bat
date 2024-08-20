@echo off

REM 定義工作目錄
set "HOME=%cd%"

REM 查看 GPU 的狀態
nvidia-smi

REM 檢查 YOLOv8 環境
python -c "import ultralytics; ultralytics.checks()"

REM 建立資料集目錄並進入
if not exist "%HOME%\datasets" (
    mkdir "%HOME%\datasets"
)
cd "%HOME%\datasets"

REM 初始化 Roboflow 並下載資料集
python -c "from roboflow import Roboflow
rf = Roboflow(api_key='vQpY4GwAhAtrSZQTm2J0')
project = rf.workspace('david-lee-d0rhs').project('american-sign-language-letters')
dataset = project.version(1).download('yolov5')"

REM 使用 YOLOv8 進行訓練
yolo device=0,1 task=detect mode=train model=yolov8l.pt optimizer="auto" batch=32 data=%dataset.location%\data.yaml epochs=50 imgsz=800
