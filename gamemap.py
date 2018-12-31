from entities import Entity

class Tile(Entity):
	def __init__(self, image, name, x, y):
		super().__init__(name, x, y)
		self.image = image

class Level(object):
	def __init__(self, width, height):
		self.height = height
		self.width = width
		self.map = []

		h = []
		for i in range(self.width):
			h.append(0)
		for i in range(self.height):
			self.map.append(h)


	def print_map(self):
		for h in self.map:
			for i in h:
				print(i, end=" ")
			print()

class Map(object):
	"""docstring for Map"""
	def __init__(self):
		level = Level(50,40)
		self.levels = [level]
		self.current_level = "dirt"	#the level that the player is currently on

	def get_level(self):
		return self.levels[self.current_level]




		


levelOne = Level(10,10)

levelOne.print_map()

grassTile = Tile("tiles/grass.png", "grass", 1, 3)

print(grassTile.name)