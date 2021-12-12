from . import main, players_handler, games_handler
from flask import render_template, redirect, url_for, request, session


@main.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@main.route("/join", methods=["POST"])
def join():
    new_player = players_handler.new_player(request.form["name"])
    session["user-id"] = new_player.id
    if request.form["join-btn"] == "join":
        game_id = request.form["game-id"]
        valid = games_handler.join_game(game_id, new_player)
        if not valid:
            return redirect("/")
    else:
        game_id = games_handler.create_game(new_player)
    return redirect(f"/game/{game_id}")
