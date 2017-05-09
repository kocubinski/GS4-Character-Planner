import Globals as globals
import math

'''
The primary purpose of the calculations file is to provide the Progress Panel with the number values of
any effects the character is using. These effects can vary from a simple value to a complicated
calculation using spell ranks and/or lore ranks with a set min and max. Each method corresponses to an
effect located in the Create_Database.py file along with a set of effect tags that indicate what parameters
the effect changes.
'''

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


# Minor Spiritual (100s)	

# Spirit Warding I (101) - +10 Spiritual TD, +10 Bolt DS
def Calculate_101(effect, tag, level):
	if tag == "DS_Bolt":				
		return [10, "Bolt DS"]
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
		if level > 100:
			lore_ranks = int(globals.character.skills_list["Spell Research, Minor Spiritual"].Postcap_Get_Total_Ranks_Closest_To_Interval(level))	
			lore_ranks += int(globals.character.skills_list["Spell Research, Minor Spiritual"].total_ranks_by_level[100].get())	
		else:
			lore_ranks = int(globals.character.skills_list["Spell Research, Minor Spiritual"].total_ranks_by_level[level].get())	
			
			
		if effect.scaling_arr["Minor Spiritual"] == "D":
			if level > 100:
				level = 100
				
			scaling = min(level, int(math.floor((int(lore_ranks) - 2)/2)))			
			if scaling < 0:
				scaling = 0				
			
			bonus = 20 + scaling
			
		else:			
			scaling = min(level, int(math.floor(((int(effect.scaling_arr["Minor Spiritual"]) - 2)/2)))) 
			if scaling < 0:
				scaling = 0
		
			bonus = 20 + scaling
			
		if tag == "DS_All":
			type = "All DS"
		elif tag == "AS_Melee":
			bonus *= -1
			type = "Melee AS"
		elif tag == "UAF":
			bonus *= -1
			type = "UAF"
		
		return [bonus, type]
		
		
	return [0, ""]

	
# Spirit Barrier (103) - +10 DS
def Calculate_103(effect, tag, level):
	if tag == "DS_All":				
		return [10, "All DS"]
		
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

	return [0, ""]
	
	
# Spirit Strike (117) - +75 AS, +75 UAF
def Calculate_117(effect, tag, level):
	if tag == "AS_All":				
		return [75, "All AS"]
	elif tag == "UAF":				
		return [75, "UAF"]

	return [0, ""]	
	
	
# Lesser Shroud (120) - +15 DS, +20 Spiritual TD. +1 DS per 2 Spell Research, Minor Spiritual ranks over 20
def Calculate_120(effect, tag, level):		
	if tag == "DS_All":	
		if level > 100:
			lore_ranks = int(globals.character.skills_list["Spell Research, Minor Spiritual"].Postcap_Get_Total_Ranks_Closest_To_Interval(level))	
			lore_ranks += int(globals.character.skills_list["Spell Research, Minor Spiritual"].total_ranks_by_level[100].get())	
		else:
			lore_ranks = int(globals.character.skills_list["Spell Research, Minor Spiritual"].total_ranks_by_level[level].get())				
			
		if effect.scaling_arr["Minor Spiritual"] == "D":
			if level > 100:
				level = 100
				
			scaling = min(level, int(math.floor((int(lore_ranks) - 20)/2)))			
			if scaling < 0:
				scaling = 0			
			
		else:			
			scaling = min(level, int(math.floor(((int(effect.scaling_arr["Minor Spiritual"]) - 20)/2)))) 
			if scaling < 0:
				scaling = 0
				
		return [15 + scaling, "All DS"]
		
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
		
	return [0, ""]

	
# Wall of Force (140) - +100 DS
def Calculate_140(effect, tag, level):
	if tag == "DS_All":				
		return [100, "All DS"]
		
	return [0, ""]
	

# Major Spiritual (200s)	
	
# Spirit Shield (202) - +10 DS. +1 DS per 2 Spell Research, Major Spiritual ranks above 2, up to character level
def Calculate_202(effect, tag, level):		
	if tag == "DS_All":	
		if effect.scaling_arr["Major Spiritual"] == "D":
			if level > 100:
				spell_ranks = int(globals.character.skills_list["Spell Research, Major Spiritual"].Postcap_Get_Total_Ranks_Closest_To_Interval(level))	
				spell_ranks += int(globals.character.skills_list["Spell Research, Major Spiritual"].total_ranks_by_level[100].get())	
			else:
				spell_ranks = int(globals.character.skills_list["Spell Research, Major Spiritual"].total_ranks_by_level[level].get())		
		else:
			spell_ranks  = int(effect.scaling_arr["Major Spiritual"])				
				
		bonus = min(100, 10 + math.floor(max(0, spell_ranks - 2)/2))				
				
		return [bonus, "All DS"]	
		
	return [0, ""]
	
	
# Bravery (211)	- +15 AS, +15 UAF
def Calculate_211(effect, tag, level):
	if tag == "AS_All":				
		return [15, "All AS"]
	elif tag == "UAF":				
		return [15, "UAF"]

	return [0, ""]	


# Heroism (215) - +25 AS, +25 UAF, +1 AS for every 10 Spiritual Lore, Blessing ranks		
def Calculate_215(effect, tag, level):
	if tag == "AS_All" or tag == "UAF":		
		if level > 100:
			if effect.scaling_arr["Blessings"] == "D":
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Blessings"].Postcap_Get_Total_Ranks_Closest_To_Interval(level))	
				lore_ranks += int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[100].get())	
			else:
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Blessings"])				
	
		bonus = 25 + math.floor(lore_ranks/10)
			
		if tag == "AS_All":			
			type = "All AS"
		elif tag == "UAF":	
			type = "UAF"		
		
		return [bonus, type]
		
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

	return [0, ""]
	
	
# Spirit Slayer (240) - +25 bolt AS, +25 Spiritual CS. +1 Bolt AS and Spiritual CS per summation 5 seed of Spiritual Mana Control ranks
def Calculate_240(effect, tag, level):	
	if tag == "AS_Bolt" or tag == "CS_Elemental" or tag == "CS_Mental" or tag == "CS_Spiritual" or tag == "CS_Sorcerer":
		if effect.scaling_arr["Spiritual MC"] == "D":
			if level > 100:
				ranks  = int(globals.character.skills_list["Spiritual Mana Control"].total_ranks_by_level[100].get())
				ranks += globals.character.skills_list["Spiritual Mana Control"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				ranks = int(globals.character.skills_list["Spiritual Mana Control"].total_ranks_by_level[level].get())		
		else:
			ranks  = int(effect.scaling_arr["Spiritual MC"])
		
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

	return [0, ""]	
	

# Cleric Base (300s)	
	
# Prayer of Protection (303) - +10 DS. +1 DS per 2 Spell Research, Cleric ranks above 3 up to character level
def Calculate_303(effect, tag, level):		
	if tag == "DS_All":	
		if effect.scaling_arr["Cleric"] == "D":
			if level > 100:
				lore_ranks = int(globals.character.skills_list["Spell Research, Cleric"].Postcap_Get_Total_Ranks_Closest_To_Interval(level))	
				lore_ranks += int(globals.character.skills_list["Spell Research, Cleric"].total_ranks_by_level[100].get())	
			else:
				lore_ranks = int(globals.character.skills_list["Spell Research, Cleric"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Cleric"])			
			
	
		bonus = 10 + min(99, math.floor(max(0, lore_ranks - 3)/2))			
				
		return [bonus, "All DS"]	
		
	return [0, ""]
	
	
# Benediction (307) - +5 AS, +5 ranged DS, +5 melee DS. +1 AS/DS per 2 Cleric Base ranks above 7 with a maximum bonus of +15 AS/DS, Additionally, +1 bolt AS per 2 Cleric Base ranks above 7 with a maximum bonus of +15 AS to a maximum of +51 at level 99, +5 melee and ranged DS at spell rank 7. 
def Calculate_307(effect, tag, level):	
	if tag == "AS_Melee" or tag == "AS_Ranged" or tag == "AS_Bolt" or tag == "UAF" or tag == "DS_Melee" or tag == "DS_Ranged":		
		if effect.scaling_arr["Cleric"] == "D":
			if level > 100:
				spell_ranks = int(globals.character.skills_list["Spell Research, Cleric"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Cleric"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)			
			else:	
				spell_ranks = int(globals.character.skills_list["Spell Research, Cleric"].total_ranks_by_level[level].get())		
		else:
			spell_ranks  = int(effect.scaling_arr["Cleric"])			
	
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
		if effect.scaling_arr["Cleric"] == "D":			
			if level > 100:
				spell_ranks = int(globals.character.skills_list["Spell Research, Cleric"].Postcap_Get_Total_Ranks_Closest_To_Interval(level))	
				spell_ranks += int(globals.character.skills_list["Spell Research, Cleric"].total_ranks_by_level[100].get())	
			else:
				spell_ranks = int(globals.character.skills_list["Spell Research, Cleric"].total_ranks_by_level[level].get())
		else:		
			spell_ranks  = int(effect.scaling_arr["Cleric"])			
		
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
	
# Praryer (313) - +10 Spirit TD\n+10 all DS at 35 Spell Research, Cleric ranks and increases by +1 per rank above 35 up to character level
def Calculate_313(effect, tag, level):			
	if tag == "DS_All" or tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":
		if effect.scaling_arr["Cleric"] == "D":			
			if level > 100:
				spell_ranks = int(globals.character.skills_list["Spell Research, Cleric"].Postcap_Get_Total_Ranks_Closest_To_Interval(level))	
				spell_ranks += int(globals.character.skills_list["Spell Research, Cleric"].total_ranks_by_level[100].get())	
			else:
				spell_ranks = int(globals.character.skills_list["Spell Research, Cleric"].total_ranks_by_level[level].get())
		else:		
			spell_ranks  = int(effect.scaling_arr["Cleric"])		
			
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

	return [0, ""]
	
	
#Elemental Targeting (425) -  +25 AS, +25 UAF, +25 Elemental CS. +1 AS/UAF/Elemental CS per 2 Spell Research, Minor Elemental ranks above 25 up to a +50 at 75 ranks	
def Calculate_425(effect, tag, level):	
	if tag == "AS_All" or tag == "UAF" or tag == "CS_Elemental" or tag == "CS_Mental" or tag == "CS_Spiritual" or tag == "CS_Sorcerer":
		if effect.scaling_arr["Minor Elemental"] == "D":
			if level > 100:
				spell_ranks  = int(globals.character.skills_list["Spell Research, Minor Elemental"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Minor Elemental"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				spell_ranks = int(globals.character.skills_list["Spell Research, Minor Elemental"].total_ranks_by_level[level].get())		
		else:
			spell_ranks  = int(effect.scaling_arr["Minor Elemental"])
		
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

	return [0, ""]			
	

# Elemental Barrier (430) - +15 DS, +15 Elemental TD. +1 DS/Elemental TD per 2 Spell Research, Minor Elemental ranks above 30	
def Calculate_430(effect, tag, level):	
	if tag == "DS_All" or tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":		
		type = ""
		if effect.scaling_arr["Minor Elemental"] == "D":
			if level > 100:
				spell_ranks  = int(globals.character.skills_list["Spell Research, Minor Elemental"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Minor Elemental"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				spell_ranks = int(globals.character.skills_list["Spell Research, Minor Elemental"].total_ranks_by_level[level].get())		
		else:
			spell_ranks  = int(effect.scaling_arr["Minor Elemental"])
		
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

	return [0, ""]			
	

# Major Elemental (500s)	
	
# Thurfel's Ward (503) - +20 DS. +1 DS per 4 Spell Research, Major Elemental ranks above 3. 
def Calculate_503(effect, tag, level):	
	if tag == "DS_All":		
		if effect.scaling_arr["Major Elemental"] == "D":
			if level > 100:
				spell_ranks  = int(globals.character.skills_list["Spell Research, Major Elemental"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Major Elemental"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				spell_ranks = int(globals.character.skills_list["Spell Research, Major Elemental"].total_ranks_by_level[level].get())		
		else:
			spell_ranks  = int(effect.scaling_arr["Major Elemental"])
		
		bonus = 20 + math.floor(max(0, spell_ranks - 3)/4)			
	
		return [bonus, "All DS"]	

	return [0, ""]		
	
	
# Elemental Deflection (507) - +20 DS. +1 DS per 2 Spell Research, Major Elemental ranks above 7	
def Calculate_507(effect, tag, level):	
	if tag == "DS_All":		
		if effect.scaling_arr["Major Elemental"] == "D":
			if level > 100:
				spell_ranks  = int(globals.character.skills_list["Spell Research, Major Elemental"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Major Elemental"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				spell_ranks = int(globals.character.skills_list["Spell Research, Major Elemental"].total_ranks_by_level[level].get())		
		else:
			spell_ranks  = int(effect.scaling_arr["Major Elemental"])
		
		bonus = 20 + math.floor(max(0, spell_ranks - 7)/2)			
	
		return [bonus, "All DS"]	

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
		
	return [0, ""]
		
		
# Strength (509) - +15 melee AS, +15 UAF. +1 melee AS/UAF when self-cast per seed 4 summation of Elemental Lore, Earth ranks	
def Calculate_509(effect, tag, level):
	if tag == "AS_Melee" or tag == "UAF":				
		if effect.scaling_arr["Earth"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Elemental Lore, Earth"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Elemental Lore, Earth"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Elemental Lore, Earth"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Earth"])
		
		bonus = 15 + Get_Summation_Bonus(4, lore_ranks)		
					
		if tag == "AS_Melee":
			type = "Melee AS"
		elif tag == "UAF":
			type = "UAF"		
		
		return [bonus, type]					

	return [0, ""]		
	
		
# Elemental Focus (513)	- +20 bolt AS. +1 bolt AS when self-cast per 2 Spell Research, Major Elemental ranks above 13 capped at character level
def Calculate_513(effect, tag, level):
	if tag == "AS_Bolt":			
		if effect.scaling_arr["Major Elemental"] == "D":
			if level > 100:
				spell_ranks  = int(globals.character.skills_list["Spell Research, Major Elemental"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Major Elemental"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
				level = 100
			else:				
				spell_ranks = int(globals.character.skills_list["Spell Research, Major Elemental"].total_ranks_by_level[level].get())	
				bonus = min(100, math.floor(max(0, spell_ranks - 13)/2))	
		else:
			spell_ranks  = int(effect.scaling_arr["Major Elemental"])		
			
		bonus = 20 + min(level, math.floor(max(0, spell_ranks - 13)/2))
		
		return [bonus, "Bolt AS"]					

	return [0, ""]	


# Temporal Revision (540) - +200 all DS	
def Calculate_540(effect, tag, level):
	if tag == "DS_All":				
		return [200, "All DS"]

	return [0, ""]	
		

# Ranger Base (600s)
		
# Natural Colors (601) - +10 all DS. +1 DS per seed 5 summation of Spiritual Lore, Blessings ranks	
def Calculate_601(effect, tag, level):
	if tag == "DS_All":					
		if effect.scaling_arr["Blessings"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Spiritual Lore, Blessings"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Blessings"])
		
		bonus = 10 + Get_Summation_Bonus(5, lore_ranks)	
		
		return [bonus, "All DS"]				
	
	return [0, ""]
	
		
# Resist Elements (602) - +10 fire/ice/electrical bolt DS. +1 fire/ice/electrical bolt DS when self-cast per seed 5 summation of Spiritual Lore, Blessings ranks	
def Calculate_602(effect, tag, level):
	if tag == "DS_Bolt":					
		if effect.scaling_arr["Blessings"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Spiritual Lore, Blessings"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Blessings"])
		
		bonus = 10 + Get_Summation_Bonus(5, lore_ranks)	
		
		return [bonus, "Bolt DS vs fire/cold/electric"]				
	
	return [0, ""]
		

# Phoen's Strength (606) - +10 melee AS, +10 UAF		
def Calculate_606(effect, tag, level):
	if tag == "AS_Melee":				
		return [10, "Melee AS"]
	elif tag == "UAF":				
		return [10, "UAF"]

	return [0, ""]
	
	
# Camouflage (608) - +30 AS, +30 UAF		
def Calculate_608(effect, tag, level):
	if tag == "AS_All":				
		return [30, "All AS"]
	elif tag == "UAF":				
		return [30, "UAF"]

	return [0, ""]		
		

# Self Control (613) - +20 melee DS, +20 Spiritual TD. +1 Spiritual TD per seed 5 summation of Spiritual Lore, Blessings ranks, +1 melee DS per 2 Spell Research, Ranger Base ranks above 13 capped at +63		
def Calculate_613(effect, tag, level):
	if tag == "DS_Melee":					
		if effect.scaling_arr["Ranger"] == "D":
			if level > 100:
				spell_ranks  = int(globals.character.skills_list["Spell Research, Ranger"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Ranger"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				spell_ranks = int(globals.character.skills_list["Spell Research, Ranger"].total_ranks_by_level[level].get())		
		else:
			spell_ranks  = int(effect.scaling_arr["Ranger"])
		
		bonus = 15 + math.floor(max(0, spell_ranks - 13)/2)	
		bonus = min(63, bonus)
		
		return [bonus, "Melee DS"]	
		
	elif tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":	
		if effect.scaling_arr["Blessings"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Spiritual Lore, Blessings"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Blessings"])
		
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
			
	return [0, ""]	
	
	
# Mobility (618) - +20 phantom Dodging ranks. +1 phantom Dodging rank per Spell Research, Ranger Base rank over 18
def Calculate_618(effect, tag, level):	
	if tag == "Skill_Phantom_Ranks_Dodging":	
		if effect.scaling_arr["Ranger"] == "D":
			if level > 100:			
				spell_ranks = int(globals.character.skills_list["Spell Research, Ranger"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Ranger"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
				level = 100
			else:
				spell_ranks = int(globals.character.skills_list["Spell Research, Ranger"].total_ranks_by_level[level].get())
		else:
			spell_ranks = int(effect.scaling_arr["Ranger"])				
			
		bonus = 20 + math.floor(max(0, spell_ranks - 18))	
		bonus = max(level, bonus)		
		
		return [bonus, "ranks"]

	return [0, ""]
	

# Nature's Touch (625) - +1 Spiritual TD. +1 Spiritual TD per 2 Spell Research, Ranger Base ranks over 25 up to a maximum of a +12 bonus to TD at 49 ranks
def Calculate_625(effect, tag, level):	
	if tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":
		if effect.scaling_arr["Ranger"] == "D":
			if level > 100:			
				spell_ranks = int(globals.character.skills_list["Spell Research, Ranger"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Ranger"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
				level = 100
			else:
				spell_ranks = int(globals.character.skills_list["Spell Research, Ranger"].total_ranks_by_level[level].get())
		else:
			spell_ranks = int(effect.scaling_arr["Ranger"])				
			
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

	return [0, ""]

	
# Wall of Thorns (640) - +20 DS
def Calculate_640(effect, tag, level):
	if tag == "DS_All":				
		return [20, "All DS"]
		
	return [0, ""]
		

# Assume Aspect (650) Bear - +20 increase to Constitution stat, +25 maximum Health. +1 increase to Constitution stat per seed 2 summation of Spiritual Lore, Blessings ranks, +1 max Health per seed 1 summation of Spiritual Lore, Summoning ranks
def Calculate_650_Bear(effect, tag, level):			
	if tag == "Statistic_Constitution":			
		if effect.scaling_arr["Blessings"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Spiritual Lore, Blessings"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Blessings"])
		
		bonus = 20 + Get_Summation_Bonus(2, lore_ranks)		
		
		return [bonus, "statistic increase"]				
		
	elif tag == "Resource_Maximum_Health":
		if effect.scaling_arr["Summoning"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Spiritual Lore, Summoning"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Spiritual Lore, Summoning"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Summoning"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Summoning"])
			
		bonus = 25 + Get_Summation_Bonus(1, lore_ranks)	
		
		return [bonus, "maximum health"]		
		
	return [0, ""]	
			
		
# Assume Aspect (650) Hawk - +20 Perception ranks. +1 Perception rank per seed 2 summation of Spiritual Lore, Summoning ranks
def Calculate_650_Hawk(effect, tag, level):	
	if tag == "Skill_Ranks_Perception":			
		if effect.scaling_arr["Summoning"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Spiritual Lore, Summoning"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Spiritual Lore, Summoning"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Summoning"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Summoning"])
		
		bonus = 20 + Get_Summation_Bonus(2, lore_ranks)		
		
		return [bonus, "skill ranks"]				

	return [0, ""]	
		

# Assume Aspect (650) Jackal - +20 Ambush ranks. +1 Ambush rank per seed 2 summation of Spiritual Lore, Summoning ranks
def Calculate_650_Jackal(effect, tag, level):	
	if tag == "Skill_Ranks_Ambush":			
		if effect.scaling_arr["Summoning"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Spiritual Lore, Summoning"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Spiritual Lore, Summoning"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Summoning"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Summoning"])
		
		bonus = 20 + Get_Summation_Bonus(2, lore_ranks)		
		
		return [bonus, "skill ranks"]				

	return [0, ""]	
	
	
# Assume Aspect (650) Lion - +20 increase to Influence and Strength stats. +1 Influence and Strength stats per seed 2 summation of Spiritual Lore, Blessings ranks
def Calculate_650_Lion(effect, tag, level):	
	if tag == "Statistic_Strength" or tag == "Statistic_Influence":			
		if effect.scaling_arr["Blessings"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Spiritual Lore, Blessings"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Blessings"])
		
		bonus = 20 + Get_Summation_Bonus(2, lore_ranks)		
		
		return [bonus, "statistic increase"]				

	return [0, ""]
	
	
# Assume Aspect (650) Owl - +20 increase to Aura and Wisdom stats. +1 increase to Aura and Wisdom stats per seed 2 summation of Spiritual Lore, Blessings ranks
def Calculate_650_Owl(effect, tag, level):	
	if tag == "Statistic_Aura" or tag == "Statistic_Wisdom":			
		if effect.scaling_arr["Blessings"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Spiritual Lore, Blessings"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Blessings"])
		
		bonus = 20 + Get_Summation_Bonus(2, lore_ranks)		
		
		return [bonus, "statistic increase"]				

	return [0, ""]
	
	
# Assume Aspect (650) Porcupine - +20 increase to Logic stat. +1 increase to Logic stat per seed 2 summation of Spiritual Lore, Blessings ranks
def Calculate_650_Porcupine(effect, tag, level):	
	if tag == "Statistic_Logic":			
		if effect.scaling_arr["Blessings"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Spiritual Lore, Blessings"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Blessings"])
		
		bonus = 20 + Get_Summation_Bonus(2, lore_ranks)		
		
		return [bonus, "statistic increase"]				

	return [0, ""]
		
		
# Assume Aspect (650) Rat - +20 increase to Agility and Discipline stats ranks. +1 increase to Agility and Discipline stats per seed 2 summation of Spiritual Lore, Blessings ranks
def Calculate_650_Rat(effect, tag, level):	
	if tag == "Statistic_Agility" or tag == "Statistic_Discipline":			
		if effect.scaling_arr["Blessings"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Spiritual Lore, Blessings"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Blessings"])
		
		bonus = 20 + Get_Summation_Bonus(2, lore_ranks)		
		
		return [bonus, "statistic increase"]				

	return [0, ""]		
		
		
# Assume Aspect (650) Wolf - +20 increase to Dexterity and Intuition stats\n+1 increase to Dexterity and Intuition stats per seed 2 summation of Spiritual Lore, Blessings ranks
def Calculate_650_Wolf(effect, tag, level):	
	if tag == "Statistic_Dexterity" or tag == "Statistic_Intuition":			
		if effect.scaling_arr["Blessings"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Spiritual Lore, Blessings"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Blessings"])
		
		bonus = 20 + Get_Summation_Bonus(2, lore_ranks)		
		
		return [bonus, "statistic increase"]				

	return [0, ""]	

	
# Sorcerer Base (700s)
	
# Cloak of Shadows (712) - +25 DS, +20 all TD. +1 all DS per Spell Research, Sorcerer Base rank above 12 capped at +88 DS (+113 total), +1 all TD per 10 Spell Research, Sorcerer Base ranks above 12 capped at +8 DS (+28 total)	
def Calculate_712(effect, tag, level):	
	if tag == "DS_All" or tag == "TD_All":
		if effect.scaling_arr["Sorcerer"] == "D":
			if level > 100:			
				spell_ranks = int(globals.character.skills_list["Spell Research, Sorcerer"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Sorcerer"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:
				spell_ranks = int(globals.character.skills_list["Spell Research, Sorcerer"].total_ranks_by_level[level].get())
		else:
			spell_ranks = int(effect.scaling_arr["Sorcerer"])				
			
		bonus = 0
		
		if tag == "DS_All":
			type = "All DS"
			bonus = math.floor(max(0, spell_ranks - 12))	
			bonus = min(113, 25 + bonus)		
		elif tag == "TD_All":
			type = "All TD"
			bonus = math.floor(max(0, spell_ranks - 12)/10)	
			bonus = min(28, 20 + bonus)				
		
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
		
		return [bonus, type]		

	return [0, ""]	


# Wizard Base (900s)
	
# Minor Elemental Edge (902) EVOKE - +10 skill bonus to a specific weapon type\n+1 skill bonus per seed 7 summation of Elemental Lore, Earth ranks	
def Calculate_902(effect, tag, level):
	if tag == "Skill_Bonus_Edged_Weapons" or tag == "Skill_Bonus_Blunt_Weapons" or tag == "Skill_Bonus_Two_Handed_Weapons" or tag == "Skill_Bonus_Polearm_Weapons" or tag == "Skill_Bonus_Brawling" or tag == "Skill_Bonus_Ranged_Weapons" or tag == "Skill_Bonus_Thrown_Weapons":	
		if effect.scaling_arr["Earth"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Elemental Lore, Earth"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Elemental Lore, Earth"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Elemental Lore, Earth"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Earth"])
		
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
			
		if effect.scaling_arr["Wizard"] == "D":
			if level > 100:
				spell_ranks  = int(globals.character.skills_list["Spell Research, Wizard"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Wizard"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				spell_ranks = int(globals.character.skills_list["Spell Research, Wizard"].total_ranks_by_level[level].get())		
		else:
			spell_ranks  = int(effect.scaling_arr["Wizard"])
		
		if effect.scaling_arr["Earth"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Elemental Lore, Earth"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Elemental Lore, Earth"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Elemental Lore, Earth"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Earth"])			
			
		bonus += math.floor(max(0, spell_ranks - 5)/4)	
		bonus += Get_Summation_Bonus(5, lore_ranks)	
				
		return [bonus, type]				
			
	return [0, ""]	
	

# Mass Blur (911) - +20 phantom Dodging ranks. +1 phantom Dodging rank for the caster only per seed 1 summation of Elemental Lore, Air ranks	
def Calculate_911(effect, tag, level):	
	if tag == "Skill_Phantom_Ranks_Dodging":	
		if effect.scaling_arr["Air"] == "D":
			if level > 100:			
				lore_ranks = int(globals.character.skills_list["Elemental Lore, Air"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Elemental Lore, Air"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:
				lore_ranks = int(globals.character.skills_list["Elemental Lore, Air"].total_ranks_by_level[level].get())
		else:
			lore_ranks = int(effect.scaling_arr["Air"])				
			
		bonus = 20 + Get_Summation_Bonus(1, lore_ranks)	
		
		return [bonus, "ranks"]

	return [0, ""]
	
	
# Melgorehn's Aura (913) - +10 DS, +20 Elemental TD. +1 DS per Spell Research, Wizard Base rank above 13 capped at character level. +1 Elemental TD per 3 Spell Research, Wizard Base ranks above 13 capped at character level.
def Calculate_913(effect, tag, level):	
	if tag == "DS_All" or tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":
		if effect.scaling_arr["Wizard"] == "D":
			if level > 100:
				spell_ranks  = int(globals.character.skills_list["Spell Research, Wizard"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Wizard"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
				level == 100
			else:				
				spell_ranks = int(globals.character.skills_list["Spell Research, Wizard"].total_ranks_by_level[level].get())		
		else:
			spell_ranks  = int(effect.scaling_arr["Wizard"])	
		
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

	return [0, ""]


# Wizard's Shield (919) - +50 DS
def Calculate_919(effect, tag, level):
	if tag == "DS_All":				
		return [50, "All DS"]
		
	return [0, ""]

	
# Bard Base (1000s)	
	
# Fortitude Song (1003) - +10 DS
def Calculate_1003(effect, tag, level):
	if tag == "DS_All":				
		return [10, "All DS"]
		
	return [0, ""]
	

# Kai's Triumph Song (1007) - +10 AS. +1 AS per Spell Research, Bard Base rank above 7 capped at +20. +1 all AS per seed 3 summation of Mental Lore, Telepathy ranks. Maximum AS provided is capped at +31
def Calculate_1007(effect, tag, level):
	if tag == "AS_All":	
		if effect.scaling_arr["Bard"] == "D":
			if level > 100:			
				spell_ranks = int(globals.character.skills_list["Spell Research, Bard"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Bard"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:
				spell_ranks = int(globals.character.skills_list["Spell Research, Bard"].total_ranks_by_level[level].get())
		else:
			spell_ranks = int(effect.scaling_arr["Bard"])

		if effect.scaling_arr["Telepathy"] == "D":
			if level > 100:			
				lore_ranks = int(globals.character.skills_list["Mental Lore, Telepathy"].total_ranks_by_level[100].get())
				lore_ranks  += globals.character.skills_list["Mental Lore, Telepathy"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:
				lore_ranks = int(globals.character.skills_list["Mental Lore, Telepathy"].total_ranks_by_level[level].get())	
		else:
			lore_ranks = int(effect.scaling_arr["Telepathy"])				
		
		bonus = Get_Summation_Bonus(3, lore_ranks)
		bonus += min(20, max(0, spell_ranks-7))
		bonus = min(31, 10 + bonus)
		
		return [bonus, "All AS"]
		
	return [0, ""]	


# Song of Valor (1010) - +10 DS. +1 DS per 2 Spell Research, Bard Base ranks above 10
def Calculate_1010(effect, tag, level):
	if tag == "DS_All":				
		if effect.scaling_arr["Bard"] == "D":
			if level > 100:
				spell_ranks  = int(globals.character.skills_list["Spell Research, Bard"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Bard"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				spell_ranks = int(globals.character.skills_list["Spell Research, Bard"].total_ranks_by_level[level].get())	
		else:
			spell_ranks = int(effect.scaling_arr["Bard"])	
			
		bonus = 10 + math.floor((max(0, spell_ranks - 10)/2))

		return [bonus, "All DS"]			
		
	return [0, ""]

	
# Song of Mirrors (1019) - +20 phantom Dodging ranks. +1 phantom Dodging rank per 2 Spell Research, Bard Base ranks over 19
def Calculate_1019(effect, tag, level):
	if tag == "Skill_Phantom_Ranks_Dodging":				
		if effect.scaling_arr["Bard"] == "D":
			if level > 100:
				spell_ranks  = int(globals.character.skills_list["Spell Research, Bard"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Bard"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				spell_ranks = int(globals.character.skills_list["Spell Research, Bard"].total_ranks_by_level[level].get())		
		else:
			spell_ranks = int(effect.scaling_arr["Bard"])	
			
		bonus = 20 + math.floor((max(0, spell_ranks - 19)/2))

		return [bonus, "ranks"]
		
	return [0, ""]


# Song of Tonis (1035) - +20 phantom Dodging ranks, -1 Haste effect\n+1 phantom Dodging rank at the following Elemental Lore, Air rank inverals: 1,2,3,5,8,10,14,17,21,26,31,36,42,49,55,63,70,78,87,96. Haste effect improves to -2 at Elemental Lore, Air rank 30 and -3 at Elemental Lore, Air rank 75. The bonus is +1 second per rank for the first 20 ranks of ML, Telepathy.
def Calculate_1035(effect, tag, level):
	if tag == "Skill_Phantom_Ranks_Dodging":				
		if effect.scaling_arr["Air"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Elemental Lore, Air"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Elemental Lore, Air"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Elemental Lore, Air"].total_ranks_by_level[level].get())	
		else:
			spell_ranks = int(effect.scaling_arr["Air"])		
		
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
		
	return [0, ""]
	
	
# Empath Base (1100s)

# Empathic Focus (1109) = +15 Spiritual TD, +25 all DS, +15 melee AS. +1 all DS per 2 Spell Research, Empath Base ranks above 9.
def Calculate_1109(effect, tag, level):		
	if tag == "DS_All":
		if effect.scaling_arr["Empath"] == "D":
			if level > 100:
				spell_ranks  = int(globals.character.skills_list["Spell Research, Empath"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Empath"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
				level == 100
			else:				
				spell_ranks = int(globals.character.skills_list["Spell Research, Empath"].total_ranks_by_level[level].get())		
		else:
			spell_ranks  = int(effect.scaling_arr["Empath"])			
					
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

	return [0, ""]
	

# Strength of Will (1119) - +12 DS, 12 Spirtual TD. +1 DS and Spiritual TD per 3 Spell Research, Empath Base ranks above 19.
def Calculate_1119(effect, tag, level):
	if tag == "DS_All" or tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":		
		if effect.scaling_arr["Empath"] == "D":
			if level > 100:
				spell_ranks  = int(globals.character.skills_list["Spell Research, Empath"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Empath"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				spell_ranks = int(globals.character.skills_list["Spell Research, Empath"].total_ranks_by_level[level].get())		
		else:
			spell_ranks  = int(effect.scaling_arr["Empath"])			
					
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
		
	return [0, ""]
	

# Intensity (1130) - +20 DS, +20 AS. +1 AS/DS per 2 Spell Research, Empath Base ranks above 30
def Calculate_1130(effect, tag, level):
	if tag == "AS_All" or tag == "UAF" or tag == "DS_All":	
		if effect.scaling_arr["Empath"] == "D":
			if level > 100:
				spell_ranks  = int(globals.character.skills_list["Spell Research, Empath"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Empath"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
				level == 100
			else:				
				spell_ranks = int(globals.character.skills_list["Spell Research, Empath"].total_ranks_by_level[level].get())		
		else:
			spell_ranks  = int(effect.scaling_arr["Empath"])			
					
		bonus = math.floor(max(0, spell_ranks - 30)/2)		
		bonus = min(level, 20 + bonus)
		
		if tag == "AS_All":	
			type = "All AS"	
		elif tag == "DS_All":				
			type = "All DS"		
		elif tag == "UAF":			
			type = "UAF"		
			
		return [bonus, type]

	return [0, ""]

	
# Minor Mental (1200s)

# Foresight (1204) - +10 melee and ranged DS
def Calculate_1204(effect, tag, level):
	if tag == "DS_Melee":				
		return [10, "Melee DS"]
	elif tag == "DS_Ranged":				
		return [10, "Ranged DS"]
		
	return [0, ""]


# Mindward (1208) - +20 Mental TD\n+1 Mental TD 2 Spell Research, Minor Mental ranks above 8 to a maximum of +40	
def Calculate_1208(effect, tag, level):
	if tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":
		if effect.scaling_arr["Minor Mental"] == "D":
			if level > 100:
				spell_ranks  = int(globals.character.skills_list["Spell Research, Minor Mental"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Minor Mental"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				spell_ranks = int(globals.character.skills_list["Spell Research, Minor Mental"].total_ranks_by_level[level].get())		
		else:
			spell_ranks  = int(effect.scaling_arr["Minor Mental"])		
			
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
		
	return [0, ""]

	
# Dragonclaw (1209) - +10 UAF
def Calculate_1209(effect, tag, level):
	if tag == "UAF":				
		if effect.scaling_arr["Transformation"] == "D":
			if level > 100:			
				lore_ranks = int(globals.character.skills_list["Mental Lore, Transformation"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Mental Lore, Transformation"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:
				lore_ranks = int(globals.character.skills_list["Mental Lore, Transformation"].total_ranks_by_level[level].get())
		else:
			lore_ranks = int(effect.scaling_arr["Transformation"])				
			
		bonus = 10 + Get_Summation_Bonus(1, lore_ranks)	
		
		return [bonus, "UAF"]
		
	return [0, ""]


# Focus Barrier (1216) - +30 DS
def Calculate_1216(effect, tag, level):
	if tag == "DS_All":				
		return [30, "All DS"]
		
	return [0, ""]
	
# Premonition (1220) - +20 DS. +1 all DS per 2 Spell Research, Minor Mental ranks above 20	
def Calculate_1220(effect, tag, level):
	if tag == "DS_All":				
		if effect.scaling_arr["Minor Mental"] == "D":
			if level > 100:
				spell_ranks  = int(globals.character.skills_list["Spell Research, Minor Mental"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Minor Mental"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
				level = 100
			else:				
				spell_ranks = int(globals.character.skills_list["Spell Research, Minor Mental"].total_ranks_by_level[level].get())		
		else:
			spell_ranks = int(effect.scaling_arr["Minor Mental"])	

		bonus = math.floor(max(0, spell_ranks - 20)/2)		
		bonus = min(level, 20 + bonus)
		
		return [bonus, "All DS"]
		
	return [0, ""]


# Paladin Base (1600s)	

# Mantle of Faith (1601) +5 DS, +5 Spiritual TD. +1 DS and Spiritual TD per seed 2 summation of Spiritual Lore, Blessings ranks
def Calculate_1601(effect, tag, level):
	if tag == "DS_All" or tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":				
		if effect.scaling_arr["Blessings"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Spiritual Lore, Blessings"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Blessings"])
		
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
		
	return [0, ""]	
	
	
# Dauntless (1606) - +10 AS
def Calculate_1606(effect, tag, level):
	if tag == "AS_Melee":				
		return [10, "Melee AS"]
	elif tag == "UAF":				
		return [10, "UAF"]

	return [0, ""]
	

# Higher Vision (1610) - +10 DS. +1 DS per 2 Spell Research, Paladin Base ranks above 10 to a maximum of +20, +1 DS per seed 5 summation of Spiritual Lore, Religion ranks	
def Calculate_1610(effect, tag, level):
	if tag == "DS_All":				
		if effect.scaling_arr["Paladin"] == "D":
			if level > 100:
				spell_ranks  = int(globals.character.skills_list["Spell Research, Paladin"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Paladin"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				spell_ranks = int(globals.character.skills_list["Spell Research, Paladin"].total_ranks_by_level[level].get())		
		else:
			spell_ranks = int(effect.scaling_arr["Paladin"])	

		bonus = 10 + math.floor(max(0, spell_ranks - 10)/2)		
		bonus = min(20, bonus)
		
		if effect.scaling_arr["Religion"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Spiritual Lore, Religion"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Spiritual Lore, Religion"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Religion"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Religion"])
		
		bonus += Get_Summation_Bonus(5, lore_ranks)		
		
		return [bonus, "All DS"]
		
	return [0, ""]
	

# Patron's Blessing (1611) - +10 phantom Combat Maneuver ranks. +1 Combat Maneuver rank per seed 3 summation of Spiritual Lore, Blessings ranks. +0.75 Combat Maneuver rank per 2 Spell Research, Paladin Base rank above 11	
def Calculate_1611(effect, tag, level):	
	if tag == "Skill_Phantom_Ranks_Combat_Maneuvers":	
		if effect.scaling_arr["Paladin"] == "D":
			if level > 100:			
				spell_ranks = int(globals.character.skills_list["Spell Research, Paladin"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Paladin"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:
				spell_ranks = int(globals.character.skills_list["Spell Research, Paladin"].total_ranks_by_level[level].get())
		else:
			spell_ranks = int(effect.scaling_arr["Paladin"])

		if effect.scaling_arr["Blessings"] == "D":
			if level > 100:			
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[100].get())
				lore_ranks  += globals.character.skills_list["Spiritual Lore, Blessings"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[level].get())	
		else:
			lore_ranks = int(effect.scaling_arr["Blessings"])				
		
		bonus = 10
		bonus += Get_Summation_Bonus(3, lore_ranks) 
		bonus += math.floor(0.75 * max(0, spell_ranks-11))
		
		return [bonus, "ranks"]

	return [0, ""]
	

# Champion's Might (1612) - +15 Spiritual CS. +1 Spiritual CS per 1 Spell Research, Paladin Base rank above 12 to a maximum of +10 (+25 total)	
def Calculate_1612(effect, tag, level):
	if tag == "CS_Elemental" or tag == "CS_Mental" or tag == "CS_Spiritual" or tag == "CS_Sorcerer":	
		if effect.scaling_arr["Paladin"] == "D":
			if level > 100:			
				spell_ranks = int(globals.character.skills_list["Spell Research, Paladin"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Paladin"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:
				spell_ranks = int(globals.character.skills_list["Spell Research, Paladin"].total_ranks_by_level[level].get())
		else:
			spell_ranks = int(effect.scaling_arr["Paladin"])

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

	return [0, ""]


# Guard the Meek (1613) Group - +15 melee DS. +1 melee DS per 5 Spell Research, Paladin Base ranks above 18 to a maximum of +20. 
def Calculate_1613_Group(effect, tag, level):
	if tag == "DS_Melee":				
		if effect.scaling_arr["Paladin"] == "D":
			if level > 100:			
				spell_ranks = int(globals.character.skills_list["Spell Research, Paladin"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Paladin"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:
				spell_ranks = int(globals.character.skills_list["Spell Research, Paladin"].total_ranks_by_level[level].get())
		else:
			spell_ranks = int(effect.scaling_arr["Paladin"])

		bonus = math.floor(max(0, spell_ranks - 13)/5)		
		bonus = min(20, 15 + bonus)
		
		return [bonus, "Melee DS"]
		
	return [0, ""]

	
# Guard the Meek (1613) Self - +15 melee DS. +1 all DS per seed 6 summation of Spiritual Lore, Blessings ranks (max of +5 at 40 ranks)
def Calculate_1613_Self(effect, tag, level):
	if tag == "DS_Melee":							
		if effect.scaling_arr["Blessings"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Spiritual Lore, Blessings"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Blessings"].total_ranks_by_level[level].get())		
		else:
			lore_ranks = int(effect.scaling_arr["Blessings"])	

		bonus = Get_Summation_Bonus(6, lore_ranks)
		bonus = min(20, 15 + bonus)
		
		return [bonus, "Melee DS"]
		
	return [0, ""]
	
	
# Zealot (1617)	- +30 melee AS, -30 DS. +1 melee AS and -1 all DS per seed 1 summation of Spiritual Lore, Religion ranks
def Calculate_1617(effect, tag, level):
	if tag == "AS_Melee" or tag == "DS_All":	
		if effect.scaling_arr["Religion"] == "D":
			if level > 100:			
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Religion"].total_ranks_by_level[100].get())
				lore_ranks  += globals.character.skills_list["Spiritual Lore, Religion"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Religion"].total_ranks_by_level[level].get())	
		else:
			lore_ranks = int(effect.scaling_arr["Religion"])	
			
		bonus = 30 + Get_Summation_Bonus(1, lore_ranks)
		
		if tag == "AS_Melee":	
			return [bonus, "Melee AS"]
		elif tag == "DS_All":
			return [ -1 * bonus, "All DS"]

	return [0, ""]
	
	
# Faith Shield (1619) - +50 Spiritual TD. +3 Spiritual TD per seed 5 summation of Spiritual Lore, Religion ranks.	
def Calculate_1619(effect, tag, level):
	if tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":
		if effect.scaling_arr["Religion"] == "D":
			if level > 100:			
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Religion"].total_ranks_by_level[100].get())
				lore_ranks  += globals.character.skills_list["Spiritual Lore, Religion"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:
				lore_ranks = int(globals.character.skills_list["Spiritual Lore, Religion"].total_ranks_by_level[level].get())	
		else:
			lore_ranks = int(effect.scaling_arr["Religion"])	

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

		
# Arcane (1700s)		

# Mystic Focus (1711) - +10 CS		
def Calculate_1711(effect, tag, level):
	if tag == "CS_All":				
		return [10, "All CS"]
		
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
	
# Berserk - AS bonus equal to (guild/cman ranks - 1 + (level/4) - 20) / 2. Max AS bonus is +29
def Calculate_Berserk(effect, tag, level):
	if tag == "AS_Melee":	
		if effect.scaling_arr["Maneuver ranks"] == "D" and "Berserk" in globals.character.combat_maneuvers_list:
			man = globals.character.combat_maneuvers_list["Berserk"]		
			
			if level > 100:			
				cman_ranks = int(man.total_ranks_by_level[100].get())
				cman_ranks += int(man.Postcap_Get_Total_Ranks_Closest_To_Interval(level))
			else:		
				cman_ranks = int(man.total_ranks_by_level[level].get())
		else:			
			cman_ranks = int(effect.scaling_arr["Maneuver ranks"])	

			
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
		if effect.scaling_arr["Maneuver ranks"] == "D" and "Burst of Swiftness" in globals.character.combat_maneuvers_list:
			man = globals.character.combat_maneuvers_list["Burst of Swiftness"]		
			
			if level > 100:			
				ranks = int(man.total_ranks_by_level[100].get())
				ranks += int(man.Postcap_Get_Total_Ranks_Closest_To_Interval(level))
			else:		
				ranks = int(man.total_ranks_by_level[level].get())
		else:			
			ranks = int(effect.scaling_arr["Maneuver ranks"])
			
		if 0 < ranks < 6:
			if tag == "Statistic_Bonus_Agility":
				return [6 + (2 * ranks), "Burst of Swiftness"]		
			else:	
				return [3 + ranks, "Burst of Swiftness"]
			
	return [0, ""]		
	
	
# Combat Focus - +2 all TD per rank	
def Calculate_Combat_Focus(effect, tag, level):
	if tag == "TD_All":	
		if effect.scaling_arr["Maneuver ranks"] == "D" and "Combat Focus" in globals.character.combat_maneuvers_list:
			man = globals.character.combat_maneuvers_list["Combat Focus"]		
			
			if level > 100:			
				ranks = int(man.total_ranks_by_level[100].get())
				ranks += int(man.Postcap_Get_Total_Ranks_Closest_To_Interval(level))
			else:		
				ranks = int(man.total_ranks_by_level[level].get())
		else:			
			ranks = int(effect.scaling_arr["Maneuver ranks"])			

		return [2 * ranks, "All TD"]	
			
	return [0, ""]	
	
	
# Combat Movement - +2 all DS per rank	
def Calculate_Combat_Movement(effect, tag, level):
	if tag == "DS_Melee" or tag == "DS_Ranged":	
		if effect.scaling_arr["Maneuver ranks"] == "D" and "Combat Movement" in globals.character.combat_maneuvers_list:
			man = globals.character.combat_maneuvers_list["Combat Movement"]		
			
			if level > 100:			
				ranks = int(man.total_ranks_by_level[100].get())
				ranks += int(man.Postcap_Get_Total_Ranks_Closest_To_Interval(level))
			else:		
				ranks = int(man.total_ranks_by_level[level].get())
		else:			
			ranks = int(effect.scaling_arr["Maneuver ranks"])
			
		if tag == "DS_Melee":
			type = "Melee DS"
		elif tag == "DS_Ranged":
			type = "Ranged DS"
			
		return [2 * ranks, type]	
			
	return [0, ""]	
	
	
# Coup de Grace (Buff) - +10 to +40 AS	
def Calculate_Coup_de_Grace_Buff(effect, tag, level):
	if tag == "AS_All":
		return [int(effect.scaling_arr["All AS Bonus"]), "All AS"]	

	return [0, ""]	

	
# Perfect Self - +2/+4/+6/+8/+10 to all statistic bonuses	
def Calculate_Perfect_Self(effect, tag, level):
	if tag == "Statistic_Bonus_Strength" or tag == "Statistic_Bonus_Constitution" or tag == "Statistic_Bonus_Dexterity" or tag == "Statistic_Bonus_Agility" or tag == "Statistic_Bonus_Discipline" or tag == "Statistic_Bonus_Aura" or tag == "Statistic_Bonus_Logic" or tag == "Statistic_Bonus_Intuition" or tag == "Statistic_Bonus_Wisdom" or tag == "Statistic_Bonus_Influence":	
		if effect.scaling_arr["Maneuver ranks"] == "D" and "Perfect Self" in globals.character.combat_maneuvers_list:
			man = globals.character.combat_maneuvers_list["Perfect Self"]		
			
			if level > 100:			
				ranks = int(man.total_ranks_by_level[100].get())
				ranks += int(man.Postcap_Get_Total_Ranks_Closest_To_Interval(level))
			else:		
				ranks = int(man.total_ranks_by_level[level].get())
		else:			
			ranks = int(effect.scaling_arr["Maneuver ranks"])			
		
		return [2 * ranks, "Perfect Self"]
			
	return [0, ""]
	
	
# Shield Swiftness - +0.04 increase per rank to Shield Factor when using a Small or Medium shield	
def Calculate_Shield_Swiftness(effect, tag, level):
	if tag == "Shield_Factor":	
		if effect.scaling_arr["Maneuver ranks"] == "D" and "Shield Swiftness" in globals.character.shield_maneuvers_list:
			man = globals.character.shield_maneuvers_list["Shield Swiftness"]	
			
			if level > 100:			
				ranks = int(man.total_ranks_by_level[100].get())
				ranks += int(man.Postcap_Get_Total_Ranks_Closest_To_Interval(level))
			else:		
				ranks = int(man.total_ranks_by_level[level].get())
				
		else:			
			ranks = int(effect.scaling_arr["Maneuver ranks"])
			
		return [0.04 * ranks, "shield factor"]
			
	return [0, ""]
	
	
# Specialization I - +2 AS per rank	
def Calculate_Specialization_I(effect, tag, level):
	if tag == "AS_Melee" or tag == "AS_Ranged" or tag == "UAC":	
		if effect.scaling_arr["Maneuver ranks"] == "D" and "Specialization I" in globals.character.combat_maneuvers_list:
			man = globals.character.combat_maneuvers_list["Specialization I"]		
			
			if level > 100:			
				ranks = int(man.total_ranks_by_level[100].get())
				ranks += int(man.Postcap_Get_Total_Ranks_Closest_To_Interval(level))
			else:		
				ranks = int(man.total_ranks_by_level[level].get())
		else:			
			ranks = int(effect.scaling_arr["Maneuver ranks"])			

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
		if effect.scaling_arr["Maneuver ranks"] == "D" and "Specialization I" in globals.character.combat_maneuvers_list:
			man = globals.character.combat_maneuvers_list["Specialization I"]		
			
			if level > 100:			
				ranks = int(man.total_ranks_by_level[100].get())
				ranks += int(man.Postcap_Get_Total_Ranks_Closest_To_Interval(level))
			else:		
				ranks = int(man.total_ranks_by_level[level].get())
		else:			
			ranks = int(effect.scaling_arr["Maneuver ranks"])			

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
		if effect.scaling_arr["Maneuver ranks"] == "D" and "Specialization I" in globals.character.combat_maneuvers_list:
			man = globals.character.combat_maneuvers_list["Specialization I"]		
			
			if level > 100:			
				ranks = int(man.total_ranks_by_level[100].get())
				ranks += int(man.Postcap_Get_Total_Ranks_Closest_To_Interval(level))
			else:		
				ranks = int(man.total_ranks_by_level[level].get())
		else:			
			ranks = int(effect.scaling_arr["Maneuver ranks"])			

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
		if effect.scaling_arr["Maneuver ranks"] == "D" and "Spin Attack" in globals.character.combat_maneuvers_list:
			man = globals.character.combat_maneuvers_list["Spin Attack"]		
			
			if level > 100:			
				ranks = int(man.total_ranks_by_level[100].get())
				ranks += int(man.Postcap_Get_Total_Ranks_Closest_To_Interval(level))
			else:		
				ranks = int(man.total_ranks_by_level[level].get())
		else:			
			ranks = int(effect.scaling_arr["Maneuver ranks"])
					
		if tag == "AS_Melee":
			type = "Melee AS"	
		elif tag == "Skill_Bonus_Dodging":
			type = "skill bonus"
			
		return [3 * ranks, type]
			
	return [0, ""]	
	
	
# Surge of Strength - +8/+10/+12/+14/+16 increase to Strength bonus	
def Calculate_Surge_of_Strength(effect, tag, level):
	if tag == "Statistic_Bonus_Strength":	
		if effect.scaling_arr["Maneuver ranks"] == "D" and "Surge of Strength" in globals.character.combat_maneuvers_list:
			man = globals.character.combat_maneuvers_list["Surge of Strength"]		
			
			if level > 100:			
				ranks = int(man.total_ranks_by_level[100].get())
				ranks += int(man.Postcap_Get_Total_Ranks_Closest_To_Interval(level))
			else:		
				ranks = int(man.total_ranks_by_level[level].get())
		else:			
			ranks = int(effect.scaling_arr["Maneuver ranks"])
			
		if 0 < ranks < 6:
			return [6 + (2 * ranks), "Surge of Strength"]
			
	return [0, ""]
	
	
# War Cries - Seanette's Shout - +15 AS to group but not to self
def Calculate_War_Cries_Shout(effect, tag, level):
	if tag == "AS_All":				
		return [15, "All AS"]

	return [0, ""]	
	
	
# War Cries - Horland's Holler - +20 AS to group including self
def Calculate_War_Cries_Holler(effect, tag, level):
	if tag == "AS_All":				
		return [20, "All AS"]

	return [0, ""]	
	
	
# Weapon Bonding - +2 AS per rank	
def Calculate_Weapon_Bonding(effect, tag, level):
	if tag == "AS_Melee" or tag == "AS_Ranged" or tag == "UAC":	
		if effect.scaling_arr["Maneuver ranks"] == "D" and "Weapon Bonding" in globals.character.combat_maneuvers_list:
			man = globals.character.combat_maneuvers_list["Weapon Bonding"]		
			
			if level > 100:			
				ranks = int(man.total_ranks_by_level[100].get())
				ranks += int(man.Postcap_Get_Total_Ranks_Closest_To_Interval(level))
			else:		
				ranks = int(man.total_ranks_by_level[level].get())
		else:			
			ranks = int(effect.scaling_arr["Maneuver ranks"])

		if tag == "AS_Melee":
			type = "Melee AS"	
		elif tag == "AS_Ranged":
			type = "Ranged AS"
		elif tag == "UAC": 
			type = "UAC"		
			
		return [2 * ranks, type]
			
	return [0, ""]


# Society Powers
	
# Sigil of Defense - +1  DS per GoS rank	
def Calculate_Sigil_of_Defense(effect, tag, level):
	if tag == "DS_All":	
		if effect.scaling_arr["GoS rank"] == "D":
			if globals.character.society.get() == "Guardians of Sunfist":
				bonus = int(globals.character.society_rank.get())
			else:
				bonus = 0
		else:			
			bonus = int(effect.scaling_arr["GoS rank"])
			
		return [bonus, "All DS"]

	return [0, ""]
	
	
# Sigil of Offense - +1 AS/UAF per GoS rank	
def Calculate_Sigil_of_Offense(effect, tag, level):
	if tag == "AS_All" or tag == "UAF":	
		if effect.scaling_arr["GoS rank"] == "D":
			if globals.character.society.get() == "Guardians of Sunfist":
				bonus = int(globals.character.society_rank.get())
			else:
				bonus = 0
		else:			
			bonus = int(effect.scaling_arr["GoS rank"])
			
		if tag == "AS_All":
			type = "All AS"
		elif tag == "UAF":
			type = "UAF"
		
		return [bonus, type]

	return [0, ""]
	
	
# Sigil of Focus - +1 TD per GoS rank		
def Calculate_Sigil_of_Focus(effect, tag, level):
	if tag == "TD_All":	
		if effect.scaling_arr["GoS rank"] == "D":
			if globals.character.society.get() == "Guardians of Sunfist":
				bonus = int(globals.character.society_rank.get())
			else:
				bonus = 0
		else:			
			bonus = int(effect.scaling_arr["GoS rank"])
			
		return [bonus, "All TD"]

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
		if effect.scaling_arr["Voln rank"] == "D":
			if globals.character.society.get() == "Order of Voln":
				bonus = int(globals.character.society_rank.get())
			else:
				bonus = 0
		else:			
			bonus = int(effect.scaling_arr["Voln rank"])
			
		return [bonus, "All AS"]

	return [0, ""]
	
	
# Symbol of Protection - +1 DS per Voln rank\n+1 TD per 2 Voln ranks	
def Calculate_Symbol_of_Protection(effect, tag, level):
	if tag == "DS_All":	
		if effect.scaling_arr["Voln rank"] == "D":
			if globals.character.society.get() == "Order of Voln":
				bonus = int(globals.character.society_rank.get())
			else:
				bonus = 0
		else:			
			bonus = int(effect.scaling_arr["Voln rank"])
			
		return [bonus, "All DS"]
		
	elif tag == "TD_All":	
		if effect.scaling_arr["Voln rank"] == "D":
			if globals.character.society.get() == "Order of Voln":
				bonus = math.floor(int(globals.character.society_rank.get())/2)
			else:
				bonus = 0
		else:			
			bonus = math.floor(int(effect.scaling_arr["Voln rank"])/2)
			
		return [bonus, "All TD"]

	return [0, ""]
	
	
# Symbol of Supremecy - +1 bonus per two Voln ranks to AS/CS,CMAN, UAF against undead creatures	
def Calculate_Symbol_of_Supremecy(effect, tag, level):
	if tag == "AS_All" or tag == "UAF" or tag == "CS_All":	
		if effect.scaling_arr["Voln rank"] == "D":
			if globals.character.society.get() == "Order of Voln":
				bonus = math.floor(int(globals.character.society_rank.get()) / 2)
			else:
				bonus = 0
		else:			
			bonus = math.floor(int(effect.scaling_arr["Voln rank"]) / 2)
				
		if tag == "AS_All":
			return [bonus, "All AS vs Undead"]	
		elif tag == "CS_All":
			return [bonus, "All CS vs Undead"]
		elif tag == "UAF":
			return [bonus, "UAF vs Undead"]

	return [0, ""]

	
	
# Skill Enhansives

	
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
	
	
# Status Effects	
	
# Kneeling - -50 all AS and DS, +30 ranged AS if using a crossbow
def Calculate_Kneeling(effect, tag, level):
	if tag == "AS_All":				
		return [-50, "All AS"]
	elif tag == "DS_All":				
		return [-50, "All DS"]

	return [0, ""]

	
# Lying_Down - -50 AS and DS
def Calculate_Lying_Down(effect, tag, level):
	if tag == "AS_All":				
		return [-50, "All AS"]
	elif tag == "DS_All":				
		return [-50, "All DS"]

	return [0, ""]
	
	
# Overexerted - -10 AS	
def Calculate_Overexerted(effect, tag, level):
	if tag == "AS_All":				
		return [-10, "All AS"]

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
		return [5 * int(effect.scaling_arr["Acuity tier"]), "Bolt AS"]	
		
	return [0, ""]	
	
	
# Acuity CS Flare - +3 bonus to all CS on next cast per tier
def Calculate_Acuity_CS_Flare(effect, tag, level):
	if tag == "CS_All":
		return [3 * int(effect.scaling_arr["Acuity tier"]), "All CS"]	
		
	return [0, ""]			
	

# Ensorcell AS Flare - +5/+10/+15/+20/+25 bonus to AS on next melee, ranged, UAF attack	
def Calculate_Ensorcell_AS_Flare(effect, tag, level):
	if tag == "AS_All":
		return [5 * int(effect.scaling_arr["Ensorcell tier"]), "All AS"]	
		
	return [0, ""]	
	

# Ensorcell CS Flare - +5/+10/+15/+20/+25 bonus to CS	
def Calculate_Ensorcell_CS_Flare(effect, tag, level):
	if tag == "CS_All":
		return [5 * int(effect.scaling_arr["Ensorcell tier"]), "All CS"]	
		
	return [0, ""]	
	
	
# Spirit Warding II (107) Flare - +25 Spiritual TD	
def Calculate_107_Flare(effect, tag, level):
	if tag == "TD_Elemental" or tag == "TD_Mental" or tag == "TD_Spiritual" or tag == "TD_Sorcerer":
		bonus = 25
		
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
		if effect.scaling_arr["Fire"] == "D":
			if level > 100:
				lore_ranks  = int(globals.character.skills_list["Elemental Lore, Fire"].total_ranks_by_level[100].get())
				lore_ranks += globals.character.skills_list["Elemental Lore, Fire"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)
			else:				
				lore_ranks = int(globals.character.skills_list["Elemental Lore, Fire"].total_ranks_by_level[level].get())		
		else:
			lore_ranks  = int(effect.scaling_arr["Fire"])
		
		bonus = min(25, Get_Summation_Bonus(4, lore_ranks))
		
		return [bonus, "Bolt AS"]					

	return [0, ""]	
	
	
# Curse (715) Star - +10 bolt AS. +1 bolt AS per 3 Spell Research, Sorcerer ranks above 15, capped character level	
def Calculate_715_Flare(effect, tag, level):
	if tag == "AS_Bolt":		
		if effect.scaling_arr["Sorcerer"] == "D":
			if level > 100:
				spell_ranks = int(globals.character.skills_list["Spell Research, Sorcerer"].total_ranks_by_level[100].get())
				spell_ranks += globals.character.skills_list["Spell Research, Sorcerer"].Postcap_Get_Total_Ranks_Closest_To_Interval(level)			
			else:	
				spell_ranks = int(globals.character.skills_list["Spell Research, Sorcerer"].total_ranks_by_level[level].get())		
			bonus = min(100, 10 + math.floor(max(0, spell_ranks - 15)/3))
		else:
			spell_ranks  = int(effect.scaling_arr["Sorcerer"])			
			
		bonus = min(level, 10 + math.floor(max(0, spell_ranks - 15)/3))		
	
		return [bonus, "Bolt AS"]

	return [0, ""]		

	
# Other Effects	

# Room - Bright - -10 DS	
def Calculate_Room_Bright(effect, tag, level):
	if tag == "DS_All":				
		return [-10, "All DS"]

	return [0, ""]	

	
# Room - Bright - +20 DS		
def Calculate_Room_Dark(effect, tag, level):
	if tag == "DS_All":				
		return [20, "All DS"]

	return [0, ""]	

	
# Room - Foggy - +30 DS		
def Calculate_Room_Foggy(effect, tag, level):
	if tag == "DS_All":				
		return [30, "All DS"]

	return [0, ""]	
	
