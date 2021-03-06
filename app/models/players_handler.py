from .player import Player

import logging

LEN_PLAYER_ID = 6


class PlayersHandler:
    def __init__(self):
        self.players = {}

    def new_player(self, name):
        id = self._gen_player_id()
        new_player = Player(self, id, name)
        self.players[id] = new_player
        return new_player

    def remove_player(self, id):
        self.players.pop(id)

    def get_player(self, id):
        try:
            return self.players[id]
        except KeyError:
            logging.warning(f"Requested access to invalid user id {id}")
            return None

    def player_exists(self, player_id):
        return player_id in self.players

    def _gen_player_id(self):
        id = LEN_PLAYER_ID * "0"
        count = 0
        while id in self.players:
            count += 1
            count_str = str(count)
            id = (LEN_PLAYER_ID - len(count_str)) * "0" + count_str
        return id
