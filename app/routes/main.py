from flask import Blueprint, jsonify, request,flash,abort,redirect,url_for,render_template,session
from app import db
import json
# from data import quizzes
# from app.models import user.User, user.user ...
from app.models.user import User
from app.routes.auth import login_required
from app.models.leaderboard import Leaderboard


main = Blueprint('main', __name__)


quizzes = [
    {
        "id": 1,
        "title": "General Knowledge Quiz",
        "categories": ["General Knowledge"],
        "image": "https://source.unsplash.com/1600x900/?GeneralKnowledge",
        "number_of_questions": 5,
        "questions": [
          {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Madrid"],
            "correct_answer": "Paris"
            ,"hint":"hint x"
          },
          {
            "question": "Who painted the Mona Lisa?",
            "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo"],
            "correct_answer": "Leonardo da Vinci"
            ,"hint":"hint x"
          },
          {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Mars", "Jupiter", "Venus", "Mercury"],
            "correct_answer": "Mars"
            ,"hint":"hint x"
          },
          {
            "question": "Who wrote the play Hamlet?",
            "options": ["William Shakespeare", "Jane Austen", "Mark Twain", "Charles Dickens"],
            "correct_answer": "William Shakespeare"
            ,"hint":"hint x"
          },
          {
            "question": "What is the currency of Japan?",
            "options": ["Yen", "Euro", "Dollar", "Pound"],
            "correct_answer": "Yen"
            ,"hint":"hint x"
          }
        ]
      },
      {
        "id": 2,
        "title": "Science and Technology Quiz",
        "categories": ["Science and Technology"],
        "image": "https://source.unsplash.com/1600x900/?ScienceTechnology",
        "number_of_questions": 5,
        "questions": [
          {
            "question": "What is the chemical symbol for gold?",
            "options": ["Au", "Ag", "Fe", "Cu"],
            "correct_answer": "Au"
            ,"hint":"hint x"
          },
          {
            "question": "Who is considered the father of modern physics?",
            "options": ["Albert Einstein", "Isaac Newton", "Niels Bohr", "Galileo Galilei"],
            "correct_answer": "Albert Einstein"
            ,"hint":"hint x"
          },
          {
            "question": "What is the largest organ in the human body?",
            "options": ["Skin", "Heart", "Brain", "Liver"],
            "correct_answer": "Skin"
            ,"hint":"hint x"
          },
          {
            "question": "What is the process by which plants convert sunlight into energy called?",
            "options": ["Photosynthesis", "Respiration", "Fermentation", "Transpiration"],
            "correct_answer": "Photosynthesis"
            ,"hint":"hint x"
          },
          {
            "question": "What is the atomic number of oxygen?",
            "options": ["8", "6", "12", "16"],
            "correct_answer": "8"
            ,"hint":"hint x"
          }
        ]
      },
      {
        "id": 3,
        "title": "History Quiz",
        "categories": ["History"],
        "image": "https://source.unsplash.com/1600x900/?History",
        "number_of_questions": 5,
        "questions": [
          {
            "question": "In which year did World War II end?",
            "options": ["1945", "1939", "1918", "1941"],
            "correct_answer": "1945"
            ,"hint":"hint x"
          },
          {
            "question": "Who was the first President of the United States?",
            "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John F. Kennedy"],
            "correct_answer": "George Washington"
            ,"hint":"hint x"
          },
          {
            "question": "Which ancient civilization built the Great Wall of China?",
            "options": ["Chinese", "Roman", "Egyptian", "Incan"],
            "correct_answer": "Chinese"
            ,"hint":"hint x"
          },
          {
            "question": "Who is credited with discovering America?",
            "options": ["Christopher Columbus", "Marco Polo", "Vasco da Gama", "Amerigo Vespucci"],
            "correct_answer": "Christopher Columbus"
            ,"hint":"hint x"
          },
          {
            "question": "In which year did the Cold War end?",
            "options": ["1991", "1989", "1975", "1961"],
            "correct_answer": "1991"
            ,"hint":"hint x"
          }
        ]
      },

      {
        "id": 4,
        "title": "Geography Quiz",
        "categories": ["Geography"],
        "image": "https://source.unsplash.com/1600x900/?Geography",
        "number_of_questions": 5,
        "questions": [
          {
            "question": "What is the capital of Australia?",
            "options": ["Canberra", "Sydney", "Melbourne", "Perth"],
            "correct_answer": "Canberra"
            ,"hint":"hint x"
          },
          {
            "question": "Which is the longest river in the world?",
            "options": ["Nile", "Amazon", "Yangtze", "Mississippi"],
            "correct_answer": "Nile"
            ,"hint":"hint x"
          },
          {
            "question": "Which country is known as the 'Land of the Rising Sun'?",
            "options": ["Japan", "China", "India", "South Korea"],
            "correct_answer": "Japan"
            ,"hint":"hint x"
          },
          {
            "question": "What is the largest desert in the world?",
            "options": ["Sahara Desert", "Arabian Desert", "Gobi Desert", "Kalahari Desert"],
            "correct_answer": "Sahara Desert"
            ,"hint":"hint x"
          },
          {
            "question": "Which country is home to the famous landmark, Machu Picchu?",
            "options": ["Peru", "Mexico", "Brazil", "Chile"],
            "correct_answer": "Peru"
            ,"hint":"hint x"
          }
        ]
      },

      {
        "id": 5,
        "title": "Sports Quiz",
        "categories": ["Sports"],
        "image": "https://source.unsplash.com/1600x900/?Sports",
        "number_of_questions": 5,
        "questions": [
          {
            "question": "Who won the FIFA World Cup in 2018?",
            "options": ["France", "Croatia", "Brazil", "Germany"],
            "correct_answer": "France"
            ,"hint":"hint x"
          },
          {
            "question": "In which sport is the Ryder Cup contested?",
            "options": ["Golf", "Tennis", "Basketball", "Cricket"],
            "correct_answer": "Golf"
            ,"hint":"hint x"
          },
          {
            "question": "Who holds the record for the most Grand Slam titles in tennis?",
            "options": ["Roger Federer", "Rafael Nadal", "Novak Djokovic", "Serena Williams"],
            "correct_answer": "Novak Djokovic"
            ,"hint":"hint x"
          },
          {
            "question": "Which country won the most medals in the 2020 Tokyo Olympics?",
            "options": ["United States", "China", "Japan", "Russia"],
            "correct_answer": "United States"
            ,"hint":"hint x"
          },
          {
            "question": "Who is the all-time leading scorer in NBA history?",
            "options": ["Kareem Abdul-Jabbar", "LeBron James", "Michael Jordan", "Kobe Bryant"],
            "correct_answer": "Kareem Abdul-Jabbar"
            ,"hint":"hint x"
          }
        ]
      },
      {
        "id": 6,
        "title": "Movies and TV Quiz",
        "categories": ["Movies and TV"],
        "image": "https://source.unsplash.com/1600x900/?MoviesTV",
        "number_of_questions": 5,
        "questions": [
          {
            "question": "Who directed the movie 'The Shawshank Redemption'?",
            "options": ["Frank Darabont", "Martin Scorsese", "Steven Spielberg", "Quentin Tarantino"],
            "correct_answer": "Frank Darabont"
            ,"hint":"hint x"
          },
          {
            "question": "Which film won the Academy Award for Best Picture in 2020?",
            "options": ["Parasite", "1917", "Joker", "Once Upon a Time in Hollywood"],
            "correct_answer": "Parasite"
            ,"hint":"hint x"
          },
          {
            "question": "Who played the character of James Bond in the film 'Casino Royale'?",
            "options": ["Daniel Craig", "Pierce Brosnan", "Sean Connery", "Roger Moore"],
            "correct_answer": "Daniel Craig"
            ,"hint":"hint x"
          },
          {
            "question": "Which actor won an Oscar for portraying the Joker in 'The Dark Knight'?",
            "options": ["Heath Ledger", "Joaquin Phoenix", "Jared Leto", "Jack Nicholson"],
            "correct_answer": "Heath Ledger"
            ,"hint":"hint x"
          },
          {
            "question": "Which movie features the quote 'May the Force be with you'?",
            "options": ["Star Wars", "The Godfather", "Forrest Gump", "Titanic"],
            "correct_answer": "Star Wars"
            ,"hint":"hint x"
          }
        ]
      },
      {
        "id": 7,
        "title": "Music Quiz",
        "categories": ["Music"],
        "image": "https://source.unsplash.com/1600x900/?Music",
        "number_of_questions": 5,
        "questions": [
          {
            "question": "Who is known as the 'King of Pop'?",
            "options": ["Michael Jackson", "Elvis Presley", "Frank Sinatra", "Prince"],
            "correct_answer": "Michael Jackson"
            ,"hint":"hint x"
          },
          {
            "question": "Which band is famous for the hit song 'Bohemian Rhapsody'?",
            "options": ["Queen", "The Beatles", "Led Zeppelin", "The Rolling Stones"],
            "correct_answer": "Queen"
            ,"hint":"hint x"
          },
          {
            "question": "Who is the lead vocalist of the band Coldplay?",
            "options": ["Chris Martin", "Bono", "Thom Yorke", "Brandon Flowers"],
            "correct_answer": "Chris Martin"
            ,"hint":"hint x"
          },
          {
            "question": "Which singer released the album 'Lemonade' in 2016?",
            "options": ["Beyoncé", "Taylor Swift", "Adele", "Rihanna"],
            "correct_answer": "Beyoncé"
            ,"hint":"hint x"
          },
          {
            "question": "What is the best-selling album of all time?",
            "options": ["Thriller by Michael Jackson", "The Dark Side of the Moon by Pink Floyd", "Back in Black by AC/DC", "Bat Out of Hell by Meat Loaf"],
            "correct_answer": "Thriller by Michael Jackson"
            ,"hint":"hint x"
          }
        ]
      },
      {
        "id": 8,
        "title": "Literature Quiz",
        "categories": ["Literature"],
        "image": "https://source.unsplash.com/1600x900/?Literature",
        "number_of_questions": 5,
        "questions": [
          {
            "question": "Who wrote the novel 'Pride and Prejudice'?",
            "options": ["Jane Austen", "Emily Brontë", "Charlotte Brontë", "Virginia Woolf"],
            "correct_answer": "Jane Austen"
            ,"hint":"hint x"
          },
          {
            "question": "Which author wrote the 'Harry Potter' book series?",
            "options": ["J.K. Rowling", "Stephen King", "George R.R. Martin", "Dan Brown"],
            "correct_answer": "J.K. Rowling"
            ,"hint":"hint x"
          },
          {
            "question": "Who is the author of the play 'Romeo and Juliet'?",
            "options": ["William Shakespeare", "Oscar Wilde", "Arthur Miller", "Tennessee Williams"],
            "correct_answer": "William Shakespeare"
            ,"hint":"hint x"
          },
          {
            "question": "Which novel begins with the line 'It was a bright cold day in April, and the clocks were striking thirteen'?",
            "options": ["1984 by George Orwell", "Brave New World by Aldous Huxley", "Fahrenheit 451 by Ray Bradbury", "The Catcher in the Rye by J.D. Salinger"],
            "correct_answer": "1984 by George Orwell"
            ,"hint":"hint x"
          },
          {
            "question": "Who is the author of the 'Lord of the Rings' trilogy?",
            "options": ["J.R.R. Tolkien", "C.S. Lewis", "Philip Pullman", "George R.R. Martin"],
            "correct_answer": "J.R.R. Tolkien"
            ,"hint":"hint x"
          }
        ]
      },
      {
        "id": 9,
        "title": "Art and Culture Quiz",
        "categories": ["Art and Culture"],
        "image": "https://source.unsplash.com/1600x900/?ArtCulture",
        "number_of_questions": 5,
        "questions": [
          {
            "question": "Who painted the famous artwork 'The Starry Night'?",
            "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
            "correct_answer": "Vincent van Gogh"
            ,"hint":"hint x"
          },
          {
            "question": "Which artist is associated with the creation of the Mona Lisa?",
            "options": ["Leonardo da Vinci", "Michelangelo", "Raphael", "Salvador Dalí"],
            "correct_answer": "Leonardo da Vinci"
            ,"hint":"hint x"
          },
          {
            "question": "Who composed the symphony 'Symphony No. 5 in C minor'?",
            "options": ["Ludwig van Beethoven", "Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Franz Schubert"],
            "correct_answer": "Ludwig van Beethoven"
            ,"hint":"hint x"
          }]},

      {
        "id": 10,
        "title": "Sports Quiz",
        "categories": ["Sports"],
        "image": "https://source.unsplash.com/1600x900/?Sports",
        "number_of_questions": 5,
        "questions": [
          {
            "question": "Which country won the FIFA World Cup in 2018?",
            "options": ["France", "Brazil", "Germany", "Argentina"],
            "correct_answer": "France"
            ,"hint":"hint x"
          },
          {
            "question": "Who is the all-time leading scorer in NBA history?",
            "options": ["Kareem Abdul-Jabbar", "LeBron James", "Michael Jordan", "Kobe Bryant"],
            "correct_answer": "Kareem Abdul-Jabbar"
            ,"hint":"hint x"
          },
          {
            "question": "Which tennis player has won the most Grand Slam titles in the men's singles category?",
            "options": ["Roger Federer", "Rafael Nadal", "Novak Djokovic", "Pete Sampras"],
            "correct_answer": "Roger Federer"
            ,"hint":"hint x"
          },
          {
            "question": "Which athlete has the most Olympic gold medals of all time?",
            "options": ["Michael Phelps", "Usain Bolt", "Carl Lewis", "Simone Biles"],
            "correct_answer": "Michael Phelps"
            ,"hint":"hint x"
          },
          {
            "question": "Which country hosted the Summer Olympics in 2021?",
            "options": ["Japan", "China", "Brazil", "United States"],
            "correct_answer": "Japan"
            ,"hint":"hint x"
          }
        ]
      },
      {
        "id": 11,
        "title": "Science Quiz",
        "categories": ["Science"],
        "image": "https://source.unsplash.com/1600x900/?Science",
        "number_of_questions": 5,
        "questions": [
          {
            "question": "What is the chemical symbol for the element gold?",
            "options": ["Au", "Ag", "Go", "Gl"],
            "correct_answer": "Au"
            ,"hint":"hint x"
          },
          {
            "question": "Which planet is known as the 'Red Planet'?",
            "options": ["Mars", "Venus", "Jupiter", "Saturn"],
            "correct_answer": "Mars"
            ,"hint":"hint x"
          },
          {
            "question": "What is the largest organ in the human body?",
            "options": ["Skin", "Liver", "Heart", "Brain"],
            "correct_answer": "Skin"
            ,"hint":"hint x"
          },
          {
            "question": "What is the unit of measurement for electric current?",
            "options": ["Ampere", "Watt", "Ohm", "Volt"],
            "correct_answer": "Ampere"
            ,"hint":"hint x"
          },
          {
            "question": "What is the process by which plants convert sunlight into energy?",
            "options": ["Photosynthesis", "Respiration", "Transpiration", "Fermentation"],
            "correct_answer": "Photosynthesis"
            ,"hint":"hint x"
          }
        ]
      },
      {
        "id": 12,
        "title": "History Quiz",
        "categories": ["History"],
        "image": "https://source.unsplash.com/1600x900/?History",
        "number_of_questions": 5,
        "questions": [
          {
            "question": "Who was the first President of the United States?",
            "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John F. Kennedy"],
            "correct_answer": "George Washington"
            ,"hint":"hint x"
          },
          {
            "question": "Which war was fought between the North and South regions of the United States from 1861 to 1865?",
            "options": ["American Civil War", "World War I", "World War II", "Vietnam War"],
            "correct_answer": "American Civil War"
            ,"hint":"hint x"
          },
          {
            "question": "Who was the leader of the Soviet Union during World War II?",
            "options": ["Joseph Stalin", "Vladimir Lenin", "Nikita Khrushchev", "Mikhail Gorbachev"],
            "correct_answer": "Joseph Stalin"
            ,"hint":"hint x"
          },
          {
            "question": "Which ancient civilization built the Great Pyramids of Giza?",
            "options": ["Ancient Egyptians", "Ancient Greeks", "Mayans", "Romans"],
            "correct_answer": "Ancient Egyptians"
            ,"hint":"hint x"
          },
          {
            "question": "In which year did Christopher Columbus reach the Americas?",
            "options": ["1492", "1607", "1776", "1812"],
            "correct_answer": "1492"
            ,"hint":"hint x"
          }
        ]
      },
      {
        "id": 13,
        "title": "Geography Quiz",
        "categories": ["Geography"],
        "image": "https://source.unsplash.com/1600x900/?Geography",
        "number_of_questions": 5,
        "questions": [
          {
            "question": "What is the capital of Australia?",
            "options": ["Canberra", "Sydney", "Melbourne", "Brisbane"],
            "correct_answer": "Canberra"
            ,"hint":"hint x"
          },
          {
            "question": "Which is the largest ocean on Earth?",
            "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
            "correct_answer": "Pacific Ocean"
            ,"hint":"hint x"
          },
          {
            "question": "Which country is known as the 'Land of the Rising Sun'?",
            "options": ["Japan", "China", "South Korea", "Vietnam"],
            "correct_answer": "Japan"
            ,"hint":"hint x"
          },
          {
            "question": "What is the longest river in the world?",
            "options": ["Nile River", "Amazon River", "Mississippi River", "Yangtze River"],
            "correct_answer": "Nile River"
            ,"hint":"hint x"
          },
          {
            "question": "Which mountain range is the longest in the world?",
            "options": ["The Andes", "The Himalayas", "The Rockies", "The Alps"],
            "correct_answer": "The Andes"
            ,"hint":"hint x"
          }
        ]
      },
      {
        "id": 14,
        "title": "Technology Quiz",
        "categories": ["Technology"],
        "image": "https://source.unsplash.com/1600x900/?Technology",
        "number_of_questions": 5,
        "questions": [
          {
            "question": "Who is the CEO of Tesla Motors?",
            "options": ["Elon Musk", "Jeff Bezos", "Mark Zuckerberg", "Tim Cook"],
            "correct_answer": "Elon Musk"
            ,"hint":"hint x"
          },
          {
            "question": "What does the acronym 'URL' stand for?",
            "options": ["Uniform Resource Locator", "Universal Reference Language", "Unified Research Link", "User Retrieval Line"],
            "correct_answer": "Uniform Resource Locator"
            ,"hint":"hint x"
          },
          {
            "question": "Which company developed the first smartphone?",
            "options": ["IBM", "Samsung", "Apple", "BlackBerry"],
            "correct_answer": "IBM"
            ,"hint":"hint x"
          },
          {
            "question": "What does 'HTML' stand for in web development?",
            "options": ["Hypertext Markup Language", "Hyperlink and Text Markup Language", "Home Tool Markup Language", "Hyperloop Transport and Machine Learning"],
            "correct_answer": "Hypertext Markup Language"
            ,"hint":"hint x"
          },
          {
            "question": "Which programming language is often used for developing Android apps?",
            "options": ["Java", "Python", "C++", "Ruby"],
            "correct_answer": "Java"
            ,"hint":"hint x"
          }
        ]
      }
]


leaderboard=[{'name':'chala','score':"12"},{'name':'chube','score':"11"},{'name':'chebete','score':"10"}]

# AKfycbzWxARHNujCAnsZhUiK_FWdm6nodsGKm4dplFzdBgkTCwBuUuNopFbAR6xxiXasIHX0Lw
# https://script.google.com/macros/s/AKfycbzWxARHNujCAnsZhUiK_FWdm6nodsGKm4dplFzdBgkTCwBuUuNopFbAR6xxiXasIHX0Lw/exec

@main.route('/check_db_connection')
def check_db_connection():
    try:
        db.session.execute("SELECT 1")
        return 'Database connected!'
    except Exception as e:
        return 'Database connection failed: ' + str(e)



# @main.route('/x', methods=['GET'])
# def hello():
#     return  render_template('index.html')

@main.route('/', methods=['GET'])
def home():
    return render_template('pages/home.html',quizzes=quizzes)
@main.route('/quiz', methods=['GET'])
def hub():
    return render_template('pages/hub.html',quizzes=quizzes)
@main.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
@login_required
def quiz(quiz_id):
    if quiz_id > len(quizzes):
        return "Quiz not found"
    # if request.method == 'POST':
    #     score = 0
    #     num_questions = quizzes[quiz_id - 1]['num_questions']
    #     for i in range(num_questions):
    #         answer = request.form.get(f'question_{i+1}')
    #         if answer is not None and int(answer) == quizzes[quiz_id - 1]['questions'][i]['answer']:
    #             score += 1

    #     leaderboard.append({'quiz_id': quiz_id, 'score': score})

    #     return redirect(url_for('leaderboard_func'))
    email = session.get('email')
    leaderboard_entry = Leaderboard.query.filter_by(email=email, quiz_id=quizzes[quiz_id - 1]).first()
    if leaderboard_entry:
        return render_template('pages/quiz.html',taken=True, quiz=quizzes[quiz_id - 1])
    else:
        return render_template('pages/quiz.html', quiz=quizzes[quiz_id - 1])
@main.route('/leaderboard', methods=['POST'])
def add_leaderboard_entry_route():
    try:
        data = request.get_json()
        email = session.get('email')
        quiz_id = data.get('quiz_id')
        score = data.get('score')
        time = data.get('time')

        add_leaderboard_entry(email, quiz_id, score, time)

        return jsonify({'status': 'success'}),200
    except Exception as e:
        return jsonify({'status': 'failed'}), 500 

def add_leaderboard_entry(email, quiz_id, score, time):
    try:
        existing_entry = Leaderboard.query.filter_by(email=email, quiz_id=quiz_id).first()
        if existing_entry:
            score_time_ratio = existing_entry.score / existing_entry.time
            new_score_time_ratio = score / time

            if new_score_time_ratio > score_time_ratio:
                existing_entry.score = score
                existing_entry.time = time
                db.session.commit()
        else:
            new_entry = Leaderboard(email=email, quiz_id=quiz_id, score=score, time=time)
            db.session.add(new_entry)
            db.session.commit()
    except Exception as e:
        print('failed',e)
        return jsonify({"status":"failed"})
    

@main.route('/leaderboard', methods=['GET'])
def leaderboard_func():
    # leaderboard_sorted = sorted(leaderboard, key=lambda x: x['score'], reverse=True)
    # return render_template('pages/leaderboard.html', leaderboard=leaderboard_sorted)
    leaderboard_items = Leaderboard.query.order_by(Leaderboard.score / Leaderboard.time).all()
    return render_template('pages/leaderboard.html', leaderboard_items=leaderboard_items)









