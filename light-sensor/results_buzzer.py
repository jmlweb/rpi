from gpiozero import TonalBuzzer
from gpiozero.tones import Tone


class ResultsBuzzer:
    def __init__(self, pin):
        self.buzzer = TonalBuzzer(pin)

    def play(self, light_value):
        # light_value goes from 0 to 100,
        # so we need to convert it first
        conversion = 127 / 100
        value = round(light_value * conversion)
        self.buzzer.play(Tone(value))
