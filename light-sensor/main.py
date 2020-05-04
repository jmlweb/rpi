# 08_light_meter.py
# From the code for the Box 1 kit for the Raspberry Pi by MonkMakes.com

from gpiozero import PWMLED
from PiAnalog import *
import time
import math

p = PiAnalog()
led = LED(25)


def light_from_r(R):
    # Log the reading to compress the range
    return math.log(1000000.0/R) * 10.0

# group together all of the GUI code
# Update the reading


def update_reading():
    light = light_from_r(p.read_resistance())
    led.value = light / 100
    reading_str = "{:.0f}".format(light)
    light_text = reading_str
    print(light_text)


while True:
    update_reading()
    time.sleep(1)
