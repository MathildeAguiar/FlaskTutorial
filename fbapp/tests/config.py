import os
SECRET_KEY = 'votre_nouvelle_cle_secrete'

FB_APP_ID = 214515270213212  

basedir = os.path.abspath(os.path.dirname(__file__))

# Nouvelle base de données pour les tests.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_test.db')

# Active le debogueur
DEBUG = True
TESTING = True
LIVESERVER_PORT = 8943
LIVESERVER_TIMEOUT = 10

# Facebook test user
FB_USER_NAME = "Ellen"
FB_USER_PW = "YOLOYOLO"
FB_USER_EMAIL = "ellen_rmilrcp_page@tfbnw.net"
FB_USER_ID = 100018814390853
FB_USER_GENDER = 'female'