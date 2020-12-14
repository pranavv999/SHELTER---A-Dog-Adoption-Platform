import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL') or\
        'postgresql://pranav:password@localhost/blog_db'
    SECRET_KEY = os.environ.get('SECRET_KEY') or\
        "de2c443acafe018bca20e04de8ef1b6e"
