import logging


class Game:
    def __init__(self, games_handler, id):
        self.games_handler = games_handler
        self.id = id
        self.players = []

        logging.info(f"Created game with id {self.id}")

    def join(self, player):
        self.players.append(player)
        player.game = self
        logging.info(f"Player {player.name} joined game {self.id}")
