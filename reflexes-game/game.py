from random import choice


class Game:
    def __init__(self, options, on_new_question, on_ok, on_ko):
        self.questions = list(options.keys())
        self.current_question = None
        self.on_new_question = on_new_question
        self.on_ok = on_ok
        self.on_ko = on_ko

    def choose_question(self):
        self.current_question = choice(self.questions)
        self.on_new_question()

    def process_answer(self, answer):
        if (self.current_question == answer):
            self.answer_ok()
            self.on_ok()
        else:
            self.answer_ko()
            self.on_ko()
