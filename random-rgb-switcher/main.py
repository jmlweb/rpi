from gpiozero import RGBLED, Button
from colorzero import Color
from time import sleep

from random_list import RandomList

PIN_RED = 18
PIN_GREEN = 23
PIN_BLUE = 24
PIN_BUTTON = 25

MIN_VALUE = 0
MAX_VALUE = 255

def run():
	led = RGBLED(PIN_RED, PIN_GREEN, PIN_BLUE)
	button = Button(PIN_BUTTON)
	colors_list = RandomList(3, MIN_VALUE, MAX_VALUE)
	set_led_color()

	def set_led_color():
		led.color = Color(*colors_list.plain)

	def generate_new_color():
		colors_list.randomize()
		set_led_color()

	button.when_pressed = generate_new_color

if __name__ == "__main__":
	run()
