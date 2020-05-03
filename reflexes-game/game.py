from typing import Callable
from random import choice

from game_typings import Options


class Game:
    def __init__(
        self,
        options: Options,
        on_new_question: Callable,
        on_ok: Callable,
        on_ko: Callable
    ):
        self.questions = list(options.keys())
        self.current_question = None
        self.on_new_question = on_new_question
        self.on_ok = on_ok
        self.on_ko = on_ko

    def choose_question(self):
        self.current_question = choice(self.questions)
        self.on_new_question()

    def process_answer(self, answer):
        fn = self.on_ok if (self.current_question == answer) else self.on_ko
        fn()
