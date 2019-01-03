
class Entity(object):
	"""docstring for Entity"""
	def __init__(self, name, x, y):
		self.name = name
		self.walkable = True		# if this is true then the player can walk over this entity
		self.whackable = 0			# if this is 0 then the player cannot attack this entity
									# if this is 1 then the player can attack the entity manually
									# if this is 2 then the player defaults to attacking the entity
		self.satiation = -1			# represents how much this item removes from hunger if eaten
									# if satiation is -1, then the item cannot be eaten
		self.hunger = 0				# 0 is the minimum hunger, 100 is max
		self.wieldable = False		# if this is true then this item can be used as a weapon
		self.wearable = False		# if this is true then this item can be worn as armor
		self.x = x
		self.y = y
		self.modifier = ""
		self.condition = 100		# integer between 0,100; 100 is best condition, 0 is worst
		self.damage = 1				# how much damage this entity does when wielded
		self.inventory = []			# the items that this entity (person/creature/container) is holding
		self.weight = 1				# how much the item weighs in pounds
		self.age = 0				# how long the item's been around

	def wield(self):
		if wieldable:
			pass # TODO: make this do something

		return False

	def tick(self):
		age += 1
		
	def die(self):
		pass

	def move(self, newx, newy):
		self.x = newx
		self.y = newy

	def tick(self):
		pass

class Character(Entity):
	"""Playable characters"""
	def __init__(self, name, type, x, y):
		super().__init__(name, x, y)
		self.type = type
		self.walkable = False
		
		if self.type.lower() == "thief":
			self.weight = 160
			self.inventory = []


class Knife(object):
	"""docstring for Knife"""
	def __init__(self, name, x, y):
		super().__init__()
		self.walkable = True
		self.whackable = False
		self.wieldable = False
		self.inventory = None
		self.corroded = -1		# this number is the first tick at which the item was corroded
								# if the item is not corroded, this number is -1

	def tick(self):
		if corroded > -1:
			if self.age - self.corroded >= 1000:
				self.die()

	def die(self):
		pass


class Critter(Entity):
	def __init__(self, name, x, y):
		self.name = name
		self.x = x
		self.y = y
		self.walkable = False
		self.whackable = 1

	def set_attributes(health, weight, armor, strength, constitution, dexterity, intelligence, wisdom, charisma):
		self.health = health
		self.armor = armor
		self.strength = strength
		self.constitution = constitution
		self.dexterity = dexterity
		self.intelligence = intelligence
		self.wisdom = wisdom
		self.charisma = charisma

	def eat(self, item):
		if item.satiation == -1:
			return False
		self.hunger -= item.satiation
		return True

	def die(self):
		self.set_attributes(0,0,0,0,0,0,0,0)
