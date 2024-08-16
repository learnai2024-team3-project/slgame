wordle.js 說明文件
=================

本文件詳細說明了 `wordle.js` 文件中的各個功能模組，該文件用於處理單字猜測遊戲的邏輯，以及通過攝影機獲取影像並發送到後端進行辨識。

檔案概述
--------

`wordle.js` 是此專案的核心邏輯文件，包含以下主要功能模組：

- 單字猜測遊戲的初始化、輸入處理、結果檢查和重置功能。
- 攝影機影像的獲取與處理，以及將影像發送到後端進行辨識（目前不可用）。

主要功能模組
------------

1. **遊戲初始化**:

   - `resetGame()`
     - 此函數負責初始化遊戲狀態，包含清除當前單字、重置輸入行列、隨機生成目標單字，以及重置字母格子和鍵盤狀態。

   - **函數定義**:
   
     .. code-block:: javascript

        function resetGame() {
            currentWord = '';
            currentRow = 0;
            targetWord = generateRandomWord();
            submittedLetters.clear();
            Array.from(wordGrid.children).forEach(box => {
                box.textContent = '';
                box.className = 'letter-box';
            });
            Array.from(keyboard.children).forEach(key => key.classList.remove('used'));
        }

   - **輔助函數**:
     - `generateRandomWord()`
       - 隨機生成一個5個字母的單字作為目標單字。

2. **鍵盤輸入處理**:

   - `handleKeyPress(letter)`
     - 處理虛擬鍵盤或實體鍵盤的字母輸入，將輸入的字母更新至當前行的字母格子中。

   - **函數定義**:

     .. code-block:: javascript

        function handleKeyPress(letter) {
            if (currentWord.length < 5 && currentRow < 6) {
                currentWord += letter;
                updateGrid();
            }
        }

3. **結果檢查**:

   - `checkWord()`
     - 當使用者輸入完整的單字後，檢查該單字與目標單字的匹配情況，並更新字母格子和鍵盤的狀態。

   - **函數定義**:

     .. code-block:: javascript

        function checkWord() {
            if (currentWord.length !== 5) return;

            for (let i = 0; i < 5; i++) {
                const box = wordGrid.children[currentRow * 5 + i];
                const letter = currentWord[i];
                submittedLetters.add(letter);

                if (letter === targetWord[i]) {
                    box.classList.add('green');
                } else if (targetWord.includes(letter)) {
                    box.classList.add('yellow');
                } else {
                    box.classList.add('grey');
                }
            }

            updateKeyboard();

            if (currentWord === targetWord) {
                alert('Congratulations! You guessed the word!'); 
                resetGame();
            } else if (currentRow === 5) {
                alert(`Game over! The word was ${targetWord}`);
                resetGame();
            } else {
                currentRow++;
                currentWord = '';
            }
        }

4. **攝影機操作與影像辨識**:

   - `startWebcam()` 和 `stopWebcam()`
     - `startWebcam()` 啟動攝影機並顯示即時影像，還包含每秒擷取一個影格並發送到後端進行辨識的邏輯。
     - `stopWebcam()` 停止攝影機並釋放相關資源。

   - **函數定義**:
   
     .. code-block:: javascript

        async function startWebcam() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: true });
                webcamFeed.srcObject = stream;
                webcamPlaceholder.style.display = 'none';
                isRecording = true;
                toggleWebcamBtn.textContent = 'Stop Recording';

                const videoTrack = stream.getVideoTracks()[0];
                const imageCapture = new ImageCapture(videoTrack);
                
                setInterval(async () => {
                    const frame = await imageCapture.grabFrame();
                    sendFrameToBackend(frame);
                }, 1000);
            } catch (err) {
                console.error("Error accessing the webcam:", err);
                alert("Failed to access the webcam. Please check your permissions.");
            }
        }

     - `sendFrameToBackend(frame)`
       - 此函數負責將擷取的格轉換為 JPEG 格式的 base64 編碼，並將其發送到後端，進行影像辨識。

   - **函數定義**:

     .. code-block:: javascript

        async function sendFrameToBackend(frame) {
            const canvas = document.createElement('canvas');
            canvas.width = frame.width;
            canvas.height = frame.height;
            const context = canvas.getContext('2d');
            context.drawImage(frame, 0, 0);
            const imageData = canvas.toDataURL('image/jpeg');

            const response = await fetch('/recognize/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ image: imageData }),
            });

            const result = await response.json();
            console.log('Recognition Result:', result);
        }

使用方式
--------

1. **啟動遊戲**:

   - 確保在HTML文件中正確引用了 `wordle.js`，並通過瀏覽器載入該頁面以啟動遊戲。

2. **遊戲操作**:

   - 使用虛擬鍵盤或實體鍵盤輸入單字，每行最多輸入5個字母。
   - 按下「Enter」鍵或「Submit」按鈕提交單字。
   - 若猜測失敗，遊戲將提示正確答案並重新開始。

3. **影像辨識**:

   - 點擊「Start Webcam」按鈕啟動攝影機，程式會自動擷取影像，目前還不會進行辨識。

常見問題排解
------------

1. **攝影機無法啟動**:

   - 確認瀏覽器已授予攝影機使用權限，並且設備具備攝影機功能。

2. **遊戲無法正常運行**:

   - 檢查瀏覽器控制台有無報錯，確保 `wordle.js` 文件已正確載入。

結論
----

`wordle.js` 提供了一個簡單但有趣的單字猜測遊戲，同時還結合了攝影機影像辨識功能。通過正確配置和使用這個文件，可以為使用者提供豐富的互動體驗。
