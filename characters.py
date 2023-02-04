# basic/parent class to create other classes from.

class character:

	name = 0
	hp = 0
	mp = 0
	
	def __init__(self, name, hp, mp):
		self.name = name
		self.hp = hp
		self.mp = mp

	# the nicely function just formats it
	def nicely(self):
		print(f"""Name: {self.name}\nHealth: {self.hp}\nMagic Power: {self.mp}""")

class player(character):

	def __init__(self, name):
		self.name = name
		self.hp = 38
		self.mp = 100

	def nicely(self):
		print(f"""Name: {self.name}\nHealth: {self.hp}\nMagic Power: {self.mp}""")



class weak_enemy(character):
	type = None # whether they are vampires or orcs or dragons, etc.
	
	def __init__(self, name, type):
		self.name = name
		self.hp = 50
		self.mp = 150
		self.type = type

	def nicely(self):
		print(f"""Name: {self.name}\nHealth: {self.hp}\nMagic Power: {self.mp}\nType: {self.type}""")


class medium_enemy(character):
	type = None

	def __init__(self, name, type):
		self.name = name
		self.hp = 100
		self.mp = 250
		self.type = type

	def nicely(self):
		print(f"""Name: {self.name}\nHealth: {self.hp}\nMagic Power: {self.mp}\nType: {self.type}""")


class hard_enemy(character):
	type = None

	def __init__(self, name, type):
		self.name = name
		self.hp = 200
		self.mp = 333
		self.type = type

	def nicely(self):
		print(f"""Name: {self.name}\nHealth: {self.hp}\nMagic Power: {self.mp}\nType: {self.type}""")

# just made a generic one, the boss difficulty shall be specified to the player as they progress
class boss(character):
	type = None

	def __init__(self, name, hp, mp, type):
		self.name = name
		self.hp = hp
		self.mp = mp
		self.type = type

	def nicely(self):
		print(f"""Name: {self.name}\nHealth: {self.hp}\nMagic Power: {self.mp}\nType: {self.type}""")

