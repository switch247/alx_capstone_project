document.addEventListener('DOMContentLoaded', () => {
    setTimeout(1000)
    var q= document.getElementById('p').innerText
    var validJsonString = q.replace(/'/g, '"');
    var quiz = JSON.parse(validJsonString)
    console.log(quiz)
    q.innerText=''
    const progress = document.getElementById('progress');
    const questionElement = document.getElementById('question');
    const options = Array.from(document.getElementsByClassName('option'));
    const nextButton = document.getElementById('next-button');
    const prevButton = document.getElementById('prev-button');
    const resultDiv = document.getElementById('result');

    let currentQuestion = 0;
    let score = 0;

    function loadQuestion() {
        const question = quiz[currentQuestion];
        questionElement.textContent = question.question;
        
        options.forEach((option, index) => {
            option.textContent = question.options[index];
            option.onclick = () => selectOption(index);
        });
    }

    function selectOption(selectedIndex) {
        const question = quiz[currentQuestion];
        const correctIndex = question.answer;

        if (selectedIndex === correctIndex) {
            score++;
        }
        

    //    progress.style.width = `${((currentQuestion + 1) / quiz.length) * 100}%`;

        options.forEach((option) => {
            option.disabled = true;
        });

        if (currentQuestion === quiz.length - 1) {
            nextButton.textContent = 'Finish';
        }

        if (currentQuestion === quiz.length) {
            showResult();
        } else {
            nextButton.disabled = false;
        }
    }

    function showResult() {
        const totalScore = Math.floor((score / quiz.length) * 100);
        resultDiv.textContent = `You scored ${totalScore}%`;

        // Save the score to local storage or send it to the server
        prevButton.style.display='none';
        nextButton.style.display = 'none';
        options.forEach((option) => {
            option.style.display = 'none';
        });
        // Get the URL parameters
        const urlParams = window.location.href.split('/')
        const qid = urlParams[urlParams.length - 1];
        console.log(qid)
        // Get the value of a specific parameter
        // Store the value in local storage
        // localStorage.setItem('paramValue', paramValue);
    }

    nextButton.onclick = () => {
       progress.style.width = `${((currentQuestion + 1) / quiz.length) * 100}%`;
        if( nextButton.textContent !== 'Finish' ){
        currentQuestion++;
        loadQuestion();
        nextButton.disabled = true;
        options.forEach((option) => {
            option.disabled = false;
        });
    }
        else{
            showResult()
        }
    };
    prevButton.onclick = () => {
        if(currentQuestion>0){        
        progress.style.width = `${((currentQuestion - 1) / quiz.length) * 100}%`;
         currentQuestion--
         loadQuestion();
         nextButton.disabled = true;
         options.forEach((option) => {
             option.disabled = false;
         });
        }
    
     };

    loadQuestion();
});


