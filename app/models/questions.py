import os
import random

PATH_QUESTIONS = "questions"

categories_indexing = ["Allgemein", "Schule", "Corona", "Freizeit"]


class Questions:
    def __init__(self):
        self.questions = {}
        self.load_questions()

    def load_questions(self):
        for filename in os.listdir(PATH_QUESTIONS):
            cat_name = filename.split('.')[0]
            file_path = os.path.join(PATH_QUESTIONS, filename)
            questions = []
            with open(file_path, encoding='utf-8') as f:
                for line in f.readlines():
                    questions.append(line.strip('\n'))
            self.questions[cat_name] = questions

    def get_random_question(self, category_index, inaccepted_questions, player_name):
        rel_questions = self.questions[categories_indexing[category_index-1]]
        n_questions = len(rel_questions)
        random_number = -1
        while random_number in [-1, inaccepted_questions]:
            random_number = random.randint(0, n_questions-1)
        inaccepted_questions.append(random_number)
        sel_question = rel_questions[random_number]
        sel_question = sel_question.replace("{}", player_name)
        return sel_question
