# 深度學習模型
目前使用的深度學習模型來自 [MuhammadMoinFaisal 的專案](https://github.com/MuhammadMoinFaisal/Sign-Language-Alphabets-Detection-and-Recongition-using-YOLOv8)，可參考作者的 [Google Colab](https://colab.research.google.com/drive/1ITdJrATdpu3zE99HYPXZ42exQWLrWRp0?usp=sharing#scrollTo=Ep7iJPcKwuCx)。

其他模型選擇：Kaggle 競賽「[Google - American Sign Language Fingerspelling Recognition](https://www.kaggle.com/competitions/asl-fingerspelling)」 ，[Guthema 與 elliot robot 的作品](https://www.kaggle.com/code/gusthema/asl-fingerspelling-recognition-w-tensorflow) 。
- 研究中：[gust0811](https://www.kaggle.com/code/siniuho/gust0811)
 
[貢獻指南](CONTRIBUTING.md)

# 執行 Web app
到本專案的 Google Drive 下載模型 `best.pt` ，移動到本專案目錄的 `models/` 底下。

啟動 Django 伺服器
```shell
python manage.py runserver
```

<!-- 靜態文件收集（會收集到 `public/assets`，開發模式下還不需要）
```shell
python manage.py collectstatic
``` -->

# 遊戲介面

Wordle 遊戲介面開發中。請參考：
- `templates/wordle.html` 遊戲頁面
- `static/wordle.js` 包含遊戲邏輯、webcam 控制，目前尚未整合深度學習模型
- `static/wordle.css` 包含畫面元素，如鍵盤等
- `templates/tutorial.html` 手語教學頁面