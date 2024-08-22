# 專案介紹
結合美國手語字母（[American manual alphabet](https://en.wikipedia.org/wiki/American_manual_alphabet)）與 [Wordle](https://www.nytimes.com/games/wordle/index.html) 的小遊戲
- [貢獻指南](CONTRIBUTING.md)
- [模型說明](models/README.md)


# 執行遊戲
1. 到本專案的 Google Drive 下載模型 `best.pt` ，移動到本專案目錄的 `models/` 底下。
2. 用 Conda 或 Venv 啟用虛擬環境
3. 啟動 Django 伺服器
    ```shell
    python manage.py runserver
    ```

<!-- 靜態文件收集（會收集到 `public/assets`，開發模式下還不需要）
```shell
python manage.py collectstatic
``` -->

# 設置開發環境
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


#### 使用 VS Code 與 venv
1. 開啟 Command Palette（快速鍵：[Shift]+[Ctrl]+[P]）
2. 輸入 Create Environment
3. 點選 Python 直譯器
4. 點選 dependencies 為 `requirements.txt`
5. 點選 OK，開始安裝虛擬環境
6. 安裝完之後，到終端機啟用虛擬環境
   - Powershell `.\venv\Scripts\Activate\ps1`
   - Commnad Promt `.venv\Scripts\activate.bat`
   - Shell `.venv/Scripts\activate`
7. 在終端機執行 `pip list`，確認套件都已經安裝
8. 在終端機執行 `deactivate` 可停用虛擬環境


### 安裝相依套件

#### 批量安裝（推薦使用）
1. `cd` 到專案根目錄。
2. 如果要用學校電腦的 GPU 訓練模型，先用以下指令安裝 PyTorch，否則跳過此步驟。
    ```shell
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    ```
3. 批量安裝。
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

# Ultralytics, for YOLOv8 — 電腦視覺模型
# https://docs.ultralytics.com/quickstart/
pip install ultralytics

# Roboflow & Kaggle — 資料集下載與管理
pip install roboflow 
pip install kaggle

pip install python-decouple 
```

<!-- # PIL/Pillow — 影像處理
pip install pillow

# NumPy — 數值運算
# v1.x (required by ultralytics, etc.)
pip install numpy<=1.26.4

# PyTorch — 深度學習框架
# https://pytorch.org/get-started/locally/
pip install torch -->