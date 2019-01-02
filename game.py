from gamemap import Map
from entities import *

class Game(object):
	"""width and height are the width and height of the starting level"""
	def __init__(self, width, height):
		self.mapt = Map(width, height)
		self.entitylist = []

	def current_level(self):
		return self.mapt.get_level()

	def tick(self):
		for entity in self.entitylist:
			entity.tick()

	def move_player(self):
		pass