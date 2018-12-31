
class Entity(object):
	"""docstring for Entity"""
	def __init__(self, name, x, y):
		self.name = name
		self.walkable = True		# if this is true then the player can walk over this entity
		self.whackable = 0			# if this is 0 then the player cannot attack this entity
									# if this is 1 then the player can attack the entity manually
									# if this is 2 then the player defaults to attacking the entity
		self.wieldable = False		# if this is true then this item can be used as a weapon
		self.wearable = False			# if this is true then this item can be worn as armor
		self.x = x
		self.y = y
		self.modifier = ""
		self.condition = 100		# integer between 0,100; 100 is best condition, 0 is worst
		self.damage = 1				# how much damage this entity does when wielded
		self.inventory = []			# the items that this entity (person/creature/container) is holding


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

class Critter(Entity):
	def __init__(self, name, x, y):
		self.name = name
		self.x = x
		self.y = y
		self.walkable = False
		self.whackable = 1

	def set_attributes(health, armor, strength, constitution, dexterity, intelligence, wisdom, charisma):
		self.health = health
		self.armor = armor
		self.strength = strength
		self.constitution = constitution
		self.dexterity = dexterity
		self.intelligence = intelligence
		self.wisdom = wisdom
		self.charisma = charisma