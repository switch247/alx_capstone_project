from flask import Blueprint, jsonify, request,flash,abort,redirect,url_for,render_template
from app import db
import json
# from data import quizzes
# from app.models import user.User, user.user ...
from app.models.user import User
from app.routes.auth import login_required


main = Blueprint('main', __name__)


quizzes = [
    {
        'quiz_id': 1,
        'image': 'https://source.unsplash.com/1600x900/?work',
        'num_questions': 5,
        'questions': [
            {
                'question': 'Question 1',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 0
            },
            {
                'question': 'Question 2',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 1
            },
            {
                'question': 'Question 3',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 2
            },
            {
                'question': 'Question 4',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 3
            },
            {
                'question': 'Question 5',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 0
            }
        ]
    },
    {
        'quiz_id': 2,
        'image': 'https://source.unsplash.com/1600x900/?city',
        'num_questions': 10,
        'questions': [
            {
                'question': 'Question 1',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 0
            },
            {
                'question': 'Question 2',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 1
            },
            {
                'question': 'Question 3',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 2
            },
            {
                'question': 'Question 4',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 3
            },
            {
                'question': 'Question 5',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 0
            },
            {
                'question': 'Question 6',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 1
            },
            {
                'question': 'Question 7',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 2
            },
            {
                'question': 'Question 8',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 3
            },
            {
                'question': 'Question 9',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 0
            },
            {
                'question': 'Question 10',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 1
            }
        ]
    },
    {
        'quiz_id': 3,
        'image': 'https://source.unsplash.com/1600x900/?landscape',
        'num_questions': 7,
        'questions': [
            {
                'question': 'Question 1',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 0
            },
            {
                'question': 'Question 2',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 1
            },
            {
                'question': 'Question 3',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 2
            },
            {
                'question': 'Question 4',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 3
            },
            {
                'question': 'Question 5',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 0
            },
            {
                'question': 'Question 6',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 1
            },
            {
                'question': 'Question 7',
                'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
                'answer': 2
            }
        ]
    }
]

leaderboard=[{'name':'chala','score':"12"},{'name':'chube','score':"11"},{'name':'chebete','score':"10"}]



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

@main.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
@login_required
def quiz(quiz_id):
    if quiz_id > len(quizzes):
        return "Quiz not found"
    if request.method == 'POST':
        score = 0
        num_questions = quizzes[quiz_id - 1]['num_questions']
        for i in range(num_questions):
            answer = request.form.get(f'question_{i+1}')
            if answer is not None and int(answer) == quizzes[quiz_id - 1]['questions'][i]['answer']:
                score += 1

        leaderboard.append({'quiz_id': quiz_id, 'score': score})

        return redirect(url_for('leaderboard_func'))

    return render_template('pages/quiz.html', quiz=quizzes[quiz_id - 1]['questions'])


@main.route('/leaderboard', methods=['GET'])
def leaderboard_func():
    leaderboard_sorted = sorted(leaderboard, key=lambda x: x['score'], reverse=True)
    return render_template('pages/leaderboard.html', leaderboard=leaderboard_sorted)










@main.route('/api/users', methods=['GET'])
def get_users():
    users =User.query.all()  
    def r (x):
        x.pop('_sa_instance_state')
        return x
    x = [r(user.__dict__) for user in users]
    print(x)
    # .with_entities(user.id,user.name,user.email,user.phone_number)
    # flash('Succesful')
    return jsonify(x), 200
# /dd824ec3-7c23-4714-9cb5-0b0a529166fc
@main.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    # print( data)
    # print(data['email'])
    user1 = User.query.filter( user.email== data['email'] ).all()
    # print(user)
    if user1:
        return (jsonify({'error': 'user already exists'}),409)
    # 409 conflict
    else:
        try:
            user = user(name=data['name'], phone_number=data['phone_number'], email=data['email'])
            # return user.__dir__()
            db.session.add(user)
            db.session.commit()
            model_dict = (user.__dict__)
            # x  = {
            #     'id':user.id,
            #     'name' : user.name,
            #     'email':user.email,
            #     'phone_number':user.phone_number
            # }
            model_dict.pop('_sa_instance_state')
            # flash('Succesful')
            return jsonify(model_dict  ), 201
            
            
            # 201 = created
        except Exception as e:
            # print(e)
            return jsonify({"error":str(e.__dict__)}), 500
    
@main.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        # print(user.__dict__)
        model_dict = (user.__dict__)
        try:
            # Removing a key using the pop() method
            model_dict.pop("_sa_instance_state")
        except Exception as e:
            pass
        return jsonify(model_dict), 200
    else:
        return jsonify({'message': 'user not found'}), 404

@main.route('/api/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    # print(user)
    if user:
        data = request.get_json()
        user.name = data['name']
        user.phone_number = data['phone_number']
        # user.email = data['email']
       
        db.session.commit()
        return redirect(url_for('main.get_user', user_id=user_id))
    else:
        return jsonify({'message': 'user not found'}), 404,

@main.route('/api/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'user deleted'}), 200
    else:
        return jsonify({'message': 'user not found'}), 404
