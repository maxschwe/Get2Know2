from app import create_app, socketio
from flask import Flask, request, render_template, url_for, redirect, session
import logging

from app.models import GamesHandler, PlayersHandler

logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s] - [%(levelname)s]: %(message)s")

games_handler = GamesHandler()
players_handler = PlayersHandler()
player = players_handler.new_player("Peter")
player2 = players_handler.new_player("Max")
games_handler.create_game(player)
games_handler.join_game("0000", player2)


app = create_app(debug=True)

if __name__ == "__main__":
    socketio.run(app)
