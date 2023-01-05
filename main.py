import time, os
import random as rndm
from characters import *

# before editing the program read the notes.txt file, which will be updated from time to time


def boss_dmg(health, mp):
	"""
	the damage the boss does to the player,
 	i decided to take the mp of the boss as an extra input
	to set a threshold for mp for the boss to be able to do
 	a certain amount of damage
	"""
	damage = rndm.randint(0, 100)
	hit_or_miss = rndm.randint(1, 10)
	multiplier = rndm.uniform(0.1,0.5)
	if hit_or_miss not in [1,2,3,4]:
		if damage == 69 and mp >= 750:
			health = 0
			return health
		elif damage <= 50:
			return round(health - (multiplier * 6), 3)
		elif (damage >= 51 and damage <= 68) or (damage >= 70 and damage <= 79):
			return round(health - (multiplier * 8), 3)
		elif damage >= 80 and mp >= 750:
			return round(health - (multiplier * 10), 3)
	else:
		return print("Attack Missed")


def damage_done(health):
	"""
 	the damage the player does to the opponent
  	the else statement basically wipes out 50% of the enemy's health
	"""
	damage = rndm.randint(0, 18)
	multiplier = rndm.uniform(0.8, 1.1)
	if damage in [0, 1, 2, 3, 4, 5]:
		return round(health - (multiplier * 4), 3)
	elif damage in [6, 7, 8, 9, 10, 11]:
		return round(health - (multiplier * 7), 3)
	elif damage in [12, 13, 14, 15, 16, 17]:
		return round(health - (multiplier * 10), 3)
	else:
		return health - (health * 0.5)


def damage_received(health, difficulty):
	"""
	the damage enemies do to the player
	"""
	multiplier = rndm.uniform(0.3,0.5)
	if difficulty == "weak":
		return round(health - (5.5 * multiplier), 3)
	elif difficulty == "medium":
		return round(health - (6 * multiplier), 3)
	elif difficulty == "strong":
		return round(health - (7 * multiplier), 3)
	else:
		return print("That Input isn't valid. Please try again.")



# initialising the variable for the player
player_health = []
p1 = player(input("Enter you character\'s name: "))
hp = p1.hp
player_health.append(hp)

# dictionary to store the enemies' hp
enemy_health = {
	'weak': {''},
	'medium': {''},
	'hard': {''},
	'boss': {''}
}

# initialising the variables for the enemies and their hp's
we1 = weak_enemy('Goblin', "Goblin")
we2 = weak_enemy('Zombie', "Zombie")
we3 = weak_enemy('Turdle', "Turd")
me1 = medium_enemy('Orc', "Orc")
me2 = medium_enemy('Wizard', "Wizard")
me3 = medium_enemy('Centaur', "Centaur")
se1 = hard_enemy('Ceuthonymus', "Spirit")
se2 = hard_enemy('Almops', "Giant")
se3 = hard_enemy('Euryale', "Gorgon")
b1 = boss('Apollo', 1000, 550, "Greek God")
b2 = boss('Hades', 1500, 550, 'Greek God')
b3 = boss('Ares', 2000, 750, 'Greek God')
b4 = boss('Zeus', 2500, 800, 'Greek God')
b5 = boss('Chronos', 3000, 1000, 'Greek God')

enemy_health['weak'] = {'Goblin': we1.hp, 'Zombie': we2.hp, 'Turdle': we3.hp}
enemy_health['medium'] = {'Orc': me1.hp, 'Wizard': me2.hp, 'Centaur': me3.hp}
enemy_health['hard'] = {'Ceuthonymus': se1.hp, 'Almops': se2.hp, 'Euryale': se3.hp}
enemy_health['boss'] = {'Apollo': b1.hp, 'Hades': b2.hp, 'Ares': b3.hp, 'Zeus': b4.hp, 'Chronos': b5.hp}



# this works, but what i need to do is adjust the damage functions to make it more fair for the player, as it's currently unbalanced
# finally managed to make a function to do the battle work for me, so now i dont need to repeat these lines anymore
def battle(player_health, type, enemy_health, enemy):
	while player_health[0] > 0 and enemy_health > 0:
		dmg_enemy = damage_done(enemy_health)
		enemy_health = dmg_enemy
		print()
		print(f"{enemy.name} has been hit by {p1.name}. {enemy.name}\'s remaining hp is: {enemy_health}")
		print()
		if enemy_health > 0:
			dmg_player = damage_received(player_health[0], type)
			player_health[0] = dmg_player
			print(f"{p1.name} has been hit by {enemy.name}. {p1.name}\'s remaining hp is: {player_health[0]}")
			print()
		else:
			break

	
battle(player_health, 'weak', enemy_health['weak']['Goblin'], we1)


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
