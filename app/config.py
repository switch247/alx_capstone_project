# The Config class is used to store configuration settings for a Python application, including the
# secret key and database URI.
import os

class Config:
    # os is not working
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://root:''@localhost/test'
    # or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
