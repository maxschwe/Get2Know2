import random
import time
import json

from .questions import Questions

STATES = ["turn", "response", "selection", "overview"]
DELAY_TURN_SHOW = 2

categories_indexing = ["Allgemein", "Schule", "Corona", "Freizeit"]


class GameSystem:
    def __init__(self, game):
        self.state = "lobby"
        self.rounds = 3
        self.category = 1
        self.game = game
        self.questions = Questions()
        self.responses = []
        self.selections = []

    def start(self):
        players = list(self.game.players.values())
        random.shuffle(players)
        questions = self.questions.questions[categories_indexing[self.category-1]]
        random.shuffle(questions)
        self.data = {"rounds": self.rounds,
                     "category": categories_indexing[self.category-1], "rounds_data": []}
        for round_num in range(1, self.rounds+1):
            self.round_num = round_num
            round_data = {}
            self.data["rounds_data"].append(round_data)
            for cur_player in players:
                player_data = {}
                round_data[cur_player.id] = player_data
                if not cur_player.connected:
                    player_data = None
                    continue
                self.current_name = cur_player.name
                self.current_question = questions.pop(
                    0).replace("{}", self.current_name)
                player_data["question"] = self.current_question
                self.save_data()
                self.state = "turn"
                self.game.emit_state_changed()
                time.sleep(DELAY_TURN_SHOW)
                self.state = "response"
                self.game.emit_state_changed()
                time.sleep(5)

    def save_data(self):
        with open(f"app/data/game/{self.game.id}.txt", "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)
