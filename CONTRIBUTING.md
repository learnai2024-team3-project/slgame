# 貢獻指南

請按照以下步驟來貢獻程式碼或建議：

## 報告問題 (Issues)
請在 [GitHub Issues](https://github.com/learnai2024-team3-project/slgame/issues) 上提交問題，並提供足夠的上下文說明。

## 提交 Pull Requests
1. Fork 本專案並創建您的分支 (例如：`git checkout -b feature/your-feature`)。
2. 確保您的代碼遵循程式碼風格要求，並撰寫必要的測試。
3. 提交 Pull Request 並簡要說明您的變更內容。

## 程式碼風格
請確保您的程式碼遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 規範。

## 設置開發環境
以下是設置開發環境的步驟：
1. 克隆專案：`git clone https://github.com/learnai2024-team3-project/slgame.git`
2. 進入專案目錄：`cd slgame`
3. 建立虛擬環境並安裝相依套件，請閱讀以下說明。

### 虛擬環境

```shell
pip install -r requirements.txt
```

#### 使用 [Conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)
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

#### 使用 Python [venv](https://docs.python.org/zh-tw/3/library/venv.html)
```shell
python -m venv <path/to/slg> # <path/to/slg> 是填欲安裝目錄路徑
source <path/to/slg>/bin/activate # Windows 下為 <path/to/slg>\Scripts\activate
```

### 安裝套件

#### 批量安裝（推薦使用）
`cd` 到專案根目錄，然後執行

```shell
pip install -r requirements.txt
```

#### 個別安裝
``` shell
# Django — 網站框架
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

# Ultralytics, for YOLOv8 — 電腦視覺模型
# https://docs.ultralytics.com/quickstart/
pip install ultralytics

# Roboflow & Kaggle — 資料集管理
pip install roboflow 
pip install kaggle
```

## 建立說明文件

安裝 Sphinx
```shell
pip install -U sphinx
```

建立說明文件（HTML）
```shell
cd docs
make html
```

