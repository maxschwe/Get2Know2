from flask import Flask
from flask_socketio import SocketIO

from . import models

socketio = SocketIO()


def create_app(debug):
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)

    return app
