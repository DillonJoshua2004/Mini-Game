import time, os
import random as rndm
# from characters import * -- to access the code for the characters

# before editing the program read the notes.txt file

enemies = {"weak": {"Goblin", "Zombie", "Turdle"}, 
		   "medium": {"Orc", "Wizard", "Centaur"},
		  "hard": {"Ceuthonymus", "Almops", "Euryale"},
		  "boss": {"Chronos", "Zeus", "Freya", "Ares", "Hades"}}

def boss_dmg(health):
	damage = rndm.randint(0,100)
	hit_or_miss = rndm.randint(1,2)
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
	damage = rndm.randint(0,18)
	if damage in [0,1,2,3,4,5]:
		return health - (health * 0.08)
	elif damage in [6,7,8,9,10,11]:
		return health - (health * 0.14)
	elif damage in [12,13,14,15,16,17]:
		return health - (health * 0.18)
	else:
		return health - (health * 0.5)

def damage_received(health, difficulty):
	if difficulty == "easy":
		return health - 1
	elif difficulty == "medium":
		return health - 2
	elif difficulty == "hard":
		return health - 4
	else:
		return print("That Input isn't valid. Please try again.")

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
	



