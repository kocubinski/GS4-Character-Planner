#!/usr/bin/python

import tkinter
import math
import Globals as globals

class Character:
	#def __init__(self, parent):
	def __init__(self):
		# Statistics Panel stuff
		self.race = globals.race_list["Human"]
		self.profession = globals.prof_list["Warrior"]
		self.statistics = {}
		self.stat_bonus = {}
		self.stat_adj = {}
		
		self.StP_radio_var = tkinter.IntVar()
		self.ptp_base = tkinter.DoubleVar()
		self.mtp_base = tkinter.DoubleVar()
		self.stat_totals = [tkinter.IntVar() for i in range(101)]
		self.ptp_by_level = [tkinter.IntVar() for i in range(101)]		
		self.mtp_by_level = [tkinter.IntVar() for i in range(101)]
		
		self.health_by_level = [tkinter.IntVar() for i in range(101)]
		self.mana_by_level = [tkinter.IntVar() for i in range(101)]
		self.stamina_by_level = [tkinter.IntVar() for i in range(101)]
		self.spirit_by_level = [tkinter.IntVar() for i in range(101)]
			
		self.ptp_bgs = ["lightgray" for i in range(101)]
		self.mtp_bgs = ["lightgray" for i in range(101)]
		self.ptp_frame = ""
		self.mtp_frame = ""		
		
		
		
		self.skills_inter = ""
		self.skills = {}
		self.maneuvers = {}
		self.resources = {}
		self.calculations = {} # AS, DS, CS, UAF
		
	def StP_Init_Statistics(self, stat_objs):	
		self.statistics = stat_objs
		for stat in globals.statistics:
			self.stat_bonus[stat] = tkinter.IntVar()
			self.stat_adj[stat] = tkinter.IntVar()
			self.statistics[stat].parent = self
				
	def StP_Create_Resources_Frame(self, parent):
		myframe = tkinter.Frame(parent)	
		total_frame = tkinter.Frame(myframe)	
		self.ptp_frame = tkinter.Frame(myframe)
		self.mtp_frame = tkinter.Frame(myframe)	
		spacer_frame = tkinter.Frame(myframe)
		health_frame = tkinter.Frame(myframe)
		mana_frame = tkinter.Frame(myframe)
		stamina_frame = tkinter.Frame(myframe)
		spirit_frame = tkinter.Frame(myframe)
				
		total_frame.grid(row=0, column=0)
		self.ptp_frame.grid(row=1, column=0)
		self.mtp_frame.grid(row=2, column=0)
		spacer_frame.grid(row=3, column=0)
		health_frame.grid(row=4, column=0)
		mana_frame.grid(row=5, column=0)
		stamina_frame.grid(row=6, column=0)		
		spirit_frame.grid(row=7, column=0)		
		
		for i in range(101):
			tkinter.Label(total_frame, width=5, bg="lightgray", textvar=self.stat_totals[i]).grid(row=0, column=i, padx="1", pady="1")		
			tkinter.Label(self.ptp_frame, width=5, bg="lightgray", textvar=self.ptp_by_level[i]).grid(row=0, column=i, padx="1", pady="1")	
			tkinter.Label(self.mtp_frame, width=5, bg="lightgray", textvar=self.mtp_by_level[i]).grid(row=0, column=i, padx="1", pady="1")	
			tkinter.Label(spacer_frame, width=5, text="").grid(row=0, column=i)			
			tkinter.Label(health_frame, width=5, bg="red", fg="white", textvar=self.health_by_level[i]).grid(row=0, column=i, padx="1", pady="1")		
			tkinter.Label(mana_frame, width=5, bg="blue", fg="white", textvar=self.mana_by_level[i]).grid(row=0, column=i, padx="1", pady="1")		
			tkinter.Label(stamina_frame, width=5, bg="yellow", textvar=self.stamina_by_level[i]).grid(row=0, column=i, padx="1", pady="1")			
			tkinter.Label(spirit_frame, width=5, bg="darkgray", fg="white", textvar=self.spirit_by_level[i]).grid(row=0, column=i, padx="1", pady="1")	
	
		return myframe
	
	
	def StP_Set_TP_Backgrounds(self):
		i = 0
		for cell in self.ptp_frame.winfo_children():	
			cell["bg"] = self.ptp_bgs[i]
			i += 1
	
		i = 0
		for cell in self.mtp_frame.winfo_children():
			cell["bg"] = self.mtp_bgs[i]
			i += 1
			
			
	def StP_Change_Race(self, race):
		self.race = globals.race_list[race]
				
		for stat in globals.statistics:
			self.stat_bonus[stat].set(self.race.statistic_bonus[stat])
			self.stat_adj[stat].set(self.race.statistic_adj[stat] + self.profession.statistic_growth[stat])	
			self.statistics[stat].adj = self.race.statistic_adj[stat] + self.profession.statistic_growth[stat]
			self.statistics[stat].Calculate_Growth()
			self.statistics[stat].Update_Training_Frame()
			
		self.StP_Update_Resources()
	
	
	def StP_Change_Profession(self, prof):
		self.profession = globals.prof_list[prof]
				
		for stat in globals.statistics:			
			self.stat_adj[stat].set(self.race.statistic_adj[stat] + self.profession.statistic_growth[stat])	
			self.statistics[stat].adj = self.race.statistic_adj[stat] + self.profession.statistic_growth[stat]	
			self.statistics[stat].Calculate_Growth()
			self.statistics[stat].Update_Training_Frame()

		self.StP_Update_Resources()
		
	def StP_Change_Display_Style(self):	
		for stat in globals.statistics:
			self.statistics[stat].Update_Training_Frame()
	
		
	def StP_Update_Resources(self):	
		for i in range(101):
			STR = float(0) if self.statistics["Strength"].values_by_level[i].get() == "" else float(self.statistics["Strength"].values_by_level[i].get())
			CON = float(0) if self.statistics["Constitution"].values_by_level[i].get() == "" else float(self.statistics["Constitution"].values_by_level[i].get())
			DEX = float(0) if self.statistics["Dexterity"].values_by_level[i].get() == "" else float(self.statistics["Dexterity"].values_by_level[i].get())
			AGI = float(0) if self.statistics["Agility"].values_by_level[i].get() == "" else float(self.statistics["Agility"].values_by_level[i].get())
			DIS = float(0) if self.statistics["Discipline"].values_by_level[i].get() == "" else float(self.statistics["Discipline"].values_by_level[i].get())
			AUR = float(0) if self.statistics["Aura"].values_by_level[i].get() == "" else float(self.statistics["Aura"].values_by_level[i].get())
			LOG = float(0) if self.statistics["Logic"].values_by_level[i].get() == "" else float(self.statistics["Logic"].values_by_level[i].get())
			INT = float(0) if self.statistics["Intuition"].values_by_level[i].get() == "" else float(self.statistics["Intuition"].values_by_level[i].get())
			WIS = float(0) if self.statistics["Wisdom"].values_by_level[i].get() == "" else float(self.statistics["Wisdom"].values_by_level[i].get())
			INF = float(0) if self.statistics["Influence"].values_by_level[i].get() == "" else float(self.statistics["Influence"].values_by_level[i].get())
			
			self.stat_totals[i].set(int(STR+CON+DEX+AGI+DIS+AUR+LOG+INT+WIS+INF))			
			
			PTP_sum = (AUR * self.Is_Prime_Stat("Aura") + DIS * self.Is_Prime_Stat("Discipline")) / 2
			PTP_sum = (PTP_sum + STR * self.Is_Prime_Stat("Strength") + CON * self.Is_Prime_Stat("Constitution") + DEX * self.Is_Prime_Stat("Dexterity") + AGI * self.Is_Prime_Stat("Agility")) / 20 
			PTP_sum += 25
						
			MTP_sum = (AUR * self.Is_Prime_Stat("Aura") + DIS * self.Is_Prime_Stat("Discipline")) / 2
			MTP_sum = (MTP_sum + LOG * self.Is_Prime_Stat("Logic") + INT * self.Is_Prime_Stat("Intuition") + WIS * self.Is_Prime_Stat("Wisdom") + INF * self.Is_Prime_Stat("Influence")) / 20 
			MTP_sum += 25
							
			self.ptp_by_level[i].set(math.floor(PTP_sum))
			self.mtp_by_level[i].set(math.floor(MTP_sum))	
						
			if i == 0:
				M_bonus1 = self.statistics[self.profession.mana_statistics[0]].values_by_level[0].get()
				M_bonus2 = self.statistics[self.profession.mana_statistics[1]].values_by_level[0].get()
				M_bonus1 = 0 if M_bonus1 == "" else int(M_bonus1)
				M_bonus2 = 0 if M_bonus2 == "" else int(M_bonus2)
				M_bonus1 = (M_bonus1 - 50) / 2 + self.stat_bonus[self.profession.mana_statistics[0]].get()
				M_bonus2 = (M_bonus2 - 50) / 2 + self.stat_bonus[self.profession.mana_statistics[1]].get()	
				
				self.ptp_base.set(PTP_sum)
				self.mtp_base.set(MTP_sum)				
			else:
				if self.ptp_by_level[i].get() > self.ptp_by_level[i-1].get():
					self.ptp_bgs[i] = "#00FF00"
				else:
					self.ptp_bgs[i] = "lightgrey"
					
				if self.mtp_by_level[i].get() > self.mtp_by_level[i-1].get():
					self.mtp_bgs[i] = "#00FF00"
				else:
					self.mtp_bgs[i] = "lightgrey"
					
					
			#health
			PF_ranks = 0 # total_ranks_by_level[i]["Physical Fitness"] || 
			Combat_Toughness = 0 # (10 * total_man_ranks_by_level[i]["Combat Toughness-combat"] + 5) ||
			H_str = float(0) if self.statistics["Strength"].values_by_level[0].get() == "" else float(self.statistics["Strength"].values_by_level[0].get())
			H_con = float(0) if self.statistics["Constitution"].values_by_level[0].get() == "" else float(self.statistics["Constitution"].values_by_level[0].get())
			con_bonus = float(0) if self.statistics["Constitution"].values_by_level[0].get() == "" else float(self.statistics["Constitution"].values_by_level[0].get())
			con_bonus = (con_bonus - 50) / 2 + self.stat_bonus["Constitution"].get()
			self.health_by_level[i].set(min(math.floor((H_str + H_con) / 10) + PF_ranks*5, self.race.max_health + con_bonus) + Combat_Toughness)
		
			#mana
			HP_ranks = 0 # total_ranks_by_level[i]["Harness Power"] || 0;	
			HP_mana = 0 # (HPranks > i) ? i*3 + HPranks-i : HPranks*3;					
			self.mana_by_level[i].set(max(int(math.floor(M_bonus1 + M_bonus2) / 4), 0) + HP_mana)
	
			#stamina
			PF_bonus = 0 # total_bonus_by_level[i]["Physical Fitness"] || 0;		
			S_str = (STR - 50) / 2 + self.stat_bonus["Strength"].get()
			S_con = (CON - 50) / 2 + self.stat_bonus["Constitution"].get()
			S_agi = (AGI - 50) / 2 + self.stat_bonus["Agility"].get()
			S_dis = (DIS - 50) / 2 + self.stat_bonus["Discipline"].get()
			
			self.stamina_by_level[i].set(int(max(S_con + (S_str + S_agi + S_dis) / 3 + math.floor(PF_bonus / 3), 0)))
					
			spirit = math.floor(AUR/10)
			if (AUR - (spirit * 10)) >= 5:
				spirit += 1
			self.spirit_by_level[i].set(int(round(spirit))) 
		
		self.StP_Set_TP_Backgrounds()
		
	
	def Is_Prime_Stat(self, stat):
		try:
			self.profession.prime_statistics.index(stat)
			return 2
		except ValueError:
			return 1
		
			
