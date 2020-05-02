from time import sleep

from random_list import RandomList

PIN_RED = 18
PIN_GREEN = 23
PIN_BLUE = 24
PIN_BUTTON = 25

MIN_VALUE = 0
MAX_VALUE = 255

def run():

	def generate_new_color():
		colors_list.shuffle()
		print(colors_list.values)

	colors_list = RandomList(3, MIN_VALUE, MAX_VALUE)
	while True:
		generate_new_color()
		sleep(1)

if __name__ == "__main__":
	run()
