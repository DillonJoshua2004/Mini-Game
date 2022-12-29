import time, os
import random as rndm
from characters import *

# before editing the program read the notes.txt file, which will be updated from time to time.


def boss_dmg(health):
	# the damage the boss does to the player
	damage = rndm.randint(0, 100)
	hit_or_miss = rndm.randint(1, 10)
	if hit_or_miss in [1,2,3,4]:
		if damage == 69:
			health = 0
			return health
		elif damage <= 50:
			return health - (health * 0.15)
		elif damage >= 51 and damage <= 68 or damage >= 70 and damage <= 79:
			return health - (health * 0.30)
		elif damage >= 80:
			return health - (health * 0.40)
	else:
		return print("Attack Missed")


def damage_done(health):
	# the damage the player does to the opponent
	damage = rndm.randint(0, 18)
	if damage in [0, 1, 2, 3, 4, 5]:
		return health - (health * 0.08)
	elif damage in [6, 7, 8, 9, 10, 11]:
		return health - (health * 0.14)
	elif damage in [12, 13, 14, 15, 16, 17]:
		return health - (health * 0.18)
	else:
		return health - (health * 0.5)


def damage_received(health, difficulty):
	# the damage enemies do to the player
	if difficulty == "easy":
		return health - 1.5
	elif difficulty == "medium":
		return health - 3
	elif difficulty == "hard":
		return health - 4.5
	else:
		return print("That Input isn't valid. Please try again.")
		

# example code to do damage to the player when facing a hard enemy
"""
dmg = damage_received(player_health[0], 'hard')
player_health[0] = dmg
print(player_health)
"""

# the code below is to deal damage to the enemy using the damage_done function
"""
dmg = damage_done(enemy_health['weak']['h1'])
enemy_health['weak']['h1'] = dmg
print(enemy_health)
"""

# the code below is to deal damage to the boss using the damage_done function
"""
dmg = damage_done(enemy_health['boss']['h1'])
enemy_health['boss']['h1'] = dmg
print(enemy_health)
print()
"""


# initialising the variable for the player
player_health = []
p1 = player(input("Enter you character\'s name: "))
hp = p1.hp
print('Player health:', hp) # testing
player_health.append(hp)
print('Array with the player\'s health stored: ', player_health) # testing

# dictionary to sore the enemies' hp
enemy_health = {
	'weak': {''},
	'medium': {''},
	'hard': {''},
	'boss': {''}
}

# initialising the variables for the enemies and their hp's
we1 = weak_enemy('Goblin', "Goblin")
we2 = weak_enemy('Zombie', "Zombie")
we3 = weak_enemy('Turdle', "Turdle")
me1 = medium_enemy('Orc', "Orc")
me2 = medium_enemy('Wizard', "Wizard")
me3 = medium_enemy('Centaur', "Centaur")
se1 = hard_enemy('Ceuthonymus', "Spirit")
se2 = hard_enemy('Almops', "Giant")
se3 = hard_enemy('Euryale', "Gorgon")
b1 = boss('Apollo', 1000, 500, "Greek God")
b2 = boss('Hades', 1500, 600, 'Greek God')
b3 = boss('Ares', 2000, 700, 'Greek God')
b4 = boss('Zeus', 2500, 800, 'Greek God')
b5 = boss('Chronos', 3000, 1000, 'Greek God')

enemy_health['weak'] = {'Goblin': we1.hp, 'Zombie': we2.hp, 'Turdle': we3.hp}
enemy_health['medium'] = {'Orc': me1.hp, 'Wizard': me2.hp, 'Centaur': me3.hp}
enemy_health['hard'] = {'Ceuthonymus': se1.hp, 'Almops': se2.hp, 'Euryale': se3.hp}
enemy_health['boss'] = {'Apollo': b1.hp, 'Hades': b2.hp, 'Ares': b3.hp, 'Zeus': b4.hp, 'Chronos': b5.hp}


print(enemy_health) # testing
print('Weak Enemy (name: health)', enemy_health['weak']) # testing
print('Goblin health:', enemy_health['weak']['Goblin']) # testing

exit()

# basic loop to start the game and for the battles
while True:
	print("Initialising Game")
	time.sleep(1)
	os.system("clear")
	print(f"First battle is against {we1.name}")
	"""
	print(f"Second battle is against {we2.name}")
	print(f"Third battle is against {we3.name}")
	print(f"FIRST BOSS BATTLE\nYour Enemy is {b1.name}")
	print(f"Fourth battle is against {me1.name}")
	print(f"Fifth battle is against {me2.name}")
	print(f"Sixth battle is against {me3.name}")
	print(f"SECOND BOSS BATTLE\nYour Enemy is {b2.name}")
	print(f"THIRD BOSS BATTLE\nYour Enemy is {b3.name}")
	print(f"Seventh battle is against {se1.name}")
	print(f"Eigth battle is against {se2.name}")
	print(f"Ninth battle is against {se3.name}")
	print(f"FOURTH BOSS BATTLE\nYour Enemy is {b4.name}")
	print(f"FIFTH BOSS BATTLE\nYour Enemy is {b5.name}")
	"""
	# Commenting the rest of the code for now since i still need to make changes to the way the damage functions work
