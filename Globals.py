# This file contains variables used by 2 or more other planner files.

#!/usr/bin/python

import tkinter
import math
import Character as char

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
		#Temporary Sanity check for the skills panel. I'll remove this later
#		panels['Skills'].ClearAll_Button_Onclick()
	
	
	def Update_Training_Frame(self):	
		global panels
		radio = panels['Statistics'].StP_radio_var.get()
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
	def __init__(self, arr):	
		self.name = arr['name']
		self.man_bonus = arr['manauever_bonus']
		self.max_health = arr['max_health']
		self.base_regen = arr['health_regen']
		self.spirit_regen = arr['spirit_regen']
		self.decay_timer = arr['decay_timer']
		self.encumberance_factor = arr['encumberance_factor']
		self.weight_factor = arr['weight_factor']
		self.elemental_td = arr['elemental_td']
		self.spiritual_td = arr['spiritual_td']
		self.sorc_td = arr['sorc_td']
		self.poison_td = arr['poison_td']
		self.disease_td = arr['disease_td']
		self.statistic_bonus = { "Strength": arr['strength_bonus'], "Constitution": arr['constitution_bonus'], "Dexterity": arr['dexterity_bonus'], "Agility": arr['agility_bonus'], "Discipline": arr['discipline_bonus'], "Aura": arr['aura_bonus'], "Logic": arr['logic_bonus'], "Intuition": arr['intuition_bonus'], "Wisdom": arr['wisdom_bonus'], "Influence": arr['influence_bonus'] }
		self.statistic_adj = { "Strength": arr['strength_adj'], "Constitution": arr['constitution_adj'], "Dexterity": arr['dexterity_adj'], "Agility": arr['agility_adj'], "Discipline": arr['discipline_adj'], "Aura": arr['aura_adj'], "Logic": arr['logic_adj'], "Intuition": arr['intuition_adj'], "Wisdom": arr['wisdom_adj'], "Influence": arr['influence_adj'] }
			

class Profession:
	def __init__(self, arr):
		self.name = arr['name']
		self.type = arr['type']
		self.prime_statistics = [ arr['prime_statistics1'], arr['prime_statistics2'] ]
		self.mana_statistics = [ arr['mana_statistic1'], arr['mana_statistic1'] ]
		self.spell_circles = [ arr['spell_circle1'], arr['spell_circle2'] ]
		if arr['spell_circle3'] != "NONE":
			self.spell_circles.append(arr['spell_circle3'])
		self.statistic_growth = { "Strength": arr['strength_growth'], "Constitution": arr['constitution_growth'], "Dexterity": arr['dexterity_growth'], "Agility": arr['agility_growth'], "Discipline": arr['discipline_growth'], "Aura": arr['aura_growth'], "Logic": arr['logic_growth'], "Intuition": arr['intuition_growth'], "Wisdom": arr['wisdom_growth'], "Influence": arr['influence_growth'] }
		self.skills_PTP_costs = ""
		self.skills_MTP_costs = ""
		self.skills_max_ranks = ""


class Skill:
	def __init__(self, arr):
		self.name = arr[0]
		self.type = arr[1]
		self.subskill_of = arr[2]
		self.redux = arr[3]
		self.ptp_cost = arr[4]
		self.mtp_cost = arr[5]
		self.max_ranks = arr[6]
		

class Maneuver:
	def __init__(self, arr):
		self.name = arr[0]
		self.mnemonic = arr[1]
		self.type = arr[2]
		self.max_ranks = arr[3]	
		self.cost_by_rank = [arr[4], arr[5], arr[6], arr[7], arr[8]]
		self.prerequisites = arr[9]	
	
		for i in range(0,5):
			if self.cost_by_rank[i] == "NONE":
				self.cost_by_rank[i] = "-"

	def Get_Cost_At_Rank(self, rank, prof_type):
		if self.cost_by_rank[rank] == "-":
			return "-"
			
		if prof_type == "square" or self.type != "combat":
			modifier = 1
		elif prof_type == "semi":
			modifier = 1.5
		elif prof_type == "pure":
			modifier = 2	

		return math.floor(int(self.cost_by_rank[rank]) * modifier)
				
				
	def Get_Total_Cost_At_Rank(self, rank, prof_type):
		total = 0
		if prof_type == "square" or self.type != "combat":
			modifier = 1
		elif prof_type == "semi":
			modifier = 1.5
		elif prof_type == "pure":
			modifier = 2	
				
		if rank > 5 or self.cost_by_rank[rank-1] == "-":
			return -1
			
		for i in range(0, rank):
			total += math.floor(int(self.cost_by_rank[i]) * modifier)
			
		return total

#Planner globals		
root = tkinter.Tk();			
version = "v2.2"
db_file = "GS4_Planner.db";	
db_con = "";
db_cur = "";
panels = {}
error_dialog = ""
error_dialogmsg = tkinter.StringVar()
error_event = 0
		
# Statistics Panel globals		
races = ["Aelotoi", "Burghal Gnome", "Dark Elf", "Dwarf", "Elf", "Erithian", "Forest Gnome", "Giantman", "Half Elf", "Half Krolvin", "Halfling", "Human", "Sylvankind"]	
professions = ["Bard", "Cleric", "Empath", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warrior", "Wizard"]
statistics = ["Strength", "Constitution", "Dexterity", "Agility", "Discipline", "Aura", "Logic", "Intuition", "Wisdom", "Influence"]
statistics_list = {}		
for stat in statistics:
	statistics_list[stat] = Statistic(stat)
	
# Skills Panel globals	
skills = []
skills_list = {}	

# Maneuvers Panel globals
combat_maneuvers = []
shield_maneuvers = []
armor_maneuvers = []
combat_maneuvers_list = {}
shield_maneuvers_list = {}
armor_maneuvers_list = {}

# Character global needs to be declared last since it uses the above globals
character = char.Character();
