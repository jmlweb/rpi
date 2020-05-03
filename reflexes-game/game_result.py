from colorzero import Color


class GameResult:
    def __init__(self, result_led):
        self.result_led = result_led

    def reset(self):
        self.result_led.off()

    def error(self):
        self.result_led_color = Color("red")

    def warn(self):
        self.result_led.color = Color("yellow")

    def success(self):
        self.result_led.color = Color("green")
