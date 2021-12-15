import logging
from flask import render_template

from .game_data import GameData


class Game:
    def __init__(self, games_handler, id):
        self.games_handler = games_handler
        self.id = id
        self.data = GameData()
        self.players = {}
        logging.info(f"Created game with id {self.id}")

    def join(self, player):
        if player.name in [pl.name for pl in self.players.values()]:
            return False
        self.players[player.id] = player
        player.game = self
        logging.info(f"Player {player.name} joined game {self.id}")
        return True

    def disconnect(self, player_id):
        player = self.players.pop(player_id)
        logging.info(f"Player {player.name} disconnected game {self.id}")
        player.remove()

    def get_state(self, user_id):
        if self.data.state == "lobby":
            pass
        elif self.data.state == "turn":
            pass
        elif self.data.state == "response":
            pass
        elif self.data.state == "selection":
            pass
        elif self.data.state == "overview":
            pass
        elif self.data.state == "end":
            pass
        else:
            pass
