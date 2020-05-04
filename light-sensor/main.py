from gpiozero import PWMLED, TonalBuzzer
from gpiozero.tones import Tone
import time
import math

from light_reader import LightReader
from results_buzzer import ResultsBuzzer

PIN_LED = 25
PIN_BUZZER = 6

lr = LightReader()
rb = ResultsBuzzer(6)

led = PWMLED(PIN_LED)


def update_reading():
    global lr
    current_value = lr.value
    decimal_time = current_value / 100
    led.pulse(decimal_time, decimal_time)
    rb.play(current_value)
    reading_str = "{:.0f}".format(lr.value)
    light_text = reading_str
    print(light_text)


while True:
    update_reading()
    time.sleep(1)
