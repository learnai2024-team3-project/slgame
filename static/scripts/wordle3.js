
const wordGrid = document.getElementById('word-grid');
const keyboard = document.getElementById('keyboard');
const toggleWebcamBtn = document.getElementById('toggle-webcam');
const submitBtn = document.getElementById('submit');
const giveUpBtn = document.getElementById('give-up');
const webcamFeed = document.getElementById('webcam-feed');
const webcamPlaceholder = document.getElementById('webcam-placeholder');

const sidebar = document.getElementById('sidebar');
const slist = sidebar.querySelectorAll('a');
const currentUrl = window.location.origin;
const userid = new URLSearchParams(window.location.search).get('userid');
const scoreList = {0:100,1:80,2:60,3:40,4:20,5:0};
const scoreElement = document.getElementById('scoreText');

let score = 0
let currentWord = '';
let currentRow = 0;
let targetWord = '';
let isRecording = false;
let submittedLetters = new Set();

// Initialize the word grid
// 更改可猜的次數(刪掉letterbox)
for (let i = 0; i < 25; i++) {
    const letterBox = document.createElement('div');
    letterBox.classList.add('letter-box');
    wordGrid.appendChild(letterBox);
}

// Initialize the keyboard
'QWERTYUIOPASDFGHJKL ZXCVBNM'.split('').forEach(letter => {
    const key = document.createElement('div');
    key.classList.add('key');
    key.textContent = letter;
    if (key.textContent != ' ') {
        key.addEventListener('click', () => handleKeyPress(letter));
    }
    keyboard.appendChild(key);
});

function handleKeyPress(letter) {
    if (currentWord.length < 5 && currentRow < 6) {
        currentWord += letter;
        updateGrid();
    }
}

function updateGrid() {
    const rowStart = currentRow * 5;
    for (let i = 0; i < 5; i++) {
        wordGrid.children[rowStart + i].textContent = currentWord[i] || '';
    }
}

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
        score = scoreList[currentRow];
        sendScore();
        scoreElement.textContent = `Previous round result: ${score}`;
        resetGame();
    } else if (currentRow === 4) {       // 更改可猜的次數
        alert(`Game over! The word was ${targetWord}`);
        score = 0;
        scoreElement.textContent = `Previous round result: ${score}`;
        resetGame();
    } else {
        currentRow++;
        currentWord = '';
    }
}

function updateKeyboard() {
    Array.from(keyboard.children).forEach(key => {
        if (submittedLetters.has(key.textContent)) {
            key.classList.add('used');
        }
    });
}

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

function generateRandomWord() {
    const words = ['APPLE', 'BRAVE', 'CANDY', 'DANCE', 'EAGLE', 'FABLE', 'GRAPE', 'HONEY', 'IVORY', 'JOKER'];
    return words[Math.floor(Math.random() * words.length)];
}

function sendScore(){
    console.log(userid);
    console.log(score);
    const data = {
        'userid': userid,
        'score': score,
        'token': sessionStorage.getItem('token')
    }

    fetch(currentUrl +'/game_submit/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            if (data.status === 'success') {
               sessionStorage.setItem("totalscore",data.totalscore)
               sessionStorage.setItem("count",data.count)
               sessionStorage.setItem("rank",data.rank)
            
            } 
            // else if (data.feedback === "noToken" || !sessionStorage.getItem('token')) {
            //     Swal.fire({
            //         position: "center",
            //         icon: "error",
            //         title: "請正確登入",
            //         showConfirmButton: true,
            //         // timer: 1500
            //         }); } 
            // else {
            //         Swal.fire({
            //         position: "center",
            //         icon: "error",
            //         title: "成績送出失敗",
            //         showConfirmButton: true,
            //         // timer: 1500
            //         });
            // }
        })
        .catch((error) => {
            console.error('Error:', error);
            resultText.textContent = "Error during recognition.";
        });
}


function processRecording() {
    let blob = new Blob(chunks, { type: 'video/webm' });
    chunks = [];
    let reader = new FileReader();
    reader.onloadend = function() {
        let base64Video = reader.result.split(',')[1];
        submitVieo(base64Video);
    };
    reader.readAsDataURL(blob);
}

function submitVieo(base64Video) {
    const postData = {
        Authorization: "your_auth_token",
        file: base64Video,
        mode: "your_mode"
    };

    
    fetch(currentUrl + '/upload_video/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        if (data.status === 'success') {
            if (data.data.recognizedWord.length === 1) {
                letter = data.data.recognizedWord.toUpperCase();
                handleKeyPress(letter);
            }
        } else {
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function submitImage(base64Image) {
    const postData = {
        Authorization: "your_auth_token",
        file: base64Image,
        mode: "your_mode"
    };

    const currentUrl = window.location.origin;

    // 显示“辨识中”消息
    let overlayMessage = document.getElementById('overlay-message');
    if (!overlayMessage) {
        overlayMessage = document.createElement('div');
        overlayMessage.id = 'overlay-message';
        overlayMessage.textContent = 'Loading...';
        overlayMessage.style.position = 'absolute';
        overlayMessage.style.top = '50%';
        overlayMessage.style.left = '50%';
        overlayMessage.style.transform = 'translate(-50%, -50%)';
        overlayMessage.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
        overlayMessage.style.color = 'white';
        overlayMessage.style.padding = '10px 20px';
        overlayMessage.style.borderRadius = '5px';
        overlayMessage.style.zIndex = '20';
        overlayMessage.style.textAlign = 'center';
        overlayMessage.style.display = 'none';

        // 获取 video 或 img 容器
        const webcamContainer = document.getElementById('webcam-container');
        webcamContainer.appendChild(overlayMessage);  // 将消息添加到容器中
    }

    overlayMessage.style.display = 'block'; // 显示消息

    fetch(currentUrl + '/upload/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);

        // 显示识别的图像
        let recognizedImage = data.data.recognizedImage;
        const imageElement = document.getElementById('recognized-image');
        imageElement.src = 'data:image/png;base64,' + recognizedImage;
        imageElement.style.display = 'block';

        if (data.status === 'success') {
            if (data.data.recognizedWord.length === 1) {
                let letter = data.data.recognizedWord.toUpperCase();
                handleKeyPress(letter);
            }
        } else {
            alert('Recognition failed. Please try again.');
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    })
    .finally(() => {
        toggleWebcamBtn.textContent = 'Start Rec';
        isRecording = false;
        // 隐藏“辨识中”消息
        overlayMessage.style.display = 'none';
        toggleWebcamBtn.disabled = false;
    });
}

async function startWebcam() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        webcamFeed.srcObject = stream;
        webcamPlaceholder.style.display = 'none';
        const imageElement = document.getElementById('recognized-image');
        imageElement.style.display = 'none';  // 隐藏识别的图像
        isRecording = true;
        toggleWebcamBtn.textContent = 'Capture Image';
    } catch (err) {
        console.error("Error accessing the webcam:", err);
        alert("Failed to access the webcam. Please check your permissions.");
    }
    toggleWebcamBtn.disabled = false;
}

function stopWebcam() {
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    canvas.width = webcamFeed.videoWidth;
    canvas.height = webcamFeed.videoHeight;

    // 绘制视频帧到canvas上
    context.drawImage(webcamFeed, 0, 0, canvas.width, canvas.height);

    // 将canvas内容转为base64图像数据
    const imageData = canvas.toDataURL('image/png').replace('data:image/png;base64,', '');
   
    if (!imageData || imageData === "" || imageData === "data:,") {
        // 如果圖片內容為空就不處理
        console.log("imageData was empty!");
        toggleWebcamBtn.disabled = false;
        return
    }
   
    submitImage(imageData);

    // 停止摄像头流
    const stream = webcamFeed.srcObject;
    const tracks = stream.getTracks();

    tracks.forEach(track => {
        track.stop();
    });

    webcamFeed.srcObject = null;  // 清空video元素的srcObject
}

toggleWebcamBtn.addEventListener('click', toggleWebcam);

submitBtn.addEventListener('click', submitWord);

giveUpBtn.addEventListener('click', () => {
    alert(`The word was ${targetWord}`);
    resetGame();
});

// Handle keyboard input
document.addEventListener('keydown', (event) => {
    if (event.key >= 'a' && event.key <= 'z') {
        handleKeyPress(event.key.toUpperCase());
    } else if (event.key === 'Backspace') {
        if (currentWord.length > 0) {
            currentWord = currentWord.slice(0, -1);
            updateGrid();
        }
    } else if (event.key === 'Enter') {
        submitWord();
    } else if (event.key === ' ') {
        toggleWebcam();
    }
});

function toggleWebcam() {
    toggleWebcamBtn.disabled = true;

    if (isRecording) {
        stopWebcam();
    } else {
        startWebcam();
    }
}

function submitWord() {
    if (currentWord.length === 5) {
        checkWord();
    } else {
        alert("Please enter a 5-letter word before submitting.");
    }
}


// =================sidebar=================
document.getElementById("sidebarBtn").onclick = function() {
    var sidebar = document.getElementById("sidebar");
    
    if (sidebar.style.width === "250px") {
        sidebar.style.width = "0";        
    } else {
        sidebar.style.width = "250px";        
    }
};

// function isUserLoggedIn(){
//     if (sessionStorage.getItem("status") == "login"){
//         return true;
//     }
// }

if(sessionStorage.getItem("status") == "login"){
    slist[1].textContent = 'Logout';
}

slist[1].addEventListener('click',()=>{
    if(slist[1].textContent === 'Logout'){
        sessionStorage.removeItem('status');
        sessionStorage.removeItem('token');
        slist[1].textContent = 'Login';
    }

})
// =================sidebar=================




// Initialize the game
resetGame();
