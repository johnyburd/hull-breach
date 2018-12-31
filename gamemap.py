from entities import Entity

class Tile(Entity):
	def __init__(self, image, name, x, y):
		super().__init__(name, x, y)
		self.image = image

class Level(object):
	"""basically one level is one screen"""
	def __init__(self, width, height):
		self.height = height
		self.width = width
		self.array = []

		h = []
		for i in range(self.width):
			h.append("dirt")
		for i in range(self.height):
			self.array.append(h)


	def print_array(self):
		for h in self.array:
			for i in h:
				print(i, end=" ")
			print()

class Map(object):
	"""levels is an array of levels"""
	def __init__(self, width, height):
		level = Level(width,height)
		self.levels = [level]
		self.current_level = 0	# the level that the player is currently on

	def get_level(self):
		return self.levels[self.current_level]