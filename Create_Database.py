# This script is run outside of the Planner to create a sqlite database that the Planner needs to run.
# The database can be called from the Planner and contains all the relevant information about the following:
#  Races
#  Professions
#  Skills
#  Maneuvers

#!/usr/bin/python

import sys
import sqlite3

con = sqlite3.connect("GS4_Planner.db")
cur = con.cursor()

# Check to see if the database already exists. If it does, exit the program.
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Races';")
data = cur.fetchone()

if data != None:
	print("Database already exists. Exiting...")  
	sys.exit(1)
	
	
# Creates the Races table. This will contain all the known information about every race in GS4
cur.execute("CREATE TABLE Races (name, manauever_bonus, max_health, health_regen, spirit_regen, decay_timer, encumberance_factor, weight_factor, elemental_td, mental_td, spiritual_td, sorc_td, poison_td, disease_td, strength_bonus, constitution_bonus, dexterity_bonus, agility_bonus, discipline_bonus, aura_bonus, logic_bonus, intuition_bonus, wisdom_bonus, influence_bonus, strength_adj, constitution_adj, dexterity_adj, agility_adj, discipline_adj, aura_adj, logic_adj, intuition_adj, wisdom_adj, influence_adj)")
   
cur.execute("INSERT INTO Races VALUES('Aelotoi', 'good', 120, 1, 1, 10, 0.75, 0.65, 0, 0, 0, 0, 0, 0,  -5, 0, 5, 10, 5, 0, 5, 5, 0, -5,  0, -2, 3, 3, 2, 0, 0, 2, 0, -2) ")
cur.execute("INSERT INTO Races VALUES('Burghal Gnome', 'best', 90, 1, 1, 14, 0.78, 0.7, 0, 0, 0, 0, 0, 0,  -15, 10, 10, 10, -5, 5, 10, 5, 0, -5,  -5, 0, 3, 3, -3, -2, 5, 5, 0, 0) ")
cur.execute("INSERT INTO Races VALUES('Dark Elf', 'good', 120, 1, 1, 10, 0.84, 0.75, -5, 0, -5, -5, 10, 100,  0, -5, 10, 5, -10, 10, 0, 5, 5, -5,  0, -2, 5, 5, -2, 0, 0, 0, 0, 0) ")
cur.execute("INSERT INTO Races VALUES('Dwarf', 'average', 140, 3, 2, 16, 0.8, 0.75, 30, 0, 0, 15, 20, 15,  10, 15, 0, -5, 10, -10, 5, 0, 0, -10,  5, 5, -3, -5, 3, 0, 0, 0, 3, -2) ")
cur.execute("INSERT INTO Races VALUES('Elf', 'excellent', 130, 1, 1, 10, 0.78, 0.7, -5, 0, -5, -5, 10, 100,  0, 0, 5, 15, -15, 5, 0, 0, 0, 10,  0, -5, 5, 3, -5, 5, 0, 0, 0, 3) ")
cur.execute("INSERT INTO Races VALUES('Erithian', 'good', 120, 1, 1, 13, 0.85, 0.75, 0, 0, 0, 0, 0, 0,  -5, 10, 0, 0, 5, 0, 5, 0, 0, 10,  -2, 0, 0, 0, 3, 0, 2, 0, 0, 3) ")
cur.execute("INSERT INTO Races VALUES('Forest Gnome', 'excellent', 100, 1, 2, 16, 0.6, 0.45, 0, 0, 0, 0, 0, 0,  -10, 10, 5, 10, 5, 0, 5, 0, 5, -5,  -3, 2, 2, 3, 2, 0, 0, 0, 0, 0) ")
cur.execute("INSERT INTO Races VALUES('Giantman', 'average', 200, 3, 1, 13, 1.33, 1.2, -5, 0, 5, 0, 0, 0,  15, 10, -5, -5, 0, -5, -5, 0, 0, 5,  5, 3, -2, -2, 0, 0, 0, 2, 0, 0) ")
cur.execute("INSERT INTO Races VALUES('Half Elf', 'good', 135, 2, 1, 10, 0.92, 0.8, -5, 0, -5, -5, 0, 50,  0, 0, 5, 10, -5, 0, 0, 0, 0, 5,  2, 0, 2, 2, -2, 0, 0, 0, 0, 2) ")
cur.execute("INSERT INTO Races VALUES('Half Krolvin', 'excellent', 165, 1, 1, 13, 1.1, 1, 0, 0, 0, 0, 0, 0,  10, 10, 0, 5, 0, 0, -10, 0, -5, -5,  3, 5, 2, 2, 0, -2, -2, 0, 0, -2) ")
cur.execute("INSERT INTO Races VALUES('Halfling', 'excellent', 100, 3, 2, 16, 0.5, 0.45, 40, 0, 0, 20, 30, 30,  -15, 10, 15, 10, -5, -5, 5, 10, 0, -5,  -5, 5, 5, 5, -2, 0, -2, 0, 0, 0) ")
cur.execute("INSERT INTO Races VALUES('Human', 'average', 150, 2, 1, 14, 1, 0.9, 0, 0, 0, 0, 0, 0,  5, 0, 0, 0, 0, 0, 5, 5, 0, 0,  2, 2, 0, 0, 0, 0, 0, 2, 0, 0) ")
cur.execute("INSERT INTO Races VALUES('Sylvankind', 'good', 130, 1, 1, 10, 0.81, 0.7, -5, 0, -5, -5, 10, 100,  0, 0, 10, 5, -5, 5, 0, 0, 0, 0,  -3, -2, 5, 5, -5, 3, 0, 0, 0, 3) ")
	
	
# Creates the Professions table. This contains the general information about all the professions in GS4. Skill costs are handled by the Skills table.	
cur.execute("CREATE TABLE Professions (name, type,  prime_statistics1, prime_statistics2,  mana_statistic1,  mana_statistic2, spell_circle1, spell_circle2, spell_circle3, guild_skill1, guild_skill2, guild_skill3, guild_skill4, guild_skill5, guild_skill6,  strength_growth, constitution_growth, dexterity_growth, agility_growth, discipline_growth, aura_growth, logic_growth, intuition_growth, wisdom_growth, influence_growth)")	
	
cur.execute("INSERT INTO Professions VALUES ('Bard', 'semi',  'Influence', 'Aura',  'Influence', 'Aura',  'Minor Elemental', 'Bard', 'NONE',  'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE',  25, 20, 25, 20, 15, 25, 10, 15, 20, 30) ")
cur.execute("INSERT INTO Professions VALUES ('Cleric', 'pure',  'Wisdom', 'Intuition',  'Wisdom', 'Wisdom',  'Minor Spiritual', 'Major Spiritual',  'Cleric', 'General Alchemy', 'Cleric Potions', 'Cleric Trinkets', 'NONE', 'NONE', 'NONE',   20, 20, 10, 15, 25, 15, 25, 25, 30, 20) ")
cur.execute("INSERT INTO Professions VALUES ('Empath', 'pure',  'Wisdom', 'Influence',  'Wisdom', 'Influence',  'Minor Spiritual', 'Major Spiritual',  'Empath',  'General Alchemy', 'Empath Potions', 'Empath Trinkets', 'NONE', 'NONE', 'NONE',  10, 20, 15, 15, 25, 20, 25, 20, 30, 25) ")
cur.execute("INSERT INTO Professions VALUES ('Monk', 'square',  'Agility', 'Strength',  'Wisdom', 'Logic',  'Minor Spiritual', 'Minor Mental', 'NONE',  'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE',  25, 25, 20, 30, 25, 15, 20, 20, 15, 10) ")
cur.execute("INSERT INTO Professions VALUES ('Paladin', 'semi',  'Wisdom', 'Strength',  'Wisdom', 'Wisdom',  'Minor Spiritual', 'Paladin', 'NONE',  'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE',  30, 25, 20, 20, 25, 15, 10, 15, 25, 20) ")
cur.execute("INSERT INTO Professions VALUES ('Ranger', 'semi',  'Dexterity', 'Intuition',  'Wisdom', 'Wisdom',  'Minor Spiritual', 'Ranger', 'NONE',  'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE',  25, 20, 30, 20, 20, 15, 15, 25, 25, 10) ")
cur.execute("INSERT INTO Professions VALUES ('Rogue', 'square',  'Dexterity', 'Agility',  'Aura', 'Wisdom',  'Minor Elemental', 'Minor Spiritual', 'NONE',  'Sweep', 'Subdue', 'Stun Maneuvers', 'Lock Mastery', 'Cheapshots', 'Rogue Gambits',  25, 20, 25, 30, 20, 15, 20, 25, 10, 15) ")
cur.execute("INSERT INTO Professions VALUES ('Savant', 'pure',  'Influence', 'Logic',  'Influence', 'Influence',  'Minor Mental', 'Major Mental', 'Savant',  'General Alchemy', 'Savant Potions', 'Savant Trinkets', 'NONE', 'NONE', 'NONE',  0, 0, 0, 0, 0, 0, 0, 0, 0, 0) ")
cur.execute("INSERT INTO Professions VALUES ('Sorcerer', 'pure',  'Aura', 'Wisdom',  'Aura', 'Wisdom',  'Minor Elemental', 'Minor Spiritual', 'Sorcerer',  'General Alchemy', 'Sorcerer Potions', 'Sorcerer Trinkets', 'Illusions', 'NONE', 'NONE',  10, 15, 20, 15, 25, 30, 25, 20, 25, 20) ")
cur.execute("INSERT INTO Professions VALUES ('Warrior', 'square',  'Constitution', 'Strength',  'Aura', 'Wisdom',  'Minor Elemental', 'Minor Spiritual', 'NONE',  'Batter Barriers', 'Berserk', 'Disarm Weapon', 'Tackle', 'War Cries', 'Warrior Tricks',  30, 25, 25, 25, 20, 15, 10, 20, 15, 20) ")
cur.execute("INSERT INTO Professions VALUES ('Wizard', 'pure',  'Aura', 'Logic',  'Aura', 'Aura',  'Minor Elemental', 'Major Elemental', 'Wizard',  'General Alchemy', 'Wizard Potions', 'Wizard Trinkets', 'NONE', 'NONE', 'NONE',  10, 15, 25, 15, 20, 30, 25, 25, 20, 20) ")
	

# Creates the Skills table. This includes the name, type, subskill, redux value, and PTP/MTP costs and max ranks per level for every profession.
cur.execute("CREATE TABLE Skills (name, type, subskill_group, redux_value, bard_ptp, bard_mtp, bard_max_ranks, cleric_ptp, cleric_mtp, cleric_max_ranks, empath_ptp, empath_mtp, empath_max_ranks, monk_ptp, monk_mtp, monk_max_ranks, paladin_ptp, paladin_mtp, paladin_max_ranks, ranger_ptp, ranger_mtp, ranger_max_ranks, rogue_ptp, rogue_mtp, rogue_max_ranks, savant_ptp, savant_mtp, savant_max_ranks, sorcerer_ptp, sorcerer_mtp, sorcerer_max_ranks, warrior_ptp, warrior_mtp, warrior_max_ranks, wizard_ptp, wizard_mtp, wizard_max_ranks) ")
	
cur.execute("INSERT INTO Skills VALUES ('Armor Use', 'armor', 'NONE', 0.4,  5,0,2,  8,0,1,  15,0,1,  10,0,2,  3,0,3,  5,0,2,  5,0,2,  15,0,1,  15,0,1,  2,0,3,  14,0,1) ")
cur.execute("INSERT INTO Skills VALUES ('Shield Use', 'armor', 'NONE', 0.4,  5,0,2,  13,0,1,  13,0,1,  8,0,2,  3,0,2,  5,0,2,  4,0,2,  13,0,1,  13,0,1,  2,0,3,  13,0,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Edged Weapons', 'weapon', 'NONE', 0.3,  3,1,2,  4,2,1,  6,2,1,  2,1,2,  3,1,2,  3,1,2,  2,1,2,  6,2,1,  6,2,1,  2,1,2,  6,1,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Blunt Weapons', 'weapon', 'NONE', 0.3,  4,1,2,  4,2,1,  6,2,1,  3,1,2,  3,1,2,  4,1,2,  3,1,2,  6,2,1,  6,2,1,  2,1,2,  6,1,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Two-Handed Weapons', 'weapon', 'NONE', 0.3,  7,2,2,  10,3,1,  13,3,1,  5,2,2,  4,2,2,  6,2,2,  6,2,2,  14,3,1,  14,3,1,  3,1,2,  14,3,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Ranged Weapons', 'weapon', 'NONE', 0.3,  4,2,2,  9,3,1,  14,3,1,  4,1,2,  6,2,2,  3,1,2,  3,1,2,  14,3,1,  14,3,1,  2,1,2,  14,3,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Thrown Weapons', 'weapon', 'NONE', 0.3,  3,1,2,  9,3,1,  9,3,1,  2,1,2,  5,2,2,  2,1,2,  2,1,2,  9,3,1,  9,3,1,  2,1,2,  8,2,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Polearm Weapons', 'weapon', 'NONE', 0.3,  6,1,2,  11,3,1,  14,3,1,  6,2,2,  5,2,2,  7,2,2,  7,2,2,  14,3,1,  14,3,1,  3,1,2,  14,3,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Brawling', 'weapon', 'NONE', 0.3,  3,1,2,  6,1,1,  10,2,1,  2,1,2,  4,1,2,  4,2,2,  3,1,2,  10,2,1,  10,2,1,  2,1,2,  10,2,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Ambush', 'combat', 'NONE', 0.4,  4,4,1,  12,12,1,  15,15,1,  3,2,2,  4,5,1,  3,3,2,  2,1,2,  15,15,1,  15,14,1,  3,4,2,  15,10,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Two Weapon Combat', 'combat', 'NONE', 0.4,  3,2,2,  9,9,1,  12,12,1,  2,2,2,  3,3,2,  3,2,2,  2,2,2,  12,12,1,  12,12,1,  2,2,2,  12,12,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Combat Maneuvers', 'combat', 'NONE', 0.4,  8,4,2,  10,6,1,  12,8,1,  5,3,2,  5,4,2,  5,4,2,  4,4,2,  12,8,1,  12,8,1,  4,3,2,  12,8,1) ")
cur.execute("INSERT INTO Skills VALUES ('Multi Opponent Combat', 'combat', 'NONE', 0.4,  7,3,1,  15,8,1,  15,10,1,  5,2,2,  5,2,1,  10,4,1,  10,3,1,  15,10,1,  15,10,1,  4,3,2,  15,10,1) ")
cur.execute("INSERT INTO Skills VALUES ('Physical Fitness', 'combat', 'NONE', 1,  4,0,2,  7,0,1,  2,0,3,  2,0,3,  3,0,2,  4,0,2,  3,0,2,  8,0,1,  8,0,1,  2,0,3,  8,0,1) ")
cur.execute("INSERT INTO Skills VALUES ('Dodging', 'combat', 'NONE', 0.4,  6,6,2,  20,20,1,  20,20,1,  1,1,3,  5,3,2,  7,5,2,  2,1,3,  20,20,1,  20,20,1,  4,2,3,  20,20,1) ")
cur.execute("INSERT INTO Skills VALUES ('Arcane Symbols', 'magic', 'NONE', 0,  0,4,2,  0,2,2,  0,2,2,  0,6,1,  0,5,1,  0,5,1,  0,7,1,  0,2,2,  0,2,2,  0,7,1,  0,1,2) ")
cur.execute("INSERT INTO Skills VALUES ('Magic Item Use', 'magic', 'NONE', 0,  0,4,2,  0,2,2,  0,2,2,  0,7,1,  0,6,1,  0,5,1,  0,8,1,  0,2,2,  0,2,2,  0,8,1,  0,1,2) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Aiming', 'magic', 'NONE', 0,  3,10,1,  3,2,2,  3,1,2,  5,20,1,  5,20,1,  5,15,1,  4,22,1,  3,1,2,  3,1,2,  5,25,1,  2,1,2) ")
cur.execute("INSERT INTO Skills VALUES ('Harness Power', 'magic', 'NONE', 0,  0,5,2,  0,4,3,  0,4,3,  0,6,1,  0,5,2,  0,5,2,  0,9,1,  0,4,3,  0,4,3,  0,10,1,  0,4,3) ")
cur.execute("INSERT INTO Skills VALUES ('Elemental Mana Control', 'magic', 'NONE', 0,  0,6,1,  0,12,1,  0,12,1,  0,15,1,  0,15,1,  0,15,1,  0,10,1,  0,3,2,  0,3,2,  0,10,1,  0,4,2) ")
cur.execute("INSERT INTO Skills VALUES ('Mental Mana Control', 'magic', 'NONE', 0,  0,6,1,  0,12,1,  0,3,2,  0,8,1,  0,15,1,  0,15,1,  0,15,1,  0,3,2,  0,12,1,  0,15,1,  0,15,1) ")
cur.execute("INSERT INTO Skills VALUES ('Spiritual Mana Control', 'magic', 'NONE', 0,  0,12,1,  0,3,3,  0,3,2,  0,8,1,  0,6,1,  0,5,1,  0,10,1,  0,12,1,  0,3,2,  0,10,1,  0,15,1) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Minor Spiritual', 'magic', 'Spell Research', 0,  0,0,0,  0,8,3,  0,8,3,  0,38,1,  0,27,2,  0,17,2,  0,67,1,  0,0,0,  0,8,3,  0,120,1,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Major Spiritual', 'magic', 'Spell Research', 0,  0,0,0,  0,8,3,  0,8,3,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Cleric', 'magic', 'Spell Research', 0,  0,0,0,  0,8,3,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Minor Elemental', 'magic', 'Spell Research', 0,  0,17,2,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,67,1,  0,0,0,  0,8,3,  0,120,1,  0,8,3) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Major Elemental', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,8,3) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Ranger', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,17,2,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Sorcerer', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,8,3,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Wizard', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,8,3) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Bard', 'magic', 'Spell Research', 0,  0,17,2,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Empath', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,8,3,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Savant', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,8,3,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Minor Mental', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,0,0,  0,38,1,  0,0,0,  0,0,0,  0,0,0,  0,8,3,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Major Mental', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,8,3,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Spell Research, Paladin', 'magic', 'Spell Research', 0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,17,2,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0,  0,0,0) ")
cur.execute("INSERT INTO Skills VALUES ('Elemental Lore, Air', 'magic', 'Elemental Lore', 0,  0,8,1,  0,20,1,  0,20,1,  0,40,1,  0,20,1,  0,20,1,  0,15,1,  0,20,1,  0,7,2,  0,15,1,  0,6,2) ")
cur.execute("INSERT INTO Skills VALUES ('Elemental Lore, Earth', 'magic', 'Elemental Lore', 0,  0,8,1,  0,20,1,  0,20,1,  0,40,1,  0,20,1,  0,20,1,  0,15,1,  0,20,1,  0,7,2,  0,15,1,  0,6,2) ")
cur.execute("INSERT INTO Skills VALUES ('Elemental Lore, Fire', 'magic', 'Elemental Lore', 0,  0,8,1,  0,20,1,  0,20,1,  0,40,1,  0,20,1,  0,20,1,  0,15,1,  0,20,1,  0,7,2,  0,15,1,  0,6,2) ")
cur.execute("INSERT INTO Skills VALUES ('Elemental Lore, Water', 'magic', 'Elemental Lore', 0,  0,8,1,  0,20,1,  0,20,1,  0,40,1,  0,20,1,  0,20,1,  0,15,1,  0,20,1,  0,7,2,  0,15,1,  0,6,2) ")	
cur.execute("INSERT INTO Skills VALUES ('Spiritual Lore, Blessings', 'magic', 'Spiritual Lore', 0,  0,20,1,  0,6,2,  0,6,2,  0,12,1,  0,7,2,  0,10,1,  0,15,1,  0,20,1,  0,7,2,  0,15,1,  0,20,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Spiritual Lore, Religion', 'magic', 'Spiritual Lore', 0,  0,20,1,  0,6,2,  0,6,2,  0,12,1,  0,7,2,  0,10,1,  0,15,1,  0,20,1,  0,7,2,  0,15,1,  0,20,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Spiritual Lore, Summoning', 'magic', 'Spiritual Lore', 0,  0,20,1,  0,6,2,  0,6,2,  0,12,1,  0,7,2,  0,10,1,  0,15,1,  0,20,1,  0,7,2,  0,15,1,  0,20,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Sorcerous Lore, Demonology', 'magic', 'Sorcerous Lore', 0,  0,18,1,  0,10,1,  0,12,1,  0,35,1,  0,18,1,  0,18,1,  0,30,1,  0,12,1,  0,6,2,  0,30,1,  0,10,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Sorcerous Lore, Necromancy', 'magic', 'Sorcerous Lore', 0,  0,18,1,  0,10,1,  0,12,1,  0,35,1,  0,18,1,  0,18,1,  0,30,1,  0,12,1,  0,6,2,  0,30,1,  0,10,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Mental Lore, Divination', 'magic', 'Mental Lore', 0,  0,8,1,  0,20,1,  0,6,2,  0,12,1,  0,20,1,  0,20,1,  0,40,1,  0,6,2,  0,20,1,  0,40,1,  0,20,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Mental Lore, Manipulation', 'magic', 'Mental Lore', 0,  0,8,1,  0,20,1,  0,6,2,  0,12,1,  0,20,1,  0,20,1,  0,40,1,  0,6,2,  0,20,1,  0,40,1,  0,20,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Mental Lore, Telepathy', 'magic', 'Mental Lore', 0,  0,8,1,  0,20,1,  0,6,2,  0,12,1,  0,20,1,  0,20,1,  0,40,1,  0,6,2,  0,20,1,  0,40,1,  0,20,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Mental Lore, Transference', 'magic', 'Mental Lore', 0,  0,8,1,  0,20,1,  0,6,2,  0,12,1,  0,20,1,  0,20,1,  0,40,1,  0,6,2,  0,20,1,  0,40,1,  0,20,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Mental Lore, Transformation', 'magic', 'Mental Lore', 0,  0,8,1,  0,20,1,  0,6,2,  0,12,1,  0,20,1,  0,20,1,  0,40,1,  0,6,2,  0,20,1,  0,40,1,  0,20,1) ")	
cur.execute("INSERT INTO Skills VALUES ('Survival', 'general', 'NONE', 0,  2,2,2,  3,2,2,  3,2,2,  2,2,2,  2,2,2,  1,1,2,  2,2,2,  3,2,2,  3,2,1,  1,3,2,  3,2,2) ")	
cur.execute("INSERT INTO Skills VALUES ('Disarm Traps', 'general', 'NONE', 0,  2,3,2,  2,6,1,  2,6,1,  3,4,2,  2,5,1,  2,4,2,  1,1,3,  2,6,1,  2,6,1,  2,4,2,  2,6,1) ")
cur.execute("INSERT INTO Skills VALUES ('Picking Locks', 'general', 'NONE', 0,  2,1,2,  2,4,2,  2,4,2,  3,3,2,  2,4,2,  2,3,2,  1,1,3,  2,4,1,  2,4,1,  2,3,2,  2,4,2) ")
cur.execute("INSERT INTO Skills VALUES ('Stalking and Hiding', 'general', 'NONE', 0,  3,2,2,  5,4,1,  5,4,1,  3,2,2,  4,4,1,  2,1,2,  1,1,3,  5,4,1,  5,4,1,  3,2,2,  5,4,1) ")
cur.execute("INSERT INTO Skills VALUES ('Perception', 'general', 'NONE', 0,  0,3,2,  0,3,2,  0,3,2,  0,2,2,  0,3,2,  0,3,2,  0,1,3,  0,3,2,  0,3,2,  0,3,2,  0,3,2) ")
cur.execute("INSERT INTO Skills VALUES ('Climbing', 'general', 'NONE', 0,  3,0,2,  4,0,1,  4,0,1,  1,0,2,  3,0,2,  2,0,2,  1,0,2,  4,0,1,  4,0,1,  3,0,2,  4,0,1) ")
cur.execute("INSERT INTO Skills VALUES ('Swimming', 'general', 'NONE', 0,  3,0,2,  3,0,1,  3,0,1,  2,0,2,  2,0,2,  2,0,2,  2,0,2,  3,0,1,  3,0,1,  2,0,2,  3,0,1) ")
cur.execute("INSERT INTO Skills VALUES ('First Aid', 'general', 'NONE', 0,  2,1,2,  1,1,2,  1,0,3,  1,2,2,  1,1,2,  2,1,2,  1,2,2,  2,1,2,  2,1,2,  1,2,2,  2,1,2) ")
cur.execute("INSERT INTO Skills VALUES ('Trading', 'general', 'NONE', 0,  0,2,2,  0,3,2,  0,3,2,  0,3,2,  0,3,2,  0,3,2,  0,3,2,  0,3,2,  0,3,2,  0,4,2,  0,3,2) ")
cur.execute("INSERT INTO Skills VALUES ('Pickpocketing', 'general', 'NONE', 0,  2,1,2,  3,3,1,  3,3,1,  2,2,2,  4,4,1,  2,3,1,  1,0,2,  3,3,1,  3,3,1,  2,3,1,  3,3,1) ")
	
	
# Creates the Maneuvers table. This table contains every Combat Maneuver, Shield Maneuver, and Armor Specializion. The base costs, profession availability, and prerequisites are also in this table.
cur.execute("CREATE TABLE Maneuvers (name, mnemonic, type, ranks, cost_rank1, cost_rank2, cost_rank3, cost_rank4, cost_rank5, available_bard, available_cleric, available_empath, available_monk, available_paladin, available_ranger, available_rogue, available_savant, available_sorcerer, available_warrior, available_wizard, prerequisites)")
	
cur.execute("INSERT INTO Maneuvers VALUES ('Armor Spike Focus', 'SPIKEFOCUS', 'combat', 2,  5, 10, 'NONE', 'NONE', 'NONE',  0,0,0,0,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Bearhug', 'BEARHUG', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Berserk', 'BERSERK', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Block Mastery', 'BMASTERY', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Bull Rush', 'BULLRUSH', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Burst of Swiftness', 'BURST', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Charge', 'CHARGE', 'combat', 5,  2, 4, 6, 8, 10,  1,0,0,1,1,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Cheapshots', 'CHEAPSHOTS', 'combat', 5,  2, 3, 4, 5, 6,  1,0,0,1,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Combat Focus', 'FOCUS', 'combat', 5,  2, 4, 6, 8, 10,  1,0,0,1,1,1,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Combat Mastery', 'CMASTERY', 'combat', 2,  2, 4, 'NONE', 'NONE', 'NONE',  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Combat Mobility', 'MOBILITY', 'combat', 2,  5, 10, 'NONE', 'NONE', 'NONE',  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Combat Movement', 'CMOVEMENT', 'combat', 5,  2, 3, 4, 5, 6,  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Combat Toughness', 'TOUGHNESS', 'combat', 3,  6, 8, 10, 'NONE', 'NONE',  0,0,0,1,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Coup de Grace', 'COUPDEGRACE', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Crowd Press', 'CPRESS', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Cunning Defense', 'CDEFENSE', 'combat', 5,  2, 3, 4, 5, 6,  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Cutthroat', 'CUTTROAT', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Dirtkick', 'DIRTKICK', 'combat', 5,  2, 3, 4, 5, 6,  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Disarm Weapon', 'DISARM', 'combat', 5,  2, 4, 6, 8, 10,  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Divert', 'DIVERT', 'combat', 5,  2, 3, 4, 5, 6,  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Duck and Weave', 'WEAVE', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,1,0,0,0,0, 'CM:Combat Movement:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Dust Shroud', 'SSHROUD', 'combat', 5,  2, 3, 4, 5, 6,  0,0,0,0,0,0,1,0,0,0,0, 'CM:Dirtkick:5') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Evade Mastery', 'EMSATERY', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES (\"Executioner's Stance\", 'EXECUTIONER', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Feint', 'FEINT', 'combat', 5,  2, 3, 5, 7, 10,  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Flurry of Blows', 'FLURRY', 'combat', 3,  3, 6, 9, 'NONE', 'NONE',  0,0,0,1,0,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Garrote', 'GARROTE', 'combat', 5,  2, 4, 6, 8, 10,  1,0,0,1,0,1,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Grapple Mastery', 'GMSATERY', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES (\"Griffin's Voice\", 'GRIFFIN', 'combat', 3,  3, 6, 9, 'NONE', 'NONE',  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Groin Kick', 'GKICK', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Hamstring', 'HAMSTRING', 'combat', 5,  2, 4, 6, 8, 10,  1,0,0,0,0,1,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Haymaker', 'HAYMAKER', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Headbutt', 'HAYMAKER', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Inner Harmony', 'IHARMONY', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Internal Power', 'IPOWER', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Ki Focus', 'IPOWER', 'combat', 3,  3, 6, 9, 'NONE', 'NONE',  0,0,0,1,0,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Kick Mastery', 'KMSATERY', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Mighty Blow', 'MBLOW', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Multi-Fire', 'DISARM', 'combat', 5,  2, 4, 6, 8, 10,  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Mystic Strike', 'MYSTICSTRIKE', 'combat', 5,  2, 3, 4, 5, 6,  0,0,0,1,0,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Parry Mastery', 'PMASTERY', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Perfect Self', 'PERFECTSELF', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,0,0,0,0,0, 'CM:Burst of Swiftness:3&CM:Surge of Strength:3') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Precision', 'PRECISION', 'combat', 2,  4, 6, 'NONE', 'NONE', 'NONE',  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Punch Mastery', 'PUNCHMASTERY', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES (\"Predator's Eye\", 'PREDATOR', 'combat', 3,  4, 6, 8, 'NONE', 'NONE',  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
#cur.execute("INSERT INTO Maneuvers VALUES ('Quickstrike', 'QSTRIKE', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Rolling Krynch Stance', 'KRYNCH', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shadow Mastery', 'SMASTERY', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,1,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Bash', 'SBASH', 'combat', 5,  2, 4, 6, 8, 10,  1,0,0,0,1,1,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Charge', 'SCHARGE', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Side By Side', 'SIDEBYSIDE', 'combat', 5,  2, 4, 6, 8, 10,  1,1,1,1,1,1,1,1,1,1,1, 'CM:Combat Movement:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Silent Strike', 'SILENTSTRIKE', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,1,0,0,0,0, 'CM:Shadow Mastery:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Slippery Mind', 'SLIPPERYMIND', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Specialization I', 'WSPEC1', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Specialization II', 'WSPEC2', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Specialization III', 'WSPEC3', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Spell Cleaving', 'SCLEAVE', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Spell Parry', 'SPARRY', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Spell Thieve', 'THIEVE', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Spin Attack', 'SATTACK', 'combat', 5,  2, 4, 6, 8, 10,  1,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Staggering Blow', 'SBLOW', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Stance of the Mongoose', 'MONGOOSE', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,1,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Striking Asp Stance', 'ASP', 'combat', 3,  4, 8, 12, 'NONE', 'NONE', 0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Stun Maneuvers', 'STUNMAN', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Subdue', 'SUBDUE', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Sucker Punch', 'SPUNCH', 'combat', 5,  2, 3, 4, 5, 6,  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Subdual Strike', 'SSTRIKE', 'combat', 5,  2, 3, 4, 5, 6,  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Sunder Shield', 'SUNDER', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Surge of Strength', 'SUNDER', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,1,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Sweep', 'SWEEP', 'combat', 5,  2, 4, 6, 8, 10,  1,0,0,1,0,1,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Tackle', 'TACKLE', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Tainted Bond', 'TAINTED', 'combat', 1,  12, 'NONE', 'NONE', 'NONE', 'NONE',  0,0,0,0,1,0,0,0,0,1,0, 'CM:Weapon Bonding:5|Skill:Spell Research, Paladin:25') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Trip', 'TRIP', 'combat', 5,  2, 4, 6, 8, 10,  1,1,1,1,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Truehand', 'TRUEHAND', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Twin Hammerfists', 'TWINHAMM', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Unarmed Specialist', 'UNARMEDSPEC', 'combat', 1,  6, 'NONE', 'NONE', 'NONE', 'NONE',  1,1,1,0,1,1,1,1,1,1,1, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Vanish', 'VANISH', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,0,0,0,1,0,0,0,0, 'CM:Shadow Mastery:4') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Weapon Bonding', 'BOND', 'combat', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'CM:Specialization I:3|CM:Specialization II:3|CM:Specialization III:3') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Whirling Dervish', 'DERVISH', 'combat', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,0,0,0,1,0,0,1,0, 'NONE') ")
    
cur.execute("INSERT INTO Maneuvers VALUES ('Small Shield Focus', 'SFOCUS', 'shield', 5,  4, 6, 8, 10, 12,  0,0,0,0,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Medium Shield Focus', 'MFOCUS', 'shield', 5,  4, 6, 8, 10, 12,  0,0,0,0,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Large Shield Focus', 'LFOCUS', 'shield', 5,  4, 6, 8, 10, 12,  0,0,0,0,1,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Tower Shield Focus', 'TFOCUS', 'shield', 5,  4, 6, 8, 10, 12,  0,0,0,0,1,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Bash', 'SBASH', 'shield', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Charge', 'SCHARGE', 'shield', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,0,0,0,1,0, 'SM:Shield Bash:2|CM:Shield Bash:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Push', 'PUSH', 'shield', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,0,0,0,1,0, 'SM:Shield Bash:2|CM:Shield Bash:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Pin', 'PIN', 'shield', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,0,0,0,1,0, 'SM:Shield Bash:2|CM:Shield Bash:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Swiftness', 'SWIFTNESS', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,0,0,1,0,0,1,0, 'SM:Small Shield Focus:3|SM:Medium Shield Focus:3') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shielded Brawler', 'BRAWLER', 'shield', 5,  6, 8, 10, 12, 14,  0,0,0,0,1,0,1,0,0,1,0, 'SM:Small Shield Focus:3|SM:Medium Shield Focus:3|SM:Large Shield Focus:3|SM:Tower Shield Focus:3') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Prop Up', 'PROP', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,1,0,0,0,0,1,0, 'SM:Large Shield Focus:3|SM:Tower Shield Focus:3') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Adamantine Bulwark', 'BULWARK', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,0,0,0,0,0,1,0, 'SM:Prop Up:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Riposte', 'RIPOSTE', 'shield', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,0,0,0,1,0,0,1,0, 'SM:Shield Bash:2|CM:Shield Bash:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Forward', 'FORWARD', 'shield', 3,  4, 8, 12, 'NONE', 'NONE',  0,0,0,0,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Spike Focus', 'SPIKEFOCUS', 'shield', 2,  8, 12, 'NONE', 'NONE', 'NONE',  0,0,0,0,1,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Spike Mastery', 'SPIKEMASTERY', 'shield', 2,  8, 12, 'NONE', 'NONE', 'NONE',  0,0,0,0,1,0,1,0,0,1,0, 'SM:Shield Spike Focus:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Deflection Training', 'DTRAINING', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,0,0,1,0,0,1,0, 'SM:Small Shield Focus:3|SM:Medium Shield Focus:3|SM:Large Shield Focus:3|SM:Tower Shield Focus:3') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Deflection Mastery', 'DMASTERY', 'shield', 5,  8, 10, 12, 14, 16,  0,0,0,0,0,0,1,0,0,1,0, 'SM:Deflection Training:3') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Block the Elements', 'EBLOCK', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,1,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Deflect the Elements', 'DEFLECT', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,0,0,1,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Steady Shield', 'STEADY', 'shield', 2,  4, 6, 'NONE', 'NONE', 'NONE',  0,0,0,0,0,0,1,0,0,1,0, 'CM:Stun Maneuvers:2|GS:Stun Maneuvers:20') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Disarming Presence', 'DPRESENCE', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,0,0,1,0,0,1,0, 'CM:Disarm Weapon:2|GS:Disarm Weapon:20') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Guard Mastery', 'GUARDMASTERY', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Tortoise Stance', 'TORTOISE', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,0,0,0,0,0,1,0, 'SM:Block Mastery:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Spell Block', 'SPELLBLOCK', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,1,0,1,0,0,1,0, 'SM:Small Shield Focus:3|SM:Medium Shield Focus:3|SM:Large Shield Focus:3|SM:Tower Shield Focus:3') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Mind', 'MIND', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,1,0,1,0,0,1,0, 'SM:Spell Block:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Protective Wall', 'PWALL', 'shield', 2,  4, 5, 'NONE', 'NONE', 'NONE',  0,0,0,0,1,0,0,0,0,1,0, 'SM:Tower Shield Focus:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Strike', 'STRIKE', 'shield', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,1,0,0,1,0, 'SM:Shield Bash:2|CM:Shield Bash:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Strike Mastery', 'STRIKEMASTERY', 'shield', 1,  30, 'NONE', 'NONE', 'NONE', 'NONE',  0,0,0,0,1,0,1,0,0,1,0, 'SM:Shield Strike:2&Skill:Multi Opponent Combat:30') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Trample', 'TRAMPLE', 'shield', 5,  2, 4, 6, 8, 10,  0,0,0,0,0,0,0,0,0,1,0, 'SM:Shield Charge:2') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Shield Trample Mastery', 'TMASTERY', 'shield', 3,  8, 10, 12, 'NONE', 'NONE',  0,0,0,0,0,0,0,0,0,1,0, 'SM:Shield Trample:3&Skill:Multi Opponent Combat:30') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Steely Resolve', 'RESOLVE', 'shield', 3,  6, 12, 18, 'NONE', 'NONE',  0,0,0,0,1,0,0,0,0,1,0, 'SM:Tower Shield Focus:3') ")    
cur.execute("INSERT INTO Maneuvers VALUES ('Phalanx', 'PHALANX', 'shield', 5,  2, 4, 6, 8, 10,  0,0,0,0,1,0,1,0,0,1,0, 'NONE') ")
	
cur.execute("INSERT INTO Maneuvers VALUES ('Crush Protection', 'CRUSH', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Puncture Protection', 'PUNCTURE', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Slash Protection', 'SLASH', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Armored Blessing', 'BLESSING', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,1,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Armored Casting', 'CASTING', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,1,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Armored Evasion', 'EVASION', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Armored Fluidity', 'FLUIDITY', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,1,0,0,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Armor Reinforcement', 'REINFORCE', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Armored Stealth', 'STEALTH', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,0,0,1,0,0,0,0, 'NONE') ")
cur.execute("INSERT INTO Maneuvers VALUES ('Armor Support', 'SUPPORT', 'armor', 5,  20, 30, 40, 50, 60,  0,0,0,0,0,0,0,0,0,1,0, 'NONE') ")


# Creates the Weapons table which contains all the weapons and their attributes
cur.execute("CREATE TABLE Weapons (name, weapon_type, base_weight, base_speed, minimum_speed, damage_type, str_du,  df_vs_cloth, df_vs_leather, df_vs_scale, df_vs_chain, df_vs_plate,  avd_1, avd_2,  avd_5, avd_6, avd_7, avd_8,  avd_9, avd_10, avd_11, avd_12,  avd_13, avd_14, avd_15, avd_16,  avd_17, avd_18, avd_19, avd_20  ) ")   

# Brawling
cur.execute("INSERT INTO Weapons VALUES('Blackjack', 'Brawling', 3, 1, 3, 'Crush', '50/80',  .250, .140, .090, .110, .075,  40, 40,  35, 34, 33, 32,  25, 23, 21, 19,  15, 11, 7, 3,  0, -6, -12, -18) ")
cur.execute("INSERT INTO Weapons VALUES('Cestus', 'Brawling', 2, 1, 3, 'Crush', '50/80',  .250, .175, .150, .075, .035,  40, 40,  30, 29, 28, 27,  20, 18, 16, 14,  10, 6, 2, -2,  -25, -31, -37, -43) ")
cur.execute("INSERT INTO Weapons VALUES('Closed Fist', 'Brawling', 0, 1, 3, 'Crush', '--/--',  .100, .075, .040, .036, .032,  25, 25,  20, 19, 18, 17,  10, 8, 6, 4,  5, 1, -3, -7,  -5, -11, -17, -23) ")
cur.execute("INSERT INTO Weapons VALUES('Fist-scythe', 'Brawling', 4, 2, 4, 'Slash/Puncture/Crush', '70/185',  .350, .225, .200, .175, .125,  45, 45,  40, 39, 38, 37,  30, 28, 26, 24,  37, 33, 29, 25,  20, 14, 8, 2) ")
cur.execute("INSERT INTO Weapons VALUES('Hook-knife', 'Brawling', 1, 1, 3, 'Slash/Puncture', '30/100',  .250, .175, .125, .070, .035,  40, 40,  30, 29, 28, 27,  18, 16, 14, 12,  10, 6, 2, -2,  -15, -21, -27, -33) ")
cur.execute("INSERT INTO Weapons VALUES('Jackblade', 'Brawling', 3, 2, 4, 'Slash/Crush', '60/90',  .250, .175, .150, .150, .110,  45, 45,  35, 34, 33, 32,  25, 23, 21, 19,  20, 16, 12, 8,  10, 4, -2, -8) ")
cur.execute("INSERT INTO Weapons VALUES('Knuckle-blade', 'Brawling', 2, 1, 3, 'Slash/Crush', '18/195',  .250, .150, .100, .075, .075,  45, 45,  40, 39, 38, 37,  25, 23, 21, 19,  25, 21, 17, 13,  0, -6, -12, -18) ")
cur.execute("INSERT INTO Weapons VALUES('Knuckle-duster', 'Brawling', 1, 1, 3, 'Crush', '18/199',  .250, .175, .125, .100, .040,  35, 35,  32, 31, 30, 29,  25, 23, 21, 19,  18, 14, 10, 6,  0, -6, -12, -18) ")
cur.execute("INSERT INTO Weapons VALUES('Paingrip', 'Brawling', 2, 1, 3, 'Slash/Puncture/Crush', '50/80',  .225, .200, .125, .075, .030,  40, 40,  20, 19, 18, 17,  15, 13, 11, 9,  15, 11, 7, 3,  -25, -31, -37, -43) ")
cur.execute("INSERT INTO Weapons VALUES('Razorpaw', 'Brawling', 2, 1, 3, 'Slash', '40/80',  .275, .200, .125, .050, .030,  35, 35,  20, 19, 18, 17,  10, 8, 6, 4,  0, -4, -8, -12,  -25, -31, -37, -43) ")
cur.execute("INSERT INTO Weapons VALUES('Sai', 'Brawling', 0, 2, 4, 'Puncture', '25/175',  .250, .200, .110, .150, .040,  30, 30,  31, 30, 29, 28,  25, 23, 21, 19,  33, 29, 25, 21,  6, 0, -6, -12) ")
cur.execute("INSERT INTO Weapons VALUES('Tiger-claw', 'Brawling', 1, 1, 3, 'Slash/Crush', '18/165',  .275, .200, .150, .100, .035,  40, 40,  25, 24, 23, 22,  15, 13, 11, 9,  5, 1, -3, -7,  -25, -31, -37, -43) ")
cur.execute("INSERT INTO Weapons VALUES('Troll-claw', 'Brawling', 3, 2, 4, 'Slash/Crush', '60/185',  .325, .175, .140, .120, .090,  45, 45,  35, 34, 33, 32,  25, 23, 21, 19,  25, 21, 17, 13,  15, 9, 3, -3) ")
cur.execute("INSERT INTO Weapons VALUES('Yierka-spur', 'Brawling', 2, 1, 3, 'Slash/Puncture/Crush', '18/185',  .250, .150, .125, .125, .075,  40, 40,  35, 34, 33, 32,  25, 23, 21, 19,  30, 26, 22, 18,  0, -6, -12, -18) ") 
     
# One-handed Blunt Weapons	 
cur.execute("INSERT INTO Weapons VALUES('Ball and Chain', 'Blunt Weapons', 9, 6, 5, 'Crush', '75/175',  .400, .300, .225, .260, .180,  15, 15,  20, 19, 18, 17,  27, 25, 23, 21,  35, 31, 27, 34,  30, 24, 18, 12) ")
cur.execute("INSERT INTO Weapons VALUES('Crowbill', 'Blunt Weapons', 5, 3, 4, 'Puncture/Crush', '65/250',  .350, .250, .200, .150, .125,  40, 40,  36, 35, 34, 33,  30, 28, 26, 24,  30, 26, 22, 18,  20, 14, 8, 2) ")
cur.execute("INSERT INTO Weapons VALUES('Cudgel', 'Blunt Weapons', 4, 4, 5, 'Crush', '8/130',  .350, .275, .200, .225, .150,  20, 20,  20, 19, 18, 17,  25, 23, 21, 19,  25, 21, 17, 13,  30, 24, 18, 12) ")
cur.execute("INSERT INTO Weapons VALUES('Leather Whip', 'Blunt Weapons', 5, 2, 4, 'Crush', '10/75',  .275, .150, .090, .100, .035,  35, 35,  25, 24, 23, 22,  20, 18, 16, 14,  25, 21, 17, 13,  15, 9, 3, -3) ")
cur.execute("INSERT INTO Weapons VALUES('Mace', 'Blunt Weapons', 8, 4, 5, 'Crush', '65/250',  .400, .300, .225, .250, .175,  31, 31,  32, 31, 30, 29,  35, 33, 31, 29,  42, 38, 34, 30,  36, 30, 24, 18) ")
cur.execute("INSERT INTO Weapons VALUES('Morning Star', 'Blunt Weapons', 8, 5, 5, 'Puncture/Crush', '60/155',  .410, .290, .250, .275, .200,  33, 33,  35, 34, 33, 32,  34, 32, 30, 28,  42, 38, 34, 30,  37, 31, 25, 19) ")
cur.execute("INSERT INTO Weapons VALUES('War Hammer', 'Blunt Weapons', 7, 4, 5, 'Puncture/Crush', '65/250',  .425, .325, .275, .300, .225,  25, 25,  30, 29, 28, 27,  32, 30, 28, 26,  41, 37, 33, 29,  37, 31, 25, 19) ")

# One-handed Edged Weapons	 
cur.execute("INSERT INTO Weapons VALUES('Arrows/Bolts', 'Edged Weapons', 0, 5, 5, 'Slash/Puncture', '20/40',  .200, .100, .080, .100, .040,  20, 20,  18, 17, 16, 15,  10, 8, 6, 4,  5, 1, -3, -7,  -5, -11, -17, -23) ")
cur.execute("INSERT INTO Weapons VALUES('Backsword', 'Edged Weapons', 5, 5, 5, 'Slash/Puncture/Crush', '75/160',  .440, .310, .225, .240, .150,  38, 38,  38, 37, 36, 35,  34, 32, 30, 28,  38, 34, 30, 26,  34, 28, 22, 16) ")	
cur.execute("INSERT INTO Weapons VALUES('Bastard Sword, One-Handed', 'Edged Weapons', 9, 6, 5, 'Slash/Crush', '75/200',  .450, .325, .275, .250, .180,  30, 30,  31, 30, 29, 28,  31, 29, 27, 25,  32, 28, 24, 20,  31, 25, 19, 13) ")	
cur.execute("INSERT INTO Weapons VALUES('Broadsword', 'Edged Weapons', 5, 5, 5, 'Slash/Puncture/Crush', '75/160',  .450, .300, .250, .225, .200,  36, 36,  36, 35, 34, 33,  36, 34, 32, 30,  37, 33, 29, 25,  36, 30, 24, 18) ")	
cur.execute("INSERT INTO Weapons VALUES('Dagger', 'Edged Weapons', 1, 1, 3, 'Slash/Puncture', '18/195',  .250, .200, .100, .125, .075,  25, 25,  23, 22, 21, 20,  15, 13, 11, 9,  10, 6, 2, -2,  0, -6, -12, -18) ")
cur.execute("INSERT INTO Weapons VALUES('Estoc', 'Edged Weapons', 4, 4, 5, 'Slash/Puncture', '65/160',  .425, .300, .200, .200, .150,  36, 36,  38, 37, 36, 35,  35, 33, 31, 29,  40, 36, 32, 28,  30, 24, 18, 12) ")	
cur.execute("INSERT INTO Weapons VALUES('Falchion', 'Edged Weapons', 5, 5, 5, 'Slash/Crush', '75/160',  .450, .325, .250, .250, .175,  35, 35,  37, 36, 35, 34,  38, 36, 34, 32,  39, 35, 31, 27,  39, 33, 27, 21) ")	
cur.execute("INSERT INTO Weapons VALUES('Handaxe', 'Edged Weapons', 6, 5, 5, 'Slash/Crush', '70/160',  .420, .300, .270, .240, .210,  30, 30,  32, 31, 30, 29,  38, 36, 34, 32,  41, 37, 33, 29,  41, 35, 29, 23) ")	
cur.execute("INSERT INTO Weapons VALUES('Katana, One-Handed', 'Edged Weapons/Two-Handed Weapons', 6, 5, 5, 'Slash', '75/225',  .450, .325, .250, .250, .175,  38, 38,  36, 35, 34, 33,  36, 34, 32, 30,  37, 33, 29, 25,  35, 29, 23, 17) ")	
cur.execute("INSERT INTO Weapons VALUES('Katar', 'Edged Weapons/Brawling', 4, 3, 4, 'Slash/Puncture', '70/175',  .325, .250, .225, .200, .175,  30, 30,  32, 31, 30, 29,  40, 38, 36, 34,  45, 41, 37, 33,  40, 34, 28, 22) ")	
cur.execute("INSERT INTO Weapons VALUES('Longsword', 'Edged Weapons', 5, 4, 5, 'Slash/Puncture/Crush', '65/160',  .425, .275, .225, .200, .175,  41, 41,  42, 41, 40, 39,  43, 41, 39, 37,  37, 33, 29, 25,  35, 29, 23, 17) ")	
cur.execute("INSERT INTO Weapons VALUES('Main Gauche', 'Edged Weapons', 2, 2, 4, 'Slash/Puncture', '18/190',  .275, .210, .110, .125, .075,  27, 27,  25, 24, 23, 22,  20, 18, 16, 14,  20, 16, 12, 8,  20, 14, 8, 2) ")
cur.execute("INSERT INTO Weapons VALUES('Rapier', 'Edged Weapons', 3, 2, 4, 'Slash/Puncture', '30/100',  .325, .225, .110, .125, .075,  45, 45,  40, 39, 38, 37,  30, 28, 26, 24,  35, 31, 27, 23,  15, 9, 3, -3) ")	
cur.execute("INSERT INTO Weapons VALUES('Scimitar', 'Edged Weapons', 5, 4, 5, 'Slash/Puncture/Crush', '60/150',  .375, .260, .210, .200, .165,  30, 30,  31, 30, 29, 28,  30, 28, 26, 24,  30, 26, 22, 18,  30, 24, 18, 12) ")	
cur.execute("INSERT INTO Weapons VALUES('Short Sword', 'Edged Weapons', 4, 3, 4, 'Slash/Puncture/Crush', '70/185',  .350, .240, .200, .150, .125,  40, 40,  36, 35, 34, 33,  30, 28, 26, 24,  25, 21, 17, 13,  25, 19, 13, 7) ")	
cur.execute("INSERT INTO Weapons VALUES('Whip-blade', 'Edged Weapons', 0, 2, 4, 'Slash', '30/100',  .333, .250, .225, .200, .175,  45, 45,  40, 39, 38, 37,  30, 28, 26, 24,  35, 31, 27, 23,  15, 9, 3, -3) ")	

# Polearm Weapons	 
cur.execute("INSERT INTO Weapons VALUES('Halberd', 'Polearm Weapons', 9, 6, 5, 'Slash/Crush/Puncture', '25/150',  .550, .400, .400, .300, .200,  30, 30,  30, 29, 28, 27,  31, 29, 27, 25,  32, 28, 24, 20,  32, 26, 20, 14) ")	
cur.execute("INSERT INTO Weapons VALUES('Hammer of Kai', 'Polearm Weapons', 9, 7, 5, 'Puncture/Crush', '50/190',  .550, .425, .450, .350, .250,  20, 20,  25, 24, 23, 22,  35, 33, 31, 29,  40, 36, 32, 28,  40, 34, 28, 22) ")	
cur.execute("INSERT INTO Weapons VALUES('Jeddart-axe', 'Polearm Weapons', 9, 6, 5, 'Slash/Crush', '25/150',  .550, .425, .425, .325, .250,  30, 30,  32, 31, 30, 29,  30, 28, 26, 24,  40, 36, 32, 28,  30, 24, 18, 12) ")		
cur.execute("INSERT INTO Weapons VALUES('Lance', 'Polearm Weapons', 15, 9, 5, 'Puncture/Crush', '17/105',  .725, .525, .550, .475, .350,  35, 35,  38, 37, 36, 35,  39, 37, 35, 33,  53, 49, 45, 41,  50, 44, 38, 32) ")	
cur.execute("INSERT INTO Weapons VALUES('Naginata', 'Polearm Weapons', 0, 6, 5, 'Slash/Crush/Puncture', '25/150',  .550, .400, .400, .300, .200,  50, 50,  50, 49, 48, 47,  51, 49, 47, 45,  52, 48, 44, 40,  52, 46, 40, 34) ")	
cur.execute("INSERT INTO Weapons VALUES('Pilum', 'Polearm Weapons', 5, 3, 4, 'Slash/Puncture', '50/150',  .350, .250, .225, .175, .060,  30, 30,  27, 26, 25, 24,  22, 20, 18, 16,  23, 19, 15, 11,  15, 9, 3, -3) ")	
cur.execute("INSERT INTO Weapons VALUES('Spear, One-Handed', 'Polearm Weapons', 0, 5, 5, 'Slash/Puncture', '15/130',  .425, .325, .250, .250, .260,  27, 27,  29, 28, 27, 26,  27, 25, 23, 21,  30, 26, 22, 18,  25, 19, 13, 7) ")
cur.execute("INSERT INTO Weapons VALUES('Spear, Two-Handed', 'Polearm Weapons', 0, 5, 5, 'Slash/Puncture', '15/130',  .550, .385, .340, .325, .230,  33, 33,  32, 31, 30, 29,  34, 32, 30, 28,  36, 32, 28, 24,  33, 27, 21, 15) ")	
cur.execute("INSERT INTO Weapons VALUES('Trident, One-Handed', 'Polearm Weapons', 12, 5, 5, 'Slash/Puncture', '70/190',  .425, .350, .260, .230, .150,  31, 31,  31, 30, 29, 28,  34, 32, 30, 28,  42, 38, 34, 30,  29, 23, 17, 11) ")	
cur.execute("INSERT INTO Weapons VALUES('Trident, Two-Handed', 'Polearm Weapons', 12, 6, 5, 'Slash/Puncture', '70/190',  .600, .425, .375, .300, .185,  29, 29,  30, 29, 28, 27,  30, 28, 26, 24,  37, 33, 29, 25,  25, 19, 13, 7) ")	
	
# Ranged Weapons	 
cur.execute("INSERT INTO Weapons VALUES('Composite Bow', 'Ranged Weapons', 3, 6, 3, 'Puncture', '50/225',  .350, .300, .325, .275, .150,  25, 25,  35, 34, 33, 32,  30, 28, 26, 24,  42, 38, 34, 30,  36, 30, 24, 18) ")	
cur.execute("INSERT INTO Weapons VALUES('Long Bow', 'Ranged Weapons', 3, 7, 3, 'Puncture', '60/315',  .400, .325, .350, .300, .175,  25, 25,  33, 32, 31, 30,  29, 27, 25, 23,  42, 38, 34, 30,  38, 32, 26, 20) ")	
cur.execute("INSERT INTO Weapons VALUES('Short Bow', 'Ranged Weapons', 3, 5, 3, 'Puncture', '35/180',  .325, .225, .275, .250, .100,  20, 20,  27, 26, 25, 24,  20, 18, 16, 14,  31, 27, 23, 19,  27, 21, 15, 9) ")	
cur.execute("INSERT INTO Weapons VALUES('Heavy Crossbow', 'Ranged Weapons', 12, 2, 2, 'Puncture', '60/315',  .425, .325, .375, .285, .175,  30, 30,  36, 35, 34, 33,  31, 29, 27, 25,  46, 42, 38, 34,  40, 34, 28, 22) ")	
cur.execute("INSERT INTO Weapons VALUES('Light Crossbow', 'Ranged Weapons', 8, 2, 2, 'Puncture', '60/315',  .350, .300, .325, .275, .150,  25, 25,  31, 30, 29, 28,  25, 23, 21, 19,  39, 35, 31, 27,  32, 26, 20, 14) ")	
	
# Thrown Weapons	
cur.execute("INSERT INTO Weapons VALUES('Bola', 'Thrown Weapons', 0, 5, 3, 'Crush', '12/75',  .205, .158, .107, .118, .067,  25, 25,  20, 19, 18, 17,  30, 28, 26, 24,  25, 21, 17, 13,  35, 29, 23, 17) ")
cur.execute("INSERT INTO Weapons VALUES('Dart', 'Thrown Weapons', 0, 2, 3, 'Puncture', '10/85',  .125, .100, .075, .055, .050,  35, 35,  30, 29, 28, 27,  25, 23, 21, 19,  20, 16, 12, 8,  10, 4, -2, -8) ")
cur.execute("INSERT INTO Weapons VALUES('Discuss', 'Thrown Weapons', 0, 5, 3, 'Crush', '60/195',  .255, .230, .155, .110, .057,  40, 40,  35, 34, 33, 32,  30, 28, 26, 24,  25, 21, 17, 13,  30, 24, 18, 12) ")
cur.execute("INSERT INTO Weapons VALUES('Javelin', 'Thrown Weapons', 0, 4, 3, 'Puncture', '17/105',  .402, .304, .254, .254, .102,  27, 27,  28, 27, 25, 25,  26, 24, 22, 20,  29, 25, 21, 17,  20, 14, 8, 2) ")
cur.execute("INSERT INTO Weapons VALUES('Net', 'Thrown Weapons', 0, 7, 3, 'Unbalance', '45/160',  .050, .050, .030, .030, .010,  25, 25,  25, 24, 23, 22,  30, 28, 26, 24,  40, 36, 32, 28,  50, 44, 38, 32) ")
cur.execute("INSERT INTO Weapons VALUES('Quoit', 'Thrown Weapons', 0, 5, 3, 'Slash', '60/155',  .255, .230, .155, .110, .057,  40, 40,  35, 34, 33, 32,  30, 28, 26, 24,  25, 21, 17, 13,  30, 24, 18, 12) ")
	
# Two-Handed Weapons	
cur.execute("INSERT INTO Weapons VALUES('Battle Axe', 'Two-Handed Weapons', 9, 8, 5, 'Slash/Crush', '70/155',  .650, .475, .500, .375, .275,  35, 35,  39, 38, 37, 36,  43, 41, 39, 37,  50, 46, 42, 38,  50, 44, 38, 32) ")	
cur.execute("INSERT INTO Weapons VALUES('Bastard Sword, Two-Handed', 'Two-Handed Weapons', 9, 6, 5, 'Slash/Crush', '75/200',  .550, .400, .375, .300, .225,  42, 42,  45, 44, 43, 42,  41, 39, 37, 35,  44, 40, 36, 32,  43, 37, 31, 25) ")	
cur.execute("INSERT INTO Weapons VALUES('Claidhmore, new-style', 'Two-Handed Weapons', 11, 8, 5, 'Slash/Crush', '75/200',  .625, .475, .500, .350, .225,  31, 31,  35, 34, 33, 32,  34, 32, 30, 28,  38, 34, 30, 26,  37, 31, 25, 19) ")	
cur.execute("INSERT INTO Weapons VALUES('Claidhmore, old-style', 'Two-Handed Weapons', 11, 8, 5, 'Slash/Crush', '75/200',  .625, .500, .500, .350, .275,  41, 41,  45, 44, 43, 42,  44, 42, 40, 38,  48, 44, 40, 36,  47, 41, 35, 29) ")	
cur.execute("INSERT INTO Weapons VALUES('Flail', 'Two-Handed Weapons', 0, 7, 5, 'Puncture/Crush', '60/150',  .575, .425, .400, .350, .250,  40, 40,  45, 44, 43, 42,  46, 44, 42, 40,  51, 47, 43, 39,  52, 46, 40, 34) ")	
cur.execute("INSERT INTO Weapons VALUES('Flamberge', 'Two-Handed Weapons', 10, 7, 5, 'Slash/Crush', '70/190',  .600, .450, .475, .325, .225,  39, 39,  43, 42, 41, 40,  48, 46, 44, 42,  50, 46, 42, 38,  44, 38, 32, 26) ")	
cur.execute("INSERT INTO Weapons VALUES('Katana, Two-Handed', 'Two-Handed Weapons', 6, 6, 5, 'Slash', '75/225',  .575, .425, .400, .325, .210,  39, 39,  41, 40, 39, 38,  40, 38, 36, 34,  41, 37, 33, 29,  39, 33, 27, 21) ")	
cur.execute("INSERT INTO Weapons VALUES('Maul', 'Two-Handed Weapons', 8, 7, 5, 'Crush', '60/145',  .550, .425, .425, .375, .300,  31, 31,  36, 35, 34, 33,  44, 42, 40, 38,  52, 48, 44, 40,  54, 48, 42, 36) ")	
cur.execute("INSERT INTO Weapons VALUES('Military Pick', 'Two-Handed Weapons', 8, 7, 5, 'Puncture/Crush', '60/150',  .500, .375, .425, .375, .260,  25, 25,  30, 29, 28, 27,  40, 38, 36, 34,  40, 36, 32, 28,  47, 41, 35, 29) ")	
cur.execute("INSERT INTO Weapons VALUES('Quarterstaff', 'Two-Handed Weapons', 5, 5, 5, 'Crush', '20/140',  .450, .350, .325, .175, .100,  25, 25,  26, 25, 24, 23,  25, 23, 21, 19,  26, 22, 18, 14,  24, 18, 12, 6) ")
cur.execute("INSERT INTO Weapons VALUES('Runestaff', 'Two-Handed Weapons', 5, 5, 5, 'Crush', '20/270',  .250, .200, .150, .150, .075,  10, 10,  15, 14, 13, 12,  10, 8, 6, 4,  15, 11, 7, 3,  10, 4, -2, -8) ")
cur.execute("INSERT INTO Weapons VALUES('Two-Handed Sword', 'Two-Handed Weapons', 0, 8, 5, 'Slash/Crush', '75/200',  .625, .500, .500, .350, .275,  41, 41,  45, 44, 43, 42,  44, 42, 40, 38,  48, 44, 40, 36,  47, 41, 35, 29) ")	
cur.execute("INSERT INTO Weapons VALUES('War Mattock', 'Two-Handed Weapons', 8, 7, 5, 'Crush', '60/145',  .550, .450, .425, .375, .275,  32, 32,  37, 36, 35, 34,  44, 42, 40, 38,  48, 44, 40, 36,  53, 47, 41, 35) ")	

# Unarmed Combat Gear
cur.execute("INSERT INTO Weapons VALUES('UAC Boots', 'UAC Weapons', 2, 0, 0, 'Crush', '--/--',  0, 0, 0, 0, 0,  0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0) ")
cur.execute("INSERT INTO Weapons VALUES('UAC Gloves', 'UAC Weapons', 2, 0, 0, 'Crush', '--/--',  0, 0, 0, 0, 0,  0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0) ")	

# UAC Attacks
cur.execute("INSERT INTO Weapons VALUES('Jab', 'UAC Attack', 0, 2, 2, 'Jab', '--/--',  .100, .075, .060, .050, .035,  0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0) ")
cur.execute("INSERT INTO Weapons VALUES('Punch', 'UAC Attack', 0, 3, 3, 'Punch', '--/--',  .275, .250, .200, .170, .140,  0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0) ")
cur.execute("INSERT INTO Weapons VALUES('Grapple', 'UAC Attack', 0, 3, 3, 'Grapple', '--/--',  .250, .200, .160, .120, .100,  0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0) ")
cur.execute("INSERT INTO Weapons VALUES('Kick', 'UAC Attack', 0, 4, 4, 'Kick', '--/--',  .400, .350, .300, .250, .200,  0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0) ")

# Creature Weapons
cur.execute("INSERT INTO Weapons VALUES('Bite', 'Creature Weapons', 0, 5, 5, 'Slash/Crush/Puncture', '--/--',  .400, .375, .375, .325, .300,  39, 39,  35, 34, 33, 32,  30, 28, 26, 24,  32, 28, 24, 20,  25, 19, 13, 7) ")	
cur.execute("INSERT INTO Weapons VALUES('Charge', 'Creature Weapons', 0, 5, 5, 'Crush', '--/--',  .175, .175, .150, .175, .150,  37, 37,  32, 31, 30, 29,  31, 29, 27, 25,  37, 33, 29, 25,  31, 25, 19, 13) ")
cur.execute("INSERT INTO Weapons VALUES('Claw', 'Creature Weapons', 0, 5, 5, 'Slash/Crush/Puncture', '--/--',  .225, .200, .200, .175, .175,  41, 41,  38, 37, 36, 35,  29, 27, 25, 23,  31, 27, 23, 19,  25, 19, 13, 7) ")		
cur.execute("INSERT INTO Weapons VALUES('Ensnare', 'Creature Weapons', 0, 5, 5, 'Grapple', '--/--',  .275, .225, .200, .175, .150,  25, 25,  31, 30, 29, 28,  40, 38, 36, 34,  38, 34, 30, 26,  50, 44, 38, 32) ")	
cur.execute("INSERT INTO Weapons VALUES('Nip', 'Creature Weapons', 0, 5, 5, 'Puncture', '--/--',  .125, .105, .090, .090, .100,  35, 35,  40, 39, 38, 37,  25, 23, 21, 29,  28, 24, 20, 16,  20, 14, 8, 2) ")
cur.execute("INSERT INTO Weapons VALUES('Pound', 'Creature Weapons', 0, 5, 5, 'Crush', '--/--',  .425, .350, .325, .425, .275,  38, 38,  45, 44, 43, 42,  46, 44, 42, 40,  50, 46, 42, 38,  50, 44, 38, 32) ")	
cur.execute("INSERT INTO Weapons VALUES('Stomp', 'Creature Weapons', 0, 5, 5, 'Crush', '--/--',  .350, .325, .250, .225, .225,  39, 39,  45, 44, 43, 42,  35, 33, 31, 29,  45, 41, 37, 33,  33, 27, 21, 15) ")		



# Creates the Armor table. 
cur.execute("CREATE TABLE Armor (name, AG, ASG,  roundtime, action_penalty, normal_cva, magic_cva,  base_weight,  minor_spiritual_spell_hindrance, major_spiritual_spell_hindrance, cleric_spell_hindrance,   minor_elemental_spell_hindrance, minor_mental_spell_hindrance,  major_elemental_spell_hindrance, major_mental_spell_hindrance,  savant_spell_hindrance, ranger_spell_hindrance, sorcerer_spell_hindrance, wizard_spell_hindrance, bard_spell_hindrance, empath_spell_hindrance, paladin_spell_hindrance,  max_spell_hindrance, dodging_hindrance_factor ) ")  	
	
# Cloth Armor	
cur.execute("INSERT INTO Armor VALUES('Clothing', 1, 1,  0, 0, 25, 20, 0,  0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0,  0, 1.00) ")
cur.execute("INSERT INTO Armor VALUES('Robes', 1, 2,  0, 0, 25, 15, 8,  0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0,  0, 1.00) ")
	
# Soft Leather Armor	
cur.execute("INSERT INTO Armor VALUES('Light Leather', 2, 5,  0, 0, 20, 15, 10,  0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0,  0, 1.00) ")
cur.execute("INSERT INTO Armor VALUES('Full Leather', 2, 6,  1, 0, 19, 14, 13,  0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0,  0, 1.00) ")
cur.execute("INSERT INTO Armor VALUES('Reinforced Leather', 2, 7,  2, -5, 18, 13, 15,  0, 0, 0,  0, 0, 2, 2,  2, 0, 1, 2, 0, 0, 0,  4, 0.98) ")
cur.execute("INSERT INTO Armor VALUES('Double Leather', 2, 8,  2, -6, 17, 12, 16,  0, 0, 0,  0, 2, 4, 4,  4, 0, 2, 4, 2, 0, 0,  6, 0.97) ")

# Hard Leather Armor	
cur.execute("INSERT INTO Armor VALUES('Leather Breastplate', 3, 9,  3, -7, 11, 5, 16,  3, 4, 4,  4, 4, 6, 6,  6, 3, 5, 6, 3, 4, 2,  16, 0.97) ")
cur.execute("INSERT INTO Armor VALUES('Cuirbouilli Leather', 3, 10,  4, -8, 10, 4, 17,  4, 5, 5,  5, 5, 7, 7,  7, 4, 6, 7, 3, 5, 3,  20, 0.96) ")
cur.execute("INSERT INTO Armor VALUES('Studded Leather', 3, 11,  5, -10, 9, 3, 20,  5, 6, 6,  6, 6, 9, 9,  9, 5, 8, 9, 3, 6, 4,  24, 0.95) ")
cur.execute("INSERT INTO Armor VALUES('Brigandine Armor', 3, 12,  6, -12, 8, 2, 25,  6, 7, 7,  7, 7, 12, 12,  12, 6, 11, 12, 7, 7, 5,  28, 0.94) ")

# Chain Armor	
cur.execute("INSERT INTO Armor VALUES('Chain Mail', 4, 13,  7, -13, 1, -6, 25,  7, 8, 8,  8, 8, 16, 16,  16, 7, 16, 16, 8, 8, 6,  40, 0.94) ")
cur.execute("INSERT INTO Armor VALUES('Double Chain', 4, 14,  8, -14, 0, -7, 25,  8, 9, 9,  9, 9, 20, 20,  20, 8, 18, 20, 8, 9, 7,  45, 0.93) ")
cur.execute("INSERT INTO Armor VALUES('Augmented Chain', 4, 15,  8, -16, -1, -8, 26,  9, 11, 11,  10, 10, 25, 25,  25, 9, 22, 25, 8, 11, 8,  55, 0.92) ")
cur.execute("INSERT INTO Armor VALUES('Chain Hauberk', 4, 16,  9, -18, -2, -9, 27,  11, 14, 14,  12, 15, 30, 30,  30, 11, 26, 30, 15, 14, 9,  60, 0.91) ")

# Plate Armor	
cur.execute("INSERT INTO Armor VALUES('Metal Breastplate', 5, 17,  9, -20, -10, -18, 23,  16, 25, 25,  16, 21, 35, 35,  35, 21, 29, 35, 21, 25, 10,  90, 0.90) ")
cur.execute("INSERT INTO Armor VALUES('Augmented Plate', 5, 18,  10, -25, -11, -19, 25,  17, 28, 28,  18, 21, 40, 40,  40, 24, 33, 40, 21, 28, 11,  92, 0.88) ")
cur.execute("INSERT INTO Armor VALUES('Half Plate', 5, 19,  11, -30, -12, -20, 50,  18, 32, 32,  20, 21, 45, 45,  45, 27, 39, 45, 21, 32, 12,  94, 0.85) ")
cur.execute("INSERT INTO Armor VALUES('Full Plate', 5, 20,  12, -35, -13, -21, 75,  20, 45, 45,  22, 50, 50, 50,  50, 30, 48, 50, 50, 45, 13,  96, 0.83) ")


# Creates the Shields table. Contains a list of all the shield types in the game
cur.execute("CREATE TABLE Shields (name, size, base_weight,  melee_size_modifer, ranged_size_modifer, ranged_size_bonus,  dodging_shield_factor, dodging_size_penalty ) ")  

cur.execute("INSERT INTO Shields VALUES('Small Shield', 'small', 5,  0.85, 1.20, -8,  0.78, 0) ")	
cur.execute("INSERT INTO Shields VALUES('Medium Shield', 'medium', 8,  1.00, 1.50, 0,  0.70, 0) ")	
cur.execute("INSERT INTO Shields VALUES('Large Shield', 'large', 10,  1.15, 1.80, 8,  0.62, 5) ")	
cur.execute("INSERT INTO Shields VALUES('Tower Shield', 'tower', 12,  1.30, 2.10, 16,  0.54, 10) ")	


# Creates the effects table. An effect is any sort of temporary effect that modifies the character in some way.
# Effects are setup in the Loadout panel and used as part of the calulcation of the Progression panel
# FIELDS
# name 				- name of the effect
# type 				- the type category of the effect. This could be a spell's spell circle, or an "Maneuver" type effect
# details 			- a description of what the effect does
# effect_tags 		- A | (pipe) seperated list of what attributes the effect modifies. A $ at the end of the effect means the effect only modifies the attribute with scaling, a * means
#					  it the effect modifies the attribute by default and by scaling, nothing on the end means it modifies an attribute but doesn't scale
# scaling_tags 		- NONE means the effect doesn't scale off anything. Otherwise it is a | (pipe) seperated list of things the effect will scale off of in the format of 
#	 				  <scales by>:<value range>.  A single value in <value range> means the scaling effect is from 0 to that value.
# function 			- The name of the function that will perform all the scaling calculations related to this effect
# override_options 	- A | (pipe) seperated list of parameters that need to be taken into consideration when calculating or display the effect
cur.execute("CREATE TABLE Effects (name, type, details, effect_tags, scaling_tags, function, override_options ) ")  


# Minor Spiritual (100s)
cur.execute("INSERT INTO Effects VALUES('Spirit Warding I (101)', 'MnS Spell', '+10 Spirit TD, +10 Bolt DS',  'TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer|DS_Bolt',  'NONE',  'Calculate_101',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Spirit Barrier (102)', 'MnS Spell', '+20 DS/UDF, -20 Melee AS/UAF\n+1 DS/UDF and -1 Melee AS/UAF per 2 Spell Research, Minor Spiritual ranks above 2 up to character level\n+1 mana cost per 6 Spell Research, Minor Spirit ranks above 2 up to character level',  'DS_All|AS_Melee|UAF|UDF|Mana_Cost',  'Spell Research, Minor Spiritual ranks:303', 'Calculate_102',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Spirit Defense (103)', 'MnS Spell', '+10 DS',  'DS_All',  'NONE',  'Calculate_103',  'NONE' ) ")
#cur.execute("INSERT INTO Effects VALUES('Disease Resistance (104)', 'MnS Spell', 'Extra warding against Disease\n+1 TD bonus on extra warding attempt per 2 Spiritual Lore, Blessings ranks ',  'TD_Disease',  'Spiritual Lore, Blessings ranks:202',  'Calculate_104',  'NONE' ) ")
#cur.execute("INSERT INTO Effects VALUES('Poison Resistance (105)', 'MnS Spell', 'Extra warding attempt against Posion\n+1 TD bonus on extra warding attempt per 2 Spiritual Lore, Blessings ranks ',  'TD_Posion',  'Spiritual Lore, Blessings ranks:202',  'Calculate_105',  'NONE' ) ")
# cur.execute("INSERT INTO Effects VALUES('Spirit Fog (106)', 'MnS Spell', '+30 DS to all creatures and characters\nHides caster for 30 seconds at 40 Spiritual Lore, Summoning ranks ',  'DS_All|Unique1',  'Spiritual Lore, Summoning ranks:202',  'Calculate_106',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Spirit Warding II (107)', 'MnS Spell', '+15 Spirit TD, +25 Bolt DS',  'TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer|DS_Bolt',  'NONE',  'Calculate_107',  'NONE' ) ")
# cur.execute("INSERT INTO Effects VALUES(\"Fasthr's Reward (115)\", 'MnS Spell', 'Chance for extra warding attempt. 50% spirit, 25% semi-spirit, 12.5% non-spirit\n+1% chance per seed 1 summation of Spiritual Lore, Blessings ranks',  'Unique1',  'Spiritual Lore, Blessings ranks:202',  'Calculate_115',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Spirit Strike (117)', 'MnS Spell', '+75 AS on next melee, ranged, bolt, or UAF attack',  'AS_All|UAF',  'NONE',  'Calculate_117',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Lesser Shroud (120)', 'MnS Spell', '+15 DS, +20 Spirit TD\n+1 DS 2 Spell Research, Minor Spiritual ranks above 20 up to character level\n+1 mana cost per 6 Spell Research, Minor Spirit ranks above 2 up to character level',  'DS_All|TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer|Mana_Cost',  'Spell Research, Minor Spiritual ranks:303',  'Calculate_120',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Wall of Force (140)', 'MnS Spell', '+100 DS',  'DS_All',  'NONE',  'Calculate_140',  'NONE' ) ")


# Major Spiritual (200s)
cur.execute("INSERT INTO Effects VALUES('Spirit Shield (202)', 'MjS Spell', '+10 DS\nIf self cast, +1 DS per 2 Spell Research, Major Spiritual ranks above 2 up to character level\n+1 mana cost per 9 Spell Research, Major Spiritual ranks above 2 up to character level',  'DS_All|Mana_Cost',  'Spell Research, Major Spiritual ranks:303',  'Calculate_202',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Manna (203)', 'MjS Spell', 'Regain 1 Spirit per 4 minutes\n+1 bonus to Mana Recovery with an additional +1 per seed 4 summation of Spell Research, Major Spiritual ranks\n+5 maximum Mana per seed 10 summation for Spiritual Lore, Blessing ranks',  'Mana_Recovery|Resource_Mana|Unique1',  'Spell Research, Major Spiritual ranks:303',  'Calculate_203',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Bravery (211)', 'MjS Spell', '+15 melee AS, ranged AS, bolt AS, and UAF\n+3 phantom levels against sheer fear',  'AS_All|UAF|Sheer_Fear',  'NONE',  'Calculate_211',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Heroism (215)', 'MjS Spell', '+25 melee AS, ranged AS, bolt AS, and UAF\n+3 phantom levels against sheer fear\n+1 Mana and Health per minute\nCan cast a group version with a 1 minute duration at 65 Spiritual Lore, Blessing ranks\n+1 AS when self-cast for every 10 Spiritual Lore, Blessing ranks',  'AS_All|UAF|Sheer_Fear',  'Spiritual Lore, Blessings ranks:202',  'Calculate_215',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Spell Shield (219)', 'MjS Spell', '+30 bolt DS\n+30 Spirit TD',  'DS_Bolt|TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer',  'NONE',  'Calculate_219',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Spriti Slayer (240)', 'MjS Spell', 'Spell is recast with a +25 bonus to Bolt AS or Spiritual CS\n+1 Bolt AS and Spiritual CS per summation 5 seed of Spiritual Mana Control ranks',  'AS_Bolt|CS_Elemental|CS_Mental|CS_Spiritual|CS_Sorcerer',  'Spiritual Mana Control ranks:303',  'Calculate_240',  'NONE' ) ")

# Cleric Base (300s)
cur.execute("INSERT INTO Effects VALUES('Prayer of Protection (303)', 'Clrc Spell', '+10 all DS\n+1 DS per 2 Spell Research, Cleric ranks above 3 up to character level or 99 ranks\n+1 mana cost per 6 Spell Research, Cleric ranks above 2 up to character level or 99 ranks',  'DS_All',  'Spell Research, Cleric ranks:303',  'Calculate_303',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Benediction (307)', 'Clrc Spell', '+5 all AS. This increases by 1 for every two Cleric Base ranks trained past rank 7 with a maximum bonus of +15 AS at rank 27\nAdditionally, there is a +1 bolt AS bonus that is self-cast only for every two ranks past rank 27. The maximum bolt AS bonus is +51 at level 99 with 99 spell ranks\n+5 melee and ranged DS at spell rank 7. This increases by 1 for every two Cleric Base ranks trained past rank 7 with a maximum bonus of +15 DS at rank 27\n +1 additional mana cost per bonus point past rank 7. The maximum cost is 53 mana at level 99 with 99 spell ranks\nChance for the group to receive a +15 AS bonus on a given attack at a chance of 1% per seed 6 summation of Spiritual Lore, Blessing ranks',  'DS_Melee|DS_Ranged|AS_Melee|AS_Ranged|AS_Bolt|UAF|Mana_Cost',  'Spell Research, Cleric ranks:303|Spiritual Lore, Blessings ranks:202',  'Calculate_307',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Warding Sphere (310)', 'Clrc Spell', '+10 DS, +10 Spirit TD\n+1 DS, Spirit TD, and Mana Cost per Spell Research, Cleric rank above 10 to a maximum of +20 at 20 ranks',  'DS_All|TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer|Mana_Cost',  'Spell Research, Cleric ranks:303',  'Calculate_310',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Prayer (313)', 'Clrc Spell', '+10 Spirit TD\n+10 all DS at 35 Spell Research, Cleric ranks and increases by +1 per rank above 35 up to character level\n+1 mana cost per 6 Spell Research, Minor Spirit ranks above 35 up to character level',  'DS_All|TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer|Mana_Cost|Manuever_Defense',  'Spell Research, Cleric ranks:303',  'Calculate_313',  'NONE' ) ")


# Minor Elemental (400s)
cur.execute("INSERT INTO Effects VALUES('Elemental Defense I (401)', 'MnE Spell', '+5 all DS, +5 Elemental TD',  'DS_All|TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer',  'NONE',  'Calculate_401',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Elemental Defense II (406)', 'MnE Spell', '+10 all DS, +10 Elemental TD',  'DS_All|TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer',  'NONE',  'Calculate_406',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Elemental Defense III (414)', 'MnE Spell', '+20 all DS, +15 Elemental TD',  'DS_All|TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer',  'NONE',  'Calculate_414',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Elemental Targeting (425)', 'MnE Spell', '+25 all AS, UAF and Elemental CS\n+1 all AS, UAF and Elemental CS per 2 Spell Research, Minor Elemental ranks above 25 up to a +50 at 75 ranks',  'AS_All|CS_Elemental|CS_Mental|CS_Spiritual|CS_Sorcerer',  'Spell Research, Minor Elemental ranks:303',  'Calculate_425',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Elemental Barrier (430)', 'MnE Spell', '+15 all DS and Elemental TD\n+1 all DS and Elemental TD per 2 Spell Research, Minor Elemental ranks above 30',  'DS_All|TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer|CS_Elemental',  'Spell Research, Minor Elemental ranks:303',  'Calculate_430',  'NONE' ) ")


# Major Elemental (500s)
cur.execute("INSERT INTO Effects VALUES(\"Thurfel\'s Ward (503)\", 'MjE Spell', '+20 all DS\n+1 all DS when self-cast per 4 Spell Research, Major Elemental ranks above 3\n+1 Mana Cost per 12 Spell Research, Major Elemental rank above 3\nTraining in Elemental Lore, Earth will give a chance of seed 10 summation of ranks to gain an additional +20 DS on any single attack',  'DS_All|Mana_Cost',  'Spell Research, Major Elemental ranks:303|Elemental Lore, Earth ranks:202',  'Calculate_503',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Elemental Deflection (507)', 'MjE Spell', '+20 all DS\n+1 all DS per 2 Spell Research, Major Elemental ranks above 7\n+1 Mana Cost per 12 Spell Research, Major Elemental rank above 7',  'DS_All|Mana_Cost',  'Spell Research, Major Elemental ranks:303',  'Calculate_507',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Elemental Bias (508)', 'MjE Spell', '+20 elemental TD',  'TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer',  'NONE',  'Calculate_508',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Strength (509)', 'MjE Spell', '+15 melee AS, UAF\n+1 melee AS, UAF when self-cast per seed 4 summation of Elemental Lore, Earth ranks',  'AS_Melee|UAF',  'Elemental Lore, Earth ranks:202',  'Calculate_509',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Elemental Focus (513)', 'MjE Spell', '+20 bolt AS\n+1 bolt AS when self-cast per 2 Spell Research, Major Elemental ranks above 13 capped at character level\nAdditional bolt spell cast at the same target will cause a flare that increases bolt AS',  'AS_Bolt',  'Spell Research, Major Elemental ranks:303',  'Calculate_513',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Temporal Revision (540)', 'MjE Spell', '+200 all DS',  'DS_All',  'NONE',  'Calculate_540',  'NONE' ) ")


# Ranger Base (600s)
cur.execute("INSERT INTO Effects VALUES('Natural Colors (601)', 'Rngr Spell', '+10 all DS\n+1 DS per seed 5 summation of Spiritual Lore, Blessings ranks',  'DS_All',  'Spiritual Lore, Blessings ranks:202',  'Calculate_601',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Resist Elements (602)', 'Rngr Spell', '+10 fire, ice, and electrical bolt DS\n+1 bolt DS when self-cast per seed 5 summation of Spiritual Lore, Blessings ranks',  'DS_Bolt',  'Spiritual Lore, Blessings ranks:202',  'Calculate_602',  'vs_fire|vs_ice|vs_electrical' ) ")
cur.execute("INSERT INTO Effects VALUES(\"Phoen\'s Strength (606)\", 'Rngr Spell', '+10 melee AS, UAF',  'AS_Melee|UAF',  'NONE',  'Calculate_606',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Camouflage (608)', 'Rngr Spell', '+30 all AS, UAF on next attack',  'AS_All|UAF',  'NONE',  'Calculate_608',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Self Control (613)', 'Rngr Spell', '+20 melee DS, Spiritual TD\n+1 Spiritual TD per seed 5 summation of Spiritual Lore, Blessings ranks\n+1 melee DS per 2 Spell Research, Ranger Base ranks above 13 capped at +63',  'DS_Melee|TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer',  'Spell Research, Ranger ranks:202|Spiritual Lore, Blessings ranks:202',  'Calculate_613',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Mobility (618)', 'Rngr Spell', '+20 phantom Dodging ranks\n+1 phantom Dodging rank per Spell Research, Ranger Base rank over 18\n+1 Mana Cost per 4 Spell Research, Ranger Base ranks above 18',  'Skill_Phantom_Ranks_Dodging|Mana_Cost',  'Spell Research, Ranger ranks:202',  'Calculate_618',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES(\"Nature\'s Touch (625)\", 'Rngr Spell', 'May cast Ranger spells indoors at full power\n+1 Spiritual TD\n+1 Spiritual TD per 2 Spell Research, Ranger Base ranks over 25 up to a maximum of a +12 bonus to TD at 49 rank',  'TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer',  'Spell Research, Ranger ranks:202',  'Calculate_625',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Wall of Thorns (640)', 'Rngr Spell', '+20 all DS\ngrants a 20% chance of the thorns blocking an incoming attack completely\n25% chance of poisoning the attacker on a successful block',  'DS_All',  'NONE',  'Calculate_640',  'NONE' ) ")
#cur.execute("INSERT INTO Effects VALUES('Assume Aspect (650) Bear', 'Rngr Spell', '+20 increase to Constitution stat\nIncreas maximum Health by +25\n+1 increase to Constitution stat per seed 2 summation of Spiritual Lore, Blessings ranks\n+1 increase to max Health per seed 1 summation of Spiritual Lore, Summoning ranks',  'Statistic_Constitution|Resource_Maximum_Health',  'Spiritual Lore, Blessings ranks:202|Spiritual Lore, Summoning ranks:202',  'Calculate_650_Bear',  'NONE' ) ")
#cur.execute("INSERT INTO Effects VALUES('Assume Aspect (650) Burgee', 'Rngr Spell', '+10% Block chance\n+1% Block chance per seed 2 summation of Spiritual Lore, Blessings ranks',  'Block_Chance',  'Spiritual Lore, Summoning ranks:202',  'Calculate_650_Burgee',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Assume Aspect (650) Hawk', 'Rngr Spell', '+20 Perception ranks\n+1 Perception rank per seed 2 summation of Spiritual Lore, Summoning ranks',  'Skill_Ranks_Perception',  'Spiritual Lore, Summoning ranks:202',  'Calculate_650_Hawk',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Assume Aspect (650) Jackal', 'Rngr Spell', '+20 Ambush ranks\n+1 Ambush rank per seed 2 summation of Spiritual Lore, Summoning ranks',  'Skill_Ranks_Ambush',  'Spiritual Lore, Summoning ranks:202',  'Calculate_650_Jackal',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Assume Aspect (650) Lion', 'Rngr Spell', '+20 increase to Influence and Strength stats\n+1 increase to Influence and Strength stats per seed 2 summation of Spiritual Lore, Blessings ranks',  'Statistic_Influence|Statistic_Strength',  'Spiritual Lore, Blessings ranks:202',  'Calculate_650_Lion',  'NONE' ) ")
#cur.execute("INSERT INTO Effects VALUES('Assume Aspect (650) Mantis', 'Rngr Spell', '+10% Parry chance\n+1% Parry chance per seed 2 summation of Spiritual Lore, Blessings ranks',  'Parry_Chance',  'Spiritual Lore, Summoning ranks:202',  'Calculate_650_Mantis',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Assume Aspect (650) Owl', 'Rngr Spell', '+20 increase to Aura and Wisdom stats\n+1 increase to Aura and Wisdom stats per seed 2 summation of Spiritual Lore, Blessings ranks',  'Statistic_Aura|Statistics_Wisdom',  'Spiritual Lore, Blessings ranks:202',  'Calculate_650_Owl',  'NONE' ) ")
#cur.execute("INSERT INTO Effects VALUES('Assume Aspect (650) Panther', 'Rngr Spell', '+20 Stalking and Hiding ranks\n+1 Stalking and Hiding rank per seed 2 summation of Spiritual Lore, Summoning ranks',  'Skill_Ranks_Stalking and Hiding',  'Spiritual Lore, Summoning ranks:202',  'Calculate_650_Panther',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Assume Aspect (650) Porcupine', 'Rngr Spell', '+20 increase to Logic stat\n+1 increase to Logic stat per seed 2 summation of Spiritual Lore, Blessings ranks',  'Statistic_Logic',  'Spiritual Lore, Blessings ranks:202|Spiritual Lore, Summoning ranks:202',  'Calculate_650_Porcupine',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Assume Aspect (650) Rat', 'Rngr Spell', '+20 increase to Agility and Discipline stats ranks\n+1 increase to Agility and Discipline stats per seed 2 summation of Spiritual Lore, Blessings ranks',  'Statistic_Agility|Statistic_Discipline',  'Spiritual Lore, Blessings ranks:202',  'Calculate_650_Rat',  'NONE' ) ")
#cur.execute("INSERT INTO Effects VALUES('Assume Aspect (650) Serpent', 'Rngr Spell', '+10% Evade chance\n+1% Evade chance per seed 2 summation of Spiritual Lore, Blessings ranks',  'Evade_Chance',  'Spiritual Lore, Summoning ranks:202',  'Calculate_650_Serpent',  'NONE' ) ")
#cur.execute("INSERT INTO Effects VALUES('Assume Aspect (650) Spider', 'Rngr Spell', '+20 Climbing ranks\n+1 Climbing rank per seed 2 summation of Spiritual Lore, Summoning ranks\nDouble Wed (108) charges and Web bolt causes an addition -25 (-50 total) Spiritual TD pushdown',  'Skill_Ranks_Climbing|Unique1',  'Spiritual Lore, Summoning ranks:202',  'Calculate_650_Spider',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Assume Aspect (650) Wolf', 'Rngr Spell', '+20 increase to Dexterity and Intuition stats\n+1 increase to Dexterity and Intuition stats per seed 2 summation of Spiritual Lore, Blessings ranks',  'Statistic_Dexterity|Statistic_Intuition',  'Spiritual Lore, Blessings ranks:202',  'Calculate_650_Wolf',  'NONE' ) ")
#cur.execute("INSERT INTO Effects VALUES('Assume Aspect (650) Yierka', 'Rngr Spell', '+20 Survival ranks\n+1 Survival rank per seed 2 summation of Spiritual Lore, Summoning ranks\n25% RT reduction when consuming any healing herbs or potions, sensing area conditions, or attempting to forage\n+3% addition RT reduction per seed 1 summation of Spiritual Lore, Blessing ranks',  'Skill_Ranks_Surival',  'Spiritual Lore, Blessings ranks:202|Spiritual Lore, Summoning ranks:202',  'Calculate_650_Yierka',  'NONE' ) ")


# Sorcerer Base (700s)
cur.execute("INSERT INTO Effects VALUES('Cloak of Shadows (712)', 'Sorc Spell', '+25 all DS, +20 all TD\n+1 all DS per Spell Research, Sorcerer Base rank above 12 capped at +88 DS (+113 total)\n+1 all TD per 10 Spell Research, Sorcerer Base ranks above 12 capped at +8 DS (+28 total)\n+1 Mana Cost per 3 Spell Research, Sorcerer Base rank above 12',  'DS_All|TD_All|Mana_Cost',  'Spell Research, Sorcerer ranks:303',  'Calculate_712',  'NONE' ) ")


# Wizard Base (900s)
cur.execute("INSERT INTO Effects VALUES('Minor Elemental Edge (902) EVOKE', 'Wiz Spell', '+10 skill bonus to a specific weapon type\n+1 skill bonus per seed 7 summation of Elemental Lore, Earth ranks',  'Skill_Bonus_Brawling|Skill_Bonus_Edged_Weapons|Skill_Bonus_Blunt_Weapons|Skill_Bonus_Two-Handed_Weapons|Skill_Bonus_Ranged_Weapons|Skill_Bonus_Thrown_Weapons|Skill_Bonus_Polearm_Weapons',  'Elemental Lore, Earth ranks:202',  'Calculate_902',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Prismatic Guard (905)', 'Wiz Spell', '+5 melee and ranged DS, +20 bolt DS\n+1 all DS per seed 5 summation of Elemental Lore, Earth ranks\n+1 all DS per 4 Spell Research, Wizard Base ranks over 5\n+1 Mana Cost per 15 Spell Research, Wizard Base ranks above 5',  'DS_Melee|DS_Ranged|DS_Bolt|Mana_Cost',  'Spell Research, Wizard ranks:303|Elemental Lore, Earth ranks:202',  'Calculate_905',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Mass Blur (911)', 'Wiz Spell', '+20 phantom Dodging ranks\n+1 phantom Dodging rank for the caster only per seed 1 summation of Elemental Lore, Air ranks',  'Skill_Phantom_Ranks_Dodging|Mana_Cost',  'Elemental Lore, Air ranks:202',  'Calculate_911',  'ignore_enhancive_limit' ) ")
cur.execute("INSERT INTO Effects VALUES(\"Melgorehn\'s Aura (913)\", 'Wiz Spell', '+10 all DS, +20 Elemental TD\n+1 all DS per Spell Research, Wizard Base rank above 13\n+1 Elemental TD per 3 Spell Research, Wizard Base ranks above 13\n+1 Mana Cost per 3 Spell Research, Wizard Base rank above 13',  'DS_All|TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer|Mana_Cost',  'Spell Research, Wizard ranks:303',  'Calculate_913',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES(\"Wizard\'s Shield (919)\", 'Wiz Spell', '+50 DS',  'DS_All',  'NONE',  'Calculate_919',  'NONE' ) ")


# Bard Base (1000s)
cur.execute("INSERT INTO Effects VALUES('Fortitude Song (1003)', 'Spellsong', '+10 all DS',  'DS_All',  'NONE',  'Calculate_1003',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES(\"Kai\'s Triumph Song (1007)\", 'Spellsong', '+10 all AS\n+1 all AS per Spell Research, Bard Base rank above 7 capped at +20\n+1 all AS per seed 3 summation of Mental Lore, Telepathy ranks\nMaximum AS provided is capped at +31',  'AS_All',  'Spell Research, Bard ranks:202|Mental Lore, Telepathy ranks:202', 'Calculate_1007', 'NONE'  ) ")
cur.execute("INSERT INTO Effects VALUES('Song of Valor (1010)', 'Spellsong', '+10 all DS\n+1 all DS per 2 Spell Research, Bard Base ranks above 10\n+1 Mana Cost per 2 Spell Research, Bard Base rank above 13',  'DS_All',  'Spell Research, Bard ranks:202',  'Calculate_1010',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Song of Mirrors (1019)', 'Spellsong', '+20 phantom Dodging ranks\n+1 phantom Dodging rank per 2 Spell Research, Bard Base ranks over 19\n+1 Mana Cost per 5 Spell Research, Bard Base ranks above 19',  'Skill_Phantom_Ranks_Dodging|Mana_Cost',  'Spell Research, Bard ranks:202',  'Calculate_1019',  'ignore_enhancive_limit' ) ")
cur.execute("INSERT INTO Effects VALUES('Song of Tonis (1035)', 'Spellsong', '+20 phantom Dodging ranks, -1 Haste effect\n+1 phantom Dodging rank at the following Elemental Lore, Air rank inverals: 1,2,3,5,8,10,14,17,21,26,31,36,42,49,55,63,70,78,87,96\nHaste effect improves to -2 at Elemental Lore, Air rank 30 and -3 at Elemental Lore, Air rank 75\nThe bonus is +1 second per rank for the first 20 ranks of ML, Telepathy. Every 2 lore ranks thereafter will increase the spellsong duration +1 second. The maximum duration (base + lore bonus) with 100 ranks of ML, Telepathy is 120 seconds.',  'Skill_Phantom_Ranks_Dodging|Roundtime',  'Elemental Lore, Air ranks:202|Mental Lore, Telepathy ranks:202',  'Calculate_1035',  'NONE' ) ")


# Empath Base (1100s)
cur.execute("INSERT INTO Effects VALUES('Empathic Focus (1109)', 'Emp Spell', '+15 Spiritual TD, +25 all DS, +15 melee AS\n+1 all DS per 2 Spell Research, Empath Base ranks above 9\n+1 Mana Cost per 6 Spell Research, Empath Base rank above 9',  'DS_All|TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer|AS_Melee|Mana_Cost',  'Spell Research, Empath ranks:202',  'Calculate_1109',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Strength of Will (1119)', 'Emp Spell', '+12 Spirtual TD, +12 all DS\n+1 all DS and Spiritual TD per 3 Spell Research, Empath Base ranks above 19\n+1 Mana Cost per 9 Spell Research, Empath Base rank above 19',  'DS_All|TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer|Mana_Cost',  'Spell Research, Empath ranks:202',  'Calculate_1119',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Intensity (1130)', 'Emp Spell', '+20 all DS, +20 all AS\n+1 all DS and all AS per 2 Spell Research, Empath Base ranks above 30\n+1 Mana Cost per 6 Spell Research, Empath Base rank above 30',  'DS_All|AS_All|Mana_Cost',  'Spell Research, Empath ranks:202',  'Calculate_1130',  'NONE' ) ")


# Minor Mental (1200s)
cur.execute("INSERT INTO Effects VALUES('Foresight (1204)', 'MnM Spell', '+10 melee and ranged DS',  'DS_Melee|DS_Ranged',  'NONE',  'Calculate_1204',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Mindward (1208)', 'MnM Spell', '+20 Mental TD\n+1 Mental TD 2 Spell Research, Minor Mental ranks above 8 to a maximum of +40\n+1 Mana Cost per 4 Spell Research, Minor Mental rank above 8',  'TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer|Mana_Cost',  'Spell Research, Minor Mental ranks:303',  'Calculate_1208',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Dragonclaw (1209)', 'MnM Spell', '+10 UAF\n+1 UAF per seed 1 for Mental Lore, Transformation ranks',  'UAF',  'Mental Lore, Transformation ranks:202',  'Calculate_1209',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Focus Barrier (1216)', 'MnM Spell', '+30 all DS',  'DS_All',  'NONE',  'Calculate_1216',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Premonition (1220)', 'MnM Spell', '+20 all DS\n+1 all DS per 2 Spell Research, Minor Mental ranks above 20\n+1 Mana Cost per 4 Spell Research, Minor Mental rank above 20',  'DS_All|Mana_Cost',  'Spell Research, Minor Mental ranks:303',  'Calculate_1220',  'NONE' ) ")


# Paladin Base (1600s)
cur.execute("INSERT INTO Effects VALUES('Mantle of Faith (1601)', 'Pala Spell', '+5 all DS, +5 Spiritual TD\n+1 all DS and Spiritual TD per seed 2 summation of Spiritual Lore, Blessings ranks\n+1 Mana Cost per +1 DS/TD increase',  'DS_All|TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer',  'Spiritual Lore, Blessings ranks:202',  'Calculate_1601',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES(\"Faith\'s Clarity (1603)\", 'Pala Spell', '-5% spiritual spell hindrance\nAdditional -1% spiritual spell hindrance per 3 Spiritual Lore, Summoning ranks to a maximum of -5% (-10% total)',  'Spell_Hindrance_Spiritual',  'Spiritual Lore, Summoning ranks:202',  'Calculate_1603',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Dauntless (1606)', 'Pala Spell', '+10 all AS\n+3 phantom level against sheer fear',  'AS_All|Sheer_Fear',  'NONE',  'Calculate_1606',  'NONE' ) ")
#cur.execute("INSERT INTO Effects VALUES('Divine Shield (1609)', 'Pala Spell', '+10% Block chance\n+1% block chance per seed 3 summation of Spiritual Lore, Blessings ranks',  'Block_Chance',  'Spiritual Lore, Blessings ranks:202',  'Calculate_1606',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Higher Vision (1610)', 'Pala Spell', '+10 all DS\n+1 all DS per 2 Spell Research, Paladin Base ranks above 10 to a maximum of +20\n+1 Mana Cost per 2 Spell Research, Paladin Base ranks above 10\n+1 all DS per seed 5 summation of Spiritual Lore, Religion ranks\n+1 Mana Cost per 2 Spell Research, Paladin Base rank above 20',  'DS_All|Mana_Cost',  'Spell Research, Paladin ranks:202|Spiritual Lore, Religion ranks:202',  'Calculate_1610',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES(\"Patron\'s Blessing (1611)\", 'Pala Spell', '+10 phantom Combat Maneuver ranks\n+1 Combat Maneuver rank per seed 3 summation of Spiritual Lore, Blessings ranks\n+0.75 Combat Maneuver rank per 2 Spell Research, Paladin Base rank above 11\n+1 Mana Cost per 4 Spell Research, Paladin Base rank above 11',  'Skill_Phantom_Ranks_Combat_Maneuvers|Mana_Cost',  'Spell Research, Paladin ranks:202|Spiritual Lore, Blessings ranks:202',  'Calculate_1611',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES(\"Champion\'s Might (1612)\", 'Pala Spell', '+15 Spiritual CS\n+1 Spiritual CS per 1 Spell Research, Paladin Base rank above 12 to a maximum of +10 (+25 total)',  'CS_Elemental|CS_Mental|CS_Spiritual|CS_Sorcerer',  'Spell Research, Paladin ranks:202',  'Calculate_1612',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Guard the Meek (1613) Group', 'Pala Spell', '+15 melee DS\n+1 melee DS per 5 Spell Research, Paladin Base ranks above 18 to a maximum of +20\n+1 all DS per seed 6 summation of Spiritual Lore, Blessings ranks (max of +5 at 40 ranks',  'DS_Melee',  'Spell Research, Paladin ranks:202',  'Calculate_1613_Group',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Guard the Meek (1613) Self', 'Pala Spell', '+15 melee DS\n+1 all DS per seed 6 summation of Spiritual Lore, Blessings ranks (max of +5 at 40 ranks)',  'DS_Melee',  'Spiritual Lore, Blessings ranks:202',  'Calculate_1613_Self',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Zealot (1617)', 'Pala Spell', '+30 melee AS, -30 all DS\n+1 melee AS and -1 all DS per seed 1 summation of Spiritual Lore, Religion ranks',  'DS_All|AS_Melee',  'Spiritual Lore, Religion ranks:202',  'Calculate_1617',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Faith Shield (1619)', 'Pala Spell', '+50 Spiritual TD\n+3 Spiritual TD per seed 5 summation of Spiritual Lore, Religion ranks',  'DS_All|TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer',  'Spiritual Lore, Religion ranks:202',  'Calculate_1619',  'NONE' ) ")


# Arcane (1700s)
cur.execute("INSERT INTO Effects VALUES('Mystic Focus (1711)', 'Arc Spell', '+10 all CS',  'CS_All',  'NONE',  'Calculate_1711',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Spirit Guard (1712)', 'Arc Spell', '+25 all DS',  'DS_All',  'NONE',  'Calculate_1712',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES(\"V\'tull\'s Fury (1718)\", 'Arc Spell', '+30 melee AS',  'AS_Melee',  'NONE',  'Calculate_1718',  'NONE' ) ")


# Effects related to Combat, Shield, or Armor Maneuvers
#cur.execute("INSERT INTO Effects VALUES('Armored Evasion', 'Maneuver', 'Reduces Armor Action Penalty by [Rank * (7 - Armor Group of worn armor)] / 2',  'Action_Penalty',  'Maneuver ranks:1-5',  'Calculate_Armored_Evasion',  'NONE' ) ")
#cur.execute("INSERT INTO Effects VALUES('Armored Fluidity', 'Maneuver', 'Reduces the base Spell Hinderance of Armor by 10% per rank',  'Spell_Hindrance_Armor',  'Maneuver ranks:1-5',  'Calculate_Armored_Fluidity',  'NONE' ) ")
#cur.execute("INSERT INTO Effects VALUES('Armored Support', 'Maneuver', ' Reduces encumbrance by a number of pounds equal to 5 + ((Armor Group of worn armor + 1) * Rank)',  'Encumberance',  'Maneuver ranks:1-5',  'Calculate_Armored_Evasion',  'NONE' ) ")
#cur.execute("INSERT INTO Effects VALUES('Block Mastery', 'Maneuver', '+5% Block chance per rank',  'Block_Chance',  'Maneuver ranks:1-3',  'Calculate_Block_Mastery',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Berserk', 'Maneuver', 'AS bonus equal to (guild/cman ranks - 1 + (level/4) - 20) / 2. Max AS bonus is +29',  'AS_Melee',  'Guild skill ranks:1-63|Maneuver ranks:1-5',  'Calculate_Berserk',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Burst of Swiftness', 'Maneuver', '+6 increase to Agility bonus and +3 increase to Dexterity\n+2 Agility and +1 Dexterity per rank above 1',  'Statistic_Bonus_Dexterity|Statistic_Bonus_Agility',  'Maneuver ranks:1-5',  'Calculate_Burst_of_Swiftness',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Combat Focus', 'Maneuver', '+2 all TD per rank',  'TD_All',  'Maneuver ranks:1-5',  'Calculate_Combat_Focus',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Combat Movement', 'Maneuver', '+2 melee and ranged DS per rank',  'DS_Melee|DS_Ranged',  'Maneuver ranks:1-5',  'Calculate_Combat_Movement',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Coup de Grace (Buff)', 'Maneuver', '+10 to +40 all AS',  'AS_All',  'Generic AS Bonus:1-40',  'Calculate_Coup_de_Grace_Buff',  'no_dynamic_scaling' ) ")
#cur.execute("INSERT INTO Effects VALUES('Evade Mastery', 'Maneuver', '+5% Evade chance per rank',  'Evade_Chance',  'Maneuver ranks:1-3',  'Calculate_Evade_Mastery',  'NONE' ) ")
#cur.execute("INSERT INTO Effects VALUES('Parry Mastery', 'Maneuver', '+5% Parry chance per rank',  'Parry_Chance',  'Maneuver ranks:1-3',  'Calculate_Parry_Mastery',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Perfect Self', 'Maneuver', '+2/+4/+6/+8/+10 to all statistic bonuses',  'Statistic_Bonus_Strength|Statistic_Bonus_Constitution|Statistic_Bonus_Dexterity|Statistic_Bonus_Agility|Statistic_Bonus_Discipline|Statistic_Bonus_Aura|Statistic_Bonus_Logic|Statistic_Bonus_Intuition|Stat_BonusWisdom|Statistic_Bonus_Influence',  'Maneuver ranks:1-5',  'Calculate_Perfect_Self',  'NONE' ) ")
#cur.execute("INSERT INTO Effects VALUES('Shield Forward', 'Maneuver', '+10 skill bonus to Shield Use per rank',  'Skill_Bonus_Shield_Use',  'Maneuver ranks:1-3',  'Calculate_Shield_Forward',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Shield Swiftness', 'Maneuver', '+0.04 increase per rank to Shield Factor when using a Small or Medium shield',  'Shield_Factor',  'Maneuver ranks:1-3',  'Calculate_Shield_Swiftness',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Specialization I', 'Maneuver', '+2 AS per rank',  'AS_Melee|AS_Ranged|UAC',  'Maneuver ranks:1-5',  'Calculate_Specialization_I',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Specialization II', 'Maneuver', '+2 AS per rank',  'AS_Melee|AS_Ranged|UAC',  'Maneuver ranks:1-5',  'Calculate_Specialization_II',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Specialization III', 'Maneuver', '+2 AS per rank',  'AS_Melee|AS_Ranged|UAC',  'Maneuver ranks:1-5',  'Calculate_Specialization_III',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Spin Attack', 'Maneuver', '+3 all AS and Dodging bonus per rank',  'AS_Melee|Skill_Bonus_Dodging',  'Maneuver ranks:1-5',  'Calculate_Spin_Attack',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Surge of Strength', 'Maneuver', '+8/+10/+12/+14/+16 increase to Strength bonus',  'Statistic_Bonus_Strength',  'Maneuver ranks:1-5',  'Calculate_Surge_of_Strength',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES(\"War Cries - Seanette\'s Shout\", 'Maneuver', '+15 AS to group but not to self',  'AS_All',  'NONE',  'Calculate_War_Cries_Shout',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES(\"War Cries - Horland\'s Holler\", 'Maneuver', '+20 AS to group including self',  'AS_All',  'NONE',  'Calculate_War_Cries_Holler',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Weapon Bonding', 'Maneuver', '+2 AS per rank',  'AS_Melee|AS_Ranged|UAC',  'Maneuver ranks:1-5',  'Calculate_Weapon_Bonding',  'NONE' ) ")


# Effects related to Society powers
#cur.execute("INSERT INTO Effects VALUES('Sigil of Concentration', 'Society', '+5 mana regeneration',  'Mana_Recovery',  'NONE',  'Calculate_Sigil_of_Concentration',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Sigil of Defense', 'Society', '+1 DS per GoS rank',  'DS_All',  'Guardians of Sunfist rank:0-20',  'Calculate_Sigil_of_Defense',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Sigil of Focus', 'Society', '+1 TD per GoS rank',  'TD_All',  'Guardians of Sunfist rank:0-20',  'Calculate_Sigil_of_Focus',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Sigil of Major Bane', 'Society', '+10 AS, +10 UAF',  'AS_All|UAF',  'NONE',  'Calculate_Sigil_of_Major_Bane',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Sigil of Major Protection', 'Society', '+10 DS',  'DS_All',  'NONE',  'Calculate_Sigil_of_Major_Protection',  'NONE' ) ")
#cur.execute("INSERT INTO Effects VALUES('Sigil of Mending', 'Society', '+15 Health Recovery',  'Health_ Recovery',  'NONE',  'Calculate_Sigil_of_Mending',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Sigil of Minor Bane', 'Society', '+5 AS, +5 UAF',  'AS_All|UAF',  'NONE',  'Calculate_Sigil_of_Minor_Bane',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Sigil of Minor Protection', 'Society', '+5 DS',  'DS_All',  'NONE',  'Calculate_Sigil_of_Minor_Protection',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Sigil of Offense', 'Society', '+1 AS/UAF per GoS rank',  'AS_All|UAF',  'Guardians of Sunfist rank:0-20',  'Calculate_Sigil_of_Offense',  'NONE' ) ")
#cur.execute("INSERT INTO Effects VALUES('Sigil of Resolve', 'Society', '+1 skill bonus to Climbing, Swimming and Survival\nper 2 Guardians of Sunfist ranks',  'Skill_Bonus_Climbing|Skill_Bonus_Survival|Skill_Bonus_Swimming',  'Guardians of Sunfist rank:0-20',  'Calculate_Sigil_of_Resolve',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Sign of Defending', 'Society', '+10 DS',  'DS_All',  'NONE',  'Calculate_Sign_of_Defending',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Sign of Deflection', 'Society', '+20 bolt DS',  'DS_Bolt',  'NONE',  'Calculate_Sign_of_Deflection',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Sign of Dissipation', 'Society', '+20 TD',  'TD_All',  'NONE',  'Calculate_Sign_of_Dissipation',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Sign of Madness', 'Society', '+50 AS, +50 UAF, -50 DS',  'AS_All|DS_All|UAF',  'NONE',  'Calculate_Sign_of_Madness',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Sign of Shields', 'Society', '+20 DS',  'DS_All',  'NONE',  'Calculate_Sign_of_Shields',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Sign of Smiting', 'Society', '+10 AS, +10 UAF',  'AS_All|UAF',  'NONE',  'Calculate_Sign_of_Smiting',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Sign of Striking', 'Society', '+5 AS, +5 UAF',  'AS_All|UAF',  'NONE',  'Calculate_Sign_of_Striking',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Sign of Swords', 'Society', '+20 AS, +20 UAF',  'AS_All|UAF',  'NONE',  'Calculate_Sign_of_Swords',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Sign of Warding', 'Society', '+5 DS',  'DS_All',  'NONE',  'Calculate_Sign_of_Warding',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Symbol of Courage', 'Society', '+1 AS and UAF per Voln rank',  'AS_All|UAF',  'Order of Voln rank:0-26',  'Calculate_Symbol_of_Courage',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Symbol of Protection', 'Society', '+1 DS per Voln rank\n+1 TD per 2 Voln ranks',  'DS_All|TD_All',  'Order of Voln rank:0-26',  'Calculate_Symbol_of_Protection',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Symbol of Supremecy', 'Society', '+1 bonus per two Voln ranks to AS/CS,CMAN, UAF against undead creatures',  'AS_All|CS_All|UAF',  'Order of Voln rank:0-26',  'Calculate_Symbol_of_Supremecy',  'vs_undead' ) ")


# Enhancive effects that increase or improve the recovery of Health, Mana, Stamina, or Spirit. Also, DB items.
cur.execute("INSERT INTO Effects VALUES('Health Recovery', 'Enhancive Resource', 'Increases Health Recovery',  'Resource_Health_Recovery',  'Resource recovery:0-50',  'Calculate_Enhancive_Health_Recovery',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Mana Recovery', 'Enhancive Resource', 'Increases Mana Recovery',  'Resource_Mana_Recovery',  'Resource recovery:0-50',  'Calculate_Enhancive_Mana_Recovery',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Stamina Recovery', 'Enhancive Resource', 'Increases Stamina Recovery',  'Resource_Stamina_Recovery',  'Resource recovery:0-50',  'Calculate_Enhancive_Stamina_Recovery',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Spirit Recovery', 'Enhancive Resource', 'Increases Spirit Recovery',  'Resource_Spirit_Recovery',  'Resource recovery:0-3',  'Calculate_Enhancive_Spirit_Recovery',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Maximum Health', 'Enhancive Resource', 'Increases Maximum Health',  'Resource_Maximum_Health',  'Resource maximum increase:0-50',  'Calculate_Enhancive_Maximum_Health',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Maximum Mana', 'Enhancive Resource', 'Increases Maximum Mana',  'Resource_Maximum_Mana',  'Resource maximum increase:0-50',  'Calculate_Enhancive_Maximum_Mana',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Maximum Stamina', 'Enhancive Resource', 'Increases Maximum Stamina',  'Resource_Maximum_Stamina',  'Resource maximum increase:0-50',  'Calculate_Enhancive_Maximum_Stamina',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Maximum Spirit', 'Enhancive Resource', 'Increases Maximum Spirit',  'Resource_Maximum_Spirit',  'Resource maximum increase:0-3',  'Calculate_Enhancive_Maximum_Spirit',  'no_dynamic_scaling' ) ")
#cur.execute("INSERT INTO Effects VALUES('Defense Bonus', 'Enhancive Resource', 'Bonus to all DS. (DB item)',  'DS_All',  'Generic DS Bonus:0-50',  'Calculate_Enhancive_Defense_Bonus',  'no_dynamic_scaling' ) ")


# Enhancive effects that modify character skill ranks or bonuses
cur.execute("INSERT INTO Effects VALUES('Armor Use', 'Enhancive Skill', 'Increases skill bonus/ranks in Armor Use',  'Skill_Bonus_Armor_Use|Skill_Ranks_Armor_Use',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Armor_Use',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Shield Use', 'Enhancive Skill', 'Increases skill bonus/ranks in Shield Use',  'Skill_Bonus_Shield_Use|Skill_Ranks_Shield_Use',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Shield_Use',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Edged Weapons', 'Enhancive Skill', 'Increases skill bonus/ranks in Edged Weapons',  'Skill_Bonus_Edged_Weapons|Skill_Ranks_Edged_Weapons',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Edged_Weapons',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Blunt Weapons', 'Enhancive Skill', 'Increases skill bonus/ranks in Blunt Weapons',  'Skill_Bonus_Blunt_Weapons|Skill_Ranks_Blunt_Weapons',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Blunt_Weapons',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Two-Handed Weapons', 'Enhancive Skill', 'Increases skill bonus/ranks in Two-Handed Weapons',  'Skill_Bonus_Two_Handed_Weapons|Skill_Ranks_Two_Handed_Weapons',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Two_Handed_Weapons',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Ranged Weapons', 'Enhancive Skill', 'Increases skill bonus/ranks in Ranged Weapons',  'Skill_Bonus_Ranged_Weapons|Skill_Ranks_Ranged_Weapons',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Ranged_Weapons',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Thrown Weapons', 'Enhancive Skill', 'Increases skill bonus/ranks in Thrown Weapons',  'Skill_Bonus_Thrown_Weapons|Skill_Ranks_Thrown_Weapons',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Thrown_Weapons',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Polearm Weapons', 'Enhancive Skill', 'Increases skill bonus/ranks in Polearm Weapons',  'Skill_Bonus_Polearm_Weapons|Skill_Ranks_Polearm_Weapons',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Polearm_Weapons',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Brawling', 'Enhancive Skill', 'Increases skill bonus/ranks in Brawling Weapons',  'Skill_Bonus_Brawling|Skill_Ranks_Brawling',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Brawling',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Ambush', 'Enhancive Skill', 'Increases skill bonus/ranks in Ambush',  'Skill_Bonus_Ambush|Skill_Ranks_Ambush',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Ambush',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Two Weapon Combat', 'Enhancive Skill', 'Increases skill bonus/ranks in Two Weapon Combat',  'Skill_Bonus_Two_Weapon_Combat|Skill_Ranks_Two_Weapon_Combat',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Two_Weapon_Combat',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Combat Maneuvers', 'Enhancive Skill', 'Increases skill bonus/ranks in Combat Maneuvers',  'Skill_Bonus_Combat_Maneuvers|Skill_Ranks_Combat_Maneuvers',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Combat_Maneuvers',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Multi Opponent Combat', 'Enhancive Skill', 'Increases skill bonus/ranks in Multi Opponent Combat',  'Skill_Bonus_Multi_Opponent_Combat|Skill_Ranks_Multi_Opponent_Combat',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Multi_Opponent_Combat',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Physical Fitness', 'Enhancive Skill', 'Increases skill bonus/ranks in Physical Fitness',  'Skill_Bonus_Physical_Fitness|Skill_Ranks_Physical_Fitness',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Physical_Fitness',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Dodging', 'Enhancive Skill', 'Increases skill bonus/ranks in Dodging',  'Skill_Bonus_Dodging|Skill_Ranks_Dodging',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Dodging',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Arcane Symbols', 'Enhancive Skill', 'Increases skill bonus/ranks in Arcane Symbols',  'Skill_Bonus_Arcane_Symbols|Skill_Ranks_Arcane_Symbols',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Arcane_Symbols',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Magic Item Use', 'Enhancive Skill', 'Increases skill bonus/ranks in Magic Item Use',  'Skill_Bonus_Magic_Item_Use|Skill_Ranks_Magic_Item_Use',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Magic_Item_Use',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Spell Aiming', 'Enhancive Skill', 'Increases skill bonus/ranks in Spell Aiming',  'Skill_Bonus_Spell_Aiming|Skill_Ranks_Spell_Aiming',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Spell_Aiming',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Harness Power', 'Enhancive Skill', 'Increases skill bonus/ranks in Harness Power',  'Skill_Bonus_Harness_Power|Skill_Ranks_Harness_Power',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Harness_Power',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Elemental Mana Control', 'Enhancive Skill', 'Increases skill bonus/ranks in Elemental Mana Control',  'Skill_Bonus_Elemental_Mana_Control|Skill_Ranks_Elemental_Mana_Control',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Elemental_Mana_Control',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Mental Mana Control', 'Enhancive Skill', 'Increases skill bonus/ranks in Mental Mana Control',  'Skill_Bonus_Mental_Mana_Control|Skill_Ranks_Mental_Mana_Control',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Mental_Mana_Control',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Spiritual Mana Control', 'Enhancive Skill', 'Increases skill bonus/ranks in Spiritual Mana Control',  'Skill_Bonus_Spiritual_Mana_Control|Skill_Ranks_Spiritual_Mana_Control',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Spiritual_Mana_Control',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Elemental Lore, Air', 'Enhancive Skill', 'Increases skill bonus/ranks in Elemental Lore, Air',  'Skill_Bonus_Elemental_Lore_Air|Skill_Ranks_Elemental_Lore_Air',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Elemental_Lore_Air',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Elemental Lore, Earth', 'Enhancive Skill', 'Increases skill bonus/ranks in Elemental Lore, Earth',  'Skill_Bonus_Elemental_Lore_Earth|Skill_Ranks_Elemental_Lore_Earth',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Elemental_Lore_Earth',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Elemental Lore, Fire', 'Enhancive Skill', 'Increases skill bonus/ranks in Elemental Lore, Fire',  'Skill_Bonus_Elemental_Lore_Fire|Skill_Ranks_Elemental_Lore_Fire',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Elemental_Lore_Fire',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Elemental Lore, Water', 'Enhancive Skill', 'Increases skill bonus/ranks in Elemental Lore, Water',  'Skill_Bonus_Elemental_Lore_Water|Skill_Ranks_Elemental_Lore_Water',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Elemental_Lore_Water',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Spiritual Lore, Blessings', 'Enhancive Skill', 'Increases skill bonus/ranks in Spiritual Lore, Blessings',  'Skill_Bonus_Spiritual_Lore_Blessings|Skill_Ranks_Spiritual_Lore_Blessings',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Spiritual_Lore_Blessings',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Spiritual Lore, Religion', 'Enhancive Skill', 'Increases skill bonus/ranks in Spiritual Lore, Religion',  'Skill_Bonus_Spiritual_Lore_Religion|Skill_Ranks_Spiritual_Lore_Religion',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Spiritual_Lore_Religion',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Spiritual Lore, Summoning', 'Enhancive Skill', 'Increases skill bonus/ranks in Spiritual Lore, Summoning',  'Skill_Bonus_Spiritual_Lore_Summoning|Skill_Ranks_Spiritual_Lore_Summoning',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Spiritual_Lore_Summoning',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Sorcerous Lore, Demonology', 'Enhancive Skill', 'Increases skill bonus/ranks in Sorcerous Lore, Demonology',  'Skill_Bonus_Sorcerous_Lore_Demonology|Skill_Ranks_Sorcerous_Lore_Demonology',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Sorcerous_Lore_Demonology',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Sorcerous Lore, Necromancy', 'Enhancive Skill', 'Increases skill bonus/ranks in Sorcerous Lore, Necromancy',  'Skill_Bonus_Sorcerous_Lore_Necromancy|Skill_Ranks_Sorcerous_Lore_Necromancy',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Sorcerous_Lore_Necromancy',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Mental Lore, Divination', 'Enhancive Skill', 'Increases skill bonus/ranks in Mental Lore, Divination',  'Skill_Bonus_Mental_Lore_Divination|Skill_Ranks_Mental_Lore_Divination',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Mental_Lore_Divination',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Mental Lore, Manipulation', 'Enhancive Skill', 'Increases skill bonus/ranks in Mental Lore, Manipulation',  'Skill_Bonus_Mental_Lore_Manipulation|Skill_Ranks_Mental_Lore_Manipulation',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Mental_Lore_Manipulation',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Mental Lore, Telepathy', 'Enhancive Skill', 'Increases skill bonus/ranks in Mental Lore, Telepathy',  'Skill_Bonus_Mental_Lore_Telepathy|Skill_Ranks_Mental_Lore_Telepathy',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Mental_Lore_Telepathy',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Mental Lore, Transference', 'Enhancive Skill', 'Increases skill bonus/ranks in Mental Lore, Transference',  'Skill_Bonus_Mental_Lore_Transference|Skill_Ranks_Mental_Lore_Transference',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Mental_Lore_Transference',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Mental Lore, Transformation', 'Enhancive Skill', 'Increases skill bonus/ranks in Mental Lore, Transformation',  'Skill_Bonus_Mental_Lore_Transformation|Skill_Ranks_Mental_Lore_Transformation',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Mental_Lore_Transformation',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Survival', 'Enhancive Skill', 'Increases skill bonus/ranks in Survival',  'Skill_Bonus_Survival|Skill_Ranks_Survival',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Survival',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Disarm Traps', 'Enhancive Skill', 'Increases skill bonus/ranks in Disarm Traps',  'Skill_Bonus_Disarm Traps|Skill_Ranks_Disarm_Traps',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Disarm_Traps',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Picking Locks', 'Enhancive Skill', 'Increases skill bonus/ranks in Picking Locks',  'Skill_Bonus_Picking_Locks|Skill_Ranks_Picking_Locks',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Picking_Locks',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Stalking and Hiding', 'Enhancive Skill', 'Increases skill bonus/ranks in Stalking and Hiding',  'Skill_Bonus_Stalking_and_Hiding|Skill_Ranks_Stalking_and_Hiding',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Stalking_and_Hiding',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Perception', 'Enhancive Skill', 'Increases skill bonus/ranks in Perception',  'Skill_Bonus_Perception|Skill_Ranks_Perception',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Perception',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Climbing', 'Enhancive Skill', 'Increases skill bonus/ranks in Climbing',  'Skill_Bonus_Climbing|Skill_Ranks_Climbing',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Climbing',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Swimming', 'Enhancive Skill', 'Increases skill bonus/ranks in Swimming',  'Skill_Bonus_Swimming|Skill_Ranks_Swimming',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Swimming',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('First Aid', 'Enhancive Skill', 'Increases skill bonus/ranks in First Aid',  'Skill_Bonus_First_Aid|Skill_Ranks_First_Aid',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_First_Aid',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Trading', 'Enhancive Skill', 'Increases skill bonus/ranks in Trading',  'Skill_Bonus_Trading|Skill_Ranks_Trading',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Trading',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Pickpocketing', 'Enhancive Skill', 'Increases skill bonus/ranks in Pickpocketing',  'Skill_Bonus_Pickpocketing|Skill_Ranks_Pickpocketing',  'Skill ranks:0-50|Skill bonus:0-50',  'Calculate_Enhancive_Pickpocketing',  'no_dynamic_scaling' ) ")


# Enhancive effects that modify character statistics
cur.execute("INSERT INTO Effects VALUES('Strength Enhancive', 'Enhancive Statistic', 'Increases Strength statistic/bonus',  'Statistic_Strength|Statistic_Bonus_Strength',  'Statistic increase:0-40|Statistic bonus:0-20',  'Calculate_Enhancive_Strength',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Constitution Enhancive', 'Enhancive Statistic', 'Increases Constitution statistic/bonus',  'Statistic_Constitution|Statistic_Bonus_Constitution',  'Statistic increase:0-40|Statistic bonus:0-20',  'Calculate_Enhancive_Constitution',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Dexterity Enhancive', 'Enhancive Statistic', 'Increases Dexterity statistic/bonus',  'Statistic_Dexterity|Statistic_Bonus_Dexterity',  'Statistic increase:0-40|Statistic bonus:0-20',  'Calculate_Enhancive_Dexterity',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Agility Enhancive', 'Enhancive Statistic', 'Increases Agility statistic/bonus',  'Statistic_Agility|Statistic_Bonus_Agility',  'Statistic increase:0-40|Statistic bonus:0-20',  'Calculate_Enhancive_Agility',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Discipline Enhancive', 'Enhancive Statistic', 'Increases Discipline statistic/bonus',  'Statistic_Discipline|Statistic_Bonus_Discipline',  'Statistic increase:0-40|Statistic bonus:0-20',  'Calculate_Enhancive_Discipline',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Aura Enhancive', 'Enhancive Statistic', 'Increases Aura statistic/bonus',  'Statistic_Aura|Statistic_Bonus_Aura',  'Statistic increase:0-40|Statistic bonus:0-20',  'Calculate_Enhancive_Aura',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Logic Enhancive', 'Enhancive Statistic', 'Increases Logic statistic/bonus',  'Statistic_Logic|Statistic_Bonus_Logic',  'Statistic increase:0-40|Statistic bonus:0-20',  'Calculate_Enhancive_Logic',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Intuition Enhancive', 'Enhancive Statistic', 'Increases Intuition statistic/bonus',  'Statistic_Intuition|Statistic_Bonus_Intuition',  'Statistic increase:0-40|Statistic bonus:0-20',  'Calculate_Enhancive_Intuition',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Wisdom Enhancive', 'Enhancive Statistic', 'Increases Wisdom statistic/bonus',  'Statistic_Wisdom|Statistic_Bonus_Wisdom',  'Statistic increase:0-40|Statistic bonus:0-20',  'Calculate_Enhancive_Wisdom',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Influence Enhancive', 'Enhancive Statistic', 'Increases Influence statistic/bonus',  'Statistic_Influence|Statistic_Bonus_Influence',  'Statistic increase:0-40|Statistic bonus:0-20',  'Calculate_Enhancive_Influence',  'no_dynamic_scaling' ) ")


# Generic effects
# Reserved for things like a random +132 melee AS boost and things like that


# Status effects
cur.execute("INSERT INTO Effects VALUES('Kneeling', 'Status', '-50 AS and DS, +30 ranged AS if using a crossbow\n+15% stamina recovery',  'AS_All|DS_All|Stamina_Recovery',  'NONE',  'Calculate_Kneeling',  'crowbow_override' ) ")
cur.execute("INSERT INTO Effects VALUES('Lying Down', 'Status', '-50 AS and DS\n+15% stamina recovery',  'AS_All|DS_All|Stamina_Recovery',  'NONE',  'Calculate_Lying_Down',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Overexerted', 'Status', '-10 AS.\nAlso known as Popped Muscles',  'AS_All',  'NONE',  'Calculate_Overexerted',  'crowbow_override' ) ")
cur.execute("INSERT INTO Effects VALUES('Rooted', 'Status', '-50 to melee AS, -25 to ranged AS, -25 to all DS\n',  'AS_Melee|AS_Ranged|DS_All',  'NONE',  'Calculate_Rooted',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Stunned', 'Status', '-20 to all DS\n50% penalty to evade, parry, and block chances\nCannot perform most actions',  'DS_All|Parry_Chance|Evade_Chance|Block_Chance',  'NONE',  'Calculate_Stunned',  'NONE' ) ")


# Flare effects. These are usually short term boosts that are triggered by another effect
cur.execute("INSERT INTO Effects VALUES('Acuity AS Flare', 'Flare', '+5 bonus to bolt AS on next spell cast per tier',  'AS_Bolt',  'Acuity tier:0-10',  'Calculate_Acuity_AS_Flare',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Acuity CS Flare', 'Flare', '+3 bonus to all CS on next cast per tier',  'CS_All',  'Acuity tier:0-10',  'Calculate_Acuity_CS_Flare',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Ensorcell AS Flare', 'Flare', '+5/+10/+15/+20/+25 bonus to AS on next melee, ranged, UAF attack',  'AS_All|UAF',  'Ensorcell tier:0-5',  'Calculate_Ensorcell_AS_Flare',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Ensorcell CS Flare', 'Flare', '+5/+10/+15/+20/+25 bonus to all CS',  'CS_All',  'Ensorcell tier:0-5',  'Calculate_Ensorcell_CS_Flare',  'no_dynamic_scaling' ) ")
cur.execute("INSERT INTO Effects VALUES('Spirit Warding II (107) Flare', 'Flare', '+25 bonus to Spirit TD',  'TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer',  'NONE',  'Calculate_107_Flare',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Benediction (307) Flare', 'Flare', '+15 bonus to all AS and UAF',  'AS_All|UAF',  'NONE',  'Calculate_307_Flare',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES(\"Thurfel\'s Ward (503) Flare\", 'Flare', '+20 all DS',  'DS_All',  'NONE',  'Calculate_503_Flare',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Elemental Bias (508) Flare', 'Flare', '+20 Elemental TD, +10 Spiritual TD',  'TD_Elemental|TD_Mental|TD_Spiritual|TD_Sorcerer',  'NONE',  'Calculate_508_Flare',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Elemental Focus (513) Flare', 'Flare', '+1 Bolt AS per seed 4 summation of Elemental Lore,\nFire ranks on consecutive bolt attacks',  'AS_Bolt',  'Elemental Lore, Fire ranks:202',  'Calculate_513_Flare',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Curse (715) Star', 'Flare', '+10 bolt AS\n+1 bolt AS per 3 Spell Research, Sorcerer ranks above 15, capped character level',  'AS_Bolt',  'Spell Research, Sorcerer ranks:303',  'Calculate_715_Flare',  'NONE' ) ")


# Special Ability effects
#cur.execute("INSERT INTO Effects VALUES('Meditation (Mana)', 'Special', 'Clerics, Empaths, and Savants regenerate mana faster while meditating in a noded room\nMana recovery increased by (Discipline bonus + Wisdom bonus)/2',  'Mana_Recovery',  'NONE',  'Calculate_Meditation_Mana',  'NONE' ) ")


# Items - TODO
#cur.execute("INSERT INTO Effects VALUES('DB Item', 'Item', 'Increases all DS by 1-50',  'DS_All',  'Generic DS Bonus:1-40',  'Calculate_Item_DB',  'no_dynamic_scaling' ) ")


# Other effects that do not fit into any other category
cur.execute("INSERT INTO Effects VALUES('Room - Bright', 'Other', '-10 DS',  'DS_All',  'NONE',  'Calculate_Room_Bright',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Room - Dark', 'Other', '+20 DS',  'DS_All',  'NONE',  'Calculate_Room_Dark',  'NONE' ) ")
cur.execute("INSERT INTO Effects VALUES('Room - Foggy', 'Other', '+30 DS',  'DS_All',  'NONE',  'Calculate_Room_Foggy',  'NONE' ) ")




con.commit()
con.close()   
