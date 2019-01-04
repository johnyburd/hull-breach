from gamemap import Map
from entities import Character

class Game(object):
	"""width and height are the width and height of the starting level"""
	def __init__(self, width, height):
		self.mapt = Map(width, height)
		self.entitylist = []


		h = []
		for i in range(self.width):
			h.append("dagger")
		for i in range(self.height):
			self.entitylist.append(h)

		self.player = Character("Frank", "thief", width / 2, height / 2)

		self.entitylist[self.player.y][self.player.x] = 'guy'

	def entity_at(self, x, y):
		return entitylist[y][x]

	def current_level(self):
		return self.mapt.get_level()

	def tick(self):
		for entity in self.entitylist:
			entity.tick()

	def move_player(self, direction):	# direction should be one of N, S, E, W, NE, SE, NW, SW as a string
		# horizontal/vertical movement
		if direction.lower() == "n":
			if self.entity_at(self.player.x, self.player.y - 1).walkable:
				self.player.move(self.player.x, self.player.y - 1)
		if direction.lower() == "s":
			if self.entity_at(self.player.x, self.player.y + 1).walkable:
				self.player.move(self.player.x, self.player.y + 1)
		if direction.lower() == "e":
			if self.entity_at(self.player.x + 1, self.player.y).walkable:
				self.player.move(self.player.x - 1, self.player.y)
		if direction.lower() == "w":
			if self.entity_at(self.player.x - 1, self.player.y).walkable:
				self.player.move(self.player.x - 1, self.player.y)

		# diagonal movement
		if direction.lower() == "ne":
			if self.entity_at(self.player.x + 1, self.player.y - 1).walkable:
				self.player.move(self.player.x + 1, self.player.y - 1)
		if direction.lower() == "se":
			if self.entity_at(self.player.x + 1, self.player.y + 1).walkable:
				self.player.move(self.player.x + 1, self.player.y + 1)
		if direction.lower() == "nw":
			if self.entity_at(self.player.x - 1, self.player.y - 1).walkable:
				self.player.move(self.player.x - 1, self.player.y - 1)
		if direction.lower() == "sw":
			if self.entity_at(self.player.x - 1, self.player.y + 1).walkable:
				self.player.move(self.player.x - 1, self.player.y + 1)
