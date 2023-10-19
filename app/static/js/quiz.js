// Quiz data
// const quizData = JSON.parse(document.getElementById('p').textContent);
var q= document.getElementById('p').innerText
var validJsonString = q.replace(/'/g, '"');
var QD = JSON.parse(validJsonString)
var quizData = JSON.parse(validJsonString).questions
q.innerHTML=''
// console.log(QD)
// Get elements
const quizElement = document.getElementById('quiz');
const progressBarElement = document.getElementById('progress');
const timerElement = document.getElementById('timer');
const hintElement = document.getElementById('hint');
const hintButtonElement = document.querySelector('.btn-hint');
const questionElement = document.getElementById('question');
const optionsElement = document.getElementById('options');
const restartButtonElement = document.getElementById('restart-button');
const nextButtonElement = document.getElementById('next-button');
const resultElement = document.getElementById('result');


// Quiz state

let currentQuestionIndex = 0;
let score = 0;
let timer;

let hintCount = 0;

let timerInterval;
let totalTime = 0;

function startTOTTimer() {
  timerInterval = setInterval(() => {
    totalTime++;
    // console.log(totalTime);
  }, 1000);
}

function stopTOTTimer() {
  clearInterval(timerInterval);
}

function resetTOTTimer() {
  clearInterval(timerInterval);
  totalTime = 0;
}

// Start the quiz
function startQuiz() {
    totalTime = 0;
    currentQuestionIndex=0;
    hintCount = 0;
    score = 0;
    hintButtonElement.classList.remove('hidden');
    timerElement.classList.remove('hidden');
    questionElement.classList.remove('hidden');
    optionsElement.classList.remove('hidden');

    restartButtonElement.classList.add('hidden');
    resultElement.textContent = '';
    resetTOTTimer();
    startTOTTimer();
    loadQuestion();
}

// Load question and options
function loadQuestion() {
    startTimer();
    const currentQuestion = quizData[currentQuestionIndex];
    questionElement.textContent = currentQuestion.question;
    optionsElement.innerHTML = '';
    currentQuestion.options.forEach((option, index) => {
        const button = document.createElement('button');
        button.classList.add('btn') 
        // button.classList.add('btn-primary')
        button.textContent = option;
        button.addEventListener('click', () => selectOption(index));
        optionsElement.appendChild(button);
  });
  updateProgress();
  updateButtons();
}

// Select an option
function selectOption(optionIndex) {
  const currentQuestion = quizData[currentQuestionIndex];
  const selectedOption = currentQuestion.options[optionIndex];

  if (selectedOption === currentQuestion.correct_answer) {
    score++;
    optionsElement.children[optionIndex].classList.add('correct');
  }
  else{
    optionsElement.children[optionIndex].classList.add('wrong');
  }

  hintElement.textContent = '';
//   hintCount = 0;

  disableOptions();
  updateButtons();
 
  if (currentQuestionIndex === quizData.length-1 ) {
    endQuiz();
  }
  else
  {
    goToNextQuestion();
  }
}

// Disable options after selecting an option
function disableOptions() {
  Array.from(optionsElement.children).forEach((option) => {
    option.disabled = true;
    const currentQuestion = quizData[currentQuestionIndex];
    if (option.innerText === currentQuestion.correct_answer) {
        option.classList.add('correct');
    }
  });
}

// Update progress bar
function updateProgress() {
  const progress = ((currentQuestionIndex + 1 ) / quizData.length) * 100;
  progressBarElement.style.width = `${progress}%`;
}

// Update previous and next buttons
function updateButtons() {
//   nextButtonElement.disabled = !optionsElement.querySelector('.correct');
}

// Start the timer
function startTimer() {
  clearInterval(timer);
  let time = 11;
  timer = setInterval(() => {
    time--;
    timerElement.textContent = `Time: ${time}s`;
    if (time===0){ 
        //  clearInterval(timer);
        if(currentQuestionIndex===quizData.length-1)
        endQuiz()
    else
        goToNextQuestion();
    }
    
  }, 1000);
}



// Show a hint
function showHint() {
  if (hintCount < 3) {
    hintElement.disabled=false
    hintCount++;
    hintElement.textContent = `Hint: ${quizData[currentQuestionIndex].hint}`;
    hintElement.disabled=true
    hintButtonElement.disabled = true;
  }

  if (hintCount === 3) {
    hintButtonElement.disabled = true;
  }
}

// Go to the next question
function goToNextQuestion() {
    setTimeout(function() {
        // Code to be executed after 1 second
        if(currentQuestionIndex < quizData.length){
            currentQuestionIndex++;
            hintButtonElement.disabled = false;
            loadQuestion();
        }
        else{
            endQuiz()
        }
      }, 1000);
    
}

// End the quiz
function endQuiz() {
setTimeout(function() {
    clearInterval(timer);
    stopTOTTimer();
    //   quizElement.classList.add('hidden');
    hintButtonElement.classList.add('hidden');
    questionElement.classList.add('hidden');
    optionsElement.classList.add('hidden');
    timerElement.classList.add('hidden');
    // nextButtonElement.classList.add('hidden');
    nextButtonElement.disabled=true
    restartButtonElement.classList.remove('hidden');
    const totalScore = Math.floor((score / quizData.length) * 100);
    // resultDiv.textContent = `You scored ${totalScore}%`;
    resultElement.textContent = `Your Score: ${score}/${quizData.length} ${totalScore}%`;

    Array.from(optionsElement.children).forEach((option) => {
        optionsElement.removeChild(option);
    });
    console.log(QD.id,totalScore,totalTime)
    addLeaderboardEntry(QD.id,score,totalTime);
},1000);
}

// Event listeners
hintButtonElement.addEventListener('click', showHint);
nextButtonElement.addEventListener('click', goToNextQuestion);
restartButtonElement.addEventListener('click', startQuiz);

// Start the quiz
// startQuiz();




// update the leaderboard
function addLeaderboardEntry(quizId, score, time) {
  fetch('/leaderboard', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      quiz_id: quizId,
      score: score,
      time: time
    })
  })
  .then(response => {
    if (response.ok) {
      console.log('Leaderboard entry added successfully');
    } else {
      console.error('Failed to add leaderboard entry');
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
}
