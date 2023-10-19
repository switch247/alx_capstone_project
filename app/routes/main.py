from flask import Blueprint, jsonify, request,flash,abort,redirect,url_for,render_template,session
from app import db
import json
# from data import quizzes
# from app.models import user.User, user.user ...
from app.models.user import User
from app.routes.auth import login_required
from app.models.leaderboard import Leaderboard
import json

main = Blueprint('main', __name__)

with open('data.json') as json_file:
    quizzes = json.load(json_file)

    # AKfycbzWxARHNujCAnsZhUiK_FWdm6nodsGKm4dplFzdBgkTCwBuUuNopFbAR6xxiXasIHX0Lw
    # https://script.google.com/macros/s/AKfycbzWxARHNujCAnsZhUiK_FWdm6nodsGKm4dplFzdBgkTCwBuUuNopFbAR6xxiXasIHX0Lw/exec

    @main.route('/check_db_connection')
    def check_db_connection():
        try:
            db.session.execute("SELECT 1")
            return 'Database connected!'
        except Exception as e:
            return 'Database connection failed: ' + str(e)




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









