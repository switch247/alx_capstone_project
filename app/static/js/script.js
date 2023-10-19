var q= document.getElementById('p').innerText
var validJsonString = q.replace(/'/g, '"');
var quizData = JSON.parse(validJsonString)
console.log(quizData, quizData.length)

// Get quiz data from local storage
// const quizData = JSON.parse(localStorage.getItem('quiz'));


// Get elements
const questionElement = document.getElementById('question');
const optionsElement = document.getElementById('options');
const prevButton = document.getElementById('prev-button');
const nextButton = document.getElementById('next-button');
const resultElement = document.getElementById('result');


// Initialize current question index and score
let currentQuestionIndex = 0;
let score = 0;

// Load question and options
function loadQuestion() {
  const currentQuestion = quizData[currentQuestionIndex];
  questionElement.textContent = currentQuestion.question;

  optionsElement.innerHTML = '';
  currentQuestion.options.forEach((option, index) => {
    const button = document.createElement('button');
    button.classList.add('btn')
    button.textContent = option;
    button.disabled = option === localStorage.getItem(`selectedOption_${currentQuestionIndex}`);

    button.addEventListener('click', () => selectOption(index));
    optionsElement.appendChild(button);
  });

  updateButtons();
}

// Select an option
function selectOption(optionIndex) {
  const currentQuestion = quizData[currentQuestionIndex];
  const selectedOption = currentQuestion.options[optionIndex];

  // Store selected option in local storage
  localStorage.setItem(`selectedOption_${currentQuestionIndex}`, selectedOption);

  updateButtons();
}

// Update previous and next buttons
function updateButtons() {
  prevButton.disabled = currentQuestionIndex === 0;
  nextButton.disabled = currentQuestionIndex === quizData.length - 1;
}

// Go to the previous question
function goToPreviousQuestion() {
  currentQuestionIndex--;
  loadQuestion();
}

// Go to the next question
function goToNextQuestion() {
  currentQuestionIndex++;
  loadQuestion();
}

// Calculate and display the score
function calculateScore() {
  score = 0;
  quizData.forEach((question, index) => {
    const selectedOption = localStorage.getItem(`selectedOption_${index}`);
    if (selectedOption === question.correct_answer) {
      score++;
    }
  });

  // Display the score
  resultElement.textContent = `Your Score: ${score}`;

  // Clear local storage
  localStorage.clear();
}

// Event listeners
prevButton.addEventListener('click', goToPreviousQuestion);
nextButton.addEventListener('click', goToNextQuestion);
nextButton.addEventListener('click', () => {
  if (currentQuestionIndex === quizData.length - 1) {
    calculateScore();
  }
});

// Load initial question
loadQuestion();
