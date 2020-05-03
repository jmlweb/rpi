from gpiozero import RGBLED
from colorzero import Color


class GameResult:
    def __init__(self, result_led: RGBLED):
        self.result_led = result_led

    def reset(self):
        self.result_led.off()

    def error(self):
        self.result_led.color = Color("red")

    def warn(self):
        self.result_led.blink(0.2, 0.2, 0.1, 0.1, Color("#ffa500"))

    def success(self):
        self.result_led.color = Color("green")
