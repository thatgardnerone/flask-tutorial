import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'top-s3cr3t'
    