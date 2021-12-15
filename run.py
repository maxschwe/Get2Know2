from app import create_app, socketio
from flask import Flask, request, render_template, url_for, redirect, session
from flask.logging import default_handler
import logging

from app.models import GamesHandler, PlayersHandler

logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s] - [%(levelname)s]: %(message)s")

log = logging.getLogger('werkzeug')
log.disabled = True

app = create_app(debug=True)
app.logger.removeHandler(default_handler)

if __name__ == "__main__":
    socketio.run(app, log_output=False)
