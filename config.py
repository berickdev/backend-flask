import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma-chave-secreta-bem-segura'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root@localhost/flask_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False