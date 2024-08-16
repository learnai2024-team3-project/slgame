const alphabetLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const alphabetButtonsContainer = document.querySelector('.alphabet-buttons');
const demoImage = document.getElementById('demo-image');
const webcamVideo = document.getElementById('webcam');
const handShapeExplanation = document.getElementById('hand-shape-explanation');
const recognitionResult = document.getElementById('recognition-result');
const userScore = document.getElementById('user-score');

let path = window.location.pathname;
const directoryPath = path.substring(0, path.lastIndexOf("/"));

let currentLetter = '';
let userName = 'User'; // This should be set by user input or login
let score = 0;
let strTemp = '';

// Initialize alphabet buttons
alphabetLetters.split('').forEach(letter => {
    const button = document.createElement('button');
    button.className = 'alphabet-button';
    button.textContent = letter;
    button.onclick = () => selectLetter(letter);
    alphabetButtonsContainer.appendChild(button);
});

function selectLetter(letter) {
    // Reset all buttons to default color
    document.querySelectorAll('.alphabet-button').forEach(btn => {
        btn.classList.remove('selected');
    });

    currentLetter = letter;
    
    // Change the color of the selected button to light brown
    const selectedButton = document.querySelector(`.alphabet-button:nth-child(${alphabetLetters.indexOf(letter) + 1})`);
    selectedButton.classList.add('selected');

    // Dynamically update the demo image source using Django static files
    demoImage.src = "{% static 'images/tutorial/' %}" + letter.toLowerCase() + ".png";
    demoImage.alt = `ASL hand shape for letter ${letter}`;
    handShapeExplanation.textContent = `Demonstrating hand shape for letter ${letter}`;
}

async function startWebcam() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        webcamVideo.srcObject = stream;
    } catch (error) {
        console.error("Error accessing the webcam:", error);
        handShapeExplanation.textContent = "Error accessing the webcam. Please check your permissions and try again.";
    }
}

startWebcam();

async function startInput() {
    if (!currentLetter) {
        alert("Please select a letter first!");
        return;
    }
    
    // Here we would typically start the hand detection process
    // For this example, we'll use a placeholder function
    const detectedLetter = await detectHandShape();
    
    if (detectedLetter === currentLetter) {
        score += 10;
        recognitionResult.textContent = `Correct! The detected hand shape matches ${currentLetter}`;
    } else {
        recognitionResult.textContent = `Incorrect. The detected hand shape does not match ${currentLetter}`;
    }
    
    updateUserScore();
}

function completeAction() {
    // Placeholder for the complete action
    alert("Complete action is not yet implemented.");
}

async function detectHandShape() {
    // This is a placeholder for the actual hand shape detection
    // In a real implementation, this would use the YOLOv8 model
    return alphabetLetters[Math.floor(Math.random() * alphabetLetters.length)];
}

function updateUserScore() {
    userScore.textContent = `${userName}'s current score: ${score}`;
}

// Initialize user score
updateUserScore();

// Error handling for image loading
demoImage.onerror = function() {
    console.error("Error loading image:", demoImage.src);
    handShapeExplanation.textContent = `Error loading image. Please try another letter or check your internet connection.`;
};