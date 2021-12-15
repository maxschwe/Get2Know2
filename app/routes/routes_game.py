from . import main, players_handler, games_handler

from flask import render_template, redirect, url_for, request, session


@main.route("/game/<game_id>", methods=["GET"])
def join_game(game_id):
    if "user_id" not in session:
        session["game_id"] = game_id
        return redirect("/")
    game = games_handler.get_game(game_id)
    if game is None:
        return redirect("/")
    return render_template("game.html")


@main.route("/game_state", methods=["GET"])
def game_state():
    user_id = session["user_id"]
    game_id = session["game_id"]

    return games_handler.get_game_state(game_id, user_id)
