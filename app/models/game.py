import logging
from flask import render_template
from flask_socketio import emit, send, join_room, leave_room

from .game_system import GameSystem


class Game:
    def __init__(self, games_handler, id):
        self.games_handler = games_handler
        self.id = id
        self.data = GameSystem()
        self.players = {}
        logging.info(f"Created game with id {self.id}")

    def join(self, player):
        if player.name in self._get_player_names():
            return False
        self.players[player.id] = player
        player.game = self
        logging.info(f"Player {player.name} joined game {self.id}")
        return True

    def disconnect(self, player_id):
        active_players = self._active_players()
        if active_players == 1 and self.data.state == "lobby" or active_players < 2 and self.data.state != "lobby":
            self.data.state == "end"
            self.emit_changed_state()
        temp_players = self.players.copy()
        player = temp_players.pop(player_id)
        if player.creator:
            player.creator = False
            new_creator = list(temp_players.values())[0]
            print(new_creator.name)
            new_creator.creator = True
            if self.data.state == "lobby":
                self.emit_changed_state()

        logging.info(f"Player {player.name} disconnected game {self.id}")
        player.connected = False

    def ch_rounds(self, rounds):
        self.data.rounds = int(rounds)
        emit("changed_rounds", rounds, room=self.id, namespace="/")

    def ch_category(self, category):
        self.data.category = category
        emit("changed_category", category, room=self.id, namespace="/")

    def start_game(self):
        self.data.state = "turn"

    def emit_update_player_list(self):
        logging.info("emit_update_player_list")
        emit("update_user_list", self._get_player_names(),
             room=self.id, namespace="/")

    def emit_changed_state(self):
        logging.info("Changed state or creator left")
        emit("state_change", room=self.id, namespace="/")

    def _get_player_names(self):
        return [pl.name for pl in self.players.values() if pl.connected]

    def _active_players(self):
        return len(self._get_player_names())

    def _webpage_data(self, user_id):
        players = self._get_player_names()

        data = {"players": players,
                "creator": self.players[user_id].creator,
                "game_id": self.id}
        data = {**data, **self.data.__dict__}
        return data

    def get_state(self, user_id):
        data = self._webpage_data(user_id)
        if self.data.state == "lobby":
            return render_template("lobby.html", **data)
        elif self.data.state == "turn":
            return render_template("turn.html", **data)
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
