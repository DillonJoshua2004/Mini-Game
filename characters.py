# basic class to create other classes from.
class character:

	name = None
	hp = None
	mp = None
	
	def __init__(self, name, hp, mp):
		self.name = name
		self.hp = hp
		self.mp = mp

	# the nicely function just formats it
	def nicely(self):
		print(f"""Name: {self.name}\nHealth: {self.hp}\nMagic Power: {self.mp}""")

	def isAlive(self):
		if self.hp <= 0:
			print(f"{self.name} has died")
			return False
		else:
			print(f"{self.name} lives on!")
			return True

class player(character):

	def __init__(self, name):
		self.name = name
		self.hp = 10
		self.mp = 100

	def nicely(self):
		print(f"""Name: {self.name}\nHealth: {self.hp}\nMagic Power: {self.mp}""")


"""player1 = player(input("Enter your characters name: ")) # testing
player1.nicely()
print(player1.isAlive())
print() # the random prints are just to separate whats printed out """


class weak_enemy(character):
	type = None # whether they are vampires or orcs or dragons, etc. Default: goblin
	
	def __init__(self, name, type):
		self.name = name
		self.hp = 50
		self.mp = 150
		self.type = type

	def nicely(self):
		print(f"""Name: {self.name}\nHealth: {self.hp}\nMagic Power: {self.mp}\nType: {self.type}""")


"""goblin = weak_enemy("Goblin", "Midg3t Goblin") # testing
goblin.nicely()
print(goblin.isAlive())
print()
zombie = weak_enemy("Zombie", "Cr@ckh3ad Zombie") # testing
zombie.nicely()
print(zombie.isAlive())
print()
turdle = weak_enemy("Turdle", "Turd") # testing
turdle.nicely()
print(turdle.isAlive())
print()"""

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
		self.hp = 222
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

"""boss1 = boss("uncle gi", 2000, 20000, "couch potato") # testing
boss1.nicely()
print(boss1.isAlive())
print()"""

