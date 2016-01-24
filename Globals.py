# This file contains variables used by all the other planner files.

#!/usr/bin/python

import tkinter
import tkinter.filedialog
import math
import Pmw

# The Character object holds all the values and objects related to the character from across all the panels.
# These values can be easily accessed by all other panels and allows the planner to save and load character build file with minimum effort.
class Character:
	def __init__(self):
		global statistics
		
		# Statistics Panel variables
		self.race = ""
		self.profession = ""
		
		self.statistics_list = {}         	# Contains a list of Statistic objects using the name of each statistic as a key
		self.stat_bonus = {}            	# Contains a list of bonuses for each statistic (calculted by race) using the name of each statistic as a key
		self.stat_adj = {}					# Contains a list of statistic adjustments (combination of race and profession growths) using the name of each statistic as a key
		
		# Initialize the above variables
		for stat in statistics:
			self.statistics_list[stat] = Statistic(self, stat)
			self.stat_bonus[stat] = tkinter.IntVar()
			self.stat_adj[stat] = tkinter.IntVar()
			
		# People like seeing the decimal form of their starting Training Point values when determining their starting stats. The rounded down value of each is using for the by_level variables
		self.ptp_base = tkinter.DoubleVar()
		self.mtp_base = tkinter.DoubleVar()
		self.statistic_totals_by_level = [tkinter.IntVar() for i in range(101)]
		self.ptp_by_level = [tkinter.IntVar() for i in range(101)]		
		self.mtp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_ptp_by_level = [tkinter.IntVar() for i in range(101)]		
		self.total_mtp_by_level = [tkinter.IntVar() for i in range(101)]
		
		# Resources are shown on the Statistics Panel but all of them need Skill build information to be calculated correctly.
		self.health_by_level = [tkinter.IntVar() for i in range(101)]
		self.mana_by_level = [tkinter.IntVar() for i in range(101)]
		self.stamina_by_level = [tkinter.IntVar() for i in range(101)]
		self.spirit_by_level = [tkinter.IntVar() for i in range(101)]
					
		
		# Skills Panel variables		
		self.build_skills_list = []           # A list of Build_List_Skill objects that represent what the character wants to train in.
		self.skills_list = {}                 # Hash of skill name -> Skill objects
		
		
		# Maneuvers Panel variables		
		# Because their are different types of maneuvers, a seperate set of variables must be kept for each type: Combat, Shield, Armor		
		self.build_combat_maneuvers_list = []
		self.build_armor_maneuvers_list = []
		self.build_shield_maneuvers_list = []
		
		# Lists of Build_List_Skill objects that represent what the character wants to train in for each manevuer type
		self.combat_maneuvers_list = {}
		self.shield_maneuvers_list = {}
		self.armor_maneuvers_list = {}
		
		# Points for training in maneuvers are calculated as 1 point per rank in a specific skill. Combat -> Comabat Manevuers, Shield -> Shield Use, Armor -> Armor Use
		self.combat_points_by_level = [tkinter.IntVar() for i in range(101)]
		self.shield_points_by_level = [tkinter.IntVar() for i in range(101)]
		self.armor_points_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_combat_points_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_shield_points_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_armor_points_by_level = [tkinter.IntVar() for i in range(101)]
							

	# This method will prompt the user for a .txt file and will populate the Character class with the information saved in the file
	def Load_Character(self):
		global statistics, panels, char_name, version, root
		char_file = tkinter.filedialog.askopenfile(initialdir="Characters", filetypes=[("Text files","*.txt")], mode='r', title="Load GS4 Character")
		stat_panel = panels["Statistics"]
		skills_panel = panels["Skills"]
		man_panel = panels["Maneuvers"]
		read_mode = ""
		
		# If the user cancelled out of the file prompt, end the method immediately
		if char_file == None:
			return
		
		char_name = char_file.name.split("/")[-1].split("\\")[-1].split(".")[0]
		root.title("Gemstone IV Character Planner %s - %s" % (version, char_name))
		
		# Read the file line by line and remove the end of line character "\n" at the end of each line if it is present
		line = char_file.readline()
		while line:
			if line[-1] == "\n":
				line = line[:-1]
							
			# Sets the "read mode" of the method. Read mode determines what the method will do when it read in a line from the file.
			# Each header in the character file marks the begining of a new type of information in the save file and will change the read mode accordingly.
			# The rest of the loop is skipped when the read mode is changed.
			if line == "==CHARACTER INFORMATION==":
				read_mode = "character"
				line = char_file.readline()
				continue
			elif line == "==STATISTICS INFORMATION==":
				read_mode = "statistics"
				line = char_file.readline()
				continue
			elif line == "==SKILLS BUILD LIST==":
				read_mode = "skill"
				line = char_file.readline()
				continue
			elif line == "==COMBAT MANEUVERS BUILD LIST==":
				read_mode = "combat"
				line = char_file.readline()
				continue
			elif line == "==SHIELD MANEUVERS BUILD LIST==":
				read_mode = "shield"
				line = char_file.readline()
				continue
			elif line == "==ARMOR MANEUVERS BUILD LIST==":
				read_mode = "armor"
				line = char_file.readline()
				continue
			
			parts = line.split(":")            # Every field in the save file is divided by a semi-colon. Splitting on the semi-colon will give us the parts of the line.
			
			# Character is for the profession and race. Since the profession determines skill costs of build_list_skill objects, it needs be set immediately.
			if read_mode == "character":
				if parts[0] == "Profession":
					stat_panel.profession_dd.set(parts[1])
					stat_panel.Change_Profession(panels["Statistics"].profession_dd.get())  
				elif parts[0] == "Race":
					stat_panel.race_dd.set(parts[1])		
					stat_panel.Change_Race(panels["Statistics"].race_dd.get())		
			# For statistics, update the appropriate statistic with the listed value. All statistics will be recalculated later
			elif read_mode == "statistics":
				self.statistics_list[parts[0]].values_by_level[0].set(parts[1])		
				
			elif read_mode == "skill":
				skill = self.skills_list[parts[0]]
				location = len(self.build_skills_list)
				self.build_skills_list.insert(location, skills_panel.Create_Build_List_Skill(skills_panel.ML_Frame.interior(), parts[0], parts[1], location, 
				"%s / %s (%s)" % (skill.ptp_cost,skill.mtp_cost, skill.max_ranks), parts[3], parts[4], parts[2]) )		
				self.build_skills_list[location].Set_Training_Rate()
				
			# Each of the maneuver types will read in the line and use the information to create a Build_List_Maneuver and add it to a manevuer list.
			# The order of the build is determined by the order the maneuvers are listed in the file
			elif read_mode == "combat":
				man = self.combat_maneuvers_list[parts[0]]
				location = len(self.build_combat_maneuvers_list)
				self.build_combat_maneuvers_list.insert(location, man_panel.Create_Build_List_Maneuver(man_panel.ML_Frame.interior(), parts[0], 
				"Combat", parts[1], location, parts[3], parts[4], parts[2], (man.cost_by_rank[0], man.cost_by_rank[1], man.cost_by_rank[2], man.cost_by_rank[3], man.cost_by_rank[4]) ))	
			elif read_mode == "shield":
				man = self.shield_maneuvers_list[parts[0]]
				location = len(self.build_shield_maneuvers_list)
				self.build_shield_maneuvers_list.insert(location, man_panel.Create_Build_List_Maneuver(man_panel.ML_Frame.interior(), parts[0], 
				"Shield", parts[1], location, parts[3], parts[4], parts[2],	(man.cost_by_rank[0], man.cost_by_rank[1], man.cost_by_rank[2], man.cost_by_rank[3], man.cost_by_rank[4]) ))	
			elif read_mode == "armor":
				man = self.armor_maneuvers_list[parts[0]]
				location = len(self.build_armor_maneuvers_list)
				self.build_armor_maneuvers_list.insert(location, man_panel.Create_Build_List_Maneuver(man_panel.ML_Frame.interior(), parts[0], 
				"Armor", parts[1], location, parts[3], parts[4], parts[2], (man.cost_by_rank[0], man.cost_by_rank[1], man.cost_by_rank[2], man.cost_by_rank[3], man.cost_by_rank[4]) ))						
					
			# End of the loop, read the next line.		
			line = char_file.readline()
	
		# Post file reading Planner setup
		# Calculate the statistics' growths and make sure the skills and maneuvers have the correct order
		for stat in statistics:
			self.statistics_list[stat].Calculate_Growth()
			self.statistics_list[stat].Update_Growth_Frame()
	
		# Make sure the added Skills are displayed in the build frame in the Skills Panel
		i = 0 
		for skill in self.build_skills_list:
			skill.order.set(i+1)
			skill.SkP_Edit_Button.config(command=lambda v=i: skills_panel.Add_Edit_Button_Onclick(v))
			skill.SkP_Build_Row.grid(row=i, column=0)					
			i += 1		
			
		# Make sure the order drop down menues are setup correctly
		skills_panel.menu_size = i+1
		if skills_panel.menu_size > 1:
			for j in range(2, skills_panel.menu_size+1):
				if j > 2:
					skills_panel.edit_order_menu["menu"].insert_command("end", label=j-1, command=lambda v=j-1: skills_panel.vars_dialog_order.set(v))	
				skills_panel.add_order_menu["menu"].insert_command("end", label=j, command=lambda v=j: skills_panel.vars_dialog_order.set(v))	
			
			
		# Maneuvers are set up the same way as skills but Combat Maneuvers are shown by default instead of every maneuver
		i = 0 
		for man in self.build_combat_maneuvers_list:
			man.order.set(i+1)
			man.ManP_Edit_Button.config(command=lambda v=i: man_panel.Add_Edit_Button_Onclick(v))
			i += 1					
		man_panel.combat_menu_size = i+1
		if man_panel.combat_menu_size > 1:
			for j in range(2, man_panel.combat_menu_size+1):
				if j > 2:
					man_panel.edit_combat_order_menu["menu"].insert_command("end", label=j-1, command=lambda v=j-1: man_panel.vars_dialog_order.set(v))	
				man_panel.add_combat_order_menu["menu"].insert_command("end", label=j, command=lambda v=j: man_panel.vars_dialog_order.set(v))	
				
		i = 0 
		for man in self.build_shield_maneuvers_list:
			man.order.set(i+1)
			man.ManP_Edit_Button.config(command=lambda v=i: man_panel.Add_Edit_Button_Onclick(v))
			i += 1					
		man_panel.shield_menu_size = i+1
		if man_panel.shield_menu_size > 1:
			for j in range(2, man_panel.shield_menu_size+1):
				if j > 2:
					man_panel.edit_shield_order_menu["menu"].insert_command("end", label=j-1, command=lambda v=j-1: man_panel.vars_dialog_order.set(v))	
				man_panel.add_shield_order_menu["menu"].insert_command("end", label=j, command=lambda v=j: man_panel.vars_dialog_order.set(v))	
				
		i = 0 
		for man in self.build_armor_maneuvers_list:
			man.order.set(i+1)
			man.ManP_Edit_Button.config(command=lambda v=i: man_panel.Add_Edit_Button_Onclick(v))
			i += 1			
		man_panel.armor_menu_size = i+1
		if man_panel.armor_menu_size > 1:
			for j in range(2, man_panel.armor_menu_size+1):
				if j > 2:
					man_panel.edit_armor_order_menu["menu"].insert_command("end", label=j-1, command=lambda v=j-1: man_panel.vars_dialog_order.set(v))	
				man_panel.add_armor_order_menu["menu"].insert_command("end", label=j, command=lambda v=j: man_panel.vars_dialog_order.set(v))			
			
		man_panel.maneuver_mode.set("")
		man_panel.Maneuver_Style_Onchange("Combat")
	
	
	def Save_Character(self):
		global statistics, char_name, version, root
		char_file = tkinter.filedialog.asksaveasfile(initialdir="Characters", defaultextension=".txt", mode='w', title="Save GS4 Character As ...")
		
		if char_file == None:
			return		
			
		char_name = char_file.name.split("/")[-1].split("\\")[-1].split(".")[0]
		root.title("Gemstone IV Character Planner %s - %s" % (version, char_name))
			
		char_file.write("==CHARACTER INFORMATION==\n")	
		char_file.write("Profession:%s\n" % self.profession.name)	
		char_file.write("Race:%s\n" % self.race.name)	
		char_file.write("==STATISTICS INFORMATION==\n")	
		for stat in statistics:
			char_file.write("%s:%s\n" % (self.statistics_list[stat].name, self.statistics_list[stat].values_by_level[0].get()))
			
		if self.build_skills_list:
			char_file.write("==SKILLS BUILD LIST==\n")	
			for skill in self.build_skills_list:			
				char_file.write("%s:%s:%s:%s:%s\n" % (skill.name.get(), skill.hide.get(), skill.goal.get(), skill.slvl.get(), skill.tlvl.get()) )
				
		if self.build_combat_maneuvers_list:
			char_file.write("==COMBAT MANEUVERS BUILD LIST==\n")	
			for man in self.build_combat_maneuvers_list:			
				char_file.write("%s:%s:%s:%s:%s\n" % (man.name.get(), man.hide.get(), man.goal.get(), man.slvl.get(), man.tlvl.get()) )		
			
		if self.build_shield_maneuvers_list:
			char_file.write("==SHIELD MANEUVERS BUILD LIST==\n")	
			for man in self.build_shield_maneuvers_list:			
				char_file.write("%s:%s:%s:%s:%s\n" % (man.name.get(), man.hide.get(), man.goal.get(), man.slvl.get(), man.tlvl.get()) )
			
		if self.build_armor_maneuvers_list:
			char_file.write("==ARMOR MANEUVERS BUILD LIST==\n")	
			for man in self.build_armor_maneuvers_list:			
				char_file.write("%s:%s:%s:%s:%s\n" % (man.name.get(), man.hide.get(), man.goal.get(), man.slvl.get(), man.tlvl.get()) )

			
	# Calculate the PTP, MTP, Health, Mana, Stamina, Spirit over 100 levels. This is called after the statistics growth method has been called.
	def Update_Statistics(self):	
		global panels
	
		# Calculate everything using the 10 statistic values for this level.
		for i in range(101):
			STR = float(0) if self.statistics_list["Strength"].values_by_level[i].get() == "" else float(self.statistics_list["Strength"].values_by_level[i].get())
			CON = float(0) if self.statistics_list["Constitution"].values_by_level[i].get() == "" else float(self.statistics_list["Constitution"].values_by_level[i].get())
			DEX = float(0) if self.statistics_list["Dexterity"].values_by_level[i].get() == "" else float(self.statistics_list["Dexterity"].values_by_level[i].get())
			AGI = float(0) if self.statistics_list["Agility"].values_by_level[i].get() == "" else float(self.statistics_list["Agility"].values_by_level[i].get())
			DIS = float(0) if self.statistics_list["Discipline"].values_by_level[i].get() == "" else float(self.statistics_list["Discipline"].values_by_level[i].get())
			AUR = float(0) if self.statistics_list["Aura"].values_by_level[i].get() == "" else float(self.statistics_list["Aura"].values_by_level[i].get())
			LOG = float(0) if self.statistics_list["Logic"].values_by_level[i].get() == "" else float(self.statistics_list["Logic"].values_by_level[i].get())
			INT = float(0) if self.statistics_list["Intuition"].values_by_level[i].get() == "" else float(self.statistics_list["Intuition"].values_by_level[i].get())
			WIS = float(0) if self.statistics_list["Wisdom"].values_by_level[i].get() == "" else float(self.statistics_list["Wisdom"].values_by_level[i].get())
			INF = float(0) if self.statistics_list["Influence"].values_by_level[i].get() == "" else float(self.statistics_list["Influence"].values_by_level[i].get())
			
			# The sum of the 10 statistics is the statistic total for this level.
			self.statistic_totals_by_level[i].set(int(STR+CON+DEX+AGI+DIS+AUR+LOG+INT+WIS+INF))			
			
			# Calculate PTP/MTP. This formula is (STR + CON + DEX + AGI) + (AUR + DIS) / 2  for PTP and (LOG + INT + WIS + INF) + (AUR + DIS) / 2 for MTP. 
			# Prime statistics count as double for these calculations
			PTP_sum = (AUR * self.Is_Prime_Stat("Aura") + DIS * self.Is_Prime_Stat("Discipline")) / 2
			PTP_sum = (PTP_sum + STR * self.Is_Prime_Stat("Strength") + CON * self.Is_Prime_Stat("Constitution") + DEX * self.Is_Prime_Stat("Dexterity") + AGI * self.Is_Prime_Stat("Agility")) / 20 
			PTP_sum += 25
						
			MTP_sum = (AUR * self.Is_Prime_Stat("Aura") + DIS * self.Is_Prime_Stat("Discipline")) / 2
			MTP_sum = (MTP_sum + LOG * self.Is_Prime_Stat("Logic") + INT * self.Is_Prime_Stat("Intuition") + WIS * self.Is_Prime_Stat("Wisdom") + INF * self.Is_Prime_Stat("Influence")) / 20 
			MTP_sum += 25
							
			self.ptp_by_level[i].set(math.floor(PTP_sum))
			self.mtp_by_level[i].set(math.floor(MTP_sum))	
						
			# Only use the statistic values given at level 0 to determine starting mana			
			if i == 0:
				self.total_ptp_by_level[0].set(math.floor(PTP_sum))
				self.total_mtp_by_level[0].set(math.floor(MTP_sum))					
			
				M_bonus1 = self.statistics_list[self.profession.mana_statistics[0]].values_by_level[0].get()
				M_bonus2 = self.statistics_list[self.profession.mana_statistics[1]].values_by_level[0].get()
				M_bonus1 = 0 if M_bonus1 == "" else int(M_bonus1)
				M_bonus2 = 0 if M_bonus2 == "" else int(M_bonus2)
				M_bonus1 = (M_bonus1 - 50) / 2 + self.stat_bonus[self.profession.mana_statistics[0]].get()
				M_bonus2 = (M_bonus2 - 50) / 2 + self.stat_bonus[self.profession.mana_statistics[1]].get()	
				
				self.ptp_base.set(PTP_sum)
				self.mtp_base.set(MTP_sum)				
			# Beyond level 0, sum the total PTP/MTP and color the panels if the value for last level is less than the value for this level.
			else:
				self.total_ptp_by_level[i].set( math.floor(PTP_sum) + self.total_ptp_by_level[i-1].get() )
				self.total_mtp_by_level[i].set( math.floor(MTP_sum) + self.total_mtp_by_level[i-1].get() )	
				
				if self.ptp_by_level[i].get() > self.ptp_by_level[i-1].get():
					panels['Statistics'].ptp_bgs[i] = "#00FF00"
				else:
					panels['Statistics'].ptp_bgs[i] = "lightgrey"
					
				if self.mtp_by_level[i].get() > self.mtp_by_level[i-1].get():
					panels['Statistics'].mtp_bgs[i] = "#00FF00"
				else:
					panels['Statistics'].mtp_bgs[i] = "lightgrey"
					
					
			# Health calculation. Combines stats, Physical Training ranks, Combat Toughness maneuver ranks
			PF_ranks = 0 if not "Physical Fitness" in self.skills_list else	self.skills_list["Physical Fitness"].total_ranks_by_level[i].get() 
			Combat_Toughness = 0 # (10 * total_man_ranks_by_level[i]["Combat Toughness-combat"] + 5) or 0
			H_str = float(0) if self.statistics_list["Strength"].values_by_level[0].get() == "" else float(self.statistics_list["Strength"].values_by_level[0].get())
			H_con = float(0) if self.statistics_list["Constitution"].values_by_level[0].get() == "" else float(self.statistics_list["Constitution"].values_by_level[0].get())
			con_bonus = float(0) if self.statistics_list["Constitution"].values_by_level[0].get() == "" else float(self.statistics_list["Constitution"].values_by_level[0].get())
			con_bonus = int(math.floor((con_bonus - 50) / 2 + self.stat_bonus["Constitution"].get()))
			self.health_by_level[i].set(min(math.floor((H_str + H_con) / 10) + PF_ranks*5, self.race.max_health + con_bonus) + Combat_Toughness)
		
			# Mana calculation. Just factor in the Harness power ranks at this level
			HP_ranks = 0 if not "Harness Power" in self.skills_list else self.skills_list["Harness Power"].total_ranks_by_level[i].get() 		
			HP_mana = i*3 + HP_ranks-i if HP_ranks > i else HP_ranks*3
			self.mana_by_level[i].set(max(int(math.floor(M_bonus1 + M_bonus2) / 4), 0) + HP_mana)
	
			# Stamina calculation.
			PF_bonus = 0 if not "Physical Fitness" in self.skills_list else	self.skills_list["Physical Fitness"].bonus_by_level[i].get() 
			S_str = (STR - 50) / 2 + self.stat_bonus["Strength"].get()
			S_con = (CON - 50) / 2 + self.stat_bonus["Constitution"].get()
			S_agi = (AGI - 50) / 2 + self.stat_bonus["Agility"].get()
			S_dis = (DIS - 50) / 2 + self.stat_bonus["Discipline"].get()
			
			self.stamina_by_level[i].set(int(max(S_con + (S_str + S_agi + S_dis) / 3 + math.floor(PF_bonus / 3), 0)))
					
			# Spirit calculation
			spirit = math.floor(AUR/10)
			if (AUR - (spirit * 10)) >= 5:
				spirit += 1
			self.spirit_by_level[i].set(int(round(spirit))) 
		

		# Sets the background colors of the cells.	
		i = 0
		for cell in panels['Statistics'].ptp_frame.winfo_children():	
			cell["bg"] = panels['Statistics'].ptp_bgs[i]
			i += 1
	
		i = 0
		for cell in panels['Statistics'].mtp_frame.winfo_children():
			cell["bg"] = panels['Statistics'].mtp_bgs[i]
			i += 1	

			
	# Small function that determines if the profession considers stat a prime statistic. The multiplier for determining TP is returned. 2 if yes, 1 if no
	def Is_Prime_Stat(self, stat):
		try:
			self.profession.prime_statistics.index(stat)
			return 2
		except ValueError:
			return 1
	
	
	# This method is called when the Profession is changed. It makes a database call using the new profession and gets the new skill costs and max ranks for that skill.
	def Update_Skills(self):
		global db_cur, db_con, skill_names, panels, Skill
		skill_panel = panels['Skills']
		
		name = self.profession.name.lower()
		db_cur.execute("SELECT name, %s_ptp, %s_mtp, %s_max_ranks FROM Skills" % (name, name, name))		
		db_con.commit()		
		data = db_cur.fetchall()	
			
		# Update all the skills with new costs
		for skill in data:
			character.skills_list[skill[0]].Update_Skill_Information(skill)		
				
		# Reset the scrolling on the schedule and build frames		
		skill_panel.dialog_menu_skill_names['menu'].delete(0, "end")
		skill_panel.ML_Frame.yview("moveto", 0, "units")
		skill_panel.MR_Frame.yview("moveto", 0, "units")
		
		# Remove all the skills 
		for key, row in self.skills_list.items():
			if row.SkP_schedule_row == "":
				break
			row.SkP_schedule_row.grid_remove()
		
		# Add all the skills from the skills_list to the schedule frame that the profession can use (ie: spell research)
		i = 0
		for name in skill_names:				
			if self.skills_list[name].active_skill:
				skill_panel.dialog_menu_skill_names['menu'].add_command(label=name, command=lambda s=name: skill_panel.Skills_Menu_Onchange(s))
				self.skills_list[name].SkP_schedule_row.grid(row=i, column=0)
				i += 1
			
		# Reset the skills panel and make sure the schedule frame looks right	
		skill_panel.level_counter.setvalue(0)
		skill_panel.ML_Frame.yview("moveto", 0, "units")
		skill_panel.MR_Frame.yview("moveto", 0, "units")
		skill_panel.Update_Schedule_Frames()
		
	
	# Because Skills with the same subgroup need to be taken into account when calculating cost and max ranks, this method will determine how much TP to refund for each subgroup.
	def Calculate_Subskill_Regained_TP(self, level, subskill_group):
		global skill_names
		
		# Abort if there is no subgroup or the level is not 1-100
		if subskill_group == "NONE" or level < 1 or level > 100:
			return (0,0)

		pcost = 0; mcost = 0; tranks = 0; prev_tranks = 0; prev_pcost = 0; prev_mcost = 0; 
		skill_ptp = 0; skill_mtp = 0		
		
		# Get the total ranks taken this level and the previous level for all the skills 
		for s in skill_names:
			skill = self.skills_list[s]
			if skill.subskill_group == subskill_group:
				skill_ptp = skill.ptp_cost
				skill_mtp = skill.mtp_cost
				prev_tranks += skill.total_ranks_by_level[level-1].get()
				tranks += skill.total_ranks_by_level[level].get()
				
		# No ranks were taken? Abort method.
		if tranks == 0:
			return (0,0)
		
		# Otherwise calculate the cost for both levels and return the different or 0 if it is a negative amount
		triple_train = max(0, tranks - 2 * (level + 1))
		double_train = max(0, tranks - triple_train - (level + 1))
		single_train = max(0, tranks - triple_train - double_train)		
		prev_triple_train = max(0, prev_tranks - 2 * (level))
		prev_double_train = max(0, prev_tranks - prev_triple_train - (level))
		prev_single_train = max(0, prev_tranks - prev_triple_train - prev_double_train)		
				
		pcost = skill_ptp * single_train  +  2 * skill_ptp * double_train  +  4 * skill_ptp * triple_train
		mcost = skill_mtp * single_train  +  2 * skill_mtp * double_train  +  4 * skill_mtp * triple_train	
		prev_pcost = skill_ptp * prev_single_train  +  2 * skill_ptp * prev_double_train  +  4 * skill_ptp * prev_triple_train
		prev_mcost = skill_mtp * prev_single_train  +  2 * skill_mtp * prev_double_train  +  4 * skill_mtp * prev_triple_train	
		

		return ( max(0, prev_pcost - pcost), max(0, prev_mcost - mcost) )
			
	
	# Given a subskill group and a skill name, find all the skills that have that subskills EXECEPT for "skill name" and return the combined total ranks for those skills
	def Get_Total_Ranks_Of_Subskill(self, name, level, subskill_group):
		global skill_names
		total = 0
		
		if subskill_group == "NONE":
			return 0
		
		for s in skill_names:
			skill = self.skills_list[s]
			if s == name or skill.subskill_group != subskill_group:
				continue
				
			total += skill.total_ranks_by_level[level].get()
		return total

		
	# This method is called when the Profession is changed. Using the new profession, it determines what maneuver that profession can learn and adds them the manevuer lists.
	def Update_Maneuvers(self):
		global combat_maneuver_names, shield_maneuver_names, armor_maneuver_names, panels
		man_panel = panels['Maneuvers']										
		prof = self.profession.name
		
		# Clear the maneuvers before adding the new maneuvers
		man_panel.dialog_combat_names_menu['menu'].delete(0, "end")
		man_panel.dialog_armor_names_menu['menu'].delete(0, "end")
		man_panel.dialog_shield_names_menu['menu'].delete(0, "end")
		if man_panel.armor_menu_size > 1:
			man_panel.add_armor_order_menu['menu'].delete(1, "end")
			if man_panel.armor_menu_size > 2:
				man_panel.edit_armor_order_menu['menu'].delete(1, "end")
			man_panel.armor_menu_size = 1	
		if man_panel.combat_menu_size > 1:
			man_panel.add_combat_order_menu['menu'].delete(1, "end")
			if man_panel.combat_menu_size > 2:
				man_panel.edit_combat_order_menu['menu'].delete(1, "end")
			man_panel.combat_menu_size = 1	
		if man_panel.shield_menu_size > 1:		
			man_panel.add_shield_order_menu['menu'].delete(1, "end")
			if man_panel.shield_menu_size > 1:		
				man_panel.edit_shield_order_menu['menu'].delete(1, "end")
			man_panel.shield_menu_size = 1	
		
		man_panel.man_select_menu['menu'].delete(0, "end")	
		man_panel.ML_Frame.yview("moveto", 0, "units")
		man_panel.MR_Frame.yview("moveto", 0, "units")		

		# Remove all Build Rows from the build frame
		for man in self.build_combat_maneuvers_list:
			man.ManP_Build_Row.grid_remove()
		for man in self.build_shield_maneuvers_list:	
			man.ManP_Build_Row.grid_remove()
		for man in self.build_armor_maneuvers_list:	
			man.ManP_Build_Row.grid_remove()
		
		# Clear the build lists
		self.build_combat_maneuvers_list = []
		self.build_shield_maneuvers_list = []
		self.build_armor_maneuvers_list = []
		
		# Add each maneuver to the appropriate list if it can learn that manevuer.
		for name in combat_maneuver_names:	
			man = self.combat_maneuvers_list[name]
			man.Set_To_Default()	
			if man.availability[prof]:
				man_panel.dialog_combat_names_menu['menu'].add_command(label=name, command=lambda s=name: man_panel.Dialog_Menu_Onchange(s))
		for name in shield_maneuver_names:
			man = self.shield_maneuvers_list[name]
			man.Set_To_Default()	
			if man.availability[prof]:
				man_panel.dialog_shield_names_menu['menu'].add_command(label=name, command=lambda s=name: man_panel.Dialog_Menu_Onchange(s))
		for name in armor_maneuver_names:
			man = self.armor_maneuvers_list[name]
			man.Set_To_Default()	
			if man.availability[prof]:
				man_panel.dialog_armor_names_menu['menu'].add_command(label=name, command=lambda s=name: man_panel.Dialog_Menu_Onchange(s))
						
		# Remove/Add the Shield and Armor options to the maneuver style menue and show the Shield and Armor footers 
		if prof == "Warrior" or prof == "Rogue" or prof == "Paladin":
			man_panel.sfooter_shield_row.grid(row=2, column=0, padx="1")
			man_panel.sfooter_armor_row.grid(row=3, column=0, padx="1")
			man_panel.man_select_menu["menu"].insert_command("end", label="Combat", command=lambda s="Combat": man_panel.Maneuver_Style_Onchange(s))
			man_panel.man_select_menu["menu"].insert_command("end", label="Shield", command=lambda s="Shield": man_panel.Maneuver_Style_Onchange(s))
			man_panel.man_select_menu["menu"].insert_command("end", label="Armor", command=lambda s="Armor": man_panel.Maneuver_Style_Onchange(s))
		else:		
			man_panel.man_select_menu["menu"].insert_command("end", label="Combat", command=lambda s="Combat": man_panel.Maneuver_Style_Onchange(s))
			man_panel.sfooter_shield_row.grid_remove()
			man_panel.sfooter_armor_row.grid_remove()		
			
		# Finally reset the maneuvers panel
		man_panel.ManP_radio_var.set(1)
		man_panel.level_counter.setvalue(0)		
		man_panel.maneuver_mode.set("")
		man_panel.Maneuver_Style_Onchange("Combat")	

	
	# Checks to see if the character meets the prerequisites to train in a maneuver at a given level.
	def Meets_Maneuver_Prerequisites(self, level, name, type):
		if type == "combat":
			man = self.combat_maneuvers_list[name]
		elif type == "shield":
			man = self.shield_maneuvers_list[name]
		elif type == "armor":		
			man = self.armor_maneuvers_list[name]
			
		requirements = man.prerequisites
		or_valid = 0
		and_valid = 0
		true_valid = 1
		
		if requirements == "NONE":
			return True
			
		# Maneuver prerequisites are stored in the format in the database TYPE:NAME:RANKS
		# TYPE is what kind of prerequisite it is. Skill, CM, SM are the values 
		# NAME is the name of Skill, Combat Maneuver, Shield Maneuver.
		# RANKS is a number indicating how many ranks the character must have to gain a rank in the maneuver
		# Each prerequisite can be followed by another prerequisite with the seperator "|" for OR or "&" for AND
		and_parts = requirements.split("&")
		for apart in and_parts:
			or_parts = apart.split("|")
			or_valid = 0
			for opart in or_parts:
				semi_parts = opart.split(":")
				if semi_parts[0] == "CM":
					val = self.combat_maneuvers_list[semi_parts[1]].total_ranks_by_level[level].get()
				elif semi_parts[0] == "SM":
					val = self.shield_maneuvers_list[semi_parts[1]].total_ranks_by_level[level].get()
				elif semi_parts[0] == "Skill":
					val = self.skills_list[semi_parts[1]].total_ranks_by_level[level].get()			
			
				if val >= int(semi_parts[2]):
					or_valid = 1
					break
			
			if or_valid == 0:
				true_valid = 0
				break
		
		if true_valid == 1:
			return True
		else:
			return False

			
# The Race object hold all the information for the character's current race. 	
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
			

# The Profession object hold all the information for the character's current profession. This does not include skill costs or max ranks
class Profession:
	def __init__(self, arr):
		self.name = arr['name']
		self.type = arr['type']
		self.prime_statistics = [ arr['prime_statistics1'], arr['prime_statistics2'] ]
		self.mana_statistics = [ arr['mana_statistic1'], arr['mana_statistic2'] ]
		self.spell_circles = [ arr['spell_circle1'], arr['spell_circle2'] ]
		if arr['spell_circle3'] != "NONE":
			self.spell_circles.append(arr['spell_circle3'])
		self.statistic_growth = { "Strength": arr['strength_growth'], "Constitution": arr['constitution_growth'], "Dexterity": arr['dexterity_growth'], "Agility": arr['agility_growth'], "Discipline": arr['discipline_growth'], "Aura": arr['aura_growth'], "Logic": arr['logic_growth'], "Intuition": arr['intuition_growth'], "Wisdom": arr['wisdom_growth'], "Influence": arr['influence_growth'] }
			

# Statistic objects are responsible for mantaining the growth for their specific statistic.
# They are also responsible for the growth and statistics rows in the Statistics Panel. Including the values, bonuses, the Entry box and colors.
class Statistic:
	def __init__(self, parent, name):
		self.name = name
		self.parent = parent                   # Character object
		self.adj = 0;
		self.values_by_level = [tkinter.StringVar() for i in range(101)]
		self.bonuses_by_level = [tkinter.IntVar() for i in range(101)]
		self.values_bgs = ["lightgray" for i in range(101)]
		self.bonuses_bgs = ["lightgray" for i in range(101)]
		self.StP_display_values = [tkinter.StringVar() for i in range(101)]
		self.StP_display_bgs = ["lightgray" for i in range(101)]
		self.StP_statistic_row = ""
		self.StP_growth_row = ""
		self.entrybox = ""
		self.display_label = ""
		self.display_var = tkinter.StringVar()

		self.values_by_level[0].set("20")		
		self.display_var.set(self.name)

		
	# Returns the statistic to 20 and calculates it's growth
	def Set_To_Default(self):
		self.values_by_level[0].set("20")	
		self.Calculate_Growth()
		
		
	# Part of the Statistics panel, this Frame will show the statistic's name, bonus/penalty provided by race, growth index, and Entry Box to edit the starting statistic value.
	def Create_Statistic_Row_Frame(self, panel, stat):
		frame = tkinter.Frame(panel)
		var = self.parent.statistics_list[stat].values_by_level[0]
		mycmd = (root.register(self.Entrybox_Validate), '%d', '%S', '%s', '%P')
		var.trace_variable("w", self.Entrybox_On_Update)
		
		self.display_label = tkinter.Label(frame, width="20", anchor="w", bg="lightgray", textvar=self.display_var)
		tkinter.Label(frame, width="10", bg="lightgray", textvar=self.parent.stat_bonus[stat]).grid(row=0, column=1, padx="1", pady="1")
		tkinter.Label(frame, width="10", bg="lightgray", textvar=self.parent.stat_adj[stat]).grid(row=0, column=2, padx="1", pady="1")
		self.entrybox = tkinter.Entry(frame, width="6", justify="center", validate="key", validatecommand=mycmd, textvariable=var)
		
		self.entrybox.bind("<Down>", self.Entrybox_On_Move)
		self.entrybox.bind("<Up>", self.Entrybox_On_Move)	
		self.display_label.grid(row=0, column=0, sticky="w", padx="1", pady="1")		
		self.entrybox.grid(row=0, column=3, padx="1")
						
		return frame

		
	# This frame show the growth of a statistic or the growth of a statistic's bonus. Depends on the setting in the Statistics Panel.
	def Create_Growth_Row_Frame(self, parent):
		frame = tkinter.Frame(parent)	
	
		for i in range(101):
			tkinter.Label(frame, width=5, bg=self.StP_display_bgs[i], textvar=self.StP_display_values[i]).grid(row=0, column=i, padx="1", pady="1")	
			
		return frame		
	
	
	# Places either the value or bonus for each level in the display values to be shown in the frame. It will also color the background of each frame.
	def Update_Growth_Frame(self):	
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
		for cell in self.StP_growth_row.winfo_children():	
			cell["bg"] = self.StP_display_bgs[i]
			i += 1
			
	
	def Calculate_Growth(self):		
		if self.StP_growth_row == "":           #ignore the call if the training frame has not been created yet
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

			
	# Makes sure that the character placed in the Entry box doesn't make the length greater than 3 and that the value is less than or equal to 100. False results prevent the edit from occuring.
	def Entrybox_Validate(self, d, S, s, P):		
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
	
	
	# When something in the Entrybox changes, recalculate the statistic growth and update all the things related to statistics
	def Entrybox_On_Update(self, *args):
		self.Calculate_Growth()
		self.Update_Growth_Frame()
		self.parent.Update_Statistics()

		
	# This event files when any key is pressed while the Entrybox has focus. This method will allow a user to move up and down between Entryboxes using the Arrow keys
	def Entrybox_On_Move(self, event):
		global statistics
		new_stat = ""; found = 0
		
		if event.keysym == "Up":
			for stat in statistics:				
				if stat == self.name:
					break
				new_stat = stat
					
		elif event.keysym == "Down":
			for stat in statistics:
				if found == 1:
					new_stat = stat
					break
				elif stat == self.name:
					found = 1
			
		if new_stat == "":
			return
			
		self.parent.statistics_list[new_stat].entrybox.focus()
		self.parent.statistics_list[new_stat].entrybox.icursor("end")
		
	
	# Stat Important is a method that updates the display label for the statistic name with extra tags to indicate if the stat is a prime statistic and/or a mana statistic
	def Set_Stat_Importance(self, action):
		if action == "none":
			self.display_var.set(self.name)
		elif action == "prime":			
			self.display_var.set("%s    (P)" % self.name)
		elif action == "mana":
			self.display_var.set("%s     (M)" % self.name)
		elif action == "prime/mana":
			self.display_var.set("%s     (P,M)" % self.name)


# Each Skill object contains all the information about a skill as well as methods to update, reset, and train ranks in the skill
class Skill:
	def __init__(self, arr):
		self.name = arr[0]
		self.type = arr[1]
		self.subskill_group = arr[2]
		self.redux = arr[3]
		self.ptp_cost = ""
		self.mtp_cost = ""
		self.max_ranks = ""

		self.active_skill = 0
		self.calculated_subskill = 0
		self.cost = tkinter.StringVar()
		self.ranks = tkinter.IntVar()
		self.total_ranks = tkinter.IntVar()
		self.bonus = tkinter.IntVar()		
		self.SkP_schedule_row = ""		
		
		self.ranks_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_ranks_by_level = [tkinter.IntVar() for i in range(101)]
		self.bonus_by_level = [tkinter.IntVar() for i in range(101)]
		self.ptp_cost_at_level = [tkinter.IntVar() for i in range(101)]
		self.mtp_cost_at_level = [tkinter.IntVar() for i in range(101)]
		self.total_ptp_cost_at_level = [tkinter.IntVar() for i in range(101)]
		self.total_mtp_cost_at_level = [tkinter.IntVar() for i in range(101)]
		self.ptp_regained_at_level = [tkinter.IntVar() for i in range(101)]
		self.mtp_regained_at_level = [tkinter.IntVar() for i in range(101)]
					
		self.Set_To_Default()
		

	# Resets the Skill object	
	def Set_To_Default(self):
		for i in range(101):
			self.ranks_by_level[i].set(0)
			self.total_ranks_by_level[i].set(0)
			self.bonus_by_level[i].set(0)
			self.ptp_cost_at_level[i].set(0)
			self.mtp_cost_at_level[i].set(0)
			self.total_ptp_cost_at_level[i].set(0)
			self.total_mtp_cost_at_level[i].set(0)
			self.ptp_regained_at_level[i].set(0)
			self.mtp_regained_at_level[i].set(0)

			
	# When a new Profession is chosen, this method will be called for each Skill to change the costs and max ranks.
	# If the profession can use the skill, active_skill is set to 1 which lets it appear in the Add/Edit Dialog box and schedule array. In short, it lets the user train in it.
	def Update_Skill_Information(self, arr):
		self.name = arr[0]
		self.ptp_cost = arr[1]
		self.mtp_cost = arr[2]
		self.max_ranks = arr[3]
		
		if arr[3] > 0:
			self.active_skill = 1
		else:
			self.active_skill = 0
		
		self.Set_To_Default()

		
	# The schedule row shows the training for the current level in the skill, the cost of that training and the training and bonus for the total ranks the character has in the skill
	def Create_SkP_schedule_row(self, parent):		
		if self.SkP_schedule_row != "":
			return
			
		self.SkP_schedule_row = tkinter.Frame(parent)	
		self.SkP_schedule_row.bindtags("SkP_schedule")
		
		L1 = tkinter.Label(self.SkP_schedule_row, width="26", bg="lightgray", anchor="w", text=self.name)
		L1.grid(row=0, column=0, padx="1", pady="1")
		L1.bindtags("SkP_schedule")
		L2 = tkinter.Label(self.SkP_schedule_row, width="8", bg="lightgray", textvariable=self.ranks)	 
		L2.grid(row=0, column=1, padx="1", pady="1")	
		L2.bindtags("SkP_schedule")
		L3 = tkinter.Label(self.SkP_schedule_row, width="12", bg="lightgray", textvariable=self.cost) 		
		L3.grid(row=0, column=2, padx="1", pady="1")	
		L3.bindtags("SkP_schedule")
		L4 = tkinter.Label(self.SkP_schedule_row, width="10", bg="lightgray", textvariable=self.total_ranks)
		L4.bindtags("SkP_schedule")		
		L4.grid(row=0, column=3, padx="1", pady="1")	
		L5 = tkinter.Label(self.SkP_schedule_row, width="11", bg="lightgray", textvariable=self.bonus)	
		L5.grid(row=0, column=4, padx="1", pady="1")
		L5.bindtags("SkP_schedule")		
	
	
	# This method will calculate the cost of training "ranks" ranks in this skill at "level". This cost is based on the current level and the total number of ranks + subskill_ranks.
	# The cost is returned at the end of the method after the new ranks are added to the ranks_this_level and total_ranks_by_level variables.
	def Train_New_Ranks(self, level, subskill_ranks, ranks):
		pcost = 0	
		mcost = 0	
		pregain = 0
		mregain = 0
		tpcost = 0
		tmpcost = 0
		prev_total_ranks = self.total_ranks_by_level[level].get()	
		prev_ranks = self.ranks_by_level[level].get()	
		self.ranks_by_level[level].set(prev_ranks + ranks)	
		ranks_this_level = self.ranks_by_level[level].get()
		max = prev_total_ranks - prev_ranks
		
		# Calculate the PTP and MTP cost for training in the skill. Takes triple trains and double trains into consideration as well
		for x in range(1, ranks_this_level+1):
			if x + max + subskill_ranks > 2 * (level + 1):
				pcost += self.ptp_cost * 4
				mcost += self.mtp_cost * 4
			elif x + max + subskill_ranks > (level + 1):
				pcost += self.ptp_cost * 2
				mcost += self.mtp_cost * 2
			else:
				pcost += self.ptp_cost
				mcost += self.mtp_cost	
				
		self.ptp_cost_at_level[level].set(pcost)
		self.mtp_cost_at_level[level].set(mcost)	
		
		# Set Total Ranks and Bonus for each level
		for i in range(level, 101):
			pcost = 0	
			mcost = 0
			if i > level:
				ranks = self.ranks_by_level[i].get()					
						
			self.total_ranks_by_level[i].set(ranks + prev_total_ranks)			
			self.bonus_by_level[i].set(self.Get_Skill_Bonus(ranks + prev_total_ranks))
			prev_total_ranks = self.total_ranks_by_level[i].get()
			
			if i == level or (i > 0 and self.total_ranks_by_level[i-1].get() > i):				
				# This will calculate the cost a skill using all existing ranks relative to a specific level.
				(tpcost, tmcost) = self.Get_Total_Skill_Cost(subskill_ranks, i, i)		
				self.total_ptp_cost_at_level[i].set(tpcost)
				self.total_mtp_cost_at_level[i].set(tmcost)
			
				
	# A short method that takes the number of ranks and converts it's bonus counterpart
	def Get_Skill_Bonus(self, ranks):
		if ranks >= 40:
			return (ranks - 40) + 140
		elif ranks >= 30:
			return 2 * (ranks - 30) + 120
		elif ranks >= 20:
			return 3 * (ranks - 20) + 90
		elif ranks >= 10:
			return 4 * (ranks - 10) + 50
		else:
			return ranks * 5
			
			
	# When the character gains a level, any skills above the level+1 are converted down a level. IE triple trains become double trains and double trains become single trains.
	# The result of this is a TP refund to the character for the shift down. This method will calculate out all the refunds from start to end
	def Calculate_TP_Regain(self, start, end):
		if start < 1 or end > 100:
			return			
			
		for i in range(start, end+1):
			(pregain, mregain) = self.Get_Total_Skill_Cost(0, i, i-1)				
			self.ptp_regained_at_level[i].set(max(0, self.total_ptp_cost_at_level[i-1].get() - pregain))
			self.mtp_regained_at_level[i].set(max(0, self.total_mtp_cost_at_level[i-1].get() - mregain))	
			if self.total_ranks_by_level[i].get() == self.total_ranks_by_level[100].get() and (self.ptp_regained_at_level[i].get() == 0 and self.mtp_regained_at_level[i].get() == 0):
				break		
				
				
	# Figures out the skill cost using the existing ranks and any subskill ranks.
	def Get_Total_Skill_Cost(self, subskill_ranks, current_level, tranks_level):
		pcost = 0; mcost = 0		
		tranks = self.total_ranks_by_level[tranks_level].get()
		
		triple_train = max(0, tranks + subskill_ranks - 2 * (current_level + 1))
		double_train = max(0, tranks + subskill_ranks- triple_train - (current_level + 1))
		single_train = max(0, tranks + subskill_ranks- triple_train - double_train)		
				
		pcost = self.ptp_cost * single_train  +  2 * self.ptp_cost * double_train  +  4 * self.ptp_cost * triple_train
		mcost = self.mtp_cost * single_train  +  2 * self.mtp_cost * double_train  +  4 * self.mtp_cost * triple_train	

		return (pcost, mcost)
		
		
	# Figures out how much it would cost to take "new_ranks" number of ranks in this skill given level, total ranks, and subskill ranks
	def Get_Next_Ranks_Cost(self, level, subskill_ranks, new_ranks):			
		total_ranks = self.total_ranks_by_level[level].get()
		pcost = 0; mcost = 0; end = new_ranks+1

		if total_ranks + new_ranks + subskill_ranks > self.max_ranks * (level+1):
			return (9999, 9999)
		
		for i in range(1, end):
			if total_ranks + i + subskill_ranks > 2 * (level + 1):
				pcost += 4 * self.ptp_cost
				mcost += 4 * self.mtp_cost
			elif total_ranks + i + subskill_ranks > level + 1:
				pcost += 2 * self.ptp_cost
				mcost += 2 * self.mtp_cost
			else:
				pcost += self.ptp_cost
				mcost += self.mtp_cost		
		
		return (pcost, mcost)
				

# Each maneuver object contains all the information about a maneuver as well as methods to update, reset, and train ranks in the maneuver
class Maneuver:
	def __init__(self, schedule_parent, arr):
		global professions
		
		self.name = arr[0]
		self.mnemonic = arr[1]
		self.type = arr[2]
		self.max_ranks = arr[3]	
		self.cost_by_rank = [arr[4], arr[5], arr[6], arr[7], arr[8]]
		self.availability = {}
		self.prerequisites = arr['prerequisites']	
		self.ManP_schedule_row = ""		
	
		self.ranks_by_level = [tkinter.IntVar() for i in range(101)]
		self.cost_at_level = [tkinter.IntVar() for i in range(101)]
		self.total_ranks_by_level = [tkinter.IntVar() for i in range(101)]
		self.combined_cost_by_level = [tkinter.IntVar() for i in range(101)]	
		
		self.cost = tkinter.StringVar()
		self.ranks = tkinter.IntVar()
		self.total_ranks = tkinter.IntVar()
		self.combined_cost = tkinter.IntVar()
	
		for prof in professions:
			self.availability[prof] = arr['available_'+prof.lower()]
	
		for i in range(0,5):
			if self.cost_by_rank[i] == "NONE":
				self.cost_by_rank[i] = "-"
				
		self.Create_ManP_schedule_row(schedule_parent)		
		self.Set_To_Default()


	# Resets the Skill object			
	def Set_To_Default(self):
		self.cost.set("")
		self.ranks.set(0)
		self.total_ranks.set(0)
		self.combined_cost.set(0)
		
		for i in range(101):
			self.ranks_by_level[i].set(0)
			self.cost_at_level[i].set(0)
			self.total_ranks_by_level[i].set(0)
			self.combined_cost_by_level[i].set(0)			

		self.ManP_schedule_row.grid_remove()
	

	# The schedule row shows the training for the current level in the maneuver, the cost of that training and the training for the total ranks the character has in the maneuver	
	def Create_ManP_schedule_row(self, parent):
		self.ManP_schedule_row = tkinter.Frame(parent)	
		self.ManP_schedule_row.bindtags("ManP_schedule")
		
		L1 = tkinter.Label(self.ManP_schedule_row, width="26", bg="lightgray", anchor="w", text=self.name)
		L1.grid(row=0, column=0, padx="1", pady="1")
		L1.bindtags("ManP_schedule")
		L2 = tkinter.Label(self.ManP_schedule_row, width="8", bg="lightgray", textvariable=self.ranks)	 
		L2.grid(row=0, column=1, padx="1", pady="1")	
		L2.bindtags("ManP_schedule")
		L3 = tkinter.Label(self.ManP_schedule_row, width="6", bg="lightgray", textvariable=self.cost) 		
		L3.grid(row=0, column=2, padx="1", pady="1")	
		L3.bindtags("ManP_schedule")
		L4 = tkinter.Label(self.ManP_schedule_row, width="10", bg="lightgray", textvariable=self.total_ranks)
		L4.bindtags("ManP_schedule")		
		L4.grid(row=0, column=3, padx="1", pady="1")	
		L5 = tkinter.Label(self.ManP_schedule_row, width="8", bg="lightgray", textvariable=self.combined_cost)	
		L5.grid(row=0, column=4, padx="1", pady="1")
		L5.bindtags("ManP_schedule")		

	
	# Figures out how much it cost to train in the maneuver at "rank" rank. 
	# "prof_type" will determine if there is an additional cost to train in the skill. Only "combat" maneuvers have an extra cost.
	def Get_Cost_At_Rank(self, rank, prof_type):
		if self.cost_by_rank[rank-1] == "-":
			return "-"
			
		if prof_type == "square" or self.type != "combat":
			modifier = 1
		elif prof_type == "semi":
			modifier = 1.5
		elif prof_type == "pure":
			modifier = 2	

		return math.floor(int(self.cost_by_rank[rank-1]) * modifier)				
	

	# Similar to Get_Cost_At_Rank, this method will figure out the CUMULATIVE cost to train "new_ranks" ranks in this manevuer starting at "start_rank" ranks.
	# "prof_type" will determine if there is an additional cost to train in the skill. Only "combat" maneuvers have an extra cost.
	def Get_Total_Cost_At_Rank(self, start_rank, new_ranks, prof_type):		
		total = 0
		end_rank = start_rank + new_ranks
		if prof_type == "square" or self.type != "combat":
			modifier = 1
		elif prof_type == "semi":
			modifier = 1.5
		elif prof_type == "pure":
			modifier = 2	
				
		if end_rank > 5 or self.cost_by_rank[end_rank - 1] == "-":
			return -1
			
		for i in range(start_rank, end_rank):
			total += math.floor(int(self.cost_by_rank[i]) * modifier)
			
		return total


	# This method will calculate the cost of training "ranks" ranks in this maneuver at "level". This cost is based on the existing skill ranks and what "prof_type" the characters profession is.	
	def Train_New_Ranks(self, level, ranks, prof_type):
		tcost = 0				
		new_total_ranks = self.ranks_by_level[level].get() + ranks		
		
		if level > 0:
			new_total_ranks += self.total_ranks_by_level[level-1].get()
		
		tcost =	self.Get_Total_Cost_At_Rank(0, new_total_ranks, prof_type)
		diff = self.total_ranks_by_level[level].get() - self.ranks_by_level[level].get()
		ncost = self.Get_Total_Cost_At_Rank(diff, self.ranks_by_level[level].get() + ranks, prof_type)
		
		self.cost_at_level[level].set(ncost)
		self.ranks_by_level[level].set(ranks + self.ranks_by_level[level].get())
		
		# Set Total Ranks and Bonus for each level
		for i in range(level, 101):
			self.total_ranks_by_level[i].set(new_total_ranks)				
			self.combined_cost_by_level[i].set(tcost)				
		

# The Planner's "Error Box". This dialog box will appear when an error or warning is triggered by the user.
class Information_Dialog:
	def __init__(self):
		global root	
		self.width = 400; self.height = 250; self.xpos = 450; self.ypos = 300		
		self.dialogbox = Pmw.Dialog(root, buttons = ("Okay", ), title = "Information", command = self.Button_Onclick)
		self.message = tkinter.StringVar()
		self.myframe = Pmw.ScrolledFrame(self.dialogbox.interior(), usehullsize = 1, hull_width = self.width, hull_height = self.height-35)
		self.myframe_inner = self.myframe.interior()			
			
		self.dialogbox.transient(root)	
		self.dialogbox.resizable(width=0, height=0)		
		self.dialogbox.geometry('%sx%s+%s+%s' % (self.width, self.height, self.xpos, self.ypos))

		self.myframe.configure(hscrollmode = "none")		
		self.myframe.grid(row=0, column=0, sticky="nw")	
		tkinter.Label(self.myframe_inner, anchor="w", font="-weight bold", wraplength=self.width-10, justify="left", textvariable=self.message).grid(row=0, column=0, sticky="w")
		self.dialogbox.bind("<MouseWheel>", self.Scroll_Inner_Frame)
		self.dialogbox.withdraw()

		
	# Clicking the Okay button hides the dialog box. Also, cancelling the box does this too.
	def Button_Onclick(self, result):
		self.dialogbox.grab_release()
		self.dialogbox.withdraw()
		self.message.set("")	

		
	# Makes the dialog appear with a message.
	def Show_Message(self, msg):
		self.message.set(msg)
		self.dialogbox.show()
		self.dialogbox.grab_set()

		
	def Scroll_Inner_Frame(self, event):
		self.myframe.yview("scroll", -1*(event.delta/120), "units")
		

	
#Planner globals		
root = tkinter.Tk()
version = "v2.3"
db_file = "GS4_Planner.db"
db_con = ""
db_cur = ""
panels = {}
info_dialog = Information_Dialog()
char_name = "New Character"
		
# Statistics Panel globals		
statistics = ["Strength", "Constitution", "Dexterity", "Agility", "Discipline", "Aura", "Logic", "Intuition", "Wisdom", "Influence"]
professions = ["Bard", "Cleric", "Empath", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warrior", "Wizard"]
races = ["Aelotoi", "Burghal Gnome", "Dark Elf", "Dwarf", "Elf", "Erithian", "Forest Gnome", "Giantman", "Half Elf", "Half Krolvin", "Halfling", "Human", "Sylvankind"]	
	
	
# Skills Panel globals	
skill_names = []


# Maneuvers Panel globals
combat_maneuver_names = []
shield_maneuver_names = []
armor_maneuver_names = []


# Character global needs to be declared last since it uses the above globals
character = Character();
