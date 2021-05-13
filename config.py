# To generate a new secret key:
#import random, string
#print("".join([random.choice(string.printable) for _ in range(24)]))

import os

SECRET_KEY = ";fpe6j+anFcilxi}|-i&ioBU"
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

FB_APP_ID = 214515270213212   # id non test 381439923079473

#my fb login button does not works no matter what 
# I inspected my index page and found out that error 
# The Login Button plugin no longer works on http pages. Please update your site to use https for Facebook Login.
#  https://developers.facebook.com/blog/post/2018/06/08/enforce-https-facebook-login/ 

