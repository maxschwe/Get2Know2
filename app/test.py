from flask import Flask, request, render_template, url_for, redirect, session
from flask.logging import default_handler
import logging

logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s] - [%(levelname)s]: %(message)s")

log_flask = logging.getLogger('werkzeug')


app = Flask(__name__)


@app.route("/")
def init():
    return render_template("turn.html")


if __name__ == "__main__":
    app.run(debug=True)
