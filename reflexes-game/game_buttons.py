from typing import Callable
from game_typings import Options


class GameButtons:
    def __init__(self, options: Options, cb: Callable):
        self.options = options
        self.cb = cb
        for i in self.options.keys():
            self.options[i]["button"].when_pressed = self.on_press

    def on_press(self, button):
        for i in self.options.keys():
            if self.options[i]["button"] == button:
                self.cb(i)
                break
