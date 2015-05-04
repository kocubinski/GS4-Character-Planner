#!/usr/bin/python

import tkinter
import Pmw
import Globals as globals
  
class Statistics_Panel:  
	def __init__(self, parent, panel, character):		
		self.parent = parent
		self.character = character
		
		#These are the linked scrolling frames for the Panel
		self.lvl_header_scrollframe = ""		
		self.training_middle_scrollframe = ""
		self.resource_footer_scrollframe = ""		
		
		#Create all the sub-frames of the panel
		self.UL_Frame = self.Create_Info_Header(panel)
		self.ML_Frame = self.Create_Info_Rows(panel)
		self.LL_Frame = self.Create_Info_Footer(panel)
		self.UR_Frame = self.Create_Training_Header(panel)
		self.MR_Frame = self.Create_Training_Rows(panel)
		self.LR_Frame = self.Create_Training_Footer(panel)	
		
		#Make the frames visible
		self.UL_Frame.grid(row=0, column=0, sticky="nw")
		self.ML_Frame.grid(row=1, column=0, sticky="nw")
		self.LL_Frame.grid(row=2, column=0, sticky="nw")
		self.UR_Frame.grid(row=0, column=1, sticky="nw")
		self.MR_Frame.grid(row=1, column=1, sticky="nw")
		self.LR_Frame.grid(row=2, column=1, sticky="nw")
		
		
		#initialize defaults
		self.character.StP_Change_Race("Human")
		self.character.StP_radio_var.set(1)
				
				
	def Create_Info_Header(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 350, hull_height = 100)
		myframe.component("borderframe").config(borderwidth=0)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")	
		myframe_inner = myframe.interior()
		
		# Dropdown menus
		options1 = globals.professions
		options2 = globals.races
		self.profession_dd = tkinter.StringVar()
		self.race_dd = tkinter.StringVar()				
		self.profession_dd.set(options1[8])
		self.race_dd.set(options2[11])				
		
		prof_frame = tkinter.Frame(myframe_inner)
		prof_name = tkinter.Label(prof_frame, width="20", anchor="w", text="Profession:")
		prof_options = tkinter.OptionMenu(prof_frame, self.profession_dd, *options1, command=self.character.StP_Change_Profession)
		prof_options.config(width=15)
				
		race_frame = tkinter.Frame(myframe_inner)
		race_name = tkinter.Label(race_frame, width="20", anchor="w", text="Race:")
		race_options = tkinter.OptionMenu(race_frame, self.race_dd, *options2, command=self.character.StP_Change_Race)
		race_options.config(width=15)
		
		titleframe = tkinter.Frame(myframe_inner)	
		stat_title = tkinter.Label(titleframe, width="20", bg="lightgray", text="Statistic")
		rb_title = tkinter.Label(titleframe, width="10", bg="lightgray", text="Race Bonus")
		gi_title = tkinter.Label(titleframe, bg="lightgray", text="Growth Index")
		bs_title = tkinter.Label(titleframe, width="6", bg="lightgray", text="Base")
		
		blank = tkinter.Label(myframe_inner, text="")
		
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

		
	def Create_Info_Rows(self, panel):
		i=0 		
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 350, hull_height = 233)			
		myframe.configure(hscrollmode = "none", vscrollmode = "none")				
		myframe_inner = myframe.interior()		
		
		for stat in globals.statistics:				
			self.character.statistics[stat].StP_info_row = self.character.statistics[stat].Create_Info_Row_Frame(myframe_inner, stat, self.character)
			self.character.statistics[stat].StP_info_row.grid(row=i, column=0)
			i = i + 1		
		
		return myframe	

		
	def Create_Info_Footer(self, panel):	
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 350, hull_height = 205)			
		myframe.configure(hscrollmode = "none", vscrollmode = "none")			
		myframe_inner = myframe.interior()		
		
		total_title = tkinter.Label(myframe_inner, width=42, bg="lightgray", anchor="e", text="Statistics Total")
		ptp_title = tkinter.Label(myframe_inner, width=42, bg="lightgray", anchor="e", text="PTP")
		mtp_title = tkinter.Label(myframe_inner, width=42, bg="lightgray", anchor="e", text="MTP")
		health_title = tkinter.Label(myframe_inner, width=42, bg="lightgray", anchor="e", text="Health")
		mana_title = tkinter.Label(myframe_inner, width=42, bg="lightgray", anchor="e", text="Mana")
		stamina_title = tkinter.Label(myframe_inner, width=42, bg="lightgray", anchor="e", text="Stamina")
		spirit_title = tkinter.Label(myframe_inner, width=42, bg="lightgray", anchor="e", text="Spirit")
		space_title = tkinter.Label(myframe_inner, width=42, text="")
				
		total_base = tkinter.Label(myframe_inner, width=5, bg="white", anchor="c", textvar=self.character.stat_totals[0])
		ptp_base = tkinter.Label(myframe_inner, width=5, bg="white", anchor="c", textvar=self.character.ptp_base)
		mtp_base = tkinter.Label(myframe_inner, width=5, bg="white", anchor="c", textvar=self.character.mtp_base)
		health_base = tkinter.Label(myframe_inner, width=5, bg="red", fg="white", anchor="c", textvar=self.character.health_by_level[0])
		mana_base = tkinter.Label(myframe_inner, width=5, bg="blue", fg="white", anchor="c", textvar=self.character.mana_by_level[0])
		stamina_base = tkinter.Label(myframe_inner, width=5, bg="yellow", anchor="c", textvar=self.character.stamina_by_level[0])
		spirit_base = tkinter.Label(myframe_inner, width=5, bg="darkgray", fg="white", anchor="c", textvar=self.character.spirit_by_level[0])
		space_title2 = tkinter.Label(myframe_inner, width=5, text="")
				
	
		total_title.grid(row=0, column=0, padx="2", pady="1")	
		ptp_title.grid(row=1, column=0, padx="2", pady="1")	
		mtp_title.grid(row=2, column=0, padx="2", pady="1")	
		space_title.grid(row=3, column=0)	
		health_title.grid(row=4, column=0, padx="2", pady="1")	
		mana_title.grid(row=5, column=0, padx="2", pady="1")	
		stamina_title.grid(row=6, column=0, padx="2", pady="1")	
		spirit_title.grid(row=7, column=0, padx="2", pady="1")	

		total_base.grid(row=0, column=1, pady="1")	
		ptp_base.grid(row=1, column=1, pady="1")	
		mtp_base.grid(row=2, column=1, pady="1")	
		space_title2.grid(row=3, column=1)	
		health_base.grid(row=4, column=1, pady="1")	
		mana_base.grid(row=5, column=1, pady="1")	
		stamina_base.grid(row=6, column=1, pady="1")	
		spirit_base.grid(row=7, column=1, pady="1")			
			
		return myframe
	
	
	def Create_Training_Header(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 820, hull_height = 100)
		myframe.component("borderframe").config(borderwidth=0)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")			
		myframe_inner = myframe.interior()		
		empty = tkinter.Label(myframe_inner, width=1, anchor="w", text="")
		empty2 = tkinter.Label(myframe_inner, width=1, anchor="w", text="")					
		otherframe = tkinter.Frame(myframe_inner, width=1, height=1)
		
		stat_by_lvl = tkinter.Label(otherframe, anchor="w", text="Statistics by Level")		
		radio1 = tkinter.Radiobutton(otherframe, anchor="w", text="Show Statistics Growth", command=self.character.StP_Change_Display_Style, var=self.character.StP_radio_var, value=1)
		radio2 = tkinter.Radiobutton(otherframe, anchor="w", text="Show Statistics Bonus", command=self.character.StP_Change_Display_Style , var=self.character.StP_radio_var, value=2)		
			
		self.lvl_header_scrollframe = Pmw.ScrolledFrame(myframe_inner,  usehullsize = 1, hull_width = 820, hull_height = 25 )		
		self.lvl_header_scrollframe.configure(hscrollmode = "none")		
		self.lvl_header_scrollframe_inner = self.lvl_header_scrollframe.interior()
		
		for i in range(101):
			lvl_label = tkinter.Label(self.lvl_header_scrollframe_inner, width=5, bg="black", fg="white", text=i)
			lvl_label.grid(row=0, column=i, padx="1")
	
		empty.grid(row=0, column=0, sticky="w", pady="1")	
		empty2.grid(row=1, column=0, sticky="w", pady="1")			
		stat_by_lvl.grid(row=0, column=0, sticky="w", pady="1")	
		radio1.grid(row=0, column=1, sticky="w", pady="1")	
		radio2.grid(row=0, column=2, sticky="w", pady="1")	
		otherframe.grid(row=2, column=0, sticky="w")
		self.lvl_header_scrollframe.grid(row=3, column=0, sticky="w")
	
		return myframe
		
		
	def Create_Training_Rows(self, panel):
		i=0 		
		self.training_middle_scrollframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 820, hull_height = 233)		
		self.training_middle_scrollframe_inner = self.training_middle_scrollframe.interior()
		self.training_middle_scrollframe.configure(hscrollmode = "none", vscrollmode = "none")

		for stat in globals.statistics:	
			self.character.statistics[stat].StP_training_row = self.character.statistics[stat].Create_Training_Row_Frame(self.training_middle_scrollframe_inner)
			self.character.statistics[stat].StP_training_row.grid(row=i, column=0)
			i = i + 1						
		
		return self.training_middle_scrollframe
		

	def Create_Training_Footer(self, panel):
		self.resource_footer_scrollframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 820, hull_height = 205)	
		self.resource_footer_scrollframe.configure(vscrollmode = "none")			
		self.resource_footer_scrollframe_inner = self.resource_footer_scrollframe.interior()
		
		self.resource_footer_scrollframe.component("horizscrollbar").config(command=self.Linked_Scrolling)
		
		self.character.StP_Create_Resources_Frame(self.resource_footer_scrollframe_inner).grid(row=0, column=0, sticky="nw")		
						
		return self.resource_footer_scrollframe
			
	
	def Linked_Scrolling(self, *args):
		self.training_middle_scrollframe.xview(*args)
		self.resource_footer_scrollframe.xview(*args)
		self.lvl_header_scrollframe.xview(*args)
		
		
