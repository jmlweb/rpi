from gpiozero import PWMLED, TonalBuzzer
from gpiozero.tones import Tone
import time
import math

from light_reader import LightReader

PIN_LED = 25
PIN_BUZZER = 6

lr = LightReader()

led = PWMLED(PIN_LED)
bz = TonalBuzzer(PIN_BUZZER)


def update_reading():
    global lr
    decimal_time = lr.value / 100
    led.pulse(decimal_time, decimal_time)
    bz.play(Tone(frequency=lr.value * 10))
    reading_str = "{:.0f}".format(light)
    light_text = reading_str
    print(light_text)


while True:
    update_reading()
    time.sleep(1)
