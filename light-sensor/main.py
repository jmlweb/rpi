import time
import math

from light_reader import LightReader
from results_buzzer import ResultsBuzzer
from results_led import ResultsLed

PIN_LED = 25
PIN_BUZZER = 6

lr = LightReader()
rb = ResultsBuzzer(PIN_BUZZER)
rl = ResultsLed(PIN_LED)

last_value = None


def update_reading():
    current_value = lr.value
    if current_value != last_value:
        rl.update(current_value)
        rb.update(current_value)
        last_value = current_value
    reading_str = "{:.0f}".format(current_value)
    light_text = reading_str
    print(light_text)


while True:
    update_reading()
    time.sleep(2)
