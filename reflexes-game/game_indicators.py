from game_typings import Options


class GameIndicators:
    def __init__(self, options: Options):
        self.options = options

    def reset(self):
        for option in self.options.values():
            option['indicator'].off()

    def select(self, option_key):
        self.options[option_key]['indicator'].on()
