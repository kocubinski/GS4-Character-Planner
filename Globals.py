#!/usr/bin/python

import tkinter
import math

class Statistic:
	def __init__(self,name):
		self.name = name
		self.parent = ""   #This is the character object
		self.adj = 0;
		self.values_by_level = [tkinter.StringVar() for i in range(101)]
		self.bonuses_by_level = [tkinter.IntVar() for i in range(101)]
		self.values_bgs = ["lightgray" for i in range(101)]
		self.bonuses_bgs = ["lightgray" for i in range(101)]
		self.StP_display_values = [tkinter.StringVar() for i in range(101)]
		self.StP_display_bgs = ["lightgray" for i in range(101)]
		self.StP_info_row = ""
		self.StP_training_row = ""

		self.values_by_level[0].set("20")		
		
		
	def On_EntryBox_Update(self, *args):
		self.Calculate_Growth()
		self.Update_Training_Frame()
		self.parent.StP_Update_Resources()
	
	
	def Update_Training_Frame(self):	
		radio = self.parent.StP_radio_var.get()
		for i in range(101):			
			if radio == 2:			
				self.StP_display_values[i].set(self.bonuses_by_level[i].get())
				self.StP_display_bgs[i] = self.bonuses_bgs[i]	
			else:
				self.StP_display_values[i].set(self.values_by_level[i].get())
				self.StP_display_bgs[i] = self.values_bgs[i]
		
		i = 0		
		for cell in self.StP_training_row.winfo_children():	
			cell["bg"] = self.StP_display_bgs[i]
			i += 1
			
	
	def Calculate_Growth(self):
	#	print("%s - %s" % (self.name, self.adj))			
		if self.StP_training_row == "":           #ignore the call if the training frame has not been created yet
			return 0
			
		try:				
			S = int(self.values_by_level[0].get())	
		except ValueError:
			S = 0			
		
		R = self.adj
		GI = max(math.floor(S/R),1);
		prev_stat = S;
	  
		for i in range(101):
			if i > 0 and S < 100 and (i % GI) == 0:
				S += 1
				GI = max(math.floor(S/R),1);
				
			if i != 0:	
				self.values_by_level[i].set(S)	
				
			self.bonuses_by_level[i].set(int((S - 50) / 2) + self.parent.stat_bonus[self.name].get())
									

			if i > 0 and self.bonuses_by_level[i].get() > self.bonuses_by_level[i-1].get():
				self.bonuses_bgs[i] = "#00FF00"
			else:
				self.bonuses_bgs[i] = "lightgray"									
									
			if S > prev_stat:
				self.values_bgs[i] = "#00FF00"
			else:
				self.values_bgs[i] = "lightgray"
				
			prev_stat = S
		
		
	def Create_Info_Row_Frame(self, parent, stat, char):
		frame = tkinter.Frame(parent)
		var = char.statistics[stat].values_by_level[0]
		mycmd = (root.register(self.StP_Validate_Entry), '%d', '%S', '%s', '%P')
		var.trace_variable("w", self.On_EntryBox_Update)
		
		stat_name = tkinter.Label(frame, width="20", anchor="w", bg="lightgray", text=self.name)
		race_bonus = tkinter.Label(frame, width="10", bg="lightgray", textvar=char.stat_bonus[stat])
		GI = tkinter.Label(frame, width="10", bg="lightgray", textvar=char.stat_adj[stat])
		entry = tkinter.Entry(frame, width="6", justify="center", validate="key", validatecommand=mycmd, textvariable=var)
			
		stat_name.grid(row=0, column=0, sticky="w", padx="1", pady="1")
		race_bonus.grid(row=0, column=1, padx="1", pady="1")
		GI.grid(row=0, column=2, padx="1", pady="1")
		entry.grid(row=0, column=3, padx="1")
			
		return frame
		
	def Create_Training_Row_Frame(self, parent):
		frame = tkinter.Frame(parent)	
	
		for i in range(101):
			tkinter.Label(frame, width=5, bg=self.StP_display_bgs[i], textvar=self.StP_display_values[i]).grid(row=0, column=i, padx="1", pady="1")	
			
		return frame
		
		
	def StP_Validate_Entry(self, d, S, s, P):		
	#	print("event %s" % ( d))
	#	print("%s was added/deleted to entry box. Was previously %s" % (S, s))
		if( d == "1"):
			if( (len(s) + len(S)) > 3 ):
				return False
			try:				
				if( float(P) <= 100 ):	
					return True
				else:
					return False
			except ValueError:
				return False
		
		return True
		
	
	
		
class Race:
	def __init__(self, name, health, health_regen, spirit_regen, decay, encumber, weight, eltd, sptd, sotd, potd, ditd, bonus, adj):	
		self.name = name
		self.max_health = health
		self.base_regen = health_regen
		self.spirit_regen = spirit_regen
		self.decay_timer = decay
		self.encumberance_factor = encumber
		self.weight_factor = weight
		self.elemental_td = eltd
		self.spiritual_td = sptd
		self.sorc_td = sotd
		self.poison_td = potd
		self.disease_td = ditd
		self.statistic_bonus = bonus
		self.statistic_adj = adj
		
		
		

class Profession:
	def __init__(self, name, type, prime, mana, spell, growth, ptp, mtp, ranks):
		self.name = name
		self.type = type
		self.prime_statistics = prime;
		self.mana_statistics = mana;
		self.spell_circles = spell;
		self.statistic_growth = growth;
		self.skills_PTP_costs = ptp
		self.skills_MTP_costs = mtp
		self.skills_max_ranks = ranks

		
		
root = tkinter.Tk();		
		
		
statistics = ["Strength", "Constitution", "Dexterity", "Agility", "Discipline", "Aura", "Logic", "Intuition", "Wisdom", "Influence"]
statistics_list = {}		
for stat in statistics:
	statistics_list[stat] = Statistic(stat)

	
races = ["Aelotoi", "Burghal Gnome", "Dark Elf", "Dwarf", "Elf", "Erithian", "Forest Gnome", "Giantman", "Half Elf", "Half Krolvin", "Halfling", "Human", "Sylvankind"]
race_list = {}

race_list["Aelotoi"] = Race("Aelotoi", 120, 1, 1, 10, 0.75, 0.65, 0, 0, 0, 0, 0,
		{ "Strength": -5, "Constitution": 0, "Dexterity": 5, "Agility": 10, "Discipline": 5, "Aura": 0, "Logic": 5, "Intuition": 5, "Wisdom": 0, "Influence": 0 },	
		{ "Strength": 0, "Constitution": -2, "Dexterity": 3, "Agility": 3, "Discipline": 2, "Aura": 0, "Logic": 0, "Intuition": 2, "Wisdom": 0, "Influence": 3 }
)	
race_list["Burghal Gnome"] = Race("Burghal Gnome", 90, 1, 1, 14, 0.78, 0.7, 0, 0, 0, 0, 0,
	{ "Strength": -15, "Constitution": 10, "Dexterity": 10, "Agility": 10, "Discipline": -5, "Aura": 5, "Logic": 10, "Intuition": 5, "Wisdom": 0, "Influence": -5 },
	{ "Strength": -5, "Constitution": 0, "Dexterity": 3, "Agility": 3, "Discipline": -3, "Aura": -2, "Logic": 5, "Intuition": 5, "Wisdom": 0, "Influence": 0 }
)	
race_list["Dark Elf"] = Race("Dark Elf", 120, 1, 1, 10, 0.84, 0.75, -5, -5, -5, 10, 100,
		{ "Strength": 0, "Constitution": -5, "Dexterity": 10, "Agility": 5, "Discipline": -10, "Aura": 10, "Logic": 0, "Intuition": 5, "Wisdom": 5, "Influence": -5 },
		{ "Strength": 0, "Constitution": -2, "Dexterity": 5, "Agility": 5, "Discipline": -2, "Aura": 0, "Logic": 0, "Intuition": 0, "Wisdom": 0, "Influence": 0 }		
	)	
race_list["Dwarf"] = Race("Dwarf", 140, 3, 2, 16, 0.8, 0.75, 30, 0, 15, 20, 15,
		{ "Strength": 10, "Constitution": 15, "Dexterity": 0, "Agility": -5, "Discipline": 10, "Aura": -10, "Logic": 0, "Intuition": 0, "Wisdom": 0, "Influence": -10 },
		{ "Strength": 5, "Constitution": 5, "Dexterity": -3, "Agility": -5, "Discipline": 3, "Aura": 0, "Logic": 0, "Intuition": 0, "Wisdom": 3, "Influence": -2 }		
	)
race_list["Elf"] = Race("Elf", 130, 1, 1, 10, 0.78, 0.7, -5, -5, -5, 10, 100,
		{ "Strength": 0, "Constitution": 0, "Dexterity": 5, "Agility": 15, "Discipline": -15, "Aura": 5, "Logic": 0, "Intuition": 0, "Wisdom": 0, "Influence": 10 },
		{ "Strength": 0, "Constitution": -5, "Dexterity": 5, "Agility": 3, "Discipline": -5, "Aura": 5, "Logic": 0, "Intuition": 0, "Wisdom": 0, "Influence": 3 }		
	)
race_list["Erithian"] = Race("Erithian", 120, 1, 1, 13, 0.85, 0.75, 0, 0, 0, 0, 0,
		{ "Strength": -5, "Constitution": 10, "Dexterity": 0, "Agility": 0, "Discipline": 5, "Aura": 0, "Logic": 5, "Intuition": 0, "Wisdom": 0, "Influence": 10 },
		{ "Strength": -2, "Constitution": 0, "Dexterity": 0, "Agility": 0, "Discipline": 3, "Aura": 0, "Logic": 2, "Intuition": 0, "Wisdom": 0, "Influence": 3 }		
	)
race_list["Forest Gnome"] = Race("Forest Gnome", 100, 1, 2, 16, 0.6, 0.45, 0, 0, 0, 0, 0,
		{ "Strength": -10, "Constitution": 10, "Dexterity": 5, "Agility": 10, "Discipline": 5, "Aura": 0, "Logic": 5, "Intuition": 0, "Wisdom": 5, "Influence": -5 },
		{ "Strength": -3, "Constitution": 2, "Dexterity": 2, "Agility": 3, "Discipline": 2, "Aura": 0, "Logic": 0, "Intuition": 0, "Wisdom": 0, "Influence": 0 }		
	)
race_list["Giantman"] = Race("Giantman", 200, 3, 1, 13, 1.33, 1.2, -5, -5, 0, 0, 0,
		{ "Strength": 15, "Constitution": 10, "Dexterity": -5, "Agility": -5, "Discipline": 0, "Aura": -5, "Logic": 0, "Intuition": 0, "Wisdom": 0, "Influence": 5 },
		{ "Strength": 5, "Constitution": 3, "Dexterity": -2, "Agility": -2, "Discipline": 0, "Aura": 0, "Logic": 0, "Intuition": 2, "Wisdom": 0, "Influence": 0 }		
	)
race_list["Half Elf"] = Race("Half Elf", 135, 2, 1, 10, 0.92, 0.8, -5, -5, -5, 0, 50,
		{ "Strength": 0, "Constitution": 0, "Dexterity": 5, "Agility": 10, "Discipline": -5, "Aura": 0, "Logic": 0, "Intuition": 0, "Wisdom": 0, "Influence": 5 },
		{ "Strength": 2, "Constitution": 0, "Dexterity": 2, "Agility": 2, "Discipline": -2, "Aura": 0, "Logic": 0, "Intuition": 0, "Wisdom": 0, "Influence": 0 }		
	)
race_list["Half Krolvin"] = Race("Half Krolvin", 165, 1, 1, 13, 1.1, 1, 0, 0, 0, 0, 0,
		{ "Strength": 10, "Constitution": 10, "Dexterity": 0, "Agility": 5, "Discipline": 0, "Aura": 0, "Logic": -10, "Intuition": 0, "Wisdom": -5, "Influence": -5 },
		{ "Strength": 3, "Constitution": 5, "Dexterity": 2, "Agility": 2, "Discipline": 0, "Aura": -2, "Logic": -2, "Intuition": 0, "Wisdom": 0, "Influence": -2 }		
	)
race_list["Halfling"] = Race("Halfling", 100, 3, 2, 16, 0.5, 0.45, 40, 0, 20, 30, 30,
		{ "Strength": -15, "Constitution": 10, "Dexterity": 15, "Agility": 10, "Discipline": -5, "Aura": -5, "Logic": 5, "Intuition": 10, "Wisdom": 0, "Influence": -5 },
		{ "Strength": -5, "Constitution": 5, "Dexterity": 5, "Agility": 5, "Discipline": -2, "Aura": 0, "Logic": -2, "Intuition": 0, "Wisdom": 0, "Influence": 0 }		
	)
race_list["Human"] = Race("Human", 150, 2, 1, 14, 1, 0.9, 0, 0, 0, 0, 0,
		{ "Strength": 5, "Constitution": 0, "Dexterity": 0, "Agility": 0, "Discipline": 0, "Aura": 0, "Logic": 5, "Intuition": 5, "Wisdom": 0, "Influence": 0 },
		{ "Strength": 2, "Constitution": 2, "Dexterity": 0, "Agility": 0, "Discipline": 0, "Aura": 0, "Logic": 0, "Intuition": 2, "Wisdom": 0, "Influence": 0 }		
	)
race_list["Sylvankind"] = Race("Sylvankind", 130, 1, 1, 10, 0.81, 0.7, -5, -5, -5, 10, 100,
		{ "Strength": 0, "Constitution": 0, "Dexterity": 10, "Agility": 5, "Discipline": -5, "Aura": 5, "Logic": 0, "Intuition": 0, "Wisdom": 0, "Influence": 0 },
		{ "Strength": -3, "Constitution": -2, "Dexterity": 5, "Agility": 5, "Discipline": -5, "Aura": 3, "Logic": 0, "Intuition": 0, "Wisdom": 0, "Influence": 3 }		
	)		


	
professions = ["Bard", "Cleric", "Empath", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warrior", "Wizard"]
prof_list = {}

prof_list["Bard"] = Profession( "Bard", "semi", [ "Influence", "Aura" ], [ "Influence", "Aura" ], [ "Minor Elemental", "Bard" ],
		{ "Strength": 25, "Constitution": 20, "Dexterity": 25, "Agility": 20, "Discipline": 15, "Aura": 25, "Logic": 10, "Intuition": 15, "Wisdom": 20, "Influence": 30 },
		0,0,0	
	)
prof_list["Cleric"] = Profession( "Cleric", "pure", [ "Wisdom", "Intuition" ], [ "Wisdom", "Wisdom" ], [ "Minor Spiritual", "Major Spiritual", "Cleric" ],
		{ "Strength": 20, "Constitution": 20, "Dexterity": 10, "Agility": 15, "Discipline": 25, "Aura": 15, "Logic": 25, "Intuition": 25, "Wisdom": 30, "Influence": 20 },
		0,0,0	
	)
prof_list["Empath"] = Profession( "Empath", "pure", [ "Wisdom", "Influence" ], [ "Wisdom", "Influence" ], [ "Minor Spiritual", "Major Spiritual", "Empath" ],
		{ "Strength": 10, "Constitution": 20, "Dexterity": 15, "Agility": 15, "Discipline": 25, "Aura": 20, "Logic": 25, "Intuition": 20, "Wisdom": 30, "Influence": 25 },
		0,0,0	
	)
prof_list["Monk"] = Profession( "Monk", "square", [ "Agility", "Strength" ], [ "Wisdom", "Logic" ], [ "Minor Spiritual", "Minor Mental" ],
		{ "Strength": 25, "Constitution": 25, "Dexterity": 20, "Agility": 30, "Discipline": 25, "Aura": 15, "Logic": 20, "Intuition": 20, "Wisdom": 15, "Influence": 10 },
		0,0,0	
	)
prof_list["Paladin"] = Profession( "Paladin", "semi", [ "Wisdom", "Strength" ], [ "Wisdom", "Wisdom" ], [ "Minor Spiritual", "Paladin" ],
		{ "Strength": 30, "Constitution": 25, "Dexterity": 20, "Agility": 20, "Discipline": 25, "Aura": 15, "Logic": 10, "Intuition": 15, "Wisdom": 25, "Influence": 20 },
		0,0,0	
	)
prof_list["Ranger"] = Profession( "Ranger", "semi", [ "Dexterity", "Intuition" ], [ "Wisdom", "Wisdom" ], [ "Minor Spiritual", "Ranger" ],
		{ "Strength": 25, "Constitution": 20, "Dexterity": 30, "Agility": 20, "Discipline": 20, "Aura": 15, "Logic": 15, "Intuition": 15, "Wisdom": 25, "Influence": 10 },
		0,0,0	
	)
prof_list["Rogue"] = Profession( "Rogue", "square", [ "Dexterity", "Agility" ], [ "Aura", "Wisdom" ], [ "Minor Elemental", "Minor Spiritual" ],
		{ "Strength": 25, "Constitution": 20, "Dexterity": 25, "Agility": 30, "Discipline": 20, "Aura": 15, "Logic": 20, "Intuition": 25, "Wisdom": 10, "Influence": 15 },
		0,0,0	
	)
prof_list["Sorcerer"] = Profession( "Sorcerer", "pure", [ "Aura", "Wisdom" ], [ "Aura", "Wisdom" ], [ "Minor Elemental", "Minor Spiritual", "Sorcerer" ],
		{ "Strength": 10, "Constitution": 15, "Dexterity": 20, "Agility": 15, "Discipline": 25, "Aura": 30, "Logic": 25, "Intuition": 20, "Wisdom": 25, "Influence": 20 },
		0,0,0	
	)
prof_list["Warrior"] = Profession( "Warrior", "square", [ "Constitution", "Strength" ], [ "Aura", "Wisdom" ], [ "Minor Elemental", "Minor Spiritual" ],
		{ "Strength": 30, "Constitution": 25, "Dexterity": 25, "Agility": 25, "Discipline": 20, "Aura": 15, "Logic": 10, "Intuition": 20, "Wisdom": 15, "Influence": 20 },
		0,0,0	
	)
prof_list["Wizard"] = Profession( "Wizard", "pure", [ "Aura", "Logic"], [ "Aura", "Aura"], [ "Minor Elemental", "Major Elemental", "Wizard" ],
		{ "Strength": 10, "Constitution": 15, "Dexterity": 25, "Agility": 15, "Discipline": 20, "Aura": 30, "Logic": 25, "Intuition": 25, "Wisdom": 20, "Influence": 20 },
		0,0,0	
	)	
	
