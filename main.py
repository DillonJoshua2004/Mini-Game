import time, os
import random as rndm
from characters import *

# before editing the program read the notes.txt file, which will be updated from time to time

enemies = {
 "weak": {"Goblin", "Zombie", "Turdle"},
 "medium": {"Orc", "Wizard", "Centaur"},
 "hard": {"Ceuthonymus", "Almops", "Euryale"},
 "boss": {"Chronos", "Zeus", "Freya", "Ares", "Hades"}
}


def boss_dmg(health):
	# the damage the boss does to the player
	damage = rndm.randint(0, 100)
	hit_or_miss = rndm.randint(1, 2)
	if hit_or_miss == 1:
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


# the code below is to acces the hp for the player form the player class. Then, i tested the damage_received function to check if the new health value is used as the input each time.
"""
player_health = []
hp = player('me').hp
print(health)
player_health.append(hp)
print(player_health)
print()

dmg = damage_received(player_health[0], 'hard')
player_health[0] = dmg
print(player_health)
"""


# the code below is to access the hp for the enemy from their relative classes. Now i need to test the damage_done function to check if the new health value is used as the input each time.
# I decided to use a dictionary to store the health for enemies of each difficulty as it would be easier to access. Made it into a 2d dictionary so that i can store multiple hp values as there are multiple enemies in each catagory
"""
enemy_health = {
 'weak': {''},
 'medium': {''},
 'hard': {''}
}
we_hp = weak_enemy('me', 'v').hp
print(we_hp)
enemy_health['weak'] = {'h1': we_hp, 'h2': we_hp, 'h3': we_hp}
print('accessing: ', enemy_health['weak'])
print(enemy_health)
print()

me_hp = medium_enemy('me', 'vv').hp
print(me_hp)
enemy_health['medium'] = {'h1': me_hp, 'h2': me_hp, 'h3': me_hp}
print('accessing: ', enemy_health['medium'])
print(enemy_health)
print()

se_hp = hard_enemy('me', 'vvv').hp
print(se_hp)
enemy_health['hard'] = {'h1': se_hp, 'h2': se_hp, 'h3': se_hp}
print('accessing: ', enemy_health['hard'])
print(enemy_health)
print()
"""

# the code below is to deal damage to the enemy using the damage_done function
"""
dmg = damage_done(enemy_health['weak'])
enemy_health['weak'] = dmg
print(enemy_health)
print()
"""




exit()  # this will just be here until i finish testing my code for the damage

# basic loop to start the game
while True:
	print("Initialising Game")
	time.sleep(1)
	os.system("clear")
	# need to write the rest of the story code here
	# code for meeting and facing a WEAK enemy
	# need to write the rest of the story code here
	# code for meeting and facing a WEAK enemy
	# need to write the rest of the story code here
	# code for meeting and facing a WEAK enemy
	# need to write the rest of the story code here
	# code for meeting and facing a WEAK enemy
	# need to write the rest of the story code here
	# need to write the rest of the story code here
	# code for meeting and facing a BOSS
	# code for meeting and facing a MEDIUM enemy
	# need to write the rest of the story code here
	# code for meeting and facing a MEDIUM enemy
	# need to write the rest of the story code here
	# code for meeting and facing a MEDIUM enemy
	# need to write the rest of the story code here
	# code for meeting and facing a MEDIUM enemy
	# need to write the rest of the story code here
	# code for meeting and facing a BOSS
	# need to write the rest of the story code here
	# code for meeting and facing a BOSS
	# need to write the rest of the story code here
	# code for meeting and facing a BOSS
	# code for meeting and facing a HARD enemy
	# need to write the rest of the story code here
	# code for meeting and facing a HARD enemy
	# need to write the rest of the story code here
	# code for meeting and facing a HARD enemy
	# need to write the rest of the story code here
	# code for meeting and facing a BOSS
