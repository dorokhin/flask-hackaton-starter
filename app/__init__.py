import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from raven.contrib.flask import Sentry

redis_hostname = os.environ.get('redis_hostname', 'redis')
app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS', 'app.config.DevelopmentConfig'))
sentry = Sentry(app, logging=True, level=logging.ERROR)
login = LoginManager(app)
login.login_view = 'login'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models, errors
