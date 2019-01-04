from gamemap import Map
from entities import Character

class Game(object):
	"""width and height are the width and height of the starting level"""
	def __init__(self, width, height):
		self.mapt = Map(width, height)

		self.player = Character("Frank", "thief", int(width / 2), int(height / 2))

		self.mapt.levels[0].set_entity(self.player.x, self.player.y, self.player)

	def entity_at(self, x, y):
		return entitylist[y][x]

	@property
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
