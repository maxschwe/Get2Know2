from . import main
from flask import render_template, redirect, url_for, request


@main.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")
