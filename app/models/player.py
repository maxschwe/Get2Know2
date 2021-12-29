import logging


class Player:
    def __init__(self, players_handler, id, name):
        self.players_handler = players_handler
        self.id = id
        self.name = name
        self.connected = False
        self.creator = False
        logging.info(f"Created player: {self.name}, {self.id}")

    def remove(self):
        self.players_handler.remove_player(self.id)
        logging.info(f"Removed player: {self.name}, {self.id}")
