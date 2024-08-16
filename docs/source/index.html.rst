`index.html` 文件說明
======================

本文提供了 `index.html` 的詳細說明，涵蓋其結構、功能和使用方式。

概述
----

`index.html` 是此專案的主要入口點，負責構建網頁的基本框架。它包括對外部樣式表和腳本的引用，並包含網頁的主要結構。

結構
----

`index.html` 文件分為以下幾個主要部分：

1. **Head 區塊**：

   - 包含 meta 標籤、標題以及連結至 Bootstrap 的 CSS 文件。
   
   .. code-block:: html
   
       <head>
           <meta charset="viewport" content="width=device-width, initial-scale=1.0">
           <title>Camera, MP4, and Image Upload Capture with Recognition</title>
           <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
           <style>
               /* 內嵌的樣式表，設置影片和圖像容器的寬度與對齊方式 */
               .video-container, .image-container {
                   width: 100%;
                   text-align: center;
               }

               /* 設置影片、圖片和畫布元素的顯示方式 */
               video, img, canvas {
                   display: block;
                   margin: 0 auto;
                   max-width: 100%;
                   height: auto;
               }
           </style>
       </head>

2. **Body 區塊**：

   - 這是網頁的主要內容部分，包含了以下元素：
   
   .. code-block:: html

       <body>
       <div class="container mt-5">
           <div class="row">
               <div class="col-md-6">
                   <div class="mb-3">
                       <label for="sourceSelect" class="form-label">Source:</label>
                       <select class="form-select" id="sourceSelect">
                           <!-- 下拉選單，用於選擇影像來源 -->
                           <option value="camera">Camera</option>
                           <option value="uploadVideo">Upload MP4</option>
                           <option value="uploadImage">Upload Image</option>
                       </select>
                   </div>
               </div>
               <div class="col-md-6">
                   <div class="result-box p-3 bg-light border mb-3">
                       <h5>Recognition Result:</h5>
                       <p id="resultText">No result yet</p>
                   </div>
               </div>
           </div>
           <div class="row">
               <div class="col-md-6">
                   <!-- 相機畫面容器 -->
                   <div id="cameraContainer" class="video-container">
                       <video id="camera" autoplay playsinline></video>
                   </div>
                   <!-- 上傳影片容器 -->
                   <div id="uploadVideoContainer" class="video-container d-none">
                       <input type="file" id="videoUpload" accept="video/mp4" class="form-control">
                       <video id="uploadedVideo" controls class="mt-3"></video>
                   </div>
                   <!-- 上傳圖片容器 -->
                   <div id="uploadImageContainer" class="image-container d-none">
                       <input type="file" id="imageUpload" accept="image/*" class="form-control">
                       <img id="uploadedImage" class="mt-3" alt="Uploaded Image">
                   </div>
               </div>
               <div class="col-md-6">
                   <!-- 截圖按鈕和畫布 -->
                   <button id="captureBtn" class="btn btn-primary mb-3">Capture Image</button>
                   <canvas id="canvas"></canvas>
               </div>
           </div>
       </div>
       </body>

功能說明
--------

1. **影像來源選擇**：

   - 使用者可以通過下拉選單選擇影像來源，包括「Camera」、「Upload MP4」和「Upload Image」。

2. **影像顯示區域**：

   - 當選擇「Camera」時，啟動攝影機並顯示即時影像。
   - 當選擇「Upload MP4」或「Upload Image」時，分別顯示上傳的影片或圖片。

3. **截圖與辨識**：

   - 使用者可以按下「Capture Image」按鈕擷取當前顯示的影像（來自攝影機、上傳的影片或圖片），並將擷取到的影像傳送到後端進行辨識。

使用方式
--------

1. **確保資源鏈接正確**：

   - 確保 Bootstrap 的 CSS 檔案和 JavaScript 腳本都正確連結。

2. **部署指南**：

   - 將 `index.html` 文件作為應用程式的入口點，並確保所有引用的資源（如影片、圖片）都正確配置在專案的路徑下。

常見問題排解
------------

1. **影片或圖片無法顯示**：

   - 檢查資源路徑是否正確，確保所有引用的文件存在且可讀取。
   
2. **攝影機無法啟動**：

   - 檢查瀏覽器是否允許存取攝影機，並確認所有必要的權限已授予。

結論
----

`index.html` 是此專案的核心文件之一，其正確配置對於應用程式的正常運行至關重要。通過遵循上述指南，確保頁面在所有情況下都能正確顯示和運行。
