const wordGrid = document.getElementById('word-grid');
const keyboard = document.getElementById('keyboard');
const toggleWebcamBtn = document.getElementById('toggle-webcam');
const submitBtn = document.getElementById('submit');
const giveUpBtn = document.getElementById('give-up');
const webcamFeed = document.getElementById('webcam-feed');
const webcamPlaceholder = document.getElementById('webcam-placeholder');

let currentWord = '';
let currentRow = 0;
let targetWord = '';
let isRecording = false;
let submittedLetters = new Set();

// Initialize the word grid
for (let i = 0; i < 30; i++) {
    const letterBox = document.createElement('div');
    letterBox.classList.add('letter-box');
    wordGrid.appendChild(letterBox);
}

// Initialize the keyboard
'QWERTYUIOPASDFGHJKLZXCVBNM'.split('').forEach(letter => {
    const key = document.createElement('div');
    key.classList.add('key');
    key.textContent = letter;
    key.addEventListener('click', () => handleKeyPress(letter));
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
    } else if (currentRow === 5) {
        alert(`Game over! The word was ${targetWord}`);
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
    const words = ['APPLE', 'BRAVE', 'CACTUS', 'DANCE', 'EAGLE', 'FABLE', 'GRAPE', 'HONEY', 'IVORY', 'JOKER'];
    return words[Math.floor(Math.random() * words.length)];
}

async function startWebcam() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        webcamFeed.srcObject = stream;
        webcamPlaceholder.style.display = 'none';
        isRecording = true;
        toggleWebcamBtn.textContent = 'Stop Recording';

        // New : Send each frame of the video stream to the backend
        const videoTrack = stream.getVideoTracks()[0];
        const imageCapture = new ImageCapture(videoTrack);
        
        // Capture a frame every second and send it to the backend
        setInterval(async () => {
            const frame = await imageCapture.grabFrame();
            sendFrameToBackend(frame);
        }, 1000); // Send one frame per second; adjust frequency as needed
    } catch (err) {
        console.error("Error accessing the webcam:", err);
        alert("Failed to access the webcam. Please check your permissions.");
    }
}


async function sendFrameToBackend(frame) {
    // Create a canvas element to draw the captured frame
    const canvas = document.createElement('canvas');
    canvas.width = frame.width;
    canvas.height = frame.height;
    
    // Get the 2D drawing context for the canvas
    const context = canvas.getContext('2d');
    
    // Draw the captured frame onto the canvas
    context.drawImage(frame, 0, 0);
    
    // Convert the canvas content to a base64-encoded JPEG image
    const imageData = canvas.toDataURL('image/jpeg');

    // Send the image data to the backend for recognition
    const response = await fetch('/recognize/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ image: imageData }), // Send the image data as JSON
    });

    // Parse the JSON response from the backend
    const result = await response.json();
    
    // Log the recognition result to the console
    console.log('Recognition Result:', result);
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

// Initialize the game
resetGame();
