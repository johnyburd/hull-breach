from gamemap import Map

class Game(object):
	"""width and height are the width and height of the starting level"""
	def __init__(self, width, height):
		self.mapt = Map(width, height)

	def current_level(self):
		return self.mapt.get_level()