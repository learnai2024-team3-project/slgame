const wordGrid = document.getElementById('word-grid');
const keyboard = document.getElementById('keyboard');
const toggleWebcamBtn = document.getElementById('toggle-webcam');
const submitBtn = document.getElementById('submit');
const giveUpBtn = document.getElementById('give-up');
const webcamFeed = document.getElementById('webcam-feed');
const webcamPlaceholder = document.getElementById('webcam-placeholder');

const sidebar = document.getElementById('sidebar');
const slist = sidebar.querySelectorAll('a');

let currentWord = '';
let currentRow = 0;
let targetWord = '';
let isRecording = false;
let submittedLetters = new Set();

// Initialize the word grid
for (let i = 0; i < 20; i++) {
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
        resetGame();
    } else if (currentRow === 3) {       // 更改可猜的次數
        alert(`Game over! The word was ${targetWord}.`);
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
    return wordList[Math.floor(Math.random() * wordList.length)];
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

    const currentUrl = window.location.origin;

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

    // Display "Recognizing" message
    let overlayMessage = document.getElementById('overlay-message');
    if (!overlayMessage) {
        overlayMessage = document.createElement('div');
        overlayMessage.id = 'overlay-message';
        overlayMessage.textContent = 'Recognizing...';

        // Get video or img container
        const webcamContainer = document.getElementById('webcam-container');
        webcamContainer.appendChild(overlayMessage);  // Adding message to the container
    }

    overlayMessage.style.display = 'block'; // Display message

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

        // Display tje recognized image
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
        // Hide "Recognizing" message
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
        imageElement.style.display = 'none';  // Hide recoginzed image
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

    // Draw video frames onto canvas
    context.drawImage(webcamFeed, 0, 0, canvas.width, canvas.height);

    // Convert canvas content to base64 image data
    const imageData = canvas.toDataURL('image/png').replace('data:image/png;base64,', '');
   
    if (!imageData || imageData === "" || imageData === "data:,") {
        // If the image content is empty, it will not be processed.
        console.log("imageData was empty!");
        toggleWebcamBtn.disabled = false;
        return
    }
   
    submitImage(imageData);

    // Stop camera streaming
    const stream = webcamFeed.srcObject;
    const tracks = stream.getTracks();

    tracks.forEach(track => {
        track.stop();
    });

    webcamFeed.srcObject = null;  //Clear the srcObject of the video element
}

toggleWebcamBtn.addEventListener('click', toggleWebcam);

submitBtn.addEventListener('click', submitWord);

giveUpBtn.addEventListener('click', giveUpThisTurn);

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
    } else if (event.key === 'Esc') {
        giveUpThisTurn();
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

function giveUpThisTurn() {
    alert(`The word was ${targetWord}`);
    resetGame();
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
    slist[2].textContent = 'Logout';
}

// =================sidebar=================


// Initialize the game
resetGame();