import time, os
import random as rndm
from characters import *

# before editing the program read the notes.txt file, which will be updated from time to time


"""
# function to be used after a battle to decide whether they get a potion for defeating an enemy or not
# will keep it like this until i've finished testing it

def give_potion(health):
	chance = random.randint(1,100)
	if chance <= 24 or health <= (p1.hp * 0.28):
		inventory.append('potion')

# function to use a potion to heal one's self, this will be asked after evey 3-4 rounds
def use_potion(choice, no_of_potions, current_health):
	if choice[0].lower() == 'y':
		inventory.remove('potion')
		if no_of_potions > 0:
			if current_health <= 0.5 * p1.hp:
				current_health *= 0.5
"""
		
def damage_done(health):
	"""
 	the damage the player does to the opponent
  	the else statement basically wipes out 50% of the enemy's health
   	if none of the other conditions are met
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


def damage_received(health, difficulty, mp):
	"""
	the damage enemies do to the player
	"""
	hit_or_miss = rndm.randint(1,10)
	multiplier = rndm.uniform(0.3,0.5)
	if difficulty == "weak":
		return round(health - (5.5 * multiplier), 3)
	elif difficulty == "medium":
		return round(health - (6 * multiplier), 3)
	elif difficulty == "strong":
		return round(health - (7 * multiplier), 3)
	elif difficulty == "boss":
		if mp >= 750 and hit_or_miss not in [1,2,3,4,5,6]:
			return round(health - (8.5 * multiplier), 3)
		else:
			if hit_or_miss not in [1,2,3,4,5]:
				return round(health - (8 * multiplier), 3)
	else:
		return print("That Input isn't valid. Please try again.")



# initialising the variable for the player
inventory = ['potion'] # added this just to store potions, they have 1 at the start
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
b1 = boss('Apollo', 300, 550, "Greek God")
b2 = boss('Hades', 350, 550, 'Greek God')
b3 = boss('Ares', 400, 750, 'Greek God')
b4 = boss('Zeus', 450, 800, 'Greek God')
b5 = boss('Chronos', 500, 1000, 'Greek God')

enemy_health['weak'] = {'Goblin': we1.hp, 'Zombie': we2.hp, 'Turdle': we3.hp}
enemy_health['medium'] = {'Orc': me1.hp, 'Wizard': me2.hp, 'Centaur': me3.hp}
enemy_health['hard'] = {'Ceuthonymus': se1.hp, 'Almops': se2.hp, 'Euryale': se3.hp}
enemy_health['boss'] = {'Apollo': b1.hp, 'Hades': b2.hp, 'Ares': b3.hp, 'Zeus': b4.hp, 'Chronos': b5.hp}



# this works, but what i need to do is adjust the damage functions to make it more fair for the player, as it's currently unbalanced
# finally managed to make a function to do the battle work for me, so now i dont need to repeat these lines anymore
def battle(player_health, type, enemy_health, enemy, mp):
	while player_health[0] > 0 and enemy_health > 0:
		time.sleep(2.5)
		os.system('clear')
		dmg_enemy = damage_done(enemy_health)
		enemy_health = dmg_enemy
		print()
		print(f"{enemy.name} has been hit by {p1.name}. {enemy.name}\'s remaining hp is: {enemy_health}")
		print()
		if enemy_health > 0:
			dmg_player = damage_received(player_health[0], type, mp)
			player_health[0] = dmg_player
			print(f"{p1.name} has been hit by {enemy.name}. {p1.name}\'s remaining hp is: {player_health[0]}")
			print()
		else:
			break

"""
testing out the function. it works but i need to work on adding the health prompt and the actual healing command to the code. once that's done im finished

battle(player_health, 'weak', enemy_health['weak']['Goblin'], we1, we1.mp)
battle(player_health, 'medium', enemy_health['medium']['Wizard'], me2, me2.mp)
battle(player_health, 'hard', enemy_health['hard']['Ceuthonymus'], se1, se1.mp)
battle(player_health, 'boss', enemy_health['boss']['Chronos'], b5, b5.mp)
"""

exit() # keeping this here for now until testing is done


# basic loop to start the game and for the battles
while True:
	print("Initialising Game")
	time.sleep(1.18)
	os.system("clear")
	
