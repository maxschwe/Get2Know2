from . import main, players_handler, games_handler
from .. import socketio
import logging
import time

from flask import render_template, redirect, url_for, request, session
from flask_socketio import SocketIO, emit, send, join_room, leave_room


@main.route("/game/<game_id>", methods=["GET"])
def join_game(game_id):
    session["game_id"] = game_id
    if "user_id" not in session:
        return redirect("/")
    if players_handler.get_player(session["user_id"]) is None:
        session.pop("user_id")
        return redirect("/")
    game = games_handler.get_game(game_id)
    if game is None:
        return redirect("/")

    return render_template("game.html")


@main.route("/game_state", methods=["GET"])
def game_state():
    try:
        user_id = session["user_id"]
        game_id = session["game_id"]
    except:
        return redirect("/")

    return games_handler.get_game_state(game_id, user_id)


@socketio.on("connect")
def new_connection():
    game_id = session["game_id"]
    user_id = session["user_id"]
    join_room(user_id)
    if games_handler.game_exists(game_id) and players_handler.player_exists(user_id) and user_id in games_handler.get_game(game_id).players:
        logging.info(f"{user_id} connected")
        players_handler.players[user_id].connected = True
        join_room(game_id)
        time.sleep(0.5)
        games_handler.update_player_list(game_id)
    else:
        emit("restart", room=user_id, namespace="/")
        logging.info(f"Sent restart cmd to {user_id}")
        leave_room(user_id)


@socketio.on("disconnect")
def disconnect():
    game_id = session["game_id"]
    user_id = session["user_id"]
    logging.info(f"{user_id} disconnected")
    leave_room(game_id)
    leave_room(user_id)
    games_handler.disconnect_game(game_id, user_id)
