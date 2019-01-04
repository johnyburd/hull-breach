import random
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
		self.entitylist = []


		for i in range(self.height):
			h = []		
			for i in range(self.width):
				h.append("")
			self.entitylist.append(h)

		self.set_entity(1,1,"dagger")

		for i in range(self.height):
			h = []
			for j in range(self.width):
				h.append("dirt") if random.randint(0,10) == 1 else h.append("grass")
			self.array.append(h)

	def set_entity(self, x, y, entity_id):
		self.entitylist[y][x] = entity_id

	def move_entity(self, startx, starty, endx, endy):
		entitylist[endy][endx] = entitylist[startx][starty]
		entitylist[startx][starty] = None
		# note that this only supports a 2d entitylist
		# eventually the entitylist needs to be 3d?
		# maybe


	def print_array(self):
		for h in self.entitylist:
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