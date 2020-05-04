from gpiozero import PWMLED


class ResultsLed:
    def __init__(self, pin):
        self.led = PWMLED(pin)
        self.conversion = 1 / 100

    def update(self, light_value):
        decimal_time = light_value * self.conversion
        self.led.pulse(decimal_time, decimal_time)
