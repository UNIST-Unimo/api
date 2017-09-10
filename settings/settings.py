import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2
