import logging
from .game import Game

LEN_GAME_KEY = 4


class GamesHandler:
    def __init__(self):
        self.games = {}

    def create_game(self, player):
        game_id = self._gen_game_id()
        new_game = Game(self, game_id)
        new_game.join(player)
        self.games[game_id] = new_game

    def remove_game(self, game_id):
        self.games.pop(game_id)

    def join_game(self, game_id, player):
        game = self.get_game(game_id)
        if game is None:
            return False
        game.join(player)
        return True

    def get_game(self, id):
        try:
            return self.games[id]
        except KeyError:
            logging.warning(f"Requested access to invalid game id {id}")
            return None

    def _gen_game_id(self):
        id = LEN_GAME_KEY * "0"
        count = 0
        while id in self.games:
            count += 1
            count_str = str(count)
            id = (LEN_GAME_KEY - len(count_str)) * "0" + count_str
        return id
