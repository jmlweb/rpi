class GameIndicators:
    def __init__(self, options):
        self.options = options

    def reset(self):
        for i in self.options.keys():
            self.options[i]['indicator'].off()

    def select(self, option_key):
        self.options[option_key]['indicator'].on()