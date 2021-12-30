from flask import Flask, request, render_template, url_for, redirect, session
from flask.logging import default_handler
import logging

logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s] - [%(levelname)s]: %(message)s")

log_flask = logging.getLogger('werkzeug')


app = Flask(__name__)


@app.route("/")
def init():
    return render_template("selection.html", responses=[["0001", "lfaksj;fdkajsfdl;kjfdfsjaklsdfjas"],
                                                        ["0001", "lfaksj;fdkajsfdl;kjfdfsjaklsdfjasdsfal;kjdfs;klajdfl;skajfdklsajdl;fkjas;klfdjsa"],
                                                        ["000001", "lfaksj;fdkajsfdl;kjfdfsjaklsdfjas"],
                                                        ["0001", "lfaksj;fdkajsfdl;kjfdfsjaklsdfjas"],
                                                        ["0001", "lfaksj;fdkajsfdl;kjfdfsjaklsdfjasdsfal;kjdfs;klajdfl;skajfdklsajdl;fkjas;klfdjsa"],
                                                        ["000001", "lfaksj;fdkajsfdl;kjfdfsjaklsdfjas"]])


if __name__ == "__main__":
    app.run(debug=True)
