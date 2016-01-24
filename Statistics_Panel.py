# TODO LIST
# Consider changing the scrolling table structure to a graph format.

# INDEX OF CLASSES AND METHODS
'''
class Statistics_Panel
	def __init__(self, panel)
	def Create_Statistics_Header(self, panel):	
	def Create_Statistics_Rows(self, panel):
	def Create_Statistics_Footer(self, panel):	
	def Create_Growth_Header(self, panel):
	def Create_Growth_Rows(self, panel):
	def Create_Growth_Footer(self, panel):	
	def Linked_Scrolling(self, *args):
	def Change_Display_Style(self):		
	def Change_Race(self, race):		
	def Change_Profession(self, prof):
'''


#!/usr/bin/python

import tkinter
import Pmw
import Globals as globals
  
  
# Statistics Panel will show the growth of the 10 statistics in GS4 based on race/profession combination
# All resources derived from the statistics are also calculated here. PTP, MTP, Health, Mana, Stamina, Spirit
class Statistics_Panel:  
	def __init__(self, panel):		
		self.ptp_bgs = ["lightgray" for i in range(101)]
		self.mtp_bgs = ["lightgray" for i in range(101)]
		self.ptp_frame = ""		# These frames need to be tracked because the background of their child cells will change depending stat growth
		self.mtp_frame = ""		
		self.StP_radio_var = tkinter.IntVar()
		
		#These are the linked scrolling frames for the Panel
		self.lvl_header_scrollframe = ""		
		self.training_middle_scrollframe = ""
		self.resource_footer_scrollframe = ""		
		
		#Create all the sub-frames of the panel
		self.UL_Frame = self.Create_Statistics_Header(panel)
		self.ML_Frame = self.Create_Statistics_Rows(panel)
		self.LL_Frame = self.Create_Statistics_Footer(panel)
		self.UR_Frame = self.Create_Growth_Header(panel)
		self.MR_Frame = self.Create_Growth_Rows(panel)
		self.LR_Frame = self.Create_Growth_Footer(panel)	
		
		#Make the frames visible
		self.UL_Frame.grid(row=0, column=0, sticky="nw")
		self.ML_Frame.grid(row=1, column=0, sticky="nw")
		self.LL_Frame.grid(row=2, column=0, sticky="nw")
		self.UR_Frame.grid(row=0, column=1, sticky="nw")
		self.MR_Frame.grid(row=1, column=1, sticky="nw")
		self.LR_Frame.grid(row=2, column=1, sticky="nw")
		
		#initialize defaults
		self.StP_radio_var.set(1)
		
		
	# The Statistics Header is the location of the drop down menues that are used to select a race and a profession			
	def Create_Statistics_Header(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 350, hull_height = 100)
		myframe.component("borderframe").config(borderwidth=0)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")	
		myframe_inner = myframe.interior()
		
		# Dropdown menus. Create the default variables
		options1 = globals.professions
		options2 = globals.races
		self.profession_dd = tkinter.StringVar()
		self.race_dd = tkinter.StringVar()				
		self.profession_dd.set(options1[8])
		self.race_dd.set(options2[11])				
		
		# Creates the Profession Menu and frames
		prof_frame = tkinter.Frame(myframe_inner)
		prof_name = tkinter.Label(prof_frame, width="20", anchor="w", text="Profession:")
		prof_options = tkinter.OptionMenu(prof_frame, self.profession_dd, *options1, command=self.Change_Profession)
		prof_options.config(width=15)
				
		# Creates the Race Menu and frames		
		race_frame = tkinter.Frame(myframe_inner)
		race_name = tkinter.Label(race_frame, width="20", anchor="w", text="Race:")
		race_options = tkinter.OptionMenu(race_frame, self.race_dd, *options2, command=self.Change_Race)
		race_options.config(width=15)
		
		# The title frame is used as a column header for the statistics. 
		# It's made in a different frame from the actual statistics to allow for the possiblity of scrolling without losing the header
		titleframe = tkinter.Frame(myframe_inner)	
		stat_title = tkinter.Label(titleframe, width="20", bg="lightgray", text="Statistic")
		rb_title = tkinter.Label(titleframe, width="10", bg="lightgray", text="Race Bonus")
		gi_title = tkinter.Label(titleframe, bg="lightgray", text="Growth Index")
		bs_title = tkinter.Label(titleframe, width="6", bg="lightgray", text="Base")
		
		blank = tkinter.Label(myframe_inner, text="")      #This exists because there is no way to allow an empty row or column normally with grid formatting
		
		# Add all the frames to the main frame with grid and return the main frame back
		prof_name.grid(row=0, column=0, sticky="w")		
		prof_options.grid(row=0, column=1, sticky="w", padx="1")		
		race_name.grid(row=1, column=0, sticky="w")
		race_options.grid(row=1, column=1, sticky="w", padx="1")		
		
		prof_frame.grid(row=0, column=0, sticky="w", columnspan=4)			
		race_frame.grid(row=1, column=0, sticky="w", columnspan=4)	
		blank.grid(row=2, column=0)			
		
		titleframe.grid(row=3, column=0, columnspan=2)		
		stat_title.grid(row=0, column=0, sticky="w", padx="1")	
		rb_title.grid(row=0, column=1, padx="1")		
		gi_title.grid(row=0, column=2, padx="1")
		bs_title.grid(row=0, column=3, padx="1")				
		
		return myframe

		
	# The Statistics Rows frame creates a row for each statistic. Each row had the Statistic Name, Race Bonus, Growth Index and an Editbox for the base value
	def Create_Statistics_Rows(self, panel):
		i=0 		
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 350, hull_height = 233)			
		myframe.configure(hscrollmode = "none", vscrollmode = "none")				
		myframe_inner = myframe.interior()		
		
		for stat in globals.statistics:				
			globals.character.statistics_list[stat].StP_statistic_row = globals.character.statistics_list[stat].Create_Statistic_Row_Frame(myframe_inner, stat)
			globals.character.statistics_list[stat].StP_statistic_row.grid(row=i, column=0)
			i = i + 1		
		
		return myframe	


	# The Statistics Footer creates a title and base value for the statistics total, PTP, MTP, and for each of the resources
	def Create_Statistics_Footer(self, panel):	
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 350, hull_height = 205)			
		myframe.configure(hscrollmode = "none", vscrollmode = "none")			
		myframe_inner = myframe.interior()		
		
		# This creates the titles for each row
		tkinter.Label(myframe_inner, width=42, bg="lightgray", anchor="e", text="Statistics Total").grid(row=0, column=0, padx="2", pady="1")
		tkinter.Label(myframe_inner, width=42, bg="lightgray", anchor="e", text="PTP").grid(row=1, column=0, padx="2", pady="1")
		tkinter.Label(myframe_inner, width=42, bg="lightgray", anchor="e", text="MTP").grid(row=2, column=0, padx="2", pady="1")
		tkinter.Label(myframe_inner, width=42, text="").grid(row=3, column=0)
		tkinter.Label(myframe_inner, width=42, bg="lightgray", anchor="e", text="Health").grid(row=4, column=0, padx="2", pady="1")	
		tkinter.Label(myframe_inner, width=42, bg="lightgray", anchor="e", text="Mana").grid(row=5, column=0, padx="2", pady="1")
		tkinter.Label(myframe_inner, width=42, bg="lightgray", anchor="e", text="Stamina").grid(row=6, column=0, padx="2", pady="1")
		tkinter.Label(myframe_inner, width=42, bg="lightgray", anchor="e", text="Spirit").grid(row=7, column=0, padx="2", pady="1")	

		# This creates the base value boxes for each row		
		tkinter.Label(myframe_inner, width=5, bg="white", anchor="c", textvar=globals.character.statistic_totals_by_level[0]).grid(row=0, column=1, pady="1")	
		tkinter.Label(myframe_inner, width=5, bg="white", anchor="c", textvar=globals.character.ptp_base).grid(row=1, column=1, pady="1")
		tkinter.Label(myframe_inner, width=5, bg="white", anchor="c", textvar=globals.character.mtp_base).grid(row=2, column=1, pady="1")
		tkinter.Label(myframe_inner, width=5, text="").grid(row=3, column=1)
		tkinter.Label(myframe_inner, width=5, bg="red", fg="white", anchor="c", textvar=globals.character.health_by_level[0]).grid(row=4, column=1, pady="1")	
		tkinter.Label(myframe_inner, width=5, bg="blue", fg="white", anchor="c", textvar=globals.character.mana_by_level[0]).grid(row=5, column=1, pady="1")
		tkinter.Label(myframe_inner, width=5, bg="yellow", anchor="c", textvar=globals.character.stamina_by_level[0]).grid(row=6, column=1, pady="1")
		tkinter.Label(myframe_inner, width=5, bg="darkgray", fg="white", anchor="c", textvar=globals.character.spirit_by_level[0]).grid(row=7, column=1, pady="1")	
				
		return myframe
	
	
	# The Create_Growth_Header frame holds the radio buttons that switch between the growth of statistic values and
	# statistic bonuses and a linked scrolling frame containing Level numbers from 0-100
	def Create_Growth_Header(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 820, hull_height = 100)
		myframe.component("borderframe").config(borderwidth=0)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")			
		myframe_inner = myframe.interior()					
		contentframe = tkinter.Frame(myframe_inner, width=1, height=1)
		
		# Add the spacing rows to the frame
		tkinter.Label(myframe_inner, width=1, anchor="w", text="").grid(row=0, column=0, sticky="w", pady="1")
		tkinter.Label(myframe_inner, width=1, anchor="w", text="").grid(row=1, column=0, sticky="w", pady="1")	
		contentframe.grid(row=2, column=0, sticky="w")
		
		# Create a label and the radio buttons that switch betweem display styles
		tkinter.Label(contentframe, anchor="w", text="Statistics by Level").grid(row=0, column=0, sticky="w", pady="1")	
		tkinter.Radiobutton(contentframe, anchor="w", text="Show Statistics Growth", command=self.Change_Display_Style, var=self.StP_radio_var, value=1).grid(row=0, column=1, sticky="w", pady="1")
		tkinter.Radiobutton(contentframe, anchor="w", text="Show Statistics Bonus", command=self.Change_Display_Style , var=self.StP_radio_var, value=2).grid(row=0, column=2, sticky="w", pady="1")		
		
		# Create the level header scroll frame. This is linked to the growth rows frame and growth footer frame and will scroll in unison with both when the footer's scrollbar is moved
		self.lvl_header_scrollframe = Pmw.ScrolledFrame(myframe_inner,  usehullsize = 1, hull_width = 820, hull_height = 25 )		
		self.lvl_header_scrollframe.configure(hscrollmode = "none")		
		self.lvl_header_scrollframe_inner = self.lvl_header_scrollframe.interior()
		self.lvl_header_scrollframe.grid(row=3, column=0, sticky="w")

		# Create 101 numbered cells for the level header
		for i in range(101):
			lvl_label = tkinter.Label(self.lvl_header_scrollframe_inner, width=5, bg="black", fg="white", text=i)
			lvl_label.grid(row=0, column=i, padx="1")

	
		return myframe
		
	
	# This frame holds several rows, one for each statistics, each with 101 cells representing levels 0-100. The rows are created and stored with each Statistic object as part
	# of the Character object.
	def Create_Growth_Rows(self, panel):
		i=0 		
		self.training_middle_scrollframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 820, hull_height = 233)		
		self.training_middle_scrollframe_inner = self.training_middle_scrollframe.interior()
		self.training_middle_scrollframe.configure(hscrollmode = "none", vscrollmode = "none")

		# For each statistic, add their row.
		for stat in globals.statistics:	
			globals.character.statistics_list[stat].StP_growth_row = globals.character.statistics_list[stat].Create_Growth_Row_Frame(self.training_middle_scrollframe_inner)
			globals.character.statistics_list[stat].StP_growth_row.grid(row=i, column=0)
			i = i + 1						
		
		return self.training_middle_scrollframe
		

	# This frame holds several rows, one for the statistics total, PTP, MTP, and for each of the resources, each with 101 cells representing levels 0-100. 
	def Create_Growth_Footer(self, panel):
		self.resource_footer_scrollframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 820, hull_height = 205)	
		self.resource_footer_scrollframe.configure(vscrollmode = "none")			
		self.resource_footer_scrollframe_inner = self.resource_footer_scrollframe.interior()		
		self.resource_footer_scrollframe.component("horizscrollbar").config(command=self.Linked_Scrolling)
		
		# Create each frame
		myframe = tkinter.Frame(self.resource_footer_scrollframe_inner)	
		total_frame = tkinter.Frame(myframe)	
		self.ptp_frame = tkinter.Frame(myframe)
		self.mtp_frame = tkinter.Frame(myframe)	
		spacer_frame = tkinter.Frame(myframe)
		health_frame = tkinter.Frame(myframe)
		mana_frame = tkinter.Frame(myframe)
		stamina_frame = tkinter.Frame(myframe)
		spirit_frame = tkinter.Frame(myframe)
				
		# Add each frame to the parent frame using grid
		total_frame.grid(row=0, column=0)
		self.ptp_frame.grid(row=1, column=0)
		self.mtp_frame.grid(row=2, column=0)
		spacer_frame.grid(row=3, column=0)
		health_frame.grid(row=4, column=0)
		mana_frame.grid(row=5, column=0)
		stamina_frame.grid(row=6, column=0)		
		spirit_frame.grid(row=7, column=0)		
		myframe.grid(row=0, column=0, sticky="nw")	
		
		# Create 101 cells for each row
		for i in range(101):
			tkinter.Label(total_frame, width=5, bg="lightgray", textvar=globals.character.statistic_totals_by_level[i]).grid(row=0, column=i, padx="1", pady="1")		
			tkinter.Label(self.ptp_frame, width=5, bg="lightgray", textvar=globals.character.ptp_by_level[i]).grid(row=0, column=i, padx="1", pady="1")	
			tkinter.Label(self.mtp_frame, width=5, bg="lightgray", textvar=globals.character.mtp_by_level[i]).grid(row=0, column=i, padx="1", pady="1")	
			tkinter.Label(spacer_frame, width=5, text="").grid(row=0, column=i)			
			tkinter.Label(health_frame, width=5, bg="red", fg="white", textvar=globals.character.health_by_level[i]).grid(row=0, column=i, padx="1", pady="1")		
			tkinter.Label(mana_frame, width=5, bg="blue", fg="white", textvar=globals.character.mana_by_level[i]).grid(row=0, column=i, padx="1", pady="1")		
			tkinter.Label(stamina_frame, width=5, bg="yellow", textvar=globals.character.stamina_by_level[i]).grid(row=0, column=i, padx="1", pady="1")			
			tkinter.Label(spirit_frame, width=5, bg="darkgray", fg="white", textvar=globals.character.spirit_by_level[i]).grid(row=0, column=i, padx="1", pady="1")	
						
		return self.resource_footer_scrollframe
			
	
	# The level header frame, entire Growth_Rows frame, and entire Growth_Footer frame are linked together by this method
	# When the horizontal scrollbar of the Growth_Footer is moved, the other frames will move to the same location as well
	def Linked_Scrolling(self, *args):
		self.training_middle_scrollframe.xview(*args)
		self.resource_footer_scrollframe.xview(*args)
		self.lvl_header_scrollframe.xview(*args)
	
	
	# Handles switch between showing statistic values and statistic bonuses. Called by the radio button in the Growth_Header frame
	def Change_Display_Style(self):	
		for stat in globals.statistics:
			globals.character.statistics_list[stat].Update_Growth_Frame()

			
	# Changes the Character's race and updates all calculations to reflect the change		
	def Change_Race(self, race):	
		globals.db_cur.execute("SELECT * FROM Races WHERE name='%s'" % race)
		globals.db_con.commit()		
		data = globals.db_cur.fetchone()				
		
		# Change the character's race by creating a new Race object
		globals.character.race = globals.Race(data)
		
		# This happens during the initial set up. Ignore the rest of the function
		if globals.character.profession == "":
			for stat in globals.statistics:
				globals.character.stat_bonus[stat].set(globals.character.race.statistic_bonus[stat])
			return
		
		
		# Update all the statistics with new bonuses and stat growth
		for stat in globals.statistics:
			globals.character.stat_bonus[stat].set(globals.character.race.statistic_bonus[stat])
			globals.character.stat_adj[stat].set(globals.character.race.statistic_adj[stat] + globals.character.profession.statistic_growth[stat])	
			globals.character.statistics_list[stat].adj = globals.character.race.statistic_adj[stat] + globals.character.profession.statistic_growth[stat]
			globals.character.statistics_list[stat].Calculate_Growth()
			globals.character.statistics_list[stat].Update_Growth_Frame()
			
		# Recalculate the statistics
		globals.character.Update_Statistics()

		
	# Changes the Character's profession and updates all calculations to reflect the change				
	def Change_Profession(self, prof):
		globals.db_cur.execute("SELECT * FROM Professions WHERE name='%s'" % prof)
		globals.db_con.commit()		
		data = globals.db_cur.fetchone()				

		# Change the character's profession		
		globals.character.profession = globals.Profession(data)
		
		# Update all the statistics with new bonuses and stat growth		
		for stat in globals.statistics:			
			globals.character.stat_adj[stat].set(globals.character.race.statistic_adj[stat] + globals.character.profession.statistic_growth[stat])	
			globals.character.statistics_list[stat].adj = globals.character.race.statistic_adj[stat] + globals.character.profession.statistic_growth[stat]	
			
			if stat in globals.character.profession.prime_statistics and stat in globals.character.profession.mana_statistics:
				globals.character.statistics_list[stat].Set_Stat_Importance("prime/mana")
			elif stat in globals.character.profession.prime_statistics:
				globals.character.statistics_list[stat].Set_Stat_Importance("prime")
			elif stat in globals.character.profession.mana_statistics: 
				globals.character.statistics_list[stat].Set_Stat_Importance("mana")
			else:
				globals.character.statistics_list[stat].Set_Stat_Importance("none")
				
			globals.character.statistics_list[stat].Calculate_Growth()
			globals.character.statistics_list[stat].Update_Growth_Frame()
			
		
		# Update Statistics calulcation, Skill costs, and Maneuver availablity and cost
		globals.character.Update_Skills()
		globals.character.Update_Maneuvers()
		globals.character.Update_Statistics()						
