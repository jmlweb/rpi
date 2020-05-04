import time
import math

from light_reader import LightReader
from results_buzzer import ResultsBuzzer
from results_led import ResultsLed

PIN_LED = 25
PIN_BUZZER = 6


class App:
    def __init__(self):
        self.lightReader = LightReader()
        self.resultsBuzzer = ResultsBuzzer(PIN_BUZZER)
        self.resultsLed = ResultsLed(PIN_LED)
        self.last_value = self.lightReader.value
        self.update_reading()

    def update_reading(self):
        current_value = self.lightReader.value
        if current_value != self.last_value:
            self.resultsBuzzer.update(current_value)
            self.resultsLed.update(current_value)
            self.last_value = current_value
        time.sleep(1)
        self.update_reading()


if __name__ == "__main__":
    App()
