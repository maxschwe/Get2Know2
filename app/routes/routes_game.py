from . import main, players_handler, games_handler

from flask import render_template, redirect, url_for, request, session


@main.route("/game/<game_id>", methods=["GET"])
def join_game(game_id):
    if "user-id" in session:
        user_id = session["user-id"]
    else:
        return redirect(url_for("game", game_id=game_id))
    return games_handler.render_game(game_id, user_id)
