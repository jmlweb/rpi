from gpiozero import TonalBuzzer
from gpiozero.tones import Tone


class ResultsBuzzer:
    def __init__(self, pin):
        self.buzzer = TonalBuzzer(pin)
        min = Tone(self.buzzer.min_tone).frequency
        max = Tone(self.buzzer.max_tone).frequency
        self.conversion = (max - min) / 100
        self.min = min

    def play(self, light_value):
        # light_value goes from 0 to 100,
        # so we need to convert it first
        value = round(light_value * self.conversion + self.min)
        self.buzzer.play(Tone(frequency=value))
