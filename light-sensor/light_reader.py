from PiAnalog import *


class LightReader:
    # LIGHT READER USES PINS 18 AND 23 INTERNALLY
    def __init__(self):
        self.p = PiAnalog()

    @property
    def value(self):
        r = self.p.read_resistance()
        return math.log(1000000.0/r) * 10.0
