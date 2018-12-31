
class Entity(object):
	"""docstring for Entity"""
	def __init__(self, name, x, y):
		self.name = name
		self.walkable = True		# if this is true then the player can walk over this entity
		self.whackable = False		# if this is true then the player can attack this entity
		self.wieldable = False		# if this is true then this item can be used as a weapon
		self.armor = False			# if this is true then this item can be worn as armor
		self.x = x
		self.y = y
		self.modifier = ""
		self.condition = 100		# integer between 0,100; 100 is best condition, 0 is worst
		self.damage = 1				# how much damage this entity does when wielded


	def wield(self):
		if wieldable:
			pass # TODO: make this do something

		return False
		
	def die(self):
		pass

	def move(self, newx, newy):
		self.x = newx
		self.y = newy

	def tick(self):
		pass

