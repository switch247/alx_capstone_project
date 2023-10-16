from flask import session, redirect, url_for
from flask import Blueprint, render_template, request,jsonify
from app.models.user import User
# move this to a separete file at some point
def login_required(route):
    def decorated_route(*args, **kwargs):
        if 'logged_in' in session:
            return route(*args, **kwargs)
        else:
            return redirect(url_for('auth.login'))
    return decorated_route



auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Perform authentication logic here
        # ...
        username = request.form.get('username')
        password = request.form.get('password')
        print(username,password)
        # Perform authentication logic here
        # ...
        try:
            user = User.query.filter_by(username=username, password=password).first()
            # Redirect to a protected page after successful login
            if user:
                print(user)
                # Set the 'logged_in' key in the session to indicate successful login
                session['logged_in'] = True
                session['username'] = username
                session['password'] = password
                session['id'] = user.id
                # blueprintname.function_name
                return redirect(url_for('main.home'))
            else:
                print('incorrect credentials')
        except Exception as e:
            print(e)
        
        

    return render_template('pages/login.html')

@auth_bp.route('/logout')
def logout():
    # Clear the session and redirect to the login page
    session.clear()
    return redirect(url_for('auth.login'))

