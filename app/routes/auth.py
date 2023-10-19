from flask import session, redirect, url_for
from flask import Blueprint, render_template, request,jsonify
from app.models.user import User
from app import db
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
        email = request.form.get('email')
        password = request.form.get('password')
        print(email,password)
        # Perform authentication logic here
        # ...
        try:
            user = User.query.filter_by(email=email, password=password).first()
            # Redirect to a protected page after successful login
            if user:
                print(user)
                # Set the 'logged_in' key in the session to indicate successful login
                session['logged_in'] = True
                session['username'] = user.username
                session['password'] = password
                session['id'] = user.id
                session['email']=user.email
                # blueprintname.function_name
                return redirect(url_for('main.home'))
            else:
                return render_template('pages/login.html',errors=['incorrect credentials'])
        except Exception as e:
            print(e)
        
        

    return render_template('pages/login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        errors=[]
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            errors.append('User already exists')
        # Check password strength
        if len(password) < 8:
            errors.append('Password must be at least 8 characters long')
        if len(errors)>0:
            return render_template('pages/register.html', errors=errors)

        # Create a new user
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('pages/register.html')
@auth_bp.route('/logout')
def logout():
    # Clear the session and redirect to the login page
    session.clear()
    return redirect(url_for('main.home'))

