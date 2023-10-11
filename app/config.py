# SQLALCHEMY_DATABASE_URI = 'sqlite:///employees.db'
# SQLALCHEMY_TRACK_MODIFICATIONS = False


# # config.py

# class Config:
#     DEBUG = True
#     SECRET_KEY = 'your_secret_key'



import os

class Config:
    # os is not working
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://root:''@localhost/test'
    # or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



# import os

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
