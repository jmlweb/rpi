import random

class RandomItem:
	def __init__(self, min_value: int, max_value: int):
		self.min_value = min_value
		self.max_value = max_value
		self.randomize()

	def randomize(self):
		self.value = random.randint(self.min_value, self.max_value)

class RandomList:
	def __init__(self, items_qty: int, min_value: int, max_value: int):
		self.values = list(map(lambda x: RandomItem(min_value, max_value), range(items_qty)))

	@property
	def plain(self):
		return list(map(lambda x: x.value, self.values))

	def randomize(self):
		self.values = list(map(lambda x: x.randomize(), self.values))
