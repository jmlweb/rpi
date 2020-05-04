from gpiozero import TonalBuzzer
from gpiozero.tones import Tone


class ResultsBuzzer:
    def __init__(self, pin):
        self.buzzer = TonalBuzzer(pin)
        self.min = Tone(self.buzzer.min_tone).frequency
        self.max = Tone(self.buzzer.max_tone).frequency
        self.conversion = (self.max - self.min) / 100

    def play(self, light_value):
        # light_value goes from 0 to 100,
        # so we need to convert it first
        value = round(self.max - light_value * self.conversion)
        self.buzzer.play(Tone(frequency=value))
