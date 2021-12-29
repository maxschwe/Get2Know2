from . import main, players_handler, games_handler
from .. import socketio
from flask import render_template, redirect, url_for, request, session
from flask_socketio import SocketIO, emit, send, join_room, leave_room
import logging


@socketio.on("changed-category")
def changed_category(category_num):
    game_id = session["game_id"]
    games_handler.ch_category(game_id, category_num)


@socketio.on("changed-rounds")
def changed_rounds(rounds_num):
    game_id = session["game_id"]
    games_handler.ch_rounds(game_id, rounds_num)


@socketio.on("start-game")
def start_game():
    game_id = session["game_id"]
    games_handler.start_game(game_id)
