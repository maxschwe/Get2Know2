import os
import random

PATH_QUESTIONS = "app/data/questions"


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
