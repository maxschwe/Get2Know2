import logging
from flask import redirect, render_template
from .game import Game

LEN_GAME_KEY = 4


class GamesHandler:
    def __init__(self):
        self.games = {}

    def create_game(self, player):
        game_id = self._gen_game_id()
        new_game = Game(self, game_id)
        player.creator = True
        new_game.join(player)
        self.games[game_id] = new_game
        return game_id

    def remove_game(self, game_id):
        self.games.pop(game_id)
        logging.info(f"Removed game: {game_id}")

    def join_game(self, game_id, player):
        game = self.get_game(game_id)
        if game is None:
            return False, "Diese Game-ID existiert nicht. Versuchs erneut!"
        valid = game.join(player)
        if not valid:
            return False, "Dieser Spielername existiert bereits. Such dir einen anderen aus!"
        return True, ""

    def disconnect_game(self, game_id, player_id):
        game = self.get_game(game_id)
        if game is None:
            return False, "Diese Game-ID existiert nicht. Versuchs erneut!"
        game.disconnect(player_id)

    def ch_rounds(self, game_id, rounds_num):
        game = self.get_game(game_id)
        if game is None:
            return False, "Diese Game-ID existiert nicht. Versuchs erneut!"
        game.ch_rounds(rounds_num)

    def ch_category(self, game_id, category_num):
        game = self.get_game(game_id)
        if game is None:
            return False, "Diese Game-ID existiert nicht. Versuchs erneut!"
        game.ch_category(category_num)

    def response(self, game_id, user_id, response):
        game = self.get_game(game_id)
        if game is None:
            return False, "Diese Game-ID existiert nicht. Versuchs erneut!"
        game.response(user_id, response)

    def selection(self, game_id, user_id, selected_id):
        game = self.get_game(game_id)
        if game is None:
            return False, "Diese Game-ID existiert nicht. Versuchs erneut!"
        game.selection(user_id, selected_id)

    def start_game(self, game_id):
        game = self.get_game(game_id)
        if game is None:
            return False, "Diese Game-ID existiert nicht. Versuchs erneut!"
        game.start_game()

    def get_game_state(self, game_id, user_id):
        game = self.get_game(game_id)
        if game is None:
            return redirect("/")
        return game.get_state(user_id)

    def update_player_list(self, game_id):
        game = self.get_game(game_id)
        if game is None:
            return False, "Diese Game-ID existiert nicht. Versuchs erneut!"
        game.emit_update_player_list()

    def get_game(self, id):
        try:
            return self.games[id]
        except KeyError:
            logging.warning(f"Requested access to invalid game id {id}")
            return None

    def game_exists(self, game_id):
        return game_id in self.games

    def _gen_game_id(self):
        id = LEN_GAME_KEY * "0"
        count = 0
        while id in self.games:
            count += 1
            count_str = str(count)
            id = (LEN_GAME_KEY - len(count_str)) * "0" + count_str
        return id
