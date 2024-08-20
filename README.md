# 專案介紹
結合美國手語字母（[American manual alphabet](https://en.wikipedia.org/wiki/American_manual_alphabet)）與 [Wordle](https://www.nytimes.com/games/wordle/index.html) 的小遊戲
- [貢獻指南](CONTRIBUTING.md)
- [模型說明](models/README.md)

# 訓練手語辨識模型
1. 用 Conda 或 Venv 啟用虛擬環境
2. 執行 `train.py`
    ```shell
    cd models
    python train.py
    ```

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

