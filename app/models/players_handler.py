from .player import Player

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

    def _gen_player_id(self):
        id = LEN_PLAYER_ID * "0"
        count = 0
        while id in self.players:
            count += 1
            count_str = str(count)
            id = (LEN_PLAYER_ID - len(count_str)) * "0" + count_str
        return id
