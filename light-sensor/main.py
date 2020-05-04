from gpiozero import PWMLED, TonalBuzzer
from gpiozero.tones import Tone
from PiAnalog import *
import time
import math


class Reader:
    def __init__(self, p: PiAnalog):
        self.p = p

    @property light
    def light(self):
        r = self.p.read_resistance()
        return math.log(1000000.0/r) * 10.0


p = PiAnalog()
led = PWMLED(25)
bz = TonalBuzzer(6)
reader = Reader(p)


def light_from_r(R):
    # Log the reading to compress the range
    return math.log(1000000.0/R) * 10.0

# group together all of the GUI code
# Update the reading


def update_reading():
    global reader
    light = reader.light
    decimal_time = light / 100
    led.pulse(decimal_time, decimal_time)
    bz.play(Tone("A4"))
    reading_str = "{:.0f}".format(light)
    light_text = reading_str
    print(light_text)


while True:
    update_reading()
    time.sleep(1)
