# 深度學習模型
目前使用的深度學習模型來自 [MuhammadMoinFaisal 的專案](https://github.com/MuhammadMoinFaisal/Sign-Language-Alphabets-Detection-and-Recongition-using-YOLOv8)，可參考作者的 [Google Colab](https://colab.research.google.com/drive/1ITdJrATdpu3zE99HYPXZ42exQWLrWRp0?usp=sharing#scrollTo=Ep7iJPcKwuCx)。

其他模型選擇：Kaggle 競賽「[Google - American Sign Language Fingerspelling Recognition](https://www.kaggle.com/competitions/asl-fingerspelling)」 ，[Guthema 與 elliot robot 的作品](https://www.kaggle.com/code/gusthema/asl-fingerspelling-recognition-w-tensorflow) 。
- 研究中：[gust0811](https://www.kaggle.com/code/siniuho/gust0811)

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

# 執行 Web app
到本專案的 Google Drive 下載模型 `best.pt` ，移動到本專案目錄底下的 `models/`。

啟動 Django 伺服器
```shell
python manage.py runserver
```

靜態文件收集（會收集到 `public/assets`，開發模式下還不需要）
```shell
python manage.py collectstatic
```

# 遊戲介面

Wordle 遊戲介面開發中。請參考：
- `templates/wordle.html` 遊戲頁面
- `static/wordle.js` 包含遊戲邏輯、webcam 控制，目前尚未整合深度學習模型
- `static/wordle.css` 包含畫面元素，如鍵盤等