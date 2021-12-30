import random
import time
import json

from .questions import Questions

STATES = ["turn", "response", "selection", "overview"]
DELAY_TURN_SHOW = 2
DELAY_RESPONSE = 23
DELAY_SELECTION = 23
DELAY_OVERVIEW = 3

POINTS_RIGHT_SELECTED = 1
POINTS_SOMEONE_SELECTED_YOURS = 2

categories_indexing = ["Allgemein", "Schule", "Corona", "Freizeit"]


class GameSystem:
    def __init__(self, game):
        self.state = "lobby"
        self.rounds = 3
        self.category = 1
        self.game = game
        self.questions = Questions()
        self.responses = {}
        self.selections = {}

    def start(self):
        players = list(self.game.players.values())
        random.shuffle(players)
        self.points = {pl.id: 0 for pl in players}
        questions = self.questions.questions[categories_indexing[self.category-1]]
        random.shuffle(questions)
        self.data = {"rounds": self.rounds,
                     "category": categories_indexing[self.category-1],
                     "rounds_data": []}
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
                self.current_player = cur_player
                self.current_name = cur_player.name
                self.current_question = questions.pop(
                    0).replace("{}", self.current_name)
                player_data["question"] = self.current_question
                self.save_data()
                self.state = "turn"
                self.game.emit_state_changed()
                time.sleep(DELAY_TURN_SHOW)
                self.responses = {}
                self.state = "response"
                self.game.emit_state_changed()
                start_time = time.time()
                active_players = [pl for pl in players if pl.connected]
                while (time.time() - start_time < DELAY_RESPONSE) and len(self.responses) != len(active_players):
                    time.sleep(0.5)
                    active_players = [pl for pl in players if pl.connected]

                player_data["responses"] = self.responses.copy()
                self.save_data()
                self.selections = {}
                self.state = "selection"
                self.game.emit_state_changed()
                start_time = time.time()
                active_players = [pl for pl in players if pl.connected]
                while (time.time() - start_time < DELAY_SELECTION) and len(self.selections) != len(active_players)-1:
                    time.sleep(0.5)
                    active_players = [pl for pl in players if pl.connected]
                player_data["selections"] = self.selections.copy()
                self.calc_points(cur_player.id)
                player_data["points"] = self.points.copy()
                self.save_data()
                self.state = "overview"
                self.game.emit_state_changed()
                time.sleep(DELAY_OVERVIEW)
        self.state = "end"
        self.game.emit_state_changed()

    def get_respones(self):
        ret = [[i, resp] for i, resp in self.responses.items() if resp != ""]
        print(ret)
        return ret

    def get_points(self, user_id):
        ret = [[self.game.players[id].name, points]
               for id, points in self.points.items() if id != user_id]
        ret.insert(0, [self.game.players[user_id].name, self.points[user_id]])
        print(ret)
        return ret

    def calc_points(self, cur_id):
        for id, selected in self.selections.items():
            if selected != 0:
                if cur_id == selected:
                    self.points[cur_id] += POINTS_RIGHT_SELECTED
                    self.points[id] += POINTS_RIGHT_SELECTED
                else:
                    self.points[selected] += POINTS_SOMEONE_SELECTED_YOURS

    def save_data(self):
        with open(f"app/data/game/{self.game.id}.txt", "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)
