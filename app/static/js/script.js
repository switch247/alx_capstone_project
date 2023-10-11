const startButton = document.getElementById('start-btn');
const questionContainer = document.getElementById('question-container');
const questionElement = document.getElementById('question');
const optionsButtons = document.getElementById('options').querySelectorAll('.btn');
const scoreContainer = document.getElementById('score-container');
const scoreElement = document.getElementById('score');

let currentQuestionIndex = 0;
let score = 0;

startButton.addEventListener('click', startQuiz);
optionsButtons.forEach(button => {
    button.addEventListener('click', selectOption);
});

function startQuiz() {
    startButton.classList.add('hide');
    questionContainer.classList.remove('hide');
    scoreContainer.classList.add('hide');
    currentQuestionIndex = 0;
    score = 0;
    showQuestion();
}

function showQuestion() {
    resetOptions();
    const question = questions[currentQuestionIndex];
    questionElement.innerText = question.question;
    optionsButtons.forEach((button, index) => {
        button.innerText = question.options[index];
    });
}

function resetOptions() {
    optionsButtons.forEach(button => {
        button.classList.remove('correct', 'wrong');
    });
}

function selectOption(e) {
    const selectedButton = e.target;
    const question = questions[currentQuestionIndex];
    const selectedOption = question.options.indexOf(selectedButton.innerText);
    if (selectedOption === question.answer) {
        selectedButton.classList.add('correct');
        score++;
    } else {
        selectedButton.classList.add('wrong');
    }
    setTimeout(1000)
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
        setTimeout(showQuestion, 1000);
    } else {
        showScore();
    }
}

function showScore() {
    questionContainer.classList.add('hide');
    scoreContainer.classList.remove('hide');
    scoreElement.innerText = score;
}

const questions = [
    {
        question: 'Question 1',
        options: ['A', 'Option 2', 'Option 3', 'Option 4'],
        answer: 0
    },
    {
        question: 'Question 2',
        options: ['Option 1', 'B', 'Option 3', 'Option 4'],
        answer: 1
    },
    {
        question: 'Question 3',
        options: ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
        answer: 2
    },
    {
        question: 'Question 4',
        options: ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
        answer: 3
    }
];
