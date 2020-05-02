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


# class RandomItem2:
# 	def __init__(self, min_value: int, max_value: int):
# 		self.min_value = min_value
# 		self.max_value = max_value
# 		self.value = random.randint(self.min_value, self.max_value)

# 	def randomize(self):
# 		self.value = random.randint(self.min_value, self.max_value)

# class RandomList2:
# 	def __init__(self, items_qty: int, min_value: int, max_value: int):
# 		self.values = list(map(lambda x: RandomItem(min_value, max_value), range(items_qty)))

# 	@property
# 	def plain(self):
# 		return list(map(lambda x: x.value, self.values))

# 	def randomize(self):
# 		self.values = list(map(lambda x: x.randomize(), self.values))
