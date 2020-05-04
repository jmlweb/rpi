from PiAnalog import *


class LightReader:
    def __init__(self):
        self.p = PiAnalog()

    @property
    def value(self):
        r = self.p.read_resistance()
        return math.log(1000000.0/r) * 10.0
