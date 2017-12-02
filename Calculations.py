import Globals as globals
import math

'''
The primary purpose of the calculations file is to provide the Progress Panel with the number values of
any effects the character is using. These effects can vary from a simple value to a complicated
calculation using spell ranks and/or lore ranks with a set min and max. Each method corresponses to an
effect located in the Create_Database.py file along with a set of effect tags that indicate what parameters
the effect changes.
'''

# A few select calculations are dependent on information other than skill training. This dictionary will
# keep track of that special information so the these calculations can be performed. The Progresson Panel 
# will populate the dictionary as needed.
override_dict = {}


# While it is possible to use a formula to calculate the summation bonus for each seed. The process is 
# complicated and time consuming. So instead, this functions references a table containing all the summation
# seed values and uses a simple for loop to figure out what bonus to give by comparing the given ranks to 
# each summation value of the desired seed.
def Get_Summation_Bonus(seed, ranks):
	summation_array = globals.summation_bonuses[seed]
	arr_size = len(summation_array)
	bonus = 0
	
	for i in range(arr_size):
		if ranks < summation_array[i]:
			break
				
		bonus += 1
		
	return bonus
	

# Takes the given ranks and existing bonus of a skill and converts the ranks into a skill bonus.
# To make sure the calculate is accurate, the bonus is calculated one rank at a time.	
def Convert_Ranks_To_New_Bonus(existing_bonus, new_ranks):
	total_bonus = existing_bonus
	
	while(new_ranks > 0):
		if total_bonus >= 140:
			total_bonus += new_ranks
			break
			
		elif total_bonus >= 120:
			total_bonus += 2
			new_ranks -= 1
				
		elif total_bonus >= 90:
			total_bonus += 3
			new_ranks -= 1
				
		elif total_bonus >= 50:
			total_bonus += 4
			new_ranks -= 1
				
		elif new_ranks >= 1:
			total_bonus += 5
			new_ranks -= 1			
							
	return total_bonus - existing_bonus	
	

# Takes the given bonus and existing ranks of a skill and converts the ranks into skill ranks.
# To make sure the calculate is accurate, the ranks are calculated one rank at a time from the bonus.	
def Convert_Bonus_To_New_Ranks(existing_ranks, new_bonus):	
	total_ranks = existing_ranks
	
	while(new_bonus > 0):
		if total_ranks >= 40:
			total_ranks += new_bonus
			break
			
		elif total_ranks >= 30 and new_bonus >= 2:
			if new_bonus >= 2:
				total_ranks += 1
				new_bonus -= 2
				
		elif total_ranks >= 20 and new_bonus >= 3:
			if new_bonus >= 3:
				total_ranks += 1
				new_bonus -= 3
				
		elif total_ranks >= 10 and new_bonus >= 4:
			if new_bonus >= 4:
				total_ranks += 1
				new_bonus -= 4
				
		elif new_bonus >= 5:
			total_ranks += 1
			new_bonus -= 5
				
		else:
			if total_ranks == 0 and new_bonus != 0:
				total_ranks = 1
			break
			
	return total_ranks - existing_ranks

	
# Determine how many ranks the character has at "level" in a given skill if Dynamic ("D") is set.
# Otherwise use the given number of ranks.
# This method will also determine if effect in question is part of a spell circle and if the 
# character has that spell circle. If the character has the spell circle or it is a "minor"
# circle, all ranks are used. If it is part of "major" circle the character doesn't have,
# only half the ranks are used. If it is part of a "profession" circle the character doesn't have
# only 1/3 of the ranks are used.
def Get_Skill_Ranks(effect, level, skill_name, circle_name):
	need_lore = 1 if circle_name != "" else 0
	skill = globals.LdP_effect_display_scaling["%s ranks" % skill_name]
	
	if effect.scaling_arr[skill] == "D":
		if level > 100:
			skill_ranks = int(globals.character.skills_list[skill_name].Postcap_Get_Total_Ranks_Closest_To_Interval(level))	
			skill_ranks += int(globals.character.skills_list[skill_name].total_ranks_by_level[100].get())	
		else:
			skill_ranks = int(globals.character.skills_list[skill_name].total_ranks_by_level[level].get())	
	else:
		skill_ranks  = int(effect.scaling_arr[skill])	
			
	if need_lore:
		if "Minor" in circle_name or circle_name in globals.character.profession.spell_circles:
			return skill_ranks	
		elif "Major" in circle_name:
			return math.floor(skill_ranks / 2)
		else:
			return math.floor(skill_ranks / 3)
		
	else:
		return skill_ranks


# Determine how many ranks the character has at "level" in a given maneuver if Dynamic ("D") is set. 
# Otherwise use the given number of ranks.
def Get_Maneuver_Ranks(effect, level, man_name, type):
		ranks = 0
		
		if type == "armor":
			maneuver_list = globals.character.armor_maneuvers_list
		elif type == "shield":
			maneuver_list = globals.character.shield_maneuvers_list
		elif type == "combat":
			maneuver_list = globals.character.combat_maneuvers_list			

		if effect.scaling_arr["Maneuver ranks"] == "D" and man_name in maneuver_list:
			man = maneuver_list[man_name]		
			
			if level > 100:			
				ranks = int(man.total_ranks_by_level[100].get())
				ranks += int(man.Postcap_Get_Total_Ranks_Closest_To_Interval(level))
			else:		
				ranks = int(man.total_ranks_by_level[level].get())
		else:			
			ranks = int(effect.scaling_arr["Maneuver ranks"])

		return ranks
	
	
# Get the number of rank in a given society if Dynamic ("D") is set. 
# Otherwise use the given number of ranks.
def Get_Society_Rank(effect, society_name):	
	society = globals.LdP_effect_display_scaling["%s rank" % society_name]
	if effect.scaling_arr[society] == "D":
		if globals.character.society.get() == society_name:
			rank = int(globals.character.society_rank.get())
		else:
			rank = 0
	else:			
		rank = int(effect.scaling_arr[society])
		
	return rank
	

# Calculate the true cost of a spell given it's level and how many spell research ranks in the 
# corresponding spell circle
def Get_Spellburst_Cost(skill_name, spell_level, character_level):
	spell_circle = skill_name.split(", ")[1]
	spell_ranks = 0
	extra_cost = 0 if spell_level < 9 else 0.5
	
	if spell_circle in globals.character.profession.spell_circles:
		if character_level > 100:
			spell_ranks = int(globals.character.skills_list[skill_name].Postcap_Get_Total_Ranks_Closest_To_Interval(character_level))	
			spell_ranks += int(globals.character.skills_list[skill_name].total_ranks_by_level[100].get())	
		else:
			spell_ranks = int(globals.character.skills_list[skill_name].total_ranks_by_level[character_level].get())	
		
		if spell_ranks >= spell_level:
			return 0
		else:
			return (spell_level / 2) + extra_cost					
	else:
		return spell_level + extra_cost
	

# Minor Spiritual (100s)	

# Spirit Warding I (101) - +10 Spiritual TD, +10 Bolt DS
def Calculate_101(effect, tag, level):
	if tag == "DS_Bolt":				
		return [10, "Bolt DS"]
		
	elif tag == "Spellburst":				
		return [Get_Spellburst_Cost("Spell Research, Minor Spiritual", 1, level), "mana"]
		
	elif tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":		
		TD = 10
		type = ""
		
		if tag == "TD_Spiritual":
			type = "Spiritual TD"			
		elif tag == "TD_Elemental":
			TD = math.ceil(TD * 0.5)
			type = "Elemental TD"
		elif tag == "TD_Mental": 
			TD = math.ceil(TD * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			TD = math.ceil(TD * 0.75)
			type = "Sorcerer TD"
	
		return [TD, type]

	return [0, ""]
	
	
# Spirit Barrier (102) - +20 DS, -20 melee AS and UAF. +1/-1 per 2 Spell Research, Minor Spiritual ranks above 2
def Calculate_102(effect, tag, level):		
	if tag == "AS_Melee" or tag == "DS_All" or tag == "UAF":	
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Minor Spiritual", "")		
		if level > 100:
			level = 100		
		bonus = 20 + min(level, int(math.floor((int(spell_ranks) - 2)/2)))			
			
		if tag == "DS_All":
			type = "All DS"
		elif tag == "AS_Melee":
			bonus *= -1
			type = "Melee AS"
		elif tag == "UAF":
			bonus *= -1
			type = "UAF"
		
		return [bonus, type]
		
	elif tag == "Spellburst":	
		return [Get_Spellburst_Cost("Spell Research, Minor Spiritual", 2, level), "mana"]
		
	return [0, ""]

	
# Spirit Barrier (103) - +10 DS
def Calculate_103(effect, tag, level):
	if tag == "DS_All":				
		return [10, "All DS"]
		
	elif tag == "Spellburst":	
		return [Get_Spellburst_Cost("Spell Research, Minor Spiritual", 3, level), "mana"]
		
	return [0, ""]

	
# Disease Resistance (104) - Extra warding attempt against Disease. +2 TD bonus on extra warding attempt per summation seed 1 for Spiritual Lore, Blessings ranks
def Calculate_104(effect, tag, level):
	if tag == "TD_Spiritual":				
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Minor Spiritual")			
		bonus = 2 * Get_Summation_Bonus(1, lore_ranks)	
		
		return [bonus, "Spiritual TD vs Disease"]	
		
	elif tag == "Spellburst":	
		return [Get_Spellburst_Cost("Spell Research, Minor Spiritual", 4, level), "mana"]
		
	return [0, ""]

	
# Poison Resistance (105) - Extra warding attempt against Poison. +2 TD bonus on extra warding attempt per summation seed 1 for Spiritual Lore, Blessings ranks
def Calculate_105(effect, tag, level):
	if tag == "TD_Spiritual":				
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Minor Spiritual")	
		bonus = 2 * Get_Summation_Bonus(1, lore_ranks)	
		
		return [bonus, "Spiritual TD vs Poison"]	
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Minor Spiritual", 5, level), "mana"]
	
	return [0, ""]
	

# Spirit Warding II (107) - +15 Spiritual TD, +25 Bolt DS
def Calculate_107(effect, tag, level):
	if tag == "DS_Bolt":				
		return [25, "Bolt DS"]
	elif tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":		
		TD = 15
		type = ""
		
		if tag == "TD_Spiritual":
			type = "Spiritual TD"			
		elif tag == "TD_Elemental":
			TD = math.ceil(TD * 0.5)
			type = "Elemental TD"
		elif tag == "TD_Mental": 
			TD = math.ceil(TD * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			TD = math.ceil(TD * 0.75)
			type = "Sorcerer TD"
	
		return [TD, type]
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Minor Spiritual", 7, level), "mana"]

	return [0, ""]
	
	
# Water Walking (112) - Just spellburst stuff
def Calculate_112(effect, tag, level):
	if tag == "Spellburst":				
		return [Get_Spellburst_Cost("Spell Research, Minor Spiritual", 12, level), "mana"]
		
	return [0, ""]	
	
	
# Fasthr's Reward (115) - Just spellburst stuff
def Calculate_115(effect, tag, level):
	if tag == "Spellburst":				
		return [Get_Spellburst_Cost("Spell Research, Minor Spiritual", 15, level), "mana"]
		
	return [0, ""]	
	
	
# Spirit Strike (117) - +75 AS, +75 UAF
def Calculate_117(effect, tag, level):
	if tag == "AS_All":				
		return [75, "All AS"]
	elif tag == "UAF":				
		return [75, "UAF"]

	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Minor Spiritual", 17, level), "mana"]	
		
	return [0, ""]	
	
	
# Lesser Shroud (120) - +15 DS, +20 Spiritual TD. +1 DS per 2 Spell Research, Minor Spiritual ranks over 20
def Calculate_120(effect, tag, level):		
	if tag == "DS_All":	
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Minor Spiritual", "")	
		bonus = 15 + min(40, math.floor(max(0, spell_ranks - 20)/2))
				
		return [bonus, "All DS"]
		
	elif tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":		
		TD = 20
		type = ""
		
		if tag == "TD_Spiritual":
			type = "Spiritual TD"			
		elif tag == "TD_Elemental":
			TD = math.ceil(TD * 0.5)
			type = "Elemental TD"
		elif tag == "TD_Mental": 
			TD = math.ceil(TD * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			TD = math.ceil(TD * 0.75)
			type = "Sorcerer TD"
	
		return [TD, type]		

	elif tag == "Spellburst":				
		return [Get_Spellburst_Cost("Spell Research, Minor Spiritual", 20, level), "mana"]
			
	return [0, ""]

	
# Wall of Force (140) - +100 DS
def Calculate_140(effect, tag, level):
	if tag == "DS_All":				
		return [100, "All DS"]
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Minor Spiritual", 40, level), "mana"]
		
	return [0, ""]
	

# Major Spiritual (200s)	
	
# Spirit Shield (202) - +10 DS. +1 DS per 2 Spell Research, Major Spiritual ranks above 2, up to character level
def Calculate_202(effect, tag, level):		
	if tag == "DS_All":	
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Major Spiritual", "")	
		bonus = min(100, 10 + math.floor(max(0, spell_ranks - 2)/2))				
				
		return [bonus, "All DS"]	
		
	elif tag == "Spellburst":				
		return [Get_Spellburst_Cost("Spell Research, Major Spiritual", 2, level), "mana"]
		
	return [0, ""]
	
	
# Manna (203) - +5 maximum Mana per seed 10 summation for Spiritual Lore, Blessing ranks
def Calculate_203(effect, tag, level):
	if tag == "Resource_Maximum_Mana":
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Major Spiritual")	
		bonus = 5 * Get_Summation_Bonus(10, lore_ranks)	
		
		return [bonus, "Maximum Mana"]	

	return [0, ""]	
	
	
# Unpresence (204) - Just spellburst stuff
def Calculate_204(effect, tag, level):
	if tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Major Spiritual", 4, level), "mana"]	
		
	return [0, ""]	
	
	
# Tend Lore (206) - +20 phantom First Aid ranks. +1 phantom First Aid rank per Spell Research, Ranger Base rank over 18
def Calculate_206(effect, tag, level):	
	if tag == "Skill_Phantom_Ranks_First_Aid":	
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Major Spiritual")	
		bonus = 20 + Get_Summation_Bonus(1, lore_ranks)	
		
		return [bonus, "ranks"]
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Major Spiritual", 6, level), "mana"]	
			
	return [0, ""]
	
	
# Purify Air (207) - Just spellburst stuff
def Calculate_207(effect, tag, level):
	if tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Major Spiritual", 7, level), "mana"]	
		
	return [0, ""]	
	
	
# Bravery (211)	- +15 AS, +15 UAF
def Calculate_211(effect, tag, level):
	if tag == "AS_All":				
		return [15, "All AS"]
	elif tag == "UAF":				
		return [15, "UAF"]
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Major Spiritual", 11, level), "mana"]		

	return [0, ""]	


# Heroism (215) - +25 AS, +25 UAF, +1 AS for every 10 Spiritual Lore, Blessing ranks		
def Calculate_215(effect, tag, level):
	if tag == "AS_All" or tag == "UAF":		
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Major Spiritual")		
		bonus = 25 + math.floor(lore_ranks/10)
			
		if tag == "AS_All":			
			type = "All AS"
		elif tag == "UAF":	
			type = "UAF"		
		
		return [bonus, type]
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Major Spiritual", 15, level), "mana"]			
		
	else:
		return [0, ""]		


# Spell Shield (219) - +30 bolt DS, +30 Spirit TD
def Calculate_219(effect, tag, level):
	if tag == "DS_Bolt":				
		return [30, "Bolt DS"]
	elif tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":		
		TD = 30
		type = ""
		
		if tag == "TD_Spiritual":
			type = "Spiritual TD"			
		elif tag == "TD_Elemental":
			TD = math.ceil(TD * 0.5)
			type = "Elemental TD"
		elif tag == "TD_Mental": 
			TD = math.ceil(TD * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			TD = math.ceil(TD * 0.75)
			type = "Sorcerer TD"
	
		return [TD, type]
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Major Spiritual", 19, level), "mana"]		

	return [0, ""]
	
	
# Spirit Slayer (240) - +25 bolt AS, +25 Spiritual CS. +1 Bolt AS and Spiritual CS per summation 5 seed of Spiritual Mana Control ranks
def Calculate_240(effect, tag, level):	
	if tag == "AS_Bolt" or tag == "CS_Elemental" or tag == "CS_Mental" or tag == "CS_Spiritual" or tag == "CS_Sorcerer":
		ranks = Get_Skill_Ranks(effect, level, "Spiritual Mana Control")				
		bonus = 25 + Get_Summation_Bonus(5, ranks)	
				
		if tag == "AS_Bolt":
			type = "Bolt AS"	
		elif tag == "CS_Spiritual":
			type = "Spiritual CS"		
		elif tag == "CS_Elemental":
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental CS"
		elif tag == "CS_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental CS"
		elif tag == "CS_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer CS"
			
		return [bonus, type]		

	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Major Spiritual", 40, level), "mana"]		
		
	return [0, ""]	
	

# Cleric Base (300s)	
	
# Prayer of Protection (303) - +10 DS. +1 DS per 2 Spell Research, Cleric ranks above 3 up to character level
def Calculate_303(effect, tag, level):		
	if tag == "DS_All":	
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Cleric", "")		
		bonus = 10 + min(99, math.floor(max(0, spell_ranks - 3)/2))			
				
		return [bonus, "All DS"]	
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Cleric", 3, level), "mana"]		
		
	return [0, ""]
	
	
# Benediction (307) - +5 AS, +5 ranged DS, +5 melee DS. +1 AS/DS per 2 Cleric Base ranks above 7 with a maximum bonus of +15 AS/DS, Additionally, +1 bolt AS per 2 Cleric Base ranks above 7 with a maximum bonus of +15 AS to a maximum of +51 at level 99, +5 melee and ranged DS at spell rank 7. 
def Calculate_307(effect, tag, level):	
	if tag == "AS_Melee" or tag == "AS_Ranged" or tag == "AS_Bolt" or tag == "UAF" or tag == "DS_Melee" or tag == "DS_Ranged":	
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Cleric", "")	
	
		bonus = min(10, math.floor(max(0, spell_ranks - 7)/2))
		
		if tag == "AS_Melee":
			type = "Melee AS"
		elif tag == "AS_Ranged":
			type = "Ranged AS"
		elif tag == "AS_Bolt":
			type = "Bolt AS"
			bonus += min(51, math.floor(max(0, spell_ranks - 27)/2))	
		elif tag == "UAF":
			type = "UAF"
		elif tag == "DS_Melee":
			type = "Melee DS"
		elif tag == "DS_Ranged":
			type = "Ranged DS"
	
		return [5 + bonus, type]

	return [0, ""]	
	
	
# Warding Sphere (310) - +10 DS, +10 Spiritual TD. +1 DS/TD per Spell Research, Cleric rank above 10 to a maximum bonus of +20.
def Calculate_310(effect, tag, level):		
	if tag == "DS_All" or tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Cleric", "")				
		
		bonus = 10 + math.floor((max(0, spell_ranks - 10)/2))
								
		if tag == "DS_All":
			type = "All DS"
		elif tag == "TD_Spiritual":
			type = "Spiritual TD"			
		elif tag == "TD_Elemental":
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental TD"
		elif tag == "TD_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer TD"
	
		return [bonus, type]
		
	return [0, ""]	


# Prayer (313) - +10 Spirit TD\n+10 all DS at 35 Spell Research, Cleric ranks and increases by +1 per rank above 35 up to character level
def Calculate_313(effect, tag, level):			
	if tag == "DS_All" or tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Cleric", "")					
			
		if tag == "DS_All":
			bonus = min(level, 10 + math.floor(max(0, spell_ranks - 35))) 		
			return [bonus, "All DS"]					
				
		bonus = 10		
		if tag == "TD_Spiritual":
			type = "Spiritual TD"			
		elif tag == "TD_Elemental":
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental TD"
		elif tag == "TD_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer TD"
	
		return [bonus, type]	
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Cleric", 13, level), "mana"]	
		
	return [0, ""] 
	
	
# Relieve Burden (314) - Just spellburst stuff
def Calculate_314(effect, tag, level):
	if tag == "Spellburst":				
		return [Get_Spellburst_Cost("Spell Research, Cleric", 14, level), "mana"]	
		
	return [0, ""]	
	
	
# Soul Ward (319) - Just spellburst stuff
def Calculate_319(effect, tag, level):
	if tag == "Spellburst":				
		return [Get_Spellburst_Cost("Spell Research, Cleric", 19, level), "mana"]	
		
	return [0, ""]	
	
	
# Symbol of the Proselyte (340) - Increases Bolt AS and Spiritual CS by 5 + (Influence bonus / 2)
def Calculate_340(effect, tag, level):			
	if tag == "AS_Bolt" or tag == "CS_Elemental" or tag == "CS_Mental" or tag == "CS_Spiritual" or tag == "CS_Sorcerer":	
		try:
			inf = math.ceil( int(override_dict["Influence Bonus"]) / 2 ) 					
		except:
			inf = 0
				
		bonus = 5 + inf
		
		if tag == "AS_Bolt":
			type = "Bolt AS"		
		elif tag == "CS_Spiritual":
			type = "Spiritual CS"			
		elif tag == "CS_Elemental":
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental CS"
		elif tag == "CS_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental CS"
		elif tag == "CS_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer CS"
	
		return [bonus, type]	
		
	return [0, ""]	
	
	
# Symbol of the Proselyte (340) 2 - Increases Bolt AS and Spiritual CS by 5 + (Influence bonus / 2) + (Wisdom bonus / 3)
def Calculate_340_2(effect, tag, level):			
	if tag == "AS_Bolt" or tag == "CS_Elemental" or tag == "CS_Mental" or tag == "CS_Spiritual" or tag == "CS_Sorcerer":	
		try:
			inf = math.ceil( int(override_dict["Influence Bonus"]) / 2 ) 				
		except:
			inf = 0
				
		try:
			wis = math.ceil( int(override_dict["Wisdom Bonus"]) / 3 )				
		except:
			wis = 0
			
		bonus = 5 + inf + wis
		
		if tag == "AS_Bolt":
			type = "Bolt AS"		
		elif tag == "CS_Spiritual":
			type = "Spiritual CS"			
		elif tag == "CS_Elemental":
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental CS"
		elif tag == "CS_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental CS"
		elif tag == "CS_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer CS"
	
		return [bonus, type]	
		
	return [0, ""]	
	
	
# Minor Elemental (400s)	
	
# Elemental Defense I (401) - +5 DS, +5 Elemental TD
def Calculate_401(effect, tag, level):
	if tag == "DS_All" or tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":		
		bonus = 5		
		
		if tag == "DS_All":				
			type = "All DS"	
		elif tag == "TD_Elemental":
			type = "Elemental TD"		
		elif tag == "TD_Spiritual":	
			bonus = math.ceil(bonus * 0.5)
			type = "Spritiual TD"
		elif tag == "TD_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer TD"
	
		return [bonus, type]
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Minor Elemental", 1, level), "mana"]	

	return [0, ""]
	
	
# Presence (402) - Just spellburst stuff
def Calculate_402(effect, tag, level):
	if tag == "Spellburst":				
		return [Get_Spellburst_Cost("Spell Research, Minor Elemental", 2, level), "mana"]	
		
	return [0, ""]	
	
	
# Lock Pick Enhancement (403) - Just spellburst stuff
def Calculate_403(effect, tag, level):
	if tag == "Spellburst":				
		return [Get_Spellburst_Cost("Spell Research, Minor Elemental", 3, level), "mana"]	
		
	return [0, ""]	
	
	
# Disarm Enhancement (404) - Just spellburst stuff
def Calculate_404(effect, tag, level):
	if tag == "Spellburst":				
		return [Get_Spellburst_Cost("Spell Research, Minor Elemental", 4, level), "mana"]	
		
	return [0, ""]	

	
# Elemental Defense II (406) - +10 DS, +10 Elemental TD
def Calculate_406(effect, tag, level):
	if tag == "DS_All" or tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":		
		bonus = 10		
		
		if tag == "DS_All":				
			type = "All DS"	
		elif tag == "TD_Elemental":
			type = "Elemental TD"		
		elif tag == "TD_Spiritual":	
			bonus = math.ceil(bonus * 0.5)
			type = "Spritiual TD"
		elif tag == "TD_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer TD"
	
		return [bonus, type]
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Minor Elemental", 6, level), "mana"]	

	return [0, ""]

	
# Elemental Defense III (406) - +20 DS, +15 Elemental TD
def Calculate_414(effect, tag, level):
	if tag == "DS_All" or tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":		
		bonus = 15		
		
		if tag == "DS_All":		
			bonus = 20	
			type = "All DS"	
		elif tag == "TD_Elemental":
			type = "Elemental TD"		
		elif tag == "TD_Spiritual":	
			bonus = math.ceil(bonus * 0.5)
			type = "Spritiual TD"
		elif tag == "TD_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer TD"
	
		return [bonus, type]
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Minor Elemental", 14, level), "mana"]	

	return [0, ""]	
	

# Mana Focus (418) - +10 mana recovery	
def Calculate_418(effect, tag, level):
	if tag == "Resource_Recovery_Mana_Normal":
		return [10, "Mana Recovery"]	

	return [0, ""]	
	
	
# Elemental Targeting (425) -  +25 AS, +25 UAF, +25 Elemental CS. +1 AS/UAF/Elemental CS per 2 Spell Research, Minor Elemental ranks above 25 up to a +50 at 75 ranks	
def Calculate_425(effect, tag, level):	
	if tag == "AS_All" or tag == "UAF" or tag == "CS_Elemental" or tag == "CS_Mental" or tag == "CS_Spiritual" or tag == "CS_Sorcerer":
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Minor Elemental", "")					
		
		bonus = math.floor(max(0, spell_ranks - 25)/2)		
		bonus = min(50, 25 + bonus)	
		
		if tag == "CS_Elemental":
			type = "Elemental CS"
		elif tag == "CS_Spiritual":
			bonus = math.ceil(bonus * 0.5)
			type = "Spiritual CS"		
		elif tag == "CS_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental CS"
		elif tag == "CS_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer CS"
		elif tag == "AS_All":
			type = "All AS"
		else:
			type = "UAF"		
			
		return [bonus, type]	
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Minor Elemental", 25, level), "mana"]	

	return [0, ""]		
	

# Elemental Barrier (430) - +15 DS, +15 Elemental TD. +1 DS/Elemental TD per 2 Spell Research, Minor Elemental ranks above 30	
def Calculate_430(effect, tag, level):	
	if tag == "DS_All" or tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":		
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Minor Elemental", "")					
		type = ""
		
		bonus = 15 + math.floor(max(0, spell_ranks - 30)/2)	
		
		if tag == "DS_All":
			type = "All DS"	
		elif tag == "TD_Elemental":
			type = "Elemental TD"		
		elif tag == "TD_Spiritual":	
			bonus = math.ceil(bonus * 0.5)
			type = "Spritiual TD"
		elif tag == "TD_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer TD"
	
		return [bonus, type]	
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Minor Elemental", 30, level), "mana"]	

	return [0, ""]			
	

# Major Elemental (500s)	
	
# Thurfel's Ward (503) - +20 DS. +1 DS per 4 Spell Research, Major Elemental ranks above 3. 
def Calculate_503(effect, tag, level):	
	if tag == "DS_All":		
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Major Elemental")						
		bonus = 20 + math.floor(max(0, spell_ranks - 3)/4)			
	
		return [bonus, "All DS"]	
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Major Elemental", 3, level), "mana"]	

	return [0, ""]		
	
	
# Celerity (506) - Reduces combat roundtime
def Calculate_506(effect, tag, level):
	if tag == "Roundtime_Reduction":
		'''
		if "Major Elemental" in globals.character.profession.spell_circles:
			if level > 100:
				spell_ranks  = int(globals.character.skills_list["Spell Research, Major Elemental"].Postcap_Get_Total_Ranks_Closest_To_Interval(level))	
				spell_ranks += int(globals.character.skills_list["Spell Research, Major Elemental"].total_ranks_by_level[100].get())	
			else:
				spell_ranks = int(globals.character.skills_list["Spell Research, Major Elemental"].total_ranks_by_level[level].get())	
				
		if spell_ranks > level:
			spell_ranks = level
		rP = max(.2, (50 - (0.5 * spell_ranks)) / 100)
		'''

		lore_ranks = Get_Skill_Ranks(effect, level, "Elemental Lore, Air", "Major Elemental")			

		try:
			stamina_cost = int(override_dict["Stamina Cost"])					
		except:
			stamina_cost = 11				

		bonus = 0
		rS = 30 + lore_ranks		
		stamina_total = stamina_cost
		
		# The amount of RT Reduction given by 506 is weird. Think of rS as a max threshold. You can have RT reduction equal to
		# y * stamina cost. Where y is the highest number possible where the product is equal to or less than rS.
		# While MjE ranks reduce qstrike costs, it doesn't effect roundtime directly. So it is unneed.
		while stamina_total < rS:
			stamina_total += stamina_cost
			bonus += 1			
			
		return [bonus, "Rountime Reduction"]
		
	
	
	elif tag == "Spellburst":				
		return [Get_Spellburst_Cost("Spell Research, Major Elemental", 6, level), "mana"]	
		
	return [0, ""]	
	
	
# Elemental Deflection (507) - +20 DS. +1 DS per 2 Spell Research, Major Elemental ranks above 7	
def Calculate_507(effect, tag, level):	
	if tag == "DS_All":		
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Major Elemental", "")				
		bonus = 20 + math.floor(max(0, spell_ranks - 7)/2)			
	
		return [bonus, "All DS"]		
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Major Elemental", 7, level), "mana"]	

	return [0, ""]		


# Elemental Bias (508) - +20 elemental TD	
def Calculate_508(effect, tag, level):
	if tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":		
		bonus = 20
		
		if tag == "TD_Elemental":
			type = "Elemental TD"		
		elif tag == "TD_Spiritual":	
			bonus = math.ceil(bonus * 0.5)
			type = "Spritiual TD"
		elif tag == "TD_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer TD"
	
		return [bonus, type]	
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Major Elemental", 8, level), "mana"]	
		
	return [0, ""]
		
		
# Strength (509) - +15 melee AS, +15 UAF, +15 encumbrance reduction. +1 melee AS/UAF when self-cast per seed 4 summation of Elemental Lore, Earth ranks	
def Calculate_509(effect, tag, level):
	if tag == "AS_Melee" or tag == "UAF":				
		skill_ranks = Get_Skill_Ranks(effect, level, "Elemental Lore, Earth")		
		bonus = 15 + Get_Summation_Bonus(4, skill_ranks)		
					
		if tag == "AS_Melee":
			type = "Melee AS"
		elif tag == "UAF":
			type = "UAF"		
		
		return [bonus, type]		

	elif tag == "Encumbrance_Reduction_Percent":
		return [15, "bonus"]

	elif tag == "Roundtime_Strength":
		return [15, "bonus"]
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Major Elemental", 9, level), "mana"]			

	return [0, ""]		
	
		
# Elemental Focus (513)	- +20 bolt AS. +1 bolt AS when self-cast per 2 Spell Research, Major Elemental ranks above 13 capped at character level
def Calculate_513(effect, tag, level):
	if tag == "AS_Bolt":			
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Major Elemental", "")					
		bonus = 20 + min(level, math.floor(max(0, spell_ranks - 13)/2))
		
		return [bonus, "Bolt AS"]			
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Major Elemental", 13, level), "mana"]			

	return [0, ""]	
	
	
# Mage Armor (520) Air - Air: +10 carrying capacity. +1 lb per summation seed 10 of Air Lore
def Calculate_520_Air(effect, tag, level):
	if tag == "Encumbrance_Reduction_Absolute":	
		lore_ranks = Get_Skill_Ranks(effect, level, "Elemental Lore, Air", "Major Elemental")				
		bonus = 10 + Get_Summation_Bonus(1, lore_ranks)	
		
		return [bonus, "Carry Capacity"]
		
	elif tag == "Spellburst":				
		return [Get_Spellburst_Cost("Spell Research, Major Elemental", 20, level), "mana"]	
		
	return [0, ""]	


# Temporal Revision (540) - +200 all DS	
def Calculate_540(effect, tag, level):
	if tag == "DS_All":				
		return [200, "All DS"]	
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Major Elemental", 40, level), "mana"]	
		
	return [0, ""]	

	
	
# Ranger Base (600s)
		
# Natural Colors (601) - +10 all DS. +1 DS per seed 5 summation of Spiritual Lore, Blessings ranks	
def Calculate_601(effect, tag, level):
	if tag == "DS_All":					
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Ranger")			
		bonus = 10 + Get_Summation_Bonus(5, lore_ranks)	
		
		return [bonus, "All DS"]	
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Ranger", 1, level), "mana"]	
	
	return [0, ""]
	
		
# Resist Elements (602) - +10 fire/ice/electrical bolt DS. +1 fire/ice/electrical bolt DS when self-cast per seed 5 summation of Spiritual Lore, Blessings ranks	
def Calculate_602(effect, tag, level):
	if tag == "DS_Bolt":					
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Ranger")	
		bonus = 10 + Get_Summation_Bonus(5, lore_ranks)	
		
		return [bonus, "Bolt DS vs fire/cold/electric"]			
		
	elif tag == "Spellburst":	
		return [Get_Spellburst_Cost("Spell Research, Ranger", 2, level), "mana"]			
	
	return [0, ""]
	
	
# Foraging (603) - Just spellburst stuff
def Calculate_603(effect, tag, level):
	if tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Ranger", 3, level), "mana"]	
		
	return [0, ""]	
	
	
# Skinning (604) - Just spellburst stuff
def Calculate_604(effect, tag, level):
	if tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Ranger", 4, level), "mana"]	
		
	return [0, ""]	
	
	
# Whispering Willow (605) - Just spellburst stuff
def Calculate_605(effect, tag, level):
	if tag == "Spellburst":				
		return [Get_Spellburst_Cost("Spell Research, Ranger", 5, level), "mana"]	
		
	return [0, ""]	
		

# Phoen's Strength (606) - +10 melee AS, +10 UAF, +10 encumbrance reduction		
def Calculate_606(effect, tag, level):
	if tag == "AS_Melee":				
		return [10, "Melee AS"]
	elif tag == "UAF":				
		return [10, "UAF"]

	elif tag == "Encumbrance_Reduction_Percent":
		return [10, "bonus"]
		
	elif tag == "Roundtime_Strength":
		return [10, "bonus"]
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Ranger", 6, level), "mana"]	

	return [0, ""]
	
	
# Camouflage (608) - +30 AS, +30 UAF		
def Calculate_608(effect, tag, level):
	if tag == "AS_All":				
		return [30, "All AS"]
	elif tag == "UAF":				
		return [30, "UAF"]
		
	elif tag == "Spellburst":	
		return [Get_Spellburst_Cost("Spell Research, Ranger", 8, level), "mana"]		

	return [0, ""]		
		

# Self Control (613) - +20 melee DS, +20 Spiritual TD. +1 Spiritual TD per seed 5 summation of Spiritual Lore, Blessings ranks, +1 melee DS per 2 Spell Research, Ranger Base ranks above 13 capped at +63		
def Calculate_613(effect, tag, level):
	if tag == "DS_Melee":					
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Ranger", "")	
		bonus = 15 + math.floor(max(0, spell_ranks - 13)/2)	
		bonus = min(63, bonus)
		
		return [bonus, "Melee DS"]	
		
	elif tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":	
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Ranger")	
		bonus = 20 + Get_Summation_Bonus(5, lore_ranks)	
				
		if tag == "TD_Spiritual":
			type = "Spiritual TD"			
		elif tag == "TD_Elemental":
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental TD"
		elif tag == "TD_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer TD"
	
		return [bonus, type]		
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Ranger", 13, level), "mana"]		
			
	return [0, ""]	
	
# Sneaking (617) - Just spellburst stuff
def Calculate_617(effect, tag, level):
	if tag == "Spellburst":				
		return [Get_Spellburst_Cost("Spell Research, Ranger", 17, level), "mana"]	
		
	return [0, ""]	
	
	
# Mobility (618) - +20 phantom Dodging ranks. +1 phantom Dodging rank per Spell Research, Ranger Base rank over 18
def Calculate_618(effect, tag, level):	
	if tag == "Skill_Phantom_Ranks_Dodging":	
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Ranger", "")	
		if level > 100:
			level = 100
		bonus = 20 + math.floor(max(0, spell_ranks - 18))	
		bonus = max(level, bonus)		
		
		return [bonus, "ranks"]
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Ranger", 18, level), "mana"]	

	return [0, ""]
	

# Nature's Touch (625) - +1 Spiritual TD. +1 Spiritual TD per 2 Spell Research, Ranger Base ranks over 25 up to a maximum of a +12 bonus to TD at 49 ranks
def Calculate_625(effect, tag, level):	
	if tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Ranger", "")	
		bonus = 1 + math.floor(max(0, spell_ranks - 25)/2)	
		bonus = min(12, bonus)		
		
		if tag == "TD_Spiritual":
			type = "Spiritual TD"			
		elif tag == "TD_Elemental":
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental TD"
		elif tag == "TD_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer TD"
	
		return [bonus, type]	
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Ranger", 25, level), "mana"]			

	return [0, ""]

	
# Wall of Thorns (640) - +20 DS
def Calculate_640(effect, tag, level):
	if tag == "DS_All":				
		return [20, "All DS"]
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Ranger", 40, level), "mana"]		
		
	return [0, ""]
		

# Assume Aspect (650) Bear - +20 increase to Constitution stat, +25 maximum Health. +1 increase to Constitution stat per seed 2 summation of Spiritual Lore, Blessings ranks, +1 max Health per seed 1 summation of Spiritual Lore, Summoning ranks
def Calculate_650_Bear(effect, tag, level):			
	if tag == "Statistic_Constitution":			
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Ranger")	
		bonus = 20 + Get_Summation_Bonus(2, lore_ranks)		
		
		return [bonus, "statistic increase"]				
		
	elif tag == "Resource_Maximum_Health":
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Summoning", "Ranger")	
		bonus = 25 + Get_Summation_Bonus(1, lore_ranks)	
		
		return [bonus, "maximum health"]
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Ranger", 50, level), "mana"]			
		
	return [0, ""]	
			
		
# Assume Aspect (650) Hawk - +20 Perception ranks. +1 Perception rank per seed 2 summation of Spiritual Lore, Summoning ranks
def Calculate_650_Hawk(effect, tag, level):	
	if tag == "Skill_Ranks_Perception":			
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Summoning", "Ranger")	
		bonus = 20 + Get_Summation_Bonus(2, lore_ranks)		
		
		return [bonus, "skill ranks"]	
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Ranger", 50, level), "mana"]	

	return [0, ""]	
		

# Assume Aspect (650) Jackal - +20 Ambush ranks. +1 Ambush rank per seed 2 summation of Spiritual Lore, Summoning ranks
def Calculate_650_Jackal(effect, tag, level):	
	if tag == "Skill_Ranks_Ambush":			
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Summoning", "Ranger")	
		bonus = 20 + Get_Summation_Bonus(2, lore_ranks)		
		
		return [bonus, "skill ranks"]		
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Ranger", 50, level), "mana"]		

	return [0, ""]	
	
	
# Assume Aspect (650) Lion - +20 increase to Influence and Strength stats. +1 Influence and Strength stats per seed 2 summation of Spiritual Lore, Blessings ranks
def Calculate_650_Lion(effect, tag, level):	
	if tag == "Statistic_Strength" or tag == "Statistic_Influence":		
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Ranger")	
		bonus = 20 + Get_Summation_Bonus(2, lore_ranks)		
		
		return [bonus, "statistic increase"]	
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Ranger", 50, level), "mana"]			

	return [0, ""]
	
	
# Assume Aspect (650) Owl - +20 increase to Aura and Wisdom stats. +1 increase to Aura and Wisdom stats per seed 2 summation of Spiritual Lore, Blessings ranks
def Calculate_650_Owl(effect, tag, level):	
	if tag == "Statistic_Aura" or tag == "Statistic_Wisdom":		
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Ranger")	
		bonus = 20 + Get_Summation_Bonus(2, lore_ranks)		
		
		return [bonus, "statistic increase"]	
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Ranger", 50, level), "mana"]		

	return [0, ""]
	
	
# Assume Aspect (650) Porcupine - +20 increase to Logic stat. +1 increase to Logic stat per seed 2 summation of Spiritual Lore, Blessings ranks
def Calculate_650_Porcupine(effect, tag, level):	
	if tag == "Statistic_Logic":			
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Ranger")	
		bonus = 20 + Get_Summation_Bonus(2, lore_ranks)		
		
		return [bonus, "statistic increase"]	
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Ranger", 50, level), "mana"]			

	return [0, ""]
		
		
# Assume Aspect (650) Rat - +20 increase to Agility and Discipline stats ranks. +1 increase to Agility and Discipline stats per seed 2 summation of Spiritual Lore, Blessings ranks
def Calculate_650_Rat(effect, tag, level):	
	if tag == "Statistic_Agility" or tag == "Statistic_Discipline":		
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Ranger")	
		bonus = 20 + Get_Summation_Bonus(2, lore_ranks)		
		
		return [bonus, "statistic increase"]	
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Ranger", 50, level), "mana"]		

	return [0, ""]		
		
		
# Assume Aspect (650) Wolf - +20 increase to Dexterity and Intuition stats\n+1 increase to Dexterity and Intuition stats per seed 2 summation of Spiritual Lore, Blessings ranks
def Calculate_650_Wolf(effect, tag, level):	
	if tag == "Statistic_Dexterity" or tag == "Statistic_Intuition":			
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Ranger")	
		bonus = 20 + Get_Summation_Bonus(2, lore_ranks)		
		
		return [bonus, "statistic increase"]	
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Ranger", 50, level), "mana"]			

	return [0, ""]	
		
'''		
# Assume Aspect (650) Yierka - +20 Surivial ranks\n+1 Survival rank per seed 2 summation of Spiritual Lore, Summoning ranks.
def Calculate_650_Yierka(effect, tag, level):	
	if tag == "Skill_Ranks_Surivial":			
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Summoning", "Ranger")	
		bonus = 20 + Get_Summation_Bonus(2, lore_ranks)		
		
		return [bonus, "skill ranks"]	
	
	elif tag == "Herb_Roundtime":			
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Ranger")	
		bonus = 25 + 3 * Get_Summation_Bonus(1, lore_ranks)		
		
		return [bonus, "percent roundtime reduction"]	
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Ranger", 50, level), "mana"]			

	return [0, ""]	
'''
	
# Sorcerer Base (700s)
	
# Cloak of Shadows (712) - +25 DS, +20 Sorcerer TD. +1 all DS per Spell Research, Sorcerer Base rank above 12 capped at +88 DS (+113 total), +1 Sorcerer TD per 10 Spell Research, Sorcerer Base ranks above 12 capped at +8 DS (+28 total)	
def Calculate_712(effect, tag, level):	
	if tag == "DS_All" or tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Sorcerer", "")				
		bonus = 0
		
		if tag == "DS_All":
			type = "All DS"
			bonus = math.floor(max(0, spell_ranks - 12))	
			bonus = min(113, 25 + bonus)		
		else:
			bonus = math.floor(max(0, spell_ranks - 12)/10)	
			bonus = min(28, 20 + bonus)		
			
			if tag == "TD_Spiritual":
				bonus = math.ceil(bonus * 0.75)
				type = "Spiritual TD"			
			elif tag == "TD_Elemental":
				bonus = math.ceil(bonus * 0.75)
				type = "Elemental TD"
			elif tag == "TD_Mental": 
				bonus = math.ceil(bonus * 0.5)
				type = "Mental TD"
			elif tag == "TD_Sorcerer": 
				type = "Sorcerer TD"
		
		
		return [bonus, type]		
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Sorcerer", 12, level), "mana"]	

	return [0, ""]	


# Wizard Base (900s)
	
# Minor Elemental Edge (902) EVOKE - +10 skill bonus to a specific weapon type. +1 skill bonus per seed 7 summation of Elemental Lore, Earth ranks	
def Calculate_902(effect, tag, level):
	if tag == "Skill_Bonus_Edged_Weapons" or tag == "Skill_Bonus_Blunt_Weapons" or tag == "Skill_Bonus_Two_Handed_Weapons" or tag == "Skill_Bonus_Polearm_Weapons" or tag == "Skill_Bonus_Brawling" or tag == "Skill_Bonus_Ranged_Weapons" or tag == "Skill_Bonus_Thrown_Weapons":	
		lore_ranks = Get_Skill_Ranks(effect, level, "Elemental Lore, Earth", "Wizard")			
		bonus = 10 + Get_Summation_Bonus(7, lore_ranks)		
		
		return [bonus, "skill bonus"]				

	return [0, ""]				
		
	
# Prismatic Guard (905) - +5 melee DS, +5 ranged DS, +20 bolt DS. +1 melee/ranged DS per seed 5 summation of Elemental Lore, Earth ranks, +1 melee/ranged DS per 4 Spell Research, Wizard Base ranks over 5	
def Calculate_905(effect, tag, level):
	if tag == "DS_Melee" or tag == "DS_Ranged" or tag == "DS_Bolt":				
		if tag == "DS_Melee":
			type = "Melee DS"		
			bonus = 5
		elif tag == "DS_Ranged":
			type = "Ranged DS"	
			bonus = 5
		elif tag == "DS_Bolt": 
			type = "Bolt DS"	
			bonus = 20			
			
		if globals.character.profession.name != "Wizard":
			return [bonus, type]					
			
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Wizard", "")			
		lore_ranks = Get_Skill_Ranks(effect, level, "Elemental Lore, Earth", "Wizard")		
		bonus += math.floor(max(0, spell_ranks - 5)/4)	
		bonus += Get_Summation_Bonus(5, lore_ranks)	
				
		return [bonus, type]	
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Wizard", 5, level), "mana"]		
			
	return [0, ""]	
	

# Mass Blur (911) - +20 phantom Dodging ranks. +1 phantom Dodging rank for the caster only per seed 1 summation of Elemental Lore, Air ranks	
def Calculate_911(effect, tag, level):	
	if tag == "Skill_Phantom_Ranks_Dodging":
		lore_ranks = Get_Skill_Ranks(effect, level, "Elemental Lore, Air", "Wizard")				
		bonus = 20 + Get_Summation_Bonus(1, lore_ranks)	
		
		return [bonus, "ranks"]
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Wizard", 11, level), "mana"]	

	return [0, ""]
	
	
# Melgorehn's Aura (913) - +10 DS, +20 Elemental TD. +1 DS per Spell Research, Wizard Base rank above 13 capped at character level. +1 Elemental TD per 3 Spell Research, Wizard Base ranks above 13 capped at character level.
def Calculate_913(effect, tag, level):	
	if tag == "DS_All" or tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Wizard", "")		
		
		if tag == "DS_All":
			bonus = 10 + max(0, spell_ranks - 13)
			return [bonus, "All DS"]
			
		bonus = 20 + math.floor(max(0, spell_ranks - 13)/3)		
		bonus = min(level, bonus)
		
		if tag == "TD_Elemental":
			type = "Elemental TD"
		elif tag == "TD_Spiritual":
			bonus = math.ceil(bonus * 0.5)
			type = "Spiritual TD"	
		elif tag == "TD_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer TD"
	
		return [bonus, type]		
		
	elif tag == "Spellburst":	
		return [Get_Spellburst_Cost("Spell Research, Wizard", 13, level), "mana"]		

	return [0, ""]
	
	
# Invisibility (916) - Just spellburst stuff
def Calculate_916(effect, tag, level):
	if tag == "Spellburst":				
		return [Get_Spellburst_Cost("Spell Research, Wizard", 16, level), "mana"]		
		
	return [0, ""]	


# Wizard's Shield (919) - +50 DS
def Calculate_919(effect, tag, level):
	if tag == "DS_All":				
		return [50, "All DS"]
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Wizard", 19, level), "mana"]		
		
	return [0, ""]
	
	
# Core Tap (950) - Spells cast with Core Tap have increased Bolt AS and Elemental CS\nAS Bolt = 6 * bonus per seed 10 summation of Elemental Lore, Fire ranks\nElemental CS = 6 * 3/5 * bonus per seed 10 summation of Elemental Lore, Fire ranks
def Calculate_950(effect, tag, level):			
	if tag == "AS_Bolt" or tag == "CS_Elemental":	
		lore_ranks = Get_Skill_Ranks(effect, level, "Elemental Lore, Fire", "Wizard")			
		bonus = 6 * Get_Summation_Bonus(10, lore_ranks)		
					
		if tag == "AS_Bolt":
			type = "Bolt AS"		
		elif tag == "CS_Elemental":
			bonus = math.ceil(bonus * 3/5)
			type = "Elemental CS"
	
		return [bonus, type]	
		
	return [0, ""]	

	
# Bard Base (1000s)	
	
# Fortitude Song (1003) - +10 DS
def Calculate_1003(effect, tag, level):
	if tag == "DS_All":				
		return [10, "All DS"]
		
	return [0, ""]
	

# Kai's Triumph Song (1007) - +10 AS, +10 UAF. +1 AS/UAF per Spell Research, Bard Base rank above 7 capped at +20. +1 all AS per seed 3 summation of Mental Lore, Telepathy ranks. Maximum AS provided is capped at +31
def Calculate_1007(effect, tag, level):
	if tag == "AS_All" or tag == "UAF":	
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Bard", "")	
		lore_ranks = Get_Skill_Ranks(effect, level, "Mental Lore, Telepathy", "Bard")			
		bonus = Get_Summation_Bonus(3, lore_ranks)
		bonus += min(20, max(0, spell_ranks-7))
		bonus = min(31, 10 + bonus)
		
		if tag == "AS_All":
			type = "All AS"
		if tag == "UAF":	
			type = "UAF"
			
		return [bonus, type]
		
	return [0, ""]	


# Song of Valor (1010) - +10 DS. +1 DS per 2 Spell Research, Bard Base ranks above 10
def Calculate_1010(effect, tag, level):
	if tag == "DS_All":				
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Bard", "")				
		bonus = 10 + math.floor((max(0, spell_ranks - 10)/2))

		return [bonus, "All DS"]			
		
	return [0, ""]

	
# Song of Mirrors (1019) - +20 phantom Dodging ranks. +1 phantom Dodging rank per 2 Spell Research, Bard Base ranks over 19
def Calculate_1019(effect, tag, level):
	if tag == "Skill_Phantom_Ranks_Dodging":
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Bard", "")
		bonus = 20 + math.floor((max(0, spell_ranks - 19)/2))

		return [bonus, "ranks"]
		
	return [0, ""]


# Song of Tonis (1035) - +20 phantom Dodging ranks, -1 Haste effect\n+1 phantom Dodging rank at the following Elemental Lore, Air rank inverals: 1,2,3,5,8,10,14,17,21,26,31,36,42,49,55,63,70,78,87,96. Haste effect improves to -2 at Elemental Lore, Air rank 30 and -3 at Elemental Lore, Air rank 75. The bonus is +1 second per rank for the first 20 ranks of ML, Telepathy.
def Calculate_1035(effect, tag, level):
	if tag == "Skill_Phantom_Ranks_Dodging":		
		lore_ranks = Get_Skill_Ranks(effect, level, "Elemental Lore, Air", "Bard")			
		air_arr = [1,2,3,5,8,10,14,17,21,26,31,36,42,49,55,63,70,78,87,96]		
		bonus = 20
		length = len(air_arr)
		
		for j in range(length):
			if air_arr[j] > lore_ranks:
				bonus += j
				break
				
		if lore_ranks > air_arr[-1]:
			bonus += air_arr[-1]
		
		return [bonus, "ranks"]
		
	elif tag == "Roundtime_Reduction":		
		lore_ranks = Get_Skill_Ranks(effect, level, "Elemental Lore, Air", "Bard")				
			
		if lore_ranks >= 75:
			bonus = 3
		elif lore_ranks >= 30:
			bonus = 2
		else:
			bonus = 1
			
		return [bonus, "Roundtime Reduction"]	
		
	return [0, ""]
	
	
# Empath Base (1100s)

# Empathic Focus (1109) = +15 Spiritual TD, +25 all DS, +15 melee AS. +1 all DS per 2 Spell Research, Empath Base ranks above 9.
def Calculate_1109(effect, tag, level):		
	if tag == "DS_All":
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Empath", "")
		bonus = math.floor(max(0, spell_ranks - 9)/2)		
		bonus = min(level, 25 + bonus)
		
		return [bonus, "All DS"]
		
	elif tag == "AS_Melee" or tag == "UAF" or tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":
		bonus = 15
		
		if tag == "AS_Melee":
			type = "Melee AS"	
		elif tag == "UAF":
			type = "UAF"	
		elif tag == "TD_Spiritual":
			type = "Spiritual TD"	
		elif tag == "TD_Elemental":
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental TD"
		elif tag == "TD_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer TD"
	
		return [bonus, type]	
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Empath", 9, level), "mana"]	

	return [0, ""]
	

# Strength of Will (1119) - +12 DS, 12 Spirtual TD. +1 DS and Spiritual TD per 3 Spell Research, Empath Base ranks above 19.
def Calculate_1119(effect, tag, level):
	if tag == "DS_All" or tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":		
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Empath", "")
		bonus = math.floor(max(0, spell_ranks - 19)/3)		
		bonus = min(25, 12 + bonus)
		
		if tag == "DS_All":
			type = "All DS"	
		elif tag == "TD_Spiritual":
			type = "Spiritual TD"	
		elif tag == "TD_Elemental":
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental TD"
		elif tag == "TD_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer TD"		
		
		return [bonus, type]	
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Empath", 19, level), "mana"]	
		
	return [0, ""]
	

# Intensity (1130) - +20 DS, +20 AS. +1 AS/DS per 2 Spell Research, Empath Base ranks above 30
def Calculate_1130(effect, tag, level):
	if tag == "AS_All" or tag == "UAF" or tag == "DS_All":	
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Empath", "")
		bonus = math.floor(max(0, spell_ranks - 30)/2)		
		bonus = min(level, 20 + bonus)
		
		if tag == "AS_All":	
			type = "All AS"	
		elif tag == "DS_All":				
			type = "All DS"		
		elif tag == "UAF":			
			type = "UAF"		
			
		return [bonus, type]
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Empath", 30, level), "mana"]	

	return [0, ""]

	
# Minor Mental (1200s)	
	
# Ironskin (1202) - Just spellburst stuff
def Calculate_1202(effect, tag, level):
	if tag == "Spellburst":				
		return [Get_Spellburst_Cost("Spell Research, Minor Mental", 2, level), "mana"]	
		
	return [0, ""]	
	

# Foresight (1204) - +10 melee and ranged DS
def Calculate_1204(effect, tag, level):
	if tag == "DS_Melee":				
		return [10, "Melee DS"]
	elif tag == "DS_Ranged":				
		return [10, "Ranged DS"]
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Minor Mental", 4, level), "mana"]	
		
	return [0, ""]


# Mindward (1208) - +20 Mental TD\n+1 Mental TD 2 Spell Research, Minor Mental ranks above 8 to a maximum of +40	
def Calculate_1208(effect, tag, level):
	if tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Minor Mental", "")			
		bonus = math.floor(max(0, spell_ranks - 8)/2)		
		bonus = min(40, 20 + bonus)
		
		if tag == "TD_Elemental":
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental TD"
		elif tag == "TD_Spiritual":
			bonus = math.ceil(bonus * 0.5)
			type = "Spiritual TD"	
		elif tag == "TD_Mental": 
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer TD"
	
		return [bonus, type]	
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Minor Mental", 8, level), "mana"]	
		
	return [0, ""]

	
# Dragonclaw (1209) - +10 UAF
def Calculate_1209(effect, tag, level):
	if tag == "UAF":				
		lore_ranks = Get_Skill_Ranks(effect, level, "Mental Lore, Transformation", "Minor Mental")
		bonus = 10 + Get_Summation_Bonus(1, lore_ranks)	
		
		return [bonus, "UAF"]
		
	elif tag == "Spellburst":	
		return [Get_Spellburst_Cost("Spell Research, Minor Mental", 9, level), "mana"]	
		
	return [0, ""]
	
	
# Blink (1214) - Just spellburst stuff
def Calculate_1214(effect, tag, level):
	if tag == "Spellburst":				
		return [Get_Spellburst_Cost("Spell Research, Minor Mental", 14, level), "mana"]	
		
	return [0, ""]	


# Focus Barrier (1216) - +30 DS
def Calculate_1216(effect, tag, level):
	if tag == "DS_All":				
		return [30, "All DS"]
		
	return [0, ""]
	
	
# Premonition (1220) - +20 DS. +1 all DS per 2 Spell Research, Minor Mental ranks above 20	
def Calculate_1220(effect, tag, level):
	if tag == "DS_All":				
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Minor Mental", "")			
		bonus = math.floor(max(0, spell_ranks - 20)/2)		
		bonus = min(level, 20 + bonus)
		
		return [bonus, "All DS"]
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Minor Mental", 20, level), "mana"]	
		
	return [0, ""]


# Paladin Base (1600s)	

# Mantle of Faith (1601) +5 DS, +5 Spiritual TD. +1 DS and Spiritual TD per seed 2 summation of Spiritual Lore, Blessings ranks
def Calculate_1601(effect, tag, level):
	if tag == "DS_All" or tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":		
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Paladin")		
		bonus = 5 + Get_Summation_Bonus(2, lore_ranks)	
							
		if tag == "DS_All":
			type = "All DS"	
		elif tag == "TD_Spiritual":
			type = "Spiritual TD"	
		elif tag == "TD_Elemental":
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental TD"
		elif tag == "TD_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer TD"		
		
		return [bonus, type]	
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Paladin", 1, level), "mana"]	
		
	return [0, ""]	

	
# Faith's Clarity (1603) -5% spiritual spell hindrance. Additional -1% spiritual spell hindrance per 3 Spiritual Lore, Summoning ranks to a maximum of -5% (-10% total)
def Calculate_1603(effect, tag, level):
	if tag == "Spell_Hindrance_Spiritual":				
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Summoning", "Paladin")		
		bonus = 5 + min(5, math.floor(lore_ranks / 3))
		
		return [bonus, "Spiritual Spell Hindrance"]	
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Paladin", 3, level), "mana"]	
		
	return [0, ""]
	
# Arm of the Arkati (1605) Spellburst stuff
def Calculate_1605(effect, tag, level):
	if tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Paladin", 5, level), "mana"]	
		
	return [0, ""]			
	
# Dauntless (1606) - +10 AS, +10 UAF
def Calculate_1606(effect, tag, level):
	if tag == "AS_Melee":				
		return [10, "Melee AS"]
	elif tag == "UAF":				
		return [10, "UAF"]
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Paladin", 6, level), "mana"]	

	return [0, ""]
	
	
# Rejuvenation  - Increases stamina recovery by 10% max stamina. +3 stamina per summation seed 1 of Spiritual Lore, Blessings.
# -1% every 30 seconds. Use the tier field to represent this. Tier 1 = 10%, Tier 9 = 1%
def Calculate_1607(effect, tag, level):
	if tag == "Resource_Recovery_Stamina":	
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Paladin")		
		tier = int(effect.scaling_arr["Tier"])
		
		try:
			max_stam = int(override_dict["Maximum Stamina"])		
			if max_stam == 0:
				bonus = 3 * Get_Summation_Bonus(1, lore_ranks)
			else:
				stam_percent = math.floor(max_stam * ((11 - tier) / 100))
				bonus = stam_percent + (3 * Get_Summation_Bonus(1, lore_ranks))
			
		except:
			bonus = 3 * Get_Summation_Bonus(1, lore_ranks)	
			
		return [bonus, "Stamina Recovery"]			
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Paladin", 7, level), "mana"]	
		
	return [0, ""]
	
	
# Beacon of Courage (1608) - +1 enemy ignored in Force on Force. +1 additional enemy ignored per seed 10 summation of Spiritual Lore, Blessings ranks
def Calculate_1608(effect, tag, level):
	if tag == "Force_On_Force":
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Paladin")		
		bonus = Get_Summation_Bonus(10, lore_ranks)			
			
		return [1 + bonus, "Enemies Ignored"]
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Paladin", 8, level), "mana"]	
	
	return [0, ""]
		
	
# Higher Vision (1610) - +10 DS. +1 DS per 2 Spell Research, Paladin Base ranks above 10 to a maximum of +20, +1 DS per seed 5 summation of Spiritual Lore, Religion ranks	
def Calculate_1610(effect, tag, level):
	if tag == "DS_All":				
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Paladin", "")	
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Religion", "Paladin")	
		bonus = 10 + math.floor(max(0, spell_ranks - 10)/2)		
		bonus = min(20, bonus) + Get_Summation_Bonus(5, lore_ranks)	
		
		return [bonus, "All DS"]
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Paladin", 10, level), "mana"]	
		
	return [0, ""]
	

# Patron's Blessing (1611) - +10 phantom Combat Maneuver ranks. +1 Combat Maneuver rank per seed 3 summation of Spiritual Lore, Blessings ranks. +0.75 Combat Maneuver rank per 2 Spell Research, Paladin Base rank above 11	
def Calculate_1611(effect, tag, level):	
	if tag == "Skill_Phantom_Ranks_Combat_Maneuvers":	
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Paladin", "")	
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Paladin")			
		
		bonus = 10
		bonus += Get_Summation_Bonus(3, lore_ranks) 
		bonus += math.floor(0.75 * max(0, spell_ranks-11))
		
		return [bonus, "ranks"]
		
	elif tag == "Spellburst":		
		return [Get_Spellburst_Cost("Spell Research, Paladin", 11, level), "mana"]	

	return [0, ""]
	

# Champion's Might (1612) - +15 Spiritual CS. +1 Spiritual CS per 1 Spell Research, Paladin Base rank above 12 to a maximum of +10 (+25 total)	
def Calculate_1612(effect, tag, level):
	if tag == "CS_Elemental" or tag == "CS_Mental" or tag == "CS_Spiritual" or tag == "CS_Sorcerer":	
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Paladin", "")	
		bonus = max(0, spell_ranks - 12)		
		bonus = min(25, 15 + bonus)	
			
		if tag == "CS_Spiritual":
			type = "Spiritual CS"			
		elif tag == "CS_Elemental":
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental CS"
		elif tag == "CS_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental CS"
		elif tag == "CS_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer CS"
	
		return [bonus, type]
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Paladin", 12, level), "mana"]	

	return [0, ""]


# Guard the Meek (1613) Group - +15 melee DS. +1 melee DS per 5 Spell Research, Paladin Base ranks above 18 to a maximum of +20. 
def Calculate_1613_Group(effect, tag, level):
	if tag == "DS_Melee":				
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Paladin", "")	
		bonus = math.floor(max(0, spell_ranks - 13)/5)		
		bonus = min(20, 15 + bonus)
		
		return [bonus, "Melee DS"]
		
	return [0, ""]

	
# Guard the Meek (1613) Self - +15 melee DS. +1 all DS per seed 6 summation of Spiritual Lore, Blessings ranks (max of +5 at 40 ranks)
def Calculate_1613_Self(effect, tag, level):
	if tag == "DS_Melee":							
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Paladin")		
		bonus = Get_Summation_Bonus(6, lore_ranks)
		bonus = min(20, 15 + bonus)
		
		return [bonus, "Melee DS"]
		
	return [0, ""]

	
# Vigor (1616) - +4 Constitution statistic and +8 maximum health. +1 Constitution statistic and +2 maximum health per 4 Spell Research, Paladin Base rank above 16 to a maximum of +20 and +40 at 40 ranks. Additional maximum health equal to square root of 2 * Spiritual Lore, Blessings bonus
def Calculate_1616(effect, tag, level):
	if tag == "Statistic_Constitution":				
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Paladin", "", "")	
		bonus = math.floor(spell_ranks / 4)
		bonus = min(10, 4 + bonus)
		
		return [bonus, "Statistic increase"]		
		
	elif tag == "Resource_Maximum_Health":				
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Paladin", "")	
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Blessings", "Paladin")		
		bonus = math.floor(spell_ranks / 4)
		bonus = min(20, 8 + 2 * bonus) + math.floor(math.sqrt(2 * lore_ranks))		
		
		return [bonus, "Maximum Health"]

	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Paladin", 16, level), "mana"]	
		
	return [0, ""]
	
	
# Zealot (1617)	- +30 melee AS/UAF, -30 DS. +1 melee AS/UAF and all DS per seed 1 summation of Spiritual Lore, Religion ranks
def Calculate_1617(effect, tag, level):
	if tag == "AS_Melee" or tag == "UAF" or tag == "DS_All":	
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Religion", "Paladin")		
		bonus = 30 + Get_Summation_Bonus(1, lore_ranks)
		
		if tag == "AS_Melee":	
			return [bonus, "Melee AS"]
		elif tag == "UAF":	
			return [bonus, "UAF"]
		elif tag == "DS_All":
			return [bonus, "All DS"]

	return [0, ""]
	
	
# Faith Shield (1619) - +50 Spiritual TD. +3 Spiritual TD per seed 5 summation of Spiritual Lore, Religion ranks.	
def Calculate_1619(effect, tag, level):
	if tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":
		lore_ranks = Get_Skill_Ranks(effect, level, "Spiritual Lore, Religion", "Paladin")		
		bonus = 50 + Get_Summation_Bonus(5, lore_ranks)
	
		if tag == "TD_Spiritual":
			type = "Spiritual TD"	
		elif tag == "TD_Elemental":
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental TD"
		elif tag == "TD_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer TD"		
		
		return [bonus, type]	
		
	elif tag == "Spellburst":			
		return [Get_Spellburst_Cost("Spell Research, Paladin", 19, level), "mana"]	

	return [0, ""]
		
# Arcane (1700s)		
	
# Mystic Focus (1711) Arcane Symbols - +10 CS. Grants +25 additional CS for non-native elemental circles if spell is from a scroll at 25 Arcane Symbols ranks.
# +1 for every 2 Arcane Symbols ranks over 25 up to a maximum of +50 at 75 ranks.
def Calculate_1711_AS(effect, tag, level):
	if tag == "CS_Mental":	
		return [10, "Mental CS"]
	elif tag == "CS_Spiritual":
		return [10, "Spiritual CS"]
	elif tag == "CS_Elemental" or tag == "CS_Sorcerer":
		if tag == "CS_Elemental":
			type = "Elemental CS"
		elif tag == "CS_Sorcerer": 
			type = "Sorcerer CS"
			
		try:
			ranks = int(override_dict["Arcane Symbols ranks"])			
		except:
			ranks = 0

		bonus = 0
		
		if ranks >= 25:
			bonus = math.floor(max(0, ranks - 25)/2)		
			bonus = min(50, 25 + bonus)		
			
		bonus += 10
	
		return [bonus, type]
		
	return [0, ""]
	
	
# Mystic Focus (1711) Magic Item Use - +10 CS. Grants +25 additional CS for non-native elemental circles if spell is from a magic item at 25 Magic Item Use ranks.
# +1 for every 2 Magic Item Use ranks over 25 up to a maximum of +50 at 75 ranks.
def Calculate_1711_MIU(effect, tag, level):
	if tag == "CS_Mental":	
		return [10, "Mental CS"]
	elif tag == "CS_Spiritual":
		return [10, "Spiritual CS"]
	elif tag == "CS_Elemental" or tag == "CS_Sorcerer":
		if tag == "CS_Elemental":
			type = "Elemental CS"
		elif tag == "CS_Sorcerer": 
			type = "Sorcerer CS"
			
		try:
			ranks = int(override_dict["Magic Item Use ranks"])			
		except:
			ranks = 0

		bonus = 0
		
		if ranks >= 25:
			bonus = math.floor(max(0, ranks - 25)/2)		
			bonus = min(50, 25 + bonus)		
			
		bonus += 10
	
		return [bonus, type]
		
	return [0, ""]

	
# Spirit Guard (1712) - +25 DS
def Calculate_1712(effect, tag, level):
	if tag == "DS_All":				
		return [25, "All DS"]
		
	return [0, ""]		
	

# V'tull's Fury (1718) - +30 melee AS
def Calculate_1718(effect, tag, level):
	if tag == "AS_Melee":				
		return [30, "Melee AS"]

	return [0, ""]
	
	
# Combat Maneuvers, Shield Maneuvers, or Armor Specialization		


# Armor Blessing -  Increases bolt AS, all CS for one cast after spell failure by (3 * AG * Blessing Rank) = AS bonus or ((3* AG * Blessing Rank) * 3/5) = CS bonus
def Calculate_Armor_Blessing(effect, tag, level):
	if tag == "AS_Bolt" or tag == "CS_All":	
		ranks = Get_Maneuver_Ranks(effect, level, "Armor Blessing", "armor")

		try:
			AG = int(override_dict["Armor Group"])						
				
		except:
			AG = 1
			
		if AG == 1:
			return [0, ""]				
				
		if tag == "AS_Bolt":
			bonus = 3 * AG * ranks
			type = "Bolt AS"
		elif tag == "CS_All":
			bonus = math.floor(3 * AG * ranks * 3/5)
			type = "Non-Bard CS"
				
		return [bonus, type]			

	return [0, ""]
	
	
# Armored Evasion - Reduces Armor Action Penalty by [Rank * (7 - Armor Group)] / 2. 
def Calculate_Armored_Evasion(effect, tag, level):
	if tag == "Action_Penalty":	
		ranks = Get_Maneuver_Ranks(effect, level, "Armored Evasion", "armor")

		try:
			AG = int(override_dict["Armor Group"])				
		except:
			AG = 7
			
		bonus = math.floor(ranks * (7 - AG) / 2)
			
		return [bonus, "bonus"]	
		
	return [0, ""]
	
	
# Armored Fluidity - Reduces the base Spell Hinderance of Armor by 10% per rank
def Calculate_Armored_Fluidity(effect, tag, level):
	if tag == "Spell_Hindrance_All":	
		ranks = Get_Maneuver_Ranks(effect, level, "Armored Fluidity", "armor")

		try:
			base_hindrance = int(override_dict["Armor Base Hindrance"])				
		except:
			base_hindrance = 0
			
		bonus = math.floor(.1 * ranks * base_hindrance)
			
		return [bonus, "All Spell Hindrance"]	
		
	return [0, ""]
	
	
# Armor Support - Reduces encumbrance by a number of pounds equal to 5 + ((Armor Group of worn armor + 1) * Rank) 
def Calculate_Armor_Support(effect, tag, level):
	if tag == "Encumbrance_Reduction_Absolute":	
		ranks = Get_Maneuver_Ranks(effect, level, "Armored Support", "armor")

		try:
			AG = int(override_dict["Armor Group"])		
			if AG == 0:
				bonus = 0
			else:
				bonus = 5 + ranks * (1 + AG)		
		except:
			bonus = 0
			
			
		return [bonus, "Carry Capacity"]	
		
	return [0, ""]
	
	
# Berserk - AS bonus equal to (guild/cman ranks - 1 + (level/4) - 20) / 2. Max AS bonus is +29
def Calculate_Berserk(effect, tag, level):
	if tag == "AS_Melee":	
		cman_ranks = Get_Maneuver_Ranks(effect, level, "Berserk", "combat")
			
		if effect.scaling_arr["Guild skill ranks"] == "D" and "Berserk" in globals.character.profession.guild_skills:		
			position = globals.character.profession.guild_skills.index("Berserk")
			guild_skill_ranks = int(globals.character.guild_skills_ranks[position].get())			
		else:			
			guild_skill_ranks = int(effect.scaling_arr["Guild skill ranks"])	
			
		ranks = max(10 * cman_ranks, guild_skill_ranks)	- 1
		ranks = max(ranks, 0)
		
		level = min(100, level)				
		bonus = (ranks + math.floor(level/4) - 20) / 2
		bonus = min(29, bonus)
			
		return [bonus, "Melee AS"]	
			
	return [0, ""]	
	

# Burst of Swiftness - +6 increase to Agility bonus and +3 increase to Dexterity. +2 Agility and +1 Dexterity per rank above 1
def Calculate_Burst_of_Swiftness(effect, tag, level):
	if tag == "Statistic_Bonus_Dexterity" or tag == "Statistic_Bonus_Agility":	
		ranks = Get_Maneuver_Ranks(effect, level, "Burst of Swiftness", "combat")
			
		if 0 < ranks < 6:
			if tag == "Statistic_Bonus_Agility":
				return [6 + (2 * ranks), "Burst of Swiftness"]		
			else:	
				return [3 + ranks, "Burst of Swiftness"]
			
	return [0, ""]		
	
	
# Combat Focus - +2 all TD per rank	
def Calculate_Combat_Focus(effect, tag, level):
	if tag == "TD_All":	
		ranks = Get_Maneuver_Ranks(effect, level, "Combat Focus", "combat")

		return [2 * ranks, "All TD"]	
			
	return [0, ""]	
	
	
# Combat Movement - +2 all DS per rank	
def Calculate_Combat_Movement(effect, tag, level):
	if tag == "DS_Melee" or tag == "DS_Ranged":	
		ranks = Get_Maneuver_Ranks(effect, level, "Combat Movement", "combat")
			
		if tag == "DS_Melee":
			type = "Melee DS"
		elif tag == "DS_Ranged":
			type = "Ranged DS"
			
		return [2 * ranks, type]	
			
	return [0, ""]	
	
	
# Combat Toughness - +5 bonus to maximum health. +10 additional maximum health per rank
def Calculate_Combat_Toughness(effect, tag, level):
	if tag == "Resource_Maximum_Health":	
		ranks = Get_Maneuver_Ranks(effect, level, "Combat Toughness", "combat")
					
		bonus = 10 * ranks
		if bonus > 0:
			bonus += 5
			
		return [bonus, "Maximum Health"]
			
	return [0, ""]
	
	
# Coup de Grace (Buff) - +10 to +40 AS	
def Calculate_Coup_de_Grace_Buff(effect, tag, level):
	if tag == "AS_All":
		return [int(effect.scaling_arr["All AS bonus"]), "All AS"]	

	return [0, ""]	

	
# Perfect Self - +2/+4/+6/+8/+10 to all statistic bonuses	
def Calculate_Perfect_Self(effect, tag, level):
	if tag == "Statistic_Bonus_Strength" or tag == "Statistic_Bonus_Constitution" or tag == "Statistic_Bonus_Dexterity" or tag == "Statistic_Bonus_Agility" or tag == "Statistic_Bonus_Discipline" or tag == "Statistic_Bonus_Aura" or tag == "Statistic_Bonus_Logic" or tag == "Statistic_Bonus_Intuition" or tag == "Statistic_Bonus_Wisdom" or tag == "Statistic_Bonus_Influence":	
		ranks = Get_Maneuver_Ranks(effect, level, "Perfect Self", "combat")
		
		return [2 * ranks, "Perfect Self"]
			
	return [0, ""]


# Shield Forward - +10 enhancive Shield Use ranks to per maneuver rank	
def Calculate_Shield_Forward(effect, tag, level):
	if tag == "Skill_Ranks_Shield_Use":	
		ranks = Get_Maneuver_Ranks(effect, level, "Shield Forward", "shield")					
			
		return [10 * ranks, "ranks"]
			
	return [0, ""]
	
	
# Shield Swiftness - +0.04 increase per rank to Shield Factor when using a Small or Medium shield	
def Calculate_Shield_Swiftness(effect, tag, level):
	if tag == "Shield_Factor":	
		ranks = Get_Maneuver_Ranks(effect, level, "Shield Swiftness", "shield")		
			
		return [0.04 * ranks, "shield factor"]
			
	return [0, ""]
	
	
# Specialization I - +2 AS per rank	
def Calculate_Specialization_I(effect, tag, level):
	if tag == "AS_Melee" or tag == "AS_Ranged" or tag == "UAC":	
		ranks = Get_Maneuver_Ranks(effect, level, "Specialization I", "combat")	

		if tag == "AS_Melee":
			type = "Melee AS"	
		elif tag == "AS_Ranged":
			type = "Ranged AS"
		elif tag == "UAC": 
			type = "UAC"					
			
		return [2 * ranks, type]
			
	return [0, ""]
	
		
# Specialization II - +2 AS per rank	
def Calculate_Specialization_II(effect, tag, level):
	if tag == "AS_Melee" or tag == "AS_Ranged" or tag == "UAC":	
		ranks = Get_Maneuver_Ranks(effect, level, "Specialization II", "combat")	

		if tag == "AS_Melee":
			type = "Melee AS"	
		elif tag == "AS_Ranged":
			type = "Ranged AS"
		elif tag == "UAC": 
			type = "UAC"					
			
		return [2 * ranks, type]
			
	return [0, ""]
	

# Specialization III - +2 AS per rank		
def Calculate_Specialization_III(effect, tag, level):
	if tag == "AS_Melee" or tag == "AS_Ranged" or tag == "UAC":	
		ranks = Get_Maneuver_Ranks(effect, level, "Specialization III", "combat")	

		if tag == "AS_Melee":
			type = "Melee AS"	
		elif tag == "AS_Ranged":
			type = "Ranged AS"
		elif tag == "UAC": 
			type = "UAC"					
			
		return [2 * ranks, type]
			
	return [0, ""]
	

# Spin Attack - +3 AS and Dodging bonus per rank	
def Calculate_Spin_Attack(effect, tag, level):
	if tag == "AS_Melee" or tag == "Skill_Bonus_Dodging":	
		ranks = Get_Maneuver_Ranks(effect, level, "Spin Attack", "combat")	
					
		if tag == "AS_Melee":
			type = "Melee AS"	
		elif tag == "Skill_Bonus_Dodging":
			type = "skill bonus"
			
		return [3 * ranks, type]
			
	return [0, ""]	
	
	
# Surge of Strength - +8/+10/+12/+14/+16 increase to Strength bonus	
def Calculate_Surge_of_Strength(effect, tag, level):
	if tag == "Statistic_Bonus_Strength":	
		ranks = Get_Maneuver_Ranks(effect, level, "Surge of Strength", "combat")	
			
		if 0 < ranks < 6:
			return [6 + (2 * ranks), "Surge of Strength"]
			
	return [0, ""]
	
	
# War Cries - Seanette's Shout - +15 AS/UAF to group but not to self
def Calculate_War_Cries_Shout(effect, tag, level):
	if tag == "AS_All":				
		return [15, "All AS"]
	elif tag == "UAF":				
		return [15, "UAF"]

	return [0, ""]	
	
	
# War Cries - Horland's Holler - +20 AS/UAF to group including self
def Calculate_War_Cries_Holler(effect, tag, level):
	if tag == "AS_All":				
		return [20, "All AS"]
	elif tag == "UAF":				
		return [20, "UAF"]

	return [0, ""]	
	
	
# Weapon Bonding - +2 AS/UAF per rank	
def Calculate_Weapon_Bonding(effect, tag, level):
	if tag == "AS_Melee" or tag == "AS_Ranged" or tag == "UAC":	
		ranks = Get_Maneuver_Ranks(effect, level, "Weapon Bonding", "combat")	

		if tag == "AS_Melee":
			type = "Melee AS"	
		elif tag == "AS_Ranged":
			type = "Ranged AS"
		elif tag == "UAC": 
			type = "UAC"		
			
		return [2 * ranks, type]
			
	return [0, ""]


# Society Powers

# Sigil of Concentration - +5 mana recovery	
def Calculate_Sigil_of_Concentration(effect, tag, level):
	if tag == "Resource_Recovery_Mana_Normal":				
		return [5, "Mana Recovery"]

	return [0, ""]	
	
	
# Sigil of Defense - +1  DS per GoS rank	
def Calculate_Sigil_of_Defense(effect, tag, level):
	if tag == "DS_All":	
		bonus = Get_Society_Rank(effect, "Guardians of Sunfist")
		return [bonus, "All DS"]

	return [0, ""]
	
	
# Sigil of Focus - +1 TD per GoS rank		
def Calculate_Sigil_of_Focus(effect, tag, level):
	if tag == "TD_All":	
		bonus = Get_Society_Rank(effect, "Guardians of Sunfist")
		return [bonus, "All TD"]

	return [0, ""]
	
	
# Sigil of Offense - +1 AS/UAF per GoS rank	
def Calculate_Sigil_of_Offense(effect, tag, level):
	if tag == "AS_All" or tag == "UAF":	
		bonus = Get_Society_Rank(effect, "Guardians of Sunfist")
			
		if tag == "AS_All":
			type = "All AS"
		elif tag == "UAF":
			type = "UAF"
		
		return [bonus, type]

	return [0, ""]
	
	
# Sigil of Major Bane - +10 AS/UAF	
def Calculate_Sigil_of_Major_Bane(effect, tag, level):
	if tag == "AS_All":				
		return [10, "All AS"]
	elif tag == "UAF":				
		return [10, "UAF"]

	return [0, ""]
	
	
# Sigil of Major Protection - +10 DS	
def Calculate_Sigil_of_Major_Protection(effect, tag, level):
	if tag == "DS_All":				
		return [10, "All DS"]

	return [0, ""]
	
	
# Sigil of Mending - +15 mana recovery	
def Calculate_Sigil_of_Mending(effect, tag, level):
	if tag == "Resource_Recovery_Health":				
		return [15, "Health Recovery"]

	return [0, ""]	
		
	
# Sigil of Minor Bane - +5 AS/UAF	
def Calculate_Sigil_of_Minor_Bane(effect, tag, level):
	if tag == "AS_All":				
		return [5, "All AS"]
	elif tag == "UAF":				
		return [5, "UAF"]

	return [0, ""]
	
	
# Sigil of Minor Protection - +5 DS	
def Calculate_Sigil_of_Minor_Protection(effect, tag, level):
	if tag == "DS_All":				
		return [5, "All DS"]

	return [0, ""]
	
	
# Sign of Defending	- +10 DS
def Calculate_Sign_of_Defending(effect, tag, level):
	if tag == "DS_All":				
		return [10, "All DS"]

	return [0, ""]
	
	
# Sign of Deflection - +20 bolt DS
def Calculate_Sign_of_Deflection(effect, tag, level):
	if tag == "DS_Bolt":				
		return [20, "Bolt DS"]

	return [0, ""]
	

# Sign of Dissipation - +20 TD	
def Calculate_Sign_of_Dissipation(effect, tag, level):
	if tag == "TD_All":				
		return [20, "All TD"]

	return [0, ""]
	
	
# Sign of Madness - +50 AS, +50 UAF, -50 DS	
def Calculate_Sign_of_Madness(effect, tag, level):
	if tag == "AS_All":				
		return [50, "All AS"]
	elif tag == "UAF":				
		return [50, "UAF"]
	if tag == "DS_All":				
		return [-50, "All DS"]

	return [0, ""]
	
	
# Sign of Shields - +20 DS	
def Calculate_Sign_of_Shields(effect, tag, level):
	if tag == "DS_All":				
		return [20, "All DS"]

	return [0, ""]
	

# Sign of Smiting - +10 AS	
def Calculate_Sign_of_Smiting(effect, tag, level):
	if tag == "AS_All":				
		return [10, "All AS"]
	elif tag == "UAF":				
		return [10, "UAF"]

	return [0, ""]
	
	
# Sign of Striking - +5 AS, +5 UAF	
def Calculate_Sign_of_Striking(effect, tag, level):
	if tag == "AS_All":				
		return [5, "All AS"]
	elif tag == "UAF":				
		return [5, "UAF"]

	return [0, ""]
	

# Sign of Swords - +20 AS, +20 UAF	
def Calculate_Sign_of_Swords(effect, tag, level):
	if tag == "AS_All":				
		return [20, "All AS"]
	elif tag == "UAF":				
		return [20, "UAF"]

	return [0, ""]
	
	
# Sign of Warding - +5 DS	
def Calculate_Sign_of_Warding(effect, tag, level):
	if tag == "DS_All":				
		return [5, "All DS"]

	return [0, ""]
	
	
# Symbol of Courage - +1 AS and UAF per Voln rank	
def Calculate_Symbol_of_Courage(effect, tag, level):
	if tag == "AS_All":	
		bonus = Get_Society_Rank(effect, "Order of Voln")
		return [bonus, "All AS"]

	return [0, ""]
	
	
# Symbol of Protection - +1 DS per Voln rank\n+1 TD per 2 Voln ranks	
def Calculate_Symbol_of_Protection(effect, tag, level):
	if tag == "DS_All":	
		bonus = Get_Society_Rank(effect, "Order of Voln")
		return [bonus, "All DS"]
		
	elif tag == "TD_All":	
		bonus = Get_Society_Rank(effect, "Order of Voln")	
		bonus = math.floor(bonus/2)
		return [bonus, "All TD"]

	return [0, ""]
	
	
# Symbol of Supremecy - +1 bonus per two Voln ranks to AS/CS,CMAN, UAF against undead creatures	
def Calculate_Symbol_of_Supremecy(effect, tag, level):
	if tag == "AS_All" or tag == "UAF" or tag == "CS_All":	
		bonus = Get_Society_Rank(effect, "Order of Voln")		
		bonus = math.floor(bonus/2)
		
		if tag == "AS_All":
			return [bonus, "All AS vs Undead"]	
		elif tag == "CS_All":
			return [bonus, "All CS vs Undead"]
		elif tag == "UAF":
			return [bonus, "UAF vs Undead"]

	return [0, ""]
	
	
# Special Abilities		

# CS Boost (Arcane Symbols)  - Increases CS for non-native spell circles when casting spell from a scroll. Does not stack with Elemental Targeting (425). 
# CS increase is by Arcane Symbol rank: 0.75 per rank up to character level. 0.5 per rank up to 2x character level. 0.33 per rank above 2x character level.	
def Calculate_CS_Boost_Arcane_Symbols(effect, tag, level):		
	if tag == "CS_Special":	
		try:
			ranks = int(override_dict["Arcane Symbols ranks"])			
		except:
			ranks = 0					
		
		cs_bonus = 0.0
		double_level = level * 2
		
		while ranks > 0:							
			if ranks <= level:
				cs_bonus += 0.75
			elif ranks <= double_level:
				cs_bonus += 0.5
			else:
				cs_bonus += 0.33								
				
			ranks -= 1			
		
		return [math.ceil(cs_bonus), "when cast from scroll"]
	
	return [0, ""]	
	
	
# CS Boost (Magic Item Use)  - Increases CS for non-native spell circles when casting spell from a scroll. Does not stack with Elemental Targeting (425). 
# CS increase is by Magic Item Use rank: 0.75 per rank up to character level. 0.5 per rank up to 2x character level. 0.33 per rank above 2x character level.		
def Calculate_CS_Boost_Magic_Item_Use(effect, tag, level):		
	if tag == "CS_Special":	
		try:
			ranks = int(override_dict["Magic Item Use ranks"])			
		except:
			ranks = 0					
		
		cs_bonus = 0.0
		double_level = level * 2
		
		while ranks > 0:							
			if ranks <= level:
				cs_bonus += 0.75
			elif ranks <= double_level:
				cs_bonus += 0.5
			else:
				cs_bonus += 0.33								
				
			ranks -= 1			
		
		return [math.ceil(cs_bonus), "when cast from magic item"]
	
	return [0, ""]	
	
	
# Meditate (Mana) - Mana recovery increased by (Discipline bonus + Wisdom bonus) / 2
def Calculate_Meditate_Mana(effect, tag, level):			
	if tag == "Resource_Recovery_Mana_Normal":	
		try:
			dis = int(override_dict["Discipline Bonus"])			
		except:
			dis = 0
				
		try:
			wis = int(override_dict["Wisdom Bonus"])				
		except:
			wis = 0
			
		bonus = math.floor((dis + wis) / 2)
			
		return [bonus, "Mana Recovery"]	
		
	return [0, ""]	
	
	
# Stamina Burst - +15% stamina recovery	
def Calculate_Stamina_Burst(effect, tag, level):
	if tag == "Resource_Recovery_Stamina":				
		return [15, "Stamina Recovery"]

	return [0, ""]	
	
	
# Stamina Burst (Cooldown) - -15% stamina recovery	
def Calculate_Stamina_Burst_Cooldown(effect, tag, level):
	if tag == "Resource_Recovery_Stamina":				
		return [-15, "Stamina Recovery"]

	return [0, ""]	
	

	

	
# Resource Enhancives


def Calculate_Enhancive_Resource_Recovery_Health(effect, tag, level):
	if tag == "Resource_Recovery_Health":
		return [int(effect.scaling_arr["Health recovery"]), "Health Recovery"]	

	return [0, ""]	
	
	
def Calculate_Enhancive_Resource_Maximum_Health(effect, tag, level):
	if tag == "Resource_Maximum_Health":
		return [int(effect.scaling_arr["Maximum health"]), "Maximum Health"]	

	return [0, ""]	


def Calculate_Enhancive_Resource_Recovery_Mana(effect, tag, level):
	if tag == "Resource_Recovery_Mana":
		return [int(effect.scaling_arr["Mana recovery"]), "Mana Recovery"]	

	return [0, ""]	
	
	
def Calculate_Enhancive_Resource_Maximum_Mana(effect, tag, level):
	if tag == "Resource_Maximum_Mana":
		return [int(effect.scaling_arr["Maximum mana"]), "Maximum Mana"]	

	return [0, ""]	


def Calculate_Enhancive_Resource_Recovery_Stamina(effect, tag, level):
	if tag == "Resource_Recovery_Stamina":
		return [int(effect.scaling_arr["Stamina recovery"]), "Stamina Recovery"]	

	return [0, ""]	
	
	
def Calculate_Enhancive_Resource_Maximum_Stamina(effect, tag, level):
	if tag == "Resource_Maximum_Stamina":
		return [int(effect.scaling_arr["Maximum stam"]), "Maximum Stamina"]	

	return [0, ""]	


def Calculate_Enhancive_Resource_Recovery_Spirit(effect, tag, level):
	if tag == "Resource_Recovery_Spirit":
		return [int(effect.scaling_arr["Spirit recovery"]), "Spirit Recovery"]	

	return [0, ""]	
	
	
def Calculate_Enhancive_Resource_Maximum_Spirit(effect, tag, level):
	if tag == "Resource_Maximum_Spirit":
		return [int(effect.scaling_arr["Maximum spirit"]), "Maximum Spirit"]	

	return [0, ""]	

	
	
	
# Skill Enhancives

	
def Calculate_Enhancive_Two_Weapon_Combat(effect, tag, level):
	if tag == "Skill_Ranks_Two_Weapon_Combat":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Two_Weapon_Combat":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Armor_Use(effect, tag, level):
	if tag == "Skill_Ranks_Armor_Use":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Armor_Use":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]		
	

def Calculate_Enhancive_Shield_Use(effect, tag, level):
	if tag == "Skill_Ranks_Shield_Use":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Shield_Use":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	
		
	
def Calculate_Enhancive_Combat_Maneuvers(effect, tag, level):
	if tag == "Skill_Ranks_Combat_Maneuvers":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Combat_Maneuvers":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]		
	
	
def Calculate_Enhancive_Edged_Weapons(effect, tag, level):
	if tag == "Skill_Ranks_Edged_Weapons":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Edged_Weapons":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]		
	
	
def Calculate_Enhancive_Blunt_Weapons(effect, tag, level):
	if tag == "Skill_Ranks_Blunt_Weapons":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Blunt_Weapons":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Two_Handed_Weapons(effect, tag, level):
	if tag == "Skill_Ranks_Two_Handed_Weapons":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Two_Handed_Weapons":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Ranged_Weapons(effect, tag, level):
	if tag == "Skill_Ranks_Ranged_Weapons":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Ranged_Weapons":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Thrown_Weapons(effect, tag, level):
	if tag == "Skill_Ranks_Thrown_Weapons":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Thrown_Weapons":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	
	

def Calculate_Enhancive_Polearm_Weapons(effect, tag, level):
	if tag == "Skill_Ranks_Polearm_Weapons":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Polearm_Weapons":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Brawling(effect, tag, level):
	if tag == "Skill_Ranks_Brawling":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Brawling":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	

	
def Calculate_Enhancive_Ambush(effect, tag, level):
	if tag == "Skill_Ranks_Ambush":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Ambush":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]		

	
def Calculate_Enhancive_Multi_Opponent_Combat(effect, tag, level):
	if tag == "Skill_Ranks_Multi_Opponent_Combat":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Multi_Opponent_Combat":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]				
	
	
def Calculate_Enhancive_Physical_Fitness(effect, tag, level):
	if tag == "Skill_Ranks_Physical_Fitness":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Physical_Fitness":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]		
	
	
def Calculate_Enhancive_Dodging(effect, tag, level):
	if tag == "Skill_Ranks_Dodging":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Dodging":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	
		
		
def Calculate_Enhancive_Arcane_Symbols(effect, tag, level):
	if tag == "Skill_Ranks_Arcane_Symbols":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Arcane_Symbols":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]				
		
		
def Calculate_Enhancive_Magic_Item_Use(effect, tag, level):
	if tag == "Skill_Ranks_Magic_Item_Use":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Magic_Item_Use":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]					
		
	
def Calculate_Enhancive_Spell_Aiming(effect, tag, level):
	if tag == "Skill_Ranks_Spell_Aiming":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Spell_Aiming":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]				
		
		
def Calculate_Enhancive_Harness_Power(effect, tag, level):
	if tag == "Skill_Ranks_Harness_Power":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Harness_Power":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]			
		
		
def Calculate_Enhancive_Elemental_Mana_Control(effect, tag, level):
	if tag == "Skill_Ranks_Elemental_Mana_Control":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Elemental_Mana_Control":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]		
		
		
def Calculate_Enhancive_Spiritual_Mana_Control(effect, tag, level):
	if tag == "Skill_Ranks_Spiritual_Mana_Control":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Spiritual_Mana_Control":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]		
		
		
def Calculate_Enhancive_Mental_Mana_Control(effect, tag, level):
	if tag == "Skill_Ranks_Mental_Mana_Control":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Mental_Mana_Control":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	

	
def Calculate_Enhancive_Elemental_Lore_Air(effect, tag, level):
	if tag == "Skill_Ranks_Elemental_Lore_Air":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Elemental_Lore_Air":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Elemental_Lore_Earth(effect, tag, level):
	if tag == "Skill_Ranks_Elemental_Lore_Earth":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Elemental_Lore_Earth":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	


def Calculate_Enhancive_Elemental_Lore_Fire(effect, tag, level):
	if tag == "Skill_Ranks_Elemental_Lore_Fire":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Elemental_Lore_Fire":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	


def Calculate_Enhancive_Elemental_Lore_Water(effect, tag, level):
	if tag == "Skill_Ranks_Elemental_Lore_Water":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Elemental_Lore_Water":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]		


def Calculate_Enhancive_Spiritual_Lore_Blessings(effect, tag, level):
	if tag == "Skill_Ranks_Spiritual_Lore_Blessings":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Spiritual_Lore_Blessings":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	


def Calculate_Enhancive_Spiritual_Lore_Summoning(effect, tag, level):
	if tag == "Skill_Ranks_Spiritual_Lore_Summoning":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Spiritual_Lore_Summoning":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	


def Calculate_Enhancive_Spiritual_Lore_Religion(effect, tag, level):
	if tag == "Skill_Ranks_Spiritual_Lore_Religion":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Spiritual_Lore_Religion":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	


def Calculate_Enhancive_Mental_Lore_Divination(effect, tag, level):
	if tag == "Skill_Ranks_Mental_Lore_Divination":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Mental_Lore_Divination":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	


def Calculate_Enhancive_Mental_Lore_Manipulation(effect, tag, level):
	if tag == "Skill_Ranks_Mental_Lore_Manipulation":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Mental_Lore_Manipulation":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	


def Calculate_Enhancive_Mental_Lore_Telepathy(effect, tag, level):
	if tag == "Skill_Ranks_Mental_Lore_Telepathy":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Mental_Lore_Telepathy":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	


def Calculate_Enhancive_Mental_Lore_Transference(effect, tag, level):
	if tag == "Skill_Ranks_Mental_Lore_Transference":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Mental_Lore_Transference":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	


def Calculate_Enhancive_Mental_Lore_Transformation(effect, tag, level):
	if tag == "Skill_Ranks_Mental_Lore_Transformation":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Mental_Lore_Transformation":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	


def Calculate_Enhancive_Sorcerous_Lore_Demonology(effect, tag, level):
	if tag == "Skill_Ranks_Sorcerous_Lore_Demonology":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Sorcerous_Lore_Demonology":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	


def Calculate_Enhancive_Sorcerous_Lore_Necromancy(effect, tag, level):
	if tag == "Skill_Ranks_Sorcerous_Lore_Necromancy":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Sorcerous_Lore_Necromancy":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Survival(effect, tag, level):
	if tag == "Skill_Ranks_Survival":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Survival":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]		
	
	
def Calculate_Enhancive_Disarming_Traps(effect, tag, level):
	if tag == "Skill_Ranks_Disarming_Traps":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Disarming_Traps":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]		
	
	
def Calculate_Enhancive_Picking_Locks(effect, tag, level):
	if tag == "Skill_Ranks_Picking_Locks":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Picking_Locks":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]		
	
	
def Calculate_Enhancive_Perception(effect, tag, level):
	if tag == "Skill_Ranks_Perception":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Perception":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Climbing(effect, tag, level):
	if tag == "Skill_Ranks_Climbing":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Climbing":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Swimming(effect, tag, level):
	if tag == "Skill_Ranks_Swimming":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Swimming":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_First_Aid(effect, tag, level):
	if tag == "Skill_Ranks_First_Aid":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_First_Aid":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Trading(effect, tag, level):
	if tag == "Skill_Ranks_Trading":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Trading":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Pickpocketing(effect, tag, level):
	if tag == "Skill_Ranks_Pickpocketing":
		return [int(effect.scaling_arr["Skill ranks"]), "skill ranks"]	
	elif tag == "Skill_Bonus_Pickpocketing":
		return [int(effect.scaling_arr["Skill bonus"]), "skill bonus"]

	return [0, ""]	
	

# Statistic Enhansives	
	
def Calculate_Enhancive_Strength(effect, tag, level):
	if tag == "Statistic_Strength":
		return [int(effect.scaling_arr["Statistic increase"]), "statistic increase"]	
	elif tag == "Statistic_Bonus_Strength":
		return [int(effect.scaling_arr["Statistic bonus"]), "statistic bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Constitution(effect, tag, level):
	if tag == "Statistic_Constitution":
		return [int(effect.scaling_arr["Statistic increase"]), "statistic increase"]	
	elif tag == "Statistic_Bonus_Constitution":
		return [int(effect.scaling_arr["Statistic bonus"]), "statistic bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Dexterity(effect, tag, level):
	if tag == "Statistic_Dexterity":
		return [int(effect.scaling_arr["Statistic increase"]), "statistic increase"]	
	elif tag == "Statistic_Bonus_Dexterity":
		return [int(effect.scaling_arr["Statistic bonus"]), "statistic bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Agility(effect, tag, level):
	if tag == "Statistic_Agility":
		return [int(effect.scaling_arr["Statistic increase"]), "statistic increase"]	
	elif tag == "Statistic_Bonus_Agility":
		return [int(effect.scaling_arr["Statistic bonus"]), "statistic bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Discipline(effect, tag, level):
	if tag == "Statistic_Discipline":
		return [int(effect.scaling_arr["Statistic increase"]), "statistic increase"]	
	elif tag == "Statistic_Bonus_Discipline":
		return [int(effect.scaling_arr["Statistic bonus"]), "statistic bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Aura(effect, tag, level):
	if tag == "Statistic_Aura":
		return [int(effect.scaling_arr["Statistic increase"]), "statistic increase"]	
	elif tag == "Statistic_Bonus_Aura":
		return [int(effect.scaling_arr["Statistic bonus"]), "statistic bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Logic(effect, tag, level):
	if tag == "Statistic_Logic":
		return [int(effect.scaling_arr["Statistic increase"]), "statistic increase"]	
	elif tag == "Statistic_Bonus_Logic":
		return [int(effect.scaling_arr["Statistic bonus"]), "statistic bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Intuition(effect, tag, level):
	if tag == "Statistic_Intuition":
		return [int(effect.scaling_arr["Statistic increase"]), "statistic increase"]	
	elif tag == "Statistic_Bonus_Intuition":
		return [int(effect.scaling_arr["Statistic bonus"]), "statistic bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Wisdom(effect, tag, level):
	if tag == "Statistic_Wisdom":
		return [int(effect.scaling_arr["Statistic increase"]), "statistic increase"]	
	elif tag == "Statistic_Bonus_Wisdom":
		return [int(effect.scaling_arr["Statistic bonus"]), "statistic bonus"]

	return [0, ""]	
	
	
def Calculate_Enhancive_Influence(effect, tag, level):
	if tag == "Statistic_Influence":
		return [int(effect.scaling_arr["Statistic increase"]), "statistic increase"]	
	elif tag == "Statistic_Bonus_Influence":
		return [int(effect.scaling_arr["Statistic bonus"]), "statistic bonus"]

	return [0, ""]	
	
	
	
# Generic Bonus Effects


# All AS Bonus - +1 to +100 all AS	
def Calculate_Generic_All_AS(effect, tag, level):
	if tag == "AS_All":
		return [int(effect.scaling_arr["All AS bonus"]), "All AS"]
	elif tag == "UAF":
		return [int(effect.scaling_arr["All AS bonus"]), "UAF"]

	return [0, ""]		
	
	
# Melee AS Bonus - +1 to +100 melee AS	
def Calculate_Generic_Melee_AS(effect, tag, level):
	if tag == "AS_Melee":
		return [int(effect.scaling_arr["Melee AS bonus"]), "Melee AS"]

	return [0, ""]			
	
	
# Ranged AS Bonus - +1 to +100 ranged AS	
def Calculate_Generic_Ranged_AS(effect, tag, level):
	if tag == "AS_Ranged":
		return [int(effect.scaling_arr["Ranged AS bonus"]), "Ranged AS"]

	return [0, ""]			
	
	
# Bolt AS Bonus - +1 to +100 bolt AS	
def Calculate_Generic_Bolt_AS(effect, tag, level):
	if tag == "AS_Bolt":
		return [int(effect.scaling_arr["Bolt AS bonus"]), "Bolt AS"]

	return [0, ""]			
	
	
# UAF Bonus - +1 to +100 UAF
def Calculate_Generic_UAF(effect, tag, level):
	if tag == "UAF":
		return [int(effect.scaling_arr["UAF bonus"]), "UAF"]

	return [0, ""]		
	

# All DS Bonus - +1 to +100 all DS	
def Calculate_Generic_All_DS(effect, tag, level):
	if tag == "DS_All":
		return [int(effect.scaling_arr["All DS bonus"]), "All DS"]

	return [0, ""]		
	
	
# Melee DS Bonus - +1 to +100 melee DS	
def Calculate_Generic_Melee_DS(effect, tag, level):
	if tag == "DS_Melee":
		return [int(effect.scaling_arr["Melee DS bonus"]), "Melee DS"]

	return [0, ""]			
	
	
# Ranged DS Bonus - +1 to +100 ranged DS	
def Calculate_Generic_Ranged_DS(effect, tag, level):
	if tag == "DS_Ranged":
		return [int(effect.scaling_arr["Ranged DS bonus"]), "Ranged DS"]

	return [0, ""]			
	
	
# Bolt DS Bonus - +1 to +100 bolt DS	
def Calculate_Generic_Bolt_DS(effect, tag, level):
	if tag == "DS_Bolt":
		return [int(effect.scaling_arr["Bolt DS bonus"]), "Bolt DS"]

	return [0, ""]				
	
	
# All CS Bonus - +1 to +100 all CS	
def Calculate_Generic_All_CS(effect, tag, level):
	if tag == "CS_All":
		return [int(effect.scaling_arr["All CS bonus"]), "All CS"]

	return [0, ""]	
	
	
# Elemental CS Bonus - +1 to +100 elemental CS
def Calculate_Generic_Elemental_CS(effect, tag, level):
	if tag == "CS_Elemental":
		return [int(effect.scaling_arr["Ele CS bonus"]), "Elemental CS"]

	return [0, ""]		
	
	
# Mental CS Bonus - +1 to +100 mental CS	
def Calculate_Generic_Mental_CS(effect, tag, level):
	if tag == "CS_Mental":
		return [int(effect.scaling_arr["Mental CS bonus"]), "Mental CS"]

	return [0, ""]			
	
	
# Spiritual CS Bonus - +1 to +100 spiritual CS	
def Calculate_Generic_Spiritual_CS(effect, tag, level):
	if tag == "CS_Spiritual":
		return [int(effect.scaling_arr["Spirit CS bonus"]), "Spiritual CS"]

	return [0, ""]			
	
	
# Sorcerer CS Bonus - +1 to +100 sorcerer CS	
def Calculate_Generic_Sorcerer_CS(effect, tag, level):
	if tag == "CS_Sorcerer":
		return [int(effect.scaling_arr["Sorc CS bonus"]), "Sorcerer CS"]

	return [0, ""]			
	
	
# All TD Bonus - +1 to +100 all TD	
def Calculate_Generic_All_TD(effect, tag, level):
	if tag == "TD_All":
		return [int(effect.scaling_arr["All TD bonus"]), "All TD"]

	return [0, ""]	
	
	
# Elemental TD Bonus - +1 to +100 elemental TD
def Calculate_Generic_Elemental_TD(effect, tag, level):
	if tag == "TD_Elemental":
		return [int(effect.scaling_arr["Ele TD bonus"]), "Elemental TD"]

	return [0, ""]		
	
	
# Mental TD Bonus - +1 to +100 mental TD	
def Calculate_Generic_Mental_TD(effect, tag, level):
	if tag == "TD_Mental":
		return [int(effect.scaling_arr["Mental TD bonus"]), "Mental TD"]

	return [0, ""]			
	
	
# Spiritual TD Bonus - +1 to +100 spiritual TD	
def Calculate_Generic_Spiritual_TD(effect, tag, level):
	if tag == "TD_Spiritual":
		return [int(effect.scaling_arr["Spirit TD bonus"]), "Spiritual TD"]

	return [0, ""]			
	
	
# Sorcerer TD Bonus - +1 to +100 sorcerer TD	
def Calculate_Generic_Sorcerer_TD(effect, tag, level):
	if tag == "TD_Sorcerer":
		return [int(effect.scaling_arr["Sorc TD bonus"]), "Sorcerer TD"]

	return [0, ""]	
	
	
	
	
# Status Effects	
	
# Kneeling - -50 melee, ranged, bolt AS and DS, +30 ranged AS if using a crossbow
def Calculate_Kneeling(effect, tag, level):
	if tag == "AS_Ranged":				
		try:
			if override_dict["Main Weapon"] == "Heavy Crossbow" or override_dict["Main Weapon"] == "Light Crossbow":
				return [30, "Crossbow Ranged AS"]			
		except:
			pass
			
		return [-50, "Ranged AS"]	
		
	elif tag == "AS_Melee":				
		return [-50, "Melee AS"]
	elif tag == "AS_Bolt":				
		return [-50, "Bolt AS"]
	elif tag == "DS_All":				
		return [-50, "All DS"]
	elif tag == "Resource_Recovery_Stamina_Normal":
		return [5, "Stamina Recovery"]		
		
	return [0, ""]

	
# Lying_Down - -50 melee, ranged, bolt AS and DS, +30 ranged AS if using a crossbow
def Calculate_Lying_Down(effect, tag, level):
	if tag == "AS_Ranged":				
		try:
			if override_dict["Main Weapon"] == "Heavy Crossbow" or override_dict["Main Weapon"] == "Light Crossbow":
				return [30, "Crossbow Ranged AS"]			
		except:
			pass
			
		return [-50, "Ranged AS"]	
		
	elif tag == "AS_Melee":				
		return [-50, "Melee AS"]
	elif tag == "AS_Bolt":				
		return [-50, "Bolt AS"]
	elif tag == "DS_All":				
		return [-50, "All DS"]
	elif tag == "Resource_Recovery_Stamina_Normal":
		return [5, "Stamina Recovery"]

	return [0, ""]
	
	
# Overexerted - -10 AS/UAF	
def Calculate_Overexerted(effect, tag, level):
	if tag == "AS_All":				
		return [-10, "All AS"]
	elif tag == "UAF":				
		return [-10, "UAF"]

	return [0, ""]	

	
# Rooted - -50 melee AS, -25 ranged AS, -25 DS
def Calculate_Rooted(effect, tag, level):
	if tag == "AS_Melee":				
		return [-50, "Melee AS"]
	elif tag == "AS_Ranged":				
		return [-25, "Ranged AS"]
	elif tag == "DS_All":				
		return [-25, "All DS"]

	return [0, ""]	

	
# Stunned - -20 DS	
def Calculate_Stunned(effect, tag, level):
	if tag == "DS_All":				
		return [-20, "All DS"]

	return [0, ""]	
	
	
# Flare effects.

# Acuity AS Flare - +5 bonus to bolt AS on next spell cast per tier
def Calculate_Acuity_AS_Flare(effect, tag, level):
	if tag == "AS_Bolt":
		return [5 * int(effect.scaling_arr["Tier"]), "Bolt AS"]	
		
	return [0, ""]	
	
	
# Acuity CS Flare - +3 bonus to all CS on next cast per tier
def Calculate_Acuity_CS_Flare(effect, tag, level):
	if tag == "CS_All":
		return [3 * int(effect.scaling_arr["Tier"]), "All CS"]	
		
	return [0, ""]			
	

# Ensorcell AS Flare - +5/+10/+15/+20/+25 bonus to AS on next melee, ranged, UAF attack	
def Calculate_Ensorcell_AS_Flare(effect, tag, level):
	if tag == "AS_All":
		return [5 * int(effect.scaling_arr["Tier"]), "All AS"]	
	if tag == "UAF":
		return [5 * int(effect.scaling_arr["Tier"]), "UAF"]	
		
	return [0, ""]	
	

# Ensorcell CS Flare - +5/+10/+15/+20/+25 bonus to CS	
def Calculate_Ensorcell_CS_Flare(effect, tag, level):
	if tag == "CS_All":
		return [5 * int(effect.scaling_arr["Tier"]), "All CS"]	
		
	return [0, ""]	
	
	
# Spirit Warding II (107) Flare - +25 Spiritual TD	
def Calculate_107_Flare(effect, tag, level):
	if tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":
		bonus = 25
		'''
		if tag == "TD_Spiritual":
			type = "Spiritual TD"	
		elif tag == "TD_Elemental":
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental TD"
		elif tag == "TD_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer TD"
		'''	
		return [bonus, "All TD"]

	return [0, ""]	
	
	
# Benediction (307) Flare - +15 bonus to all AS and UAF	
def Calculate_307_Flare(effect, tag, level):
	if tag == "AS_All":				
		return [15, "All AS"]
	elif tag == "UAF":				
		return [15, "UAF"]

	return [0, ""]

	
# Thurfel's Ward (503) Flare - +20 DS
def Calculate_503_Flare(effect, tag, level):
	if tag == "DS_All":				
		return [20, "All DS"]

	return [0, ""]	
	
	
# Elemental Bias (508) Flare -	+20 Elemental TD
def Calculate_508_Flare(effect, tag, level):
	if tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":
		bonus = 20
		
		if tag == "TD_Elemental":
			type = "Elemental TD"
		elif tag == "TD_Spiritual":
			bonus = math.ceil(bonus * 0.5)
			type = "Spiritual TD"	
		elif tag == "TD_Mental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Mental TD"
		elif tag == "TD_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer TD"

		return [bonus, type]
		
	return [0, ""]	
	
	
# Elemental Focus (513) Flare - +1 Bolt AS per seed 4 summation of Elemental Lore, Fire ranks on consecutive bolt attacks	
def Calculate_513_Flare(effect, tag, level):
	if tag == "AS_Bolt":			
		lore_ranks = Get_Skill_Ranks(effect, level, "Elemental Lore, Fire", "")			
		bonus = min(25, Get_Summation_Bonus(4, lore_ranks))
		
		return [bonus, "Bolt AS"]					

	return [0, ""]	
	
	
# Curse (715) Star - +10 bolt AS. +1 bolt AS per 3 Spell Research, Sorcerer ranks above 15, capped character level	
def Calculate_715_Flare(effect, tag, level):
	if tag == "AS_Bolt":		
		spell_ranks = Get_Skill_Ranks(effect, level, "Spell Research, Sorcerer", "")	
		if level > 100:
			level = 100
			
		bonus = min(level, 10 + math.floor(max(0, spell_ranks - 15)/3))		
	
		return [bonus, "Bolt AS"]

	return [0, ""]		
	

	
# Items
	
def Calculate_Item_Defense_Bonus(effect, tag, level):
	if tag == "DS_All":			
		bonus = 5 * int(effect.scaling_arr["Tier"])
		return [bonus, "All DS"]

	return [0, ""]		
	
	
def Calculate_Item_Strength_Crystal_Greater(effect, tag, level):
	if tag == "Statistic_Bonus_Strength":			
		return [10, "Strength Crystal, Greater"]

	return [0, ""]			
	
	
def Calculate_Item_Strength_Crystal_Lesser(effect, tag, level):
	if tag == "Statistic_Bonus_Strength":			
		return [5, "Strength Crystal, Lesser"]

	return [0, ""]		
	
	
def Calculate_Item_Constitution_Crystal_Greater(effect, tag, level):
	if tag == "Statistic_Bonus_Constitution":			
		return [10, "Constitution Crystal, Greater"]

	return [0, ""]			
	
	
def Calculate_Item_Constitution_Crystal_Lesser(effect, tag, level):
	if tag == "Statistic_Bonus_Constitution":			
		return [5, "Constitution Crystal, Lesser"]

	return [0, ""]		
	
	
def Calculate_Item_Aura_Crystal_Greater(effect, tag, level):
	if tag == "Statistic_Bonus_Aura":			
		return [10, "Aura Crystal, Greater"]

	return [0, ""]			
	
	
def Calculate_Item_Aura_Crystal_Lesser(effect, tag, level):
	if tag == "Statistic_Bonus_Aura":			
		return [5, "Aura Crystal, Lesser"]

	return [0, ""]	
	
	
def Calculate_Item_Logic_Potion_Greater(effect, tag, level):
	if tag == "Statistic_Bonus_Logic":			
		return [10, "Logic Potion, Greater"]

	return [0, ""]			
	
	
def Calculate_Item_Logic_Potion_Lesser(effect, tag, level):
	if tag == "Statistic_Bonus_Logic":			
		return [5, "Logic Potion, Lesser"]

	return [0, ""]			
	
	
def Calculate_Item_Intuition_Crystal_Greater(effect, tag, level):
	if tag == "Statistic_Bonus_Intuition":			
		return [10, "Intuition Crystal, Greater"]

	return [0, ""]			
	
	
def Calculate_Item_Intuition_Crystal_Lesser(effect, tag, level):
	if tag == "Statistic_Bonus_Intuition":			
		return [5, "Intuition Crystal, Lesser"]

	return [0, ""]	
	
	
def Calculate_Item_Wisdom_Potion_Greater(effect, tag, level):
	if tag == "Statistic_Bonus_Wisdom":			
		return [10, "Wisdom Potion, Greater"]

	return [0, ""]			
	
	
def Calculate_Item_Wisdom_Potion_Lesser(effect, tag, level):
	if tag == "Statistic_Bonus_Wisdom":			
		return [5, "Wisdom Potion, Greater"]

	return [0, ""]					
		

# Mana Regeneration Potion, Minor - +3 mana recovery	
def Calculate_Item_Mana_Regeneration_Potion_Minor(effect, tag, level):
	if tag == "Resource_Recovery_Mana":				
		return [3, "Mana Recovery"]

	return [0, ""]	
		

# Mana Regeneration Potion, Lesser - +8 mana recovery	
def Calculate_Item_Mana_Regeneration_Potion_Lesser(effect, tag, level):
	if tag == "Resource_Recovery_Mana":				
		return [8, "Mana Recovery"]

	return [0, ""]	
		

# Mana Regeneration Potion, Greater - +13 mana recovery	
def Calculate_Item_Mana_Regeneration_Potion_Greater(effect, tag, level):
	if tag == "Resource_Recovery_Mana":				
		return [13, "Mana Recovery"]

	return [0, ""]	
		

# Spirit Regeneration Crystal, Minor - +1 spirit recovery	
def Calculate_Item_Spirit_Regeneration_Crystal_Minor(effect, tag, level):
	if tag == "Resource_Recovery_Spirit":				
		return [1, "Mana Recovery"]

	return [0, ""]	
		

# Spirit Regeneration Crystal, Lesser - +2 spirit recovery	
def Calculate_Item_Spirit_Regeneration_Crystal_Lesser(effect, tag, level):
	if tag == "Resource_Recovery_Spirit":				
		return [2, "Spirit Recovery"]

	return [0, ""]	
		

# Spirit Regeneration Crystal, Greater - +3 spirit recovery	
def Calculate_Item_Spirit_Regeneration_Crystal_Greater(effect, tag, level):
	if tag == "Resource_Recovery_Spirit":				
		return [3, "Spirit Recovery"]

	return [0, ""]	
		

# Stamina Regeneration Crystal, Minor - +10 stamina recovery	
def Calculate_Item_Stamina_Regeneration_Crystal_Minor(effect, tag, level):
	if tag == "Resource_Recovery_Spirit":				
		return [1, "Spirit Recovery"]

	return [0, ""]	
		

# Stamina Regeneration Crystal, Lesser - +20 stamina recovery	
def Calculate_Item_Stamina_Regeneration_Crystal_Lesser(effect, tag, level):
	if tag == "Resource_Recovery_Spirit":				
		return [2, "Stamina Recovery"]

	return [0, ""]	
		

# Stamina Regeneration Crystal, Greater - +30 stamina recovery	
def Calculate_Item_Stamina_Regeneration_Crystal_Greater(effect, tag, level):
	if tag == "Resource_Recovery_Spirit":				
		return [3, "Stamina Recovery"]

	return [0, ""]	
		

# Health-well Potion, Minor - +10 maximum health	
def Calculate_Item_Health_Well_Potion_Minor(effect, tag, level):
	if tag == "Resource_Maximum_Health":				
		return [10, "Maximum Health"]

	return [0, ""]	
		

# Health-well Potion, Lesser - +25 maximum health	
def Calculate_Item_Health_Well_Potion_Lesser(effect, tag, level):
	if tag == "Resource_Maximum_Health":				
		return [25, "Maximum Health"]

	return [0, ""]	
		

# Health-well Potion, Greater - +50 maximum health
def Calculate_Item_Health_Well_Potion_Greater(effect, tag, level):
	if tag == "Resource_Maximum_Health":				
		return [50, "Maximum Health"]
		

# Mana-well Potion, Minor - +10 maximum mana	
def Calculate_Item_Mana_Well_Potion_Minor(effect, tag, level):
	if tag == "Resource_Maximum_Mana":				
		return [10, "Maximum Mana"]

	return [0, ""]	
		

# Mana-well Potion, Lesser - +25 maximum mana	
def Calculate_Item_Mana_Well_Potion_Lesser(effect, tag, level):
	if tag == "Resource_Maximum_Mana":				
		return [25, "Maximum Mana"]

	return [0, ""]	
		

# Mana-well Potion, Greater - +50 maximum mana
def Calculate_Item_Mana_Well_Potion_Greater(effect, tag, level):
	if tag == "Resource_Maximum_Mana":				
		return [50, "Maximum Mana"]
		

# Spirit-well Potion, Minor - +10 maximum spirit	
def Calculate_Item_Spirit_Well_Potion_Minor(effect, tag, level):
	if tag == "Resource_Maximum_Spirit":				
		return [1, "Maximum Spirit"]

	return [0, ""]	
		

# Spirit-well Potion, Lesser - +25 maximum spirit	
def Calculate_Item_Spirit_Well_Potion_Lesser(effect, tag, level):
	if tag == "Resource_Maximum_Spirit":				
		return [2, "Maximum Spirit"]

	return [0, ""]	
		

# Spirit-well Potion, Greater - +50 maximum spirit
def Calculate_Item_Spirit_Well_Potion_Greater(effect, tag, level):
	if tag == "Resource_Maximum_Spirit":				
		return [3, "Maximum Spirit"]
		
		
# Elemental Focus Crystal, Minor - +10 elemental CS
def Calculate_Item_Elemental_Focus_Crystal_Minor(effect, tag, level):
	if tag == "CS_Elemental" or tag == "CS_Mental" or tag == "CS_Spiritual" or tag == "CS_Sorcerer":
		bonus = 10
		
		if tag == "CS_Elemental":
			type = "Elemental CS"
		elif tag == "CS_Mental":
			bonus = math.ceil(bonus * 0.5)
			type = "Mental CS"
		elif tag == "CS_Spiritual": 
			bonus = math.ceil(bonus * 0.5)
			type = "Spiritual CS"	
		elif tag == "CS_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer CS"
			
		return [bonus, type]

	return [0, ""]				
		
		
# Elemental Focus Crystal, Lesser - +15 elemental CS
def Calculate_Item_Elemental_Focus_Crystal_Lesser(effect, tag, level):
	if tag == "CS_Elemental" or tag == "CS_Mental" or tag == "CS_Spiritual" or tag == "CS_Sorcerer":
		bonus = 15
		
		if tag == "CS_Elemental":
			type = "Elemental CS"
		elif tag == "CS_Mental":
			bonus = math.ceil(bonus * 0.5)
			type = "Mental CS"
		elif tag == "CS_Spiritual": 
			bonus = math.ceil(bonus * 0.5)
			type = "Spiritual CS"	
		elif tag == "CS_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer CS"
			
		return [bonus, type]

	return [0, ""]				
		
		
# Elemental Focus Crystal, Greater - +25 elemental CS
def Calculate_Item_Elemental_Focus_Crystal_Greater(effect, tag, level):
	if tag == "CS_Elemental" or tag == "CS_Mental" or tag == "CS_Spiritual" or tag == "CS_Sorcerer":
		bonus = 25
		
		if tag == "CS_Elemental":
			type = "Elemental CS"
		elif tag == "CS_Mental":
			bonus = math.ceil(bonus * 0.5)
			type = "Mental CS"
		elif tag == "CS_Spiritual": 
			bonus = math.ceil(bonus * 0.5)
			type = "Spiritual CS"	
		elif tag == "CS_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer CS"
			
		return [bonus, type]

	return [0, ""]			
		
		
# Mental Focus Crystal, Minor - +10 mental CS
def Calculate_Item_Mental_Focus_Crystal_Minor(effect, tag, level):
	if tag == "CS_Elemental" or tag == "CS_Mental" or tag == "CS_Spiritual" or tag == "CS_Sorcerer":
		bonus = 10
		
		if tag == "CS_Mental":
			type = "Mental CS"
		elif tag == "CS_Elemental":
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental CS"
		elif tag == "CS_Spiritual": 
			bonus = math.ceil(bonus * 0.5)
			type = "Spiritual CS"	
		elif tag == "CS_Sorcerer": 
			bonus = math.ceil(bonus * 0.5)
			type = "Sorcerer CS"
			
		return [bonus, type]	

	return [0, ""]				
		
		
# Mental Focus Crystal, Lesser - +15 mental CS
def Calculate_Item_Mental_Focus_Crystal_Lesser(effect, tag, level):
	if tag == "CS_Elemental" or tag == "CS_Mental" or tag == "CS_Spiritual" or tag == "CS_Sorcerer":
		bonus = 15
		
		if tag == "CS_Mental":
			type = "Mental CS"
		elif tag == "CS_Elemental":
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental CS"
		elif tag == "CS_Spiritual": 
			bonus = math.ceil(bonus * 0.5)
			type = "Spiritual CS"	
		elif tag == "CS_Sorcerer": 
			bonus = math.ceil(bonus * 0.5)
			type = "Sorcerer CS"
			
		return [bonus, type]	

	return [0, ""]				
		
		
# Mental Focus Crystal, Greater - +25 mental CS
def Calculate_Item_Mental_Focus_Crystal_Greater(effect, tag, level):
	if tag == "CS_Elemental" or tag == "CS_Mental" or tag == "CS_Spiritual" or tag == "CS_Sorcerer":
		bonus = 25
		
		if tag == "CS_Mental":
			type = "Mental CS"
		elif tag == "CS_Elemental":
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental CS"
		elif tag == "CS_Spiritual": 
			bonus = math.ceil(bonus * 0.5)
			type = "Spiritual CS"	
		elif tag == "CS_Sorcerer": 
			bonus = math.ceil(bonus * 0.5)
			type = "Sorcerer CS"
			
		return [bonus, type]	

	return [0, ""]		
		
		
# Spiritual Focus Crystal, Minor - +10 spiritual CS
def Calculate_Item_Spiritual_Focus_Crystal_Minor(effect, tag, level):
	if tag == "CS_Elemental" or tag == "CS_Mental" or tag == "CS_Spiritual" or tag == "CS_Sorcerer":
		bonus = 10
		
		if tag == "CS_Spiritual":
			type = "Spiritual CS"	
		elif tag == "CS_Mental":
			bonus = math.ceil(bonus * 0.5)
			type = "Mental CS"
		elif tag == "CS_Elemental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental CS"
		elif tag == "CS_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer CS"
			
		return [bonus, type]

	return [0, ""]				
		
		
# Spiritual Focus Crystal, Lesser - +15 spiritual CS
def Calculate_Item_Spiritual_Focus_Crystal_Lesser(effect, tag, level):
	if tag == "CS_Elemental" or tag == "CS_Mental" or tag == "CS_Spiritual" or tag == "CS_Sorcerer":
		bonus = 15
		
		if tag == "CS_Spiritual":
			type = "Spiritual CS"	
		elif tag == "CS_Mental":
			bonus = math.ceil(bonus * 0.5)
			type = "Mental CS"
		elif tag == "CS_Elemental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental CS"
		elif tag == "CS_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer CS"
			
		return [bonus, type]

	return [0, ""]				
		
		
# Spiritual Focus Crystal, Greater - +25 spiritual CS
def Calculate_Item_Spiritual_Focus_Crystal_Greater(effect, tag, level):
	if tag == "CS_Elemental" or tag == "CS_Mental" or tag == "CS_Spiritual" or tag == "CS_Sorcerer":
		bonus = 25
		
		if tag == "CS_Spiritual":
			type = "Spiritual CS"	
		elif tag == "CS_Mental":
			bonus = math.ceil(bonus * 0.5)
			type = "Mental CS"
		elif tag == "CS_Elemental": 
			bonus = math.ceil(bonus * 0.5)
			type = "Elemental CS"
		elif tag == "CS_Sorcerer": 
			bonus = math.ceil(bonus * 0.75)
			type = "Sorcerer CS"
			
		return [bonus, type]

	return [0, ""]	
		

# Repelling Oil, Minor - +10 DS vs undead
def Calculate_Item_Repelling_Oil_Minor(effect, tag, level):
	if tag == "DS_All":				
		return [10, "All DS vs undead"]
		
		
# Repelling Oil, Greater - +30 DS vs undead
def Calculate_Item_Repelling_Oil_Greater(effect, tag, level):
	if tag == "DS_All":				
		return [30, "All DS vs undead"]
		

# Exorcism Oil, Minor - +10 AS vs undead
def Calculate_Item_Exorcism_Oil_Minor(effect, tag, level):
	if tag == "AS_All":				
		return [10, "All AS vs undead"]
		
		
# Exorcism Oil, Greater - +30 AS vs undead
def Calculate_Item_Exorcism_Oil_Greater(effect, tag, level):
	if tag == "AS_All":				
		return [30, "All AS vs undead"]
		

# Encumbrance Potion - Reduces encumbrance by 40 pounds
def Calculate_Item_Encumbrance_Potion(effect, tag, level):
	if tag == "Encumbrance_Reduction_Absolute":				
		return [40, "Carry Capacity"]
		

# Encumbrance Charm - Reduces encumbrance by 100 pounds
def Calculate_Item_Encumbrance_Charm(effect, tag, level):
	if tag == "Encumbrance_Reduction_Absolute":				
		return [100, "Carry Capacity"]



	
# Room Effects

# Bright - -10 DS	
def Calculate_Room_Bright(effect, tag, level):
	if tag == "DS_All":				
		return [-10, "All DS"]

	return [0, ""]	

	
# Dark - +20 DS		
def Calculate_Room_Dark(effect, tag, level):
	if tag == "DS_All":				
		return [20, "All DS"]

	return [0, ""]	

	
# Foggy - +30 DS		
def Calculate_Room_Foggy(effect, tag, level):
	if tag == "DS_All":				
		return [30, "All DS"]

	return [0, ""]	
	
	
# Node - Base Mana Recovery is 25% instead of 15% (This is handled in the actual formula, not here)	
def Calculate_Room_Node(effect, tag, level):
	return [0, ""]	
	
	
# Other Effects	

	
