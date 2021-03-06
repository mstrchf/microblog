import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from logging.handlers import SMTPHandler
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
mail = Mail(app)

# email error reporting
# if not app.debug:
#     if app.config['MAIL_SERVER']:
#         auth = None
#         if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
#             auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])

#         secure = None
#         if app.config['MAIL_USE_TLS']:
#             secure = ()

#         mail_handler = SMTPHandler(
#             (app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
#             'no-reply@' + app.config['MAIL_SERVER'],
#             app.config['MAIL_DEFAULT_SENDER'], 'Microblog Failure', auth, secure)

#         mail_handler.setLevel(logging.ERROR)
#         app.logger.addHandler(mail_handler)

# logging to file


from app import routes, models, errors
