 
# 虛擬環境

## Miniconda
```shell
# 建立虛擬環境
conda create --name slg

# 啟用虛擬環境
conda activate slg

# 退出虛擬環境
conda deactivate

# 安裝並註冊 ipykernel (可使用 ipython、Jupyter Notebook 等等）
conda install -n slg ipykernel
python -m ipykernel install --user --name slg
```
 
 
# 安裝套件

## 批量安裝
`cd` 到專案根目錄，然後執行

```shell
pip install -r 'requirements.txt'
```

## 個別安裝
``` shell
# Django 網站框架
pip install django
pip install djangorestframework

# drf-yasg — 自動生成 Swagger UI
pip install -U drf-yasg

# PIL/Pillow — 影像處理
pip install pillow

# NumPy — 數值運算
# v1.x (required by ultralytics, etc.)
pip install numpy<=1.26.4

# PyTorch — 深度學習框架
# https://pytorch.org/get-started/locally/
pip install torch

# Ultralytics, for YOLOv8
# https://docs.ultralytics.com/quickstart/
pip install ultralytics
```

## 執行 Web app
到雲端硬碟下載模型 `best.pt` ，移動到本專案的 `models/`。

然後執行
```
python manage.py runserver
```

