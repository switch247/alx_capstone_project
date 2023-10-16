from flask import session, redirect, url_for
from flask import Blueprint, jsonify, request,flash,abort,redirect,url_for,render_template
from app import db
import json

from app.models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/api/users/me')
def profile():
    username = session.get('username')
    user_id =(session.get('id'))
    if username:
        return redirect(url_for('user.get_user', user_id=user_id))
        return jsonify({"username": f'{username}'})
    else:
        return 'Please log in first'




@user_bp.route('/api/users', methods=['GET'])
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
@user_bp.route('/api/users', methods=['POST'])
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
    
@user_bp.route('/api/users/<user_id>', methods=['GET'])
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

@user_bp.route('/api/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    # print(user)
    if user:
        data = request.get_json()
        user.name = data['name']
        user.phone_number = data['phone_number']
        # user.email = data['email']
       
        db.session.commit()
        return redirect(url_for('user.get_user', user_id=user_id))
    else:
        return jsonify({'message': 'user not found'}), 404,

@user_bp.route('/api/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'user deleted'}), 200
    else:
        return jsonify({'message': 'user not found'}), 404
