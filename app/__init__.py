from flask import Flask
from flask_socketio import SocketIO
import random
import time

random.seed(time.time())
socketio = SocketIO(ping_timeout=50)


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = '10clegende'

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app
