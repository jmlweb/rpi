from typing import Callable
from game_typings import Options


class GameButtons:
    """
    Maps native button events to cb
    """
    def __init__(self, options: Options, cb: Callable):
        self.options = options
        self.cb = cb
        for option in self.options.values():
            option["button"].when_pressed = self.on_press

    def on_press(self, button):
        for idx, option in self.options.items():
            if option["button"] == button:
                self.cb(i)
                break
