import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DATABASE_URL') or
                               'postgresql://localhost/conp')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OAUTH_CREDENTIALS = {'orcid': {'id': os.environ.get('OAUTH_ORCID_ID'),
                                   'secret': os.environ.get('OAUTH_ORCID_SECRET')}}
