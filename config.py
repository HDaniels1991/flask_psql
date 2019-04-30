class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'mysecretkey'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/my_website'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
