# TODO LIST
# Does this need to be seperate from the globals file? Combining this into globals might be a better idea.

#!/usr/bin/python

import tkinter
import math
import Globals as globals

class Character:
	def __init__(self):
		# Statistics Panel stuff
		self.race = ""
		self.profession = ""
		self.statistics = globals.statistics_list
		self.stat_bonus = {}
		self.stat_adj = {}
		
		self.ptp_base = tkinter.DoubleVar()
		self.mtp_base = tkinter.DoubleVar()
		self.stat_totals = [tkinter.IntVar() for i in range(101)]
		self.ptp_by_level = [tkinter.IntVar() for i in range(101)]		
		self.mtp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_ptp_by_level = [tkinter.IntVar() for i in range(101)]		
		self.total_mtp_by_level = [tkinter.IntVar() for i in range(101)]
		
		self.health_by_level = [tkinter.IntVar() for i in range(101)]
		self.mana_by_level = [tkinter.IntVar() for i in range(101)]
		self.stamina_by_level = [tkinter.IntVar() for i in range(101)]
		self.spirit_by_level = [tkinter.IntVar() for i in range(101)]
			
		for stat in globals.statistics:
			self.stat_bonus[stat] = tkinter.IntVar()
			self.stat_adj[stat] = tkinter.IntVar()
			self.statistics[stat].parent = self	
		
		
		self.build_skills_list = []
		self.scheduled_skills_list = {}
		self.SkP_ptp_leftover = [tkinter.IntVar() for i in range(101)]
		self.SkP_mtp_leftover = [tkinter.IntVar() for i in range(101)]
		
		
		self.build_combat_maneuvers_list = []
		self.build_armor_maneuvers_list = []
		self.build_shield_maneuvers_list = []
		self.maneuvers = {}
		self.combat_by_level = [tkinter.IntVar() for i in range(101)]
		self.shield_by_level = [tkinter.IntVar() for i in range(101)]
		self.armor_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_combat_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_shield_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_armor_by_level = [tkinter.IntVar() for i in range(101)]
		
		
		
		
		self.resources = {}
		self.calculations = {} # AS, DS, CS, UAF
			
		
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
				self.total_ptp_by_level[0].set(math.floor(PTP_sum))
				self.total_mtp_by_level[0].set(math.floor(MTP_sum))					
			
				M_bonus1 = self.statistics[self.profession.mana_statistics[0]].values_by_level[0].get()
				M_bonus2 = self.statistics[self.profession.mana_statistics[1]].values_by_level[0].get()
				M_bonus1 = 0 if M_bonus1 == "" else int(M_bonus1)
				M_bonus2 = 0 if M_bonus2 == "" else int(M_bonus2)
				M_bonus1 = (M_bonus1 - 50) / 2 + self.stat_bonus[self.profession.mana_statistics[0]].get()
				M_bonus2 = (M_bonus2 - 50) / 2 + self.stat_bonus[self.profession.mana_statistics[1]].get()	
				
				self.ptp_base.set(PTP_sum)
				self.mtp_base.set(MTP_sum)				
			else:
				self.total_ptp_by_level[i].set( math.floor(PTP_sum) + self.total_ptp_by_level[i-1].get() )
				self.total_mtp_by_level[i].set( math.floor(MTP_sum) + self.total_mtp_by_level[i-1].get() )	
				
				if self.ptp_by_level[i].get() > self.ptp_by_level[i-1].get():
					globals.panels['Statistics'].ptp_bgs[i] = "#00FF00"
				else:
					globals.panels['Statistics'].ptp_bgs[i] = "lightgrey"
					
				if self.mtp_by_level[i].get() > self.mtp_by_level[i-1].get():
					globals.panels['Statistics'].mtp_bgs[i] = "#00FF00"
				else:
					globals.panels['Statistics'].mtp_bgs[i] = "lightgrey"
					
					
			#health
			PF_ranks = globals.panels['Skills'].Get_Skill_By_Name("Physical Fitness").total_ranks_by_level[i].get() or 0
			Combat_Toughness = 0 # (10 * total_man_ranks_by_level[i]["Combat Toughness-combat"] + 5) or 0
			H_str = float(0) if self.statistics["Strength"].values_by_level[0].get() == "" else float(self.statistics["Strength"].values_by_level[0].get())
			H_con = float(0) if self.statistics["Constitution"].values_by_level[0].get() == "" else float(self.statistics["Constitution"].values_by_level[0].get())
			con_bonus = float(0) if self.statistics["Constitution"].values_by_level[0].get() == "" else float(self.statistics["Constitution"].values_by_level[0].get())
			con_bonus = int(math.floor((con_bonus - 50) / 2 + self.stat_bonus["Constitution"].get()))
			self.health_by_level[i].set(min(math.floor((H_str + H_con) / 10) + PF_ranks*5, self.race.max_health + con_bonus) + Combat_Toughness)
		
			#mana
			HP_ranks = globals.panels['Skills'].Get_Skill_By_Name("Harness Power").total_ranks_by_level[i].get() or 0	
			HP_mana = i*3 + HP_ranks-i if HP_ranks > i else HP_ranks*3
			self.mana_by_level[i].set(max(int(math.floor(M_bonus1 + M_bonus2) / 4), 0) + HP_mana)
	
			#stamina
			PF_bonus = globals.panels['Skills'].Get_Skill_By_Name("Physical Fitness").bonus_by_level[i].get() or 0		
			S_str = (STR - 50) / 2 + self.stat_bonus["Strength"].get()
			S_con = (CON - 50) / 2 + self.stat_bonus["Constitution"].get()
			S_agi = (AGI - 50) / 2 + self.stat_bonus["Agility"].get()
			S_dis = (DIS - 50) / 2 + self.stat_bonus["Discipline"].get()
			
			self.stamina_by_level[i].set(int(max(S_con + (S_str + S_agi + S_dis) / 3 + math.floor(PF_bonus / 3), 0)))
					
			spirit = math.floor(AUR/10)
			if (AUR - (spirit * 10)) >= 5:
				spirit += 1
			self.spirit_by_level[i].set(int(round(spirit))) 
		
		globals.panels['Statistics'].Set_TP_Backgrounds()
		
	
	def Is_Prime_Stat(self, stat):
		try:
			self.profession.prime_statistics.index(stat)
			return 2
		except ValueError:
			return 1
		
			
			
	def Update_Skills(self, prof):
		name = prof.lower()
		globals.db_cur.execute("SELECT name, type, subskill_of, redux_value, %s_ptp, %s_mtp, %s_max_ranks FROM Skills WHERE %s_max_ranks<>0" % (name, name, name, name))
		globals.db_con.commit()		
		data = globals.db_cur.fetchall()	
		
		globals.skills = []
		globals.skills_list = {}		
		for skill in data:
			globals.skills.append(skill[0])
			globals.skills_list[skill[0]] = globals.Skill(skill)
		globals.character.skills = globals.skills_list	
		
		globals.panels['Skills'].SkP_Update_Skills()
		
	def Update_Maneuvers(self, prof):
		name = prof.lower()
		globals.db_cur.execute("SELECT name, mnemonic, type, ranks, cost_rank1, cost_rank2, cost_rank3, cost_rank4, cost_rank5, prerequisites FROM Maneuvers WHERE available_%s=1 ORDER BY name" % (name))
		globals.db_con.commit()		
		data = globals.db_cur.fetchall()	

		globals.combat_maneuvers[:] = []
		globals.shield_maneuvers[:] = []
		globals.armor_maneuvers[:] = []
		globals.combat_maneuvers_list.clear()
		globals.shield_maneuvers_list.clear()
		globals.armor_maneuvers_list.clear()		
		for man in data:
			if man[2] == "combat":	
				globals.combat_maneuvers.append(man[0])
				globals.combat_maneuvers_list[man[0]] = globals.Maneuver(man)
			elif man[2] == "shield":
				globals.shield_maneuvers.append(man[0])
				globals.shield_maneuvers_list[man[0]] = globals.Maneuver(man)
			elif man[2] == "armor":
				globals.armor_maneuvers.append(man[0])
				globals.armor_maneuvers_list[man[0]] = globals.Maneuver(man)
		globals.character.combat_maneuvers = globals.combat_maneuvers_list	
		globals.character.shield_maneuvers = globals.shield_maneuvers_list	
		globals.character.armor_maneuvers = globals.armor_maneuvers_list	
						
		globals.panels['Maneuvers'].ManP_Update_Maneuvers()		
