import random

class RandomList:
	def __init__(self, items_qty: int, min_value: int, max_value: int):
		self.min_value = min_value
		self.max_value = max_value
		self.items_qty = items_qty
		self.shuffle()

	def calculate_random_value(self):
		return random.randint(self.min_value, self.max_value)

	def shuffle(self):
		self.values = list(map(lambda x: self.calculate_random_value(), range(self.items_qty)))
