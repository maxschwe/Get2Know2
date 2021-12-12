from app import create_app, socketio
from flask import Flask, request, render_template, url_for, redirect, session
import logging

from app.models import GamesHandler, PlayersHandler

logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s] - [%(levelname)s]: %(message)s")

app = create_app(debug=True)

if __name__ == "__main__":
    socketio.run(app, log_output=False)
