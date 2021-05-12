# To generate a new secret key:
#import random, string
#print("".join([random.choice(string.printable) for _ in range(24)]))

import os

SECRET_KEY = ";fpe6j+anFcilxi}|-i&ioBU"
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

FB_APP_ID = 381439923079473
