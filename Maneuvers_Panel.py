# TODO LIST
#
# Combine Add and Edit Button functions
# Add error dialog box support
# Add the actual maneuver object to the Build_List_Maneuver and Schedule_List_Maneuver objects. This will remove a lot of redundency.
# Comment the hell out of this code



#!/usr/bin/python

import tkinter
import re
import Pmw
import math
import Globals as globals
  
class Maneuvers_Panel:  
	def __init__(self, parent, panel):		
		self.parent = parent
		self.current_schedule_maneuvers_list = []
		self.combat_schedule_maneuvers_list = []
		self.shield_schedule_maneuvers_list = []
		self.armor_schedule_maneuvers_list = []
		self.ManP_radio_var = tkinter.IntVar()	
		self.maneuver_mode = tkinter.StringVar()
		self.maneuver_mode.set("Combat")
		self.man_select_menu = ""
		
		# Dialog Box vars
		self.add_armor_menu = ""
		self.add_combat_menu = ""
		self.add_shield_menu = ""
		self.add_armor_order_menu = ""
		self.add_combat_order_menu = ""
		self.add_shield_order_menu = ""
		self.edit_armor_order_menu = ""
		self.edit_combat_order_menu = ""
		self.edit_shield_order_menu = ""
		self.armor_menu_size = 1			
		self.combat_menu_size = 1			
		self.shield_menu_size = 1		

		self.vars_dialog_combat_maneuver = tkinter.StringVar()
		self.vars_dialog_shield_maneuver = tkinter.StringVar()
		self.vars_dialog_armor_maneuver = tkinter.StringVar()
		self.vars_dialog_order = tkinter.StringVar()
		self.vars_dialog_info = tkinter.StringVar()
		self.vars_dialog_hide = tkinter.StringVar()
		self.vars_dialog_goal = tkinter.StringVar()
		self.vars_dialog_slevel = tkinter.StringVar()
		self.vars_dialog_tlevel = tkinter.StringVar()
		self.vars_dialog_errormsg = tkinter.StringVar()
		self.vars_dialog_edit_location = tkinter.IntVar()		
		
		# Schedule Level Calculation
		self.total_available_combat_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_available_shield_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_available_armor_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_cost_combat_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_cost_shield_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_cost_armor_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_leftover_combat_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_leftover_shield_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_leftover_armor_by_level = [tkinter.IntVar() for i in range(101)]
		
		# Schedule Footer vars
		self.sfooter_shield_row = ""
		self.sfooter_armor_row = ""
		self.vars_sfooter_combat_earned = tkinter.IntVar()
		self.vars_sfooter_shield_earned = tkinter.IntVar()
		self.vars_sfooter_armor_earned = tkinter.IntVar()
		self.vars_sfooter_combat_available = tkinter.IntVar()
		self.vars_sfooter_shield_available = tkinter.IntVar()
		self.vars_sfooter_armor_available = tkinter.IntVar()
		self.vars_sfooter_combat_total_cost = tkinter.IntVar()
		self.vars_sfooter_shield_total_cost = tkinter.IntVar()
		self.vars_sfooter_armor_total_cost = tkinter.IntVar()
		self.vars_sfooter_combat_leftover = tkinter.IntVar()
		self.vars_sfooter_shield_leftover = tkinter.IntVar()	
		self.vars_sfooter_armor_leftover = tkinter.IntVar()	
			
		self.add_box = self.Create_Dialog_Box(panel, "Add Maneuver", ("Add Maneuver,Cancel"))	
		
		self.level_counter = ""    									 #Becomes a Pmw.counter later on
			
		#These are the linked scrolling frames for the Panel
		self.lvl_header_scrollframe = ""		
		self.training_middle_scrollframe = ""
		self.resource_footer_scrollframe = ""		
		
		#Create all the sub-frames of the panel
		self.UL_Frame = self.Create_Build_Header(panel)
		self.ML_Frame = self.Create_Build_Frame(panel)
		self.UR_Frame = self.Create_Schedule_Header(panel)
		self.MR_Frame = self.Create_Schedule_Frame(panel)
		self.LR_Frame = self.Create_Schedule_Footer(panel)	
		
		#Make the frames visible
		self.UL_Frame.grid(row=0, column=0, sticky="nw")
		self.ML_Frame.grid(row=1, column=0, sticky="nw", rowspan=2)
		self.UR_Frame.grid(row=0, column=1, sticky="nw")
		self.MR_Frame.grid(row=1, column=1, sticky="nw")
		self.LR_Frame.grid(row=2, column=1, sticky="nw")		
		
		#initialize defaults
		self.add_box.withdraw()
		self.ManP_radio_var.set(1)
		self.level_counter.setvalue(0)
		self.Update_Schedule_Frames()
							

	def Create_Build_Header(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 600, hull_height = 50)
		myframe.component("borderframe").config(borderwidth=0)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")	
		myframe_inner = myframe.interior()

		topframe = tkinter.Frame(myframe_inner)		
		topframe.grid(row=0, column=0, sticky="w")	
		choices = ["Combat", "Shield", "Armor"]
		self.man_select_menu = tkinter.OptionMenu(topframe, self.maneuver_mode, *choices, command=self.Maneuver_Style_Onchange)
		self.man_select_menu.config(width=6, heigh=1)	
		self.man_select_menu.grid(row=0, column=0, sticky="w")		
		tkinter.Button(topframe, height="1", text="Add Maneuver", command=self.Add_Button_Onclick).grid(row=0, column=1)		
		tkinter.Button(topframe, height="1", text="Calculate", command=lambda : self.Create_Schedule(self.maneuver_mode.get())).grid(row=0, column=2)		
		tkinter.Button(topframe, height="1", text="Calculate All", command=lambda v="All": self.Create_Schedule(v)).grid(row=0, column=3)	
		tkinter.Button(topframe, text="Clear", command=lambda v="": self.Clear_Button_Onclick(v)).grid(row=0, column=4, sticky="w", pady="1")	
		tkinter.Button(topframe, text="Clear All", command=lambda v="All": self.Clear_Button_Onclick(v)).grid(row=0, column=5, sticky="w", pady="1")	
		
		title_scrollframe = Pmw.ScrolledFrame(myframe_inner, usehullsize = 1, hull_width = 583, hull_height = 26 )	
		title_scrollframe.configure(hscrollmode = "none")		
		title_scrollframe.grid(row=3, column=0, sticky="w")		
		title_scrollframe_inner = title_scrollframe.interior()						
		
		tkinter.Frame(title_scrollframe_inner).grid(row=3, column=0, columnspan=3)	
		tkinter.Label(title_scrollframe_inner, width="3", bg="lightgray", text="Hide").grid(row=0, column=0, padx="1")
		tkinter.Label(title_scrollframe_inner, width="6", bg="lightgray", text="Order").grid(row=0, column=1, padx="1")
		tkinter.Label(title_scrollframe_inner, width="26", bg="lightgray", text="Maneuver Name").grid(row=0, column=2, padx="1")
		tkinter.Label(title_scrollframe_inner, width="19", bg="lightgray", text="Cost by Rank").grid(row=0, column=3, padx="3")
		tkinter.Label(title_scrollframe_inner, width="5", bg="lightgray", text="Goal").grid(row=0, column=4, padx="1")
		tkinter.Label(title_scrollframe_inner, width="5", bg="lightgray", text="S.lvl").grid(row=0, column=5, padx="1")
		tkinter.Label(title_scrollframe_inner, width="5", bg="lightgray", text="T.lvl").grid(row=0, column=6, padx="1")
		tkinter.Label(title_scrollframe_inner, width="4", bg="lightgray", text="Edit").grid(row=0, column=7, padx="1")
		
		return myframe
		
		
	def Create_Build_Frame(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 600, hull_height = 469)			
		myframe.configure(hscrollmode = "none")					
		
		return myframe			
		
		
	def Create_Schedule_Header(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 470, hull_height = 50)
		myframe.component("borderframe").config(borderwidth=0)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")			
		myframe_inner = myframe.interior()		
						
		topframe = tkinter.Frame(myframe_inner)	
		topframe.grid(row=0, column=0, sticky="w")	
		tlvl_frame = tkinter.Frame(topframe)
		tlvl_frame.grid(row=0, column=0, sticky="w", padx=3, pady="1")	
		self.level_counter = Pmw.Counter(tlvl_frame, entryfield_entry_width = 3, entryfield_validate = { 'validator':'numeric', 'min':0, 'max':100 }, labelpos = 'w', label_text = 'Training at Level', entryfield_value = 0, datatype = "numeric", entryfield_modifiedcommand=self.Update_Schedule_Frames )
		self.level_counter.grid(row=0, column=0, sticky="w", pady="1")
		
		tkinter.Radiobutton(topframe, anchor="w", text="All", command=self.Update_Schedule_Frames, var=self.ManP_radio_var, value=1).grid(row=0, column=1)	
		tkinter.Radiobutton(topframe, anchor="w", text="All Trained", command=self.Update_Schedule_Frames, var=self.ManP_radio_var, value=2).grid(row=0, column=2)		
		tkinter.Radiobutton(topframe, anchor="w", text="Trained this Level", command=self.Update_Schedule_Frames, var=self.ManP_radio_var, value=3).grid(row=0, column=3)

		title_scrollframe = Pmw.ScrolledFrame(myframe_inner, usehullsize = 1, hull_width = 450, hull_height = 28 )		
		title_scrollframe.configure(hscrollmode = "none")		
		title_scrollframe.grid(row=3, column=0, sticky="w")	
		title_scrollframe_inner = title_scrollframe.interior()							
		
		tkinter.Frame(title_scrollframe_inner).grid(row=1, column=2, sticky="w", pady="1")	
		tkinter.Label(title_scrollframe_inner, width="26", bg="lightgray", text="Maneuver Name").grid(row=0, column=0, padx="1")
		tkinter.Label(title_scrollframe_inner, width="8", bg="lightgray", text="Ranks").grid(row=0, column=1, padx="1")
		tkinter.Label(title_scrollframe_inner, width="6", bg="lightgray", text="Cost").grid(row=0, column=2, padx="1")
		tkinter.Label(title_scrollframe_inner, width="10", bg="lightgray", text="Total Ranks").grid(row=0, column=3, padx="1")
		tkinter.Label(title_scrollframe_inner, width="8", bg="lightgray", text="Sum Cost").grid(row=0, column=4, padx="1")
	
		return myframe		
		
		
	def Create_Schedule_Frame(self, panel):
		self.training_middle_scrollframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 470, hull_height = 369)		
		self.training_middle_scrollframe_inner = self.training_middle_scrollframe.interior()
		self.training_middle_scrollframe.configure(hscrollmode = "none")		
	
		return self.training_middle_scrollframe		
	

	def Create_Schedule_Footer(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 470, hull_height = 100)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")			
		myframe_inner = myframe.interior()									
		
		title_frame = tkinter.Frame(myframe_inner)
		self.sfooter_combat_row = tkinter.Frame(myframe_inner)	
		self.sfooter_shield_row = tkinter.Frame(myframe_inner)	
		self.sfooter_armor_row = tkinter.Frame(myframe_inner)	
		
		title_frame.grid(row=0, column=0, padx="1")	
		self.sfooter_combat_row.grid(row=1, column=0, padx="1")		
		self.sfooter_shield_row.grid(row=2, column=0, padx="1")		
		self.sfooter_armor_row.grid(row=3, column=0, padx="1")	
		
		
		tkinter.Label(title_frame, width=8, text="").grid(row=0, column=0, sticky="w", padx="1", pady="1")	
		tkinter.Label(title_frame, width="10", bg="lightgray", text="Earned").grid(row=0, column=1, padx="1")
		tkinter.Label(title_frame, width="10", bg="lightgray", text="Available").grid(row=0, column=2, padx="1")
		tkinter.Label(title_frame, width="10", bg="lightgray", text="Total Cost").grid(row=0, column=3, padx="1")
		tkinter.Label(title_frame, width="10", bg="lightgray", text="Leftover").grid(row=0, column=4, padx="1")
	
		tkinter.Label(self.sfooter_combat_row, width="8", bg="lightgray", text="Combat").grid(row=1, column=0, padx="2", pady="1")
		tkinter.Label(self.sfooter_combat_row, width="10", bg="lightgray", textvar=self.vars_sfooter_combat_earned).grid(row=1, column=1, padx="1")
		tkinter.Label(self.sfooter_combat_row, width="10", bg="lightgray", textvar=self.vars_sfooter_combat_available).grid(row=1, column=2, padx="1")	
		tkinter.Label(self.sfooter_combat_row, width="10", bg="lightgray", textvar=self.vars_sfooter_combat_total_cost).grid(row=1, column=3, padx="1")
		tkinter.Label(self.sfooter_combat_row, width="10", bg="lightgray", textvar=self.vars_sfooter_combat_leftover).grid(row=1, column=4, padx="1")
		
		tkinter.Label(self.sfooter_shield_row, width="8", bg="lightgray", text="Shield").grid(row=2, column=0, padx="2", pady="1")	
		tkinter.Label(self.sfooter_shield_row, width="10", bg="lightgray", textvar=self.vars_sfooter_shield_earned).grid(row=2, column=1, padx="1")	
		tkinter.Label(self.sfooter_shield_row, width="10", bg="lightgray", textvar=self.vars_sfooter_shield_available).grid(row=2, column=2, padx="1")
		tkinter.Label(self.sfooter_shield_row, width="10", bg="lightgray", textvar=self.vars_sfooter_shield_total_cost).grid(row=2, column=3, padx="1")		
		tkinter.Label(self.sfooter_shield_row, width="10", bg="lightgray", textvar=self.vars_sfooter_shield_leftover).grid(row=2, column=4, padx="1")	
		
		tkinter.Label(self.sfooter_armor_row, width="8", bg="lightgray", text="Armor").grid(row=3, column=0, padx="2", pady="1")			
		tkinter.Label(self.sfooter_armor_row, width="10", bg="lightgray", textvar=self.vars_sfooter_armor_earned).grid(row=3, column=1, padx="1")	
		tkinter.Label(self.sfooter_armor_row, width="10", bg="lightgray", textvar=self.vars_sfooter_armor_available).grid(row=3, column=2, padx="1")
		tkinter.Label(self.sfooter_armor_row, width="10", bg="lightgray", textvar=self.vars_sfooter_armor_total_cost).grid(row=3, column=3, padx="1")
		tkinter.Label(self.sfooter_armor_row, width="10", bg="lightgray", textvar=self.vars_sfooter_armor_leftover).grid(row=3, column=4, padx="1")	
					
		return myframe	
		
		
	def Create_Dialog_Box(self, panel, title, buttons):
		dialog = Pmw.Dialog(panel,
            buttons = (buttons.split(",")),
            title = title,
            command = self.Dialog_Box_Onclick)
			
		dialog.transient(panel)	
		dialog.resizable(width=0, height=0)		
		dialog.geometry('315x280+600+300')
				
		myframe = Pmw.ScrolledFrame(dialog.interior(), usehullsize = 1, hull_width = 315, hull_height = 280)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")		
		myframe.grid(row=0, column=0, sticky="nw")	
		myframe_inner = myframe.interior()	
				
		tkinter.Label(myframe_inner, width="13", anchor="w", bg="lightgray", text="Maneuver Name").grid(row=0, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="13", anchor="w", bg="lightgray", text="Cost Per Rank").grid(row=1, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="30", anchor="w", textvar=self.vars_dialog_info).grid(row=1, column=1, sticky="w")
		tkinter.Label(myframe_inner, width="13", anchor="w", text="").grid(row=2, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="13", anchor="w", bg="lightgray", text="Training Order").grid(row=3, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="13", anchor="w", bg="lightgray", text="Hide").grid(row=4, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="13", anchor="w", text="").grid(row=5, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="13", anchor="w", bg="lightgray", text="Goal").grid(row=6, column=0, sticky="w", pady=1)
		tkinter.Label(myframe_inner, width="13", anchor="w", bg="lightgray", text="Level Range").grid(row=7, column=0, sticky="w")			
								
		tkinter.Checkbutton(myframe_inner, command="", variable=self.vars_dialog_hide).grid(row=4, column=1, sticky="w")		
	

		self.add_combat_order_menu = tkinter.OptionMenu(myframe_inner, self.vars_dialog_order, "1", command="")
		self.add_combat_order_menu.config(width=1, heigh=1)	
		self.add_combat_menu = tkinter.OptionMenu(myframe_inner, self.vars_dialog_combat_maneuver, "", command="")
		self.add_combat_menu.config(width=27, heigh=1)	
		self.edit_combat_order_menu = tkinter.OptionMenu(myframe_inner, self.vars_dialog_order, "1", command="")
		self.edit_combat_order_menu.config(width=1, heigh=1)	
		
		self.add_shield_order_menu = tkinter.OptionMenu(myframe_inner, self.vars_dialog_order, "1", command="")
		self.add_shield_order_menu.config(width=1, heigh=1)	
		self.add_shield_menu = tkinter.OptionMenu(myframe_inner, self.vars_dialog_shield_maneuver, "", command="")
		self.add_shield_menu.config(width=27, heigh=1)	
		self.edit_shield_order_menu = tkinter.OptionMenu(myframe_inner, self.vars_dialog_order, "1", command="")
		self.edit_shield_order_menu.config(width=1, heigh=1)	
		
		self.add_armor_order_menu = tkinter.OptionMenu(myframe_inner, self.vars_dialog_order, "1", command="")
		self.add_armor_order_menu.config(width=1, heigh=1)	
		self.add_armor_menu = tkinter.OptionMenu(myframe_inner, self.vars_dialog_armor_maneuver, "", command="")
		self.add_armor_menu.config(width=27, heigh=1)	
		self.edit_armor_order_menu = tkinter.OptionMenu(myframe_inner, self.vars_dialog_order, "1", command="")
		self.edit_armor_order_menu.config(width=1, heigh=1)	
			
			
		self.add_combat_order_menu.grid(row=3, column=1, sticky="w")
		self.add_combat_menu.grid(row=0, column=1, sticky="w", columnspan=4)	

				
		lvlframe = tkinter.Frame(myframe_inner)
		lvlframe.grid(row=7, column=1, sticky="w", columnspan=4)	
		Pmw.Counter(lvlframe, entryfield_entry_width = 3, entryfield_validate = { 'validator':'numeric', 'min':0, 'max':100 }, labelpos = 'w', label_text = 'Start', entryfield_value = 0, datatype = "numeric", entryfield_entry_textvariable=self.vars_dialog_slevel).grid(row=0, column=0, sticky="w")
		Pmw.Counter(lvlframe, entryfield_entry_width = 3, entryfield_validate = { 'validator':'numeric', 'min':0, 'max':100 }, labelpos = 'w', label_text = 'Target', entryfield_value = 0, datatype = "numeric", entryfield_entry_textvariable=self.vars_dialog_tlevel).grid(row=0, column=1, sticky="w", columnspan=2)
		goal_box = tkinter.Entry(myframe_inner, width="6", justify="center", validate="key", validatecommand="", textvariable=self.vars_dialog_goal).grid(row=6, column=1, sticky="w", padx=2)
		tkinter.Label(myframe_inner, anchor="w", font="-weight bold", wraplength=300, justify="left", textvariable=self.vars_dialog_errormsg).grid(row=8, column=0, sticky="w", columnspan=4)
				
			
		return dialog
				
		
	def Dialog_Box_Onclick(self, result):
		i = 0
		slevel = int(self.vars_dialog_slevel.get())
		tlevel = int(self.vars_dialog_tlevel.get())
		goal = self.vars_dialog_goal.get()

		if result is None or result == "Cancel":
			self.add_box.withdraw()
			return

		if self.maneuver_mode.get() == "Combat":
			man = globals.character.combat_maneuvers[self.vars_dialog_combat_maneuver.get()]
		elif self.maneuver_mode.get() == "Shield":
			man = globals.character.shield_maneuvers[self.vars_dialog_shield_maneuver.get()]
		elif self.maneuver_mode.get() == "Armor":
			man = globals.character.armor_maneuvers[self.vars_dialog_armor_maneuver.get()]

	
		# Error checking for Add/Update choices
		if re.search(r"(^Add)|(^Update)", result):
			if slevel > tlevel:
				self.vars_dialog_errormsg.set("ERROR: Start level cannot be greater than target level." )
				return
			elif len(goal) == 0 or goal == "0" or not re.search(r"(^\d{1,3}$)", goal):
				self.vars_dialog_errormsg.set("ERROR: Goal must be number greater than 0.")
				return				
			elif int(goal) > man.max_ranks:
				self.vars_dialog_errormsg.set("ERROR: Goal is greater than maximum maneuver ranks.")
				return				
			elif man.Get_Total_Cost_At_Rank(int(goal), globals.character.profession.type) > tlevel+1:
				self.vars_dialog_errormsg.set("ERROR: Total cost cannot be greater than target level + 1.")
				return					

				
		if result == "Add Maneuver":	
			hide = "" 
			if self.vars_dialog_hide.get() == "1":
				hide = "x"				
				
			if self.maneuver_mode.get() == "Combat":
				man = globals.character.combat_maneuvers[self.vars_dialog_combat_maneuver.get()]
				self.combat_menu_size = self.combat_menu_size + 1			
				
				globals.character.build_combat_maneuvers_list.insert(int(self.vars_dialog_order.get())-1, Build_List_Maneuver(self.ML_Frame.interior(), self.vars_dialog_combat_maneuver.get(), "Combat", hide, self.vars_dialog_order.get(), 
				"TESTING", man.cost_by_rank[0], man.cost_by_rank[1], man.cost_by_rank[2], man.cost_by_rank[3], man.cost_by_rank[4], self.vars_dialog_slevel.get(), self.vars_dialog_tlevel.get(), self.vars_dialog_goal.get()))						
				globals.character.build_combat_maneuvers_list[int(self.vars_dialog_order.get())-1].ManP_Edit_Button.config(command=lambda v=int(self.vars_dialog_order.get())-1: self.Edit_Button_Onclick(v))
			
				self.add_combat_order_menu["menu"].insert_command("end", label=self.combat_menu_size, command=lambda v=self.combat_menu_size: self.vars_dialog_order.set(v))	
				if self.combat_menu_size-1 > 1:
					self.edit_combat_order_menu["menu"].insert_command("end", label=self.combat_menu_size-1, command=lambda v=self.combat_menu_size-1: self.vars_dialog_order.set(v))				
			
				for man in globals.character.build_combat_maneuvers_list:
					man.order.set(i+1)
					man.ManP_Edit_Button.config(command=lambda v=i: self.Edit_Button_Onclick(v))
					man.ManP_Info_Row.grid(row=i, column=0)			
					i += 1	
				
			elif self.maneuver_mode.get() == "Shield":
				man = globals.character.shield_maneuvers[self.vars_dialog_shield_maneuver.get()]
				self.shield_menu_size = self.shield_menu_size + 1				
				
				globals.character.build_shield_maneuvers_list.insert(int(self.vars_dialog_order.get())-1, Build_List_Maneuver(self.ML_Frame.interior(), self.vars_dialog_shield_maneuver.get(), "Shield", hide, self.vars_dialog_order.get(), 
				"TESTING", man.cost_by_rank[0], man.cost_by_rank[1], man.cost_by_rank[2], man.cost_by_rank[3], man.cost_by_rank[4], self.vars_dialog_slevel.get(), self.vars_dialog_tlevel.get(), self.vars_dialog_goal.get()))						
				globals.character.build_shield_maneuvers_list[int(self.vars_dialog_order.get())-1].ManP_Edit_Button.config(command=lambda v=int(self.vars_dialog_order.get())-1: self.Edit_Button_Onclick(v))
			
				self.add_combat_order_menu["menu"].insert_command("end", label=self.combat_menu_size, command=lambda v=self.combat_menu_size: self.vars_dialog_order.set(v))	
				if self.combat_menu_size-1 > 1:
					self.edit_shield_order_menu["menu"].insert_command("end", label=self.shield_menu_size-1, command=lambda v=self.shield_menu_size-1: self.vars_dialog_order.set(v))				
			
				for man in globals.character.build_shield_maneuvers_list:
					man.order.set(i+1)
					man.ManP_Edit_Button.config(command=lambda v=i: self.Edit_Button_Onclick(v))
					man.ManP_Info_Row.grid(row=i, column=0)			
					i += 1	
					
			elif self.maneuver_mode.get() == "Armor":
				man = globals.character.armor_maneuvers[self.vars_dialog_armor_maneuver.get()]
				self.armor_menu_size = self.armor_menu_size + 1			
				
				globals.character.build_armor_maneuvers_list.insert(int(self.vars_dialog_order.get())-1, Build_List_Maneuver(self.ML_Frame.interior(), self.vars_dialog_armor_maneuver.get(), "Armor", hide, self.vars_dialog_order.get(), 
				"TESTING", man.cost_by_rank[0], man.cost_by_rank[1], man.cost_by_rank[2], man.cost_by_rank[3], man.cost_by_rank[4], self.vars_dialog_slevel.get(), self.vars_dialog_tlevel.get(), self.vars_dialog_goal.get()))						
				globals.character.build_armor_maneuvers_list[int(self.vars_dialog_order.get())-1].ManP_Edit_Button.config(command=lambda v=int(self.vars_dialog_order.get())-1: self.Edit_Button_Onclick(v))
			
				self.add_armor_order_menu["menu"].insert_command("end", label=self.armor_menu_size, command=lambda v=self.armor_menu_size: self.vars_dialog_order.set(v))	
				if self.armor_menu_size-1 > 1:
					self.edit_armor_order_menu["menu"].insert_command("end", label=self.armor_menu_size-1, command=lambda v=self.armor_menu_size-1: self.vars_dialog_order.set(v))				
			
				for man in globals.character.build_armor_maneuvers_list:
					man.order.set(i+1)
					man.ManP_Edit_Button.config(command=lambda v=i: self.Edit_Button_Onclick(v))
					man.ManP_Info_Row.grid(row=i, column=0)			
					i += 1							


			self.add_box.withdraw()		
		
		elif result == "Update Maneuver":
			if self.maneuver_mode.get() == "Combat":
				man = globals.character.build_combat_maneuvers_list.pop(self.vars_dialog_edit_location.get())
				list = globals.character.build_combat_maneuvers_list
				man.name.set(self.vars_dialog_combat_maneuver.get())
				m_ranks = globals.combat_maneuvers_list[self.vars_dialog_combat_maneuver.get()]
			elif self.maneuver_mode.get() == "Shield":
				man = globals.character.build_shield_maneuvers_list.pop(self.vars_dialog_edit_location.get())
				list = globals.character.build_shield_maneuvers_list
				man.name.set(self.vars_dialog_shield_maneuver.get())
				m_ranks = globals.shield_maneuvers_list[self.vars_dialog_shield_maneuver.get()]
			elif self.maneuver_mode.get() == "Armor":
				man = globals.character.build_armor_maneuvers_list.pop(self.vars_dialog_edit_location.get())
				list = globals.character.build_armor_maneuvers_list
				man.name.set(self.vars_dialog_armor_maneuver.get())		
				m_ranks = globals.armor_maneuvers_list[self.vars_dialog_armor_maneuver.get()]


			man.ranks[0].set(m_ranks.cost_by_rank[0])	
			man.ranks[1].set(m_ranks.cost_by_rank[1])	
			man.ranks[2].set(m_ranks.cost_by_rank[2])	
			man.ranks[3].set(m_ranks.cost_by_rank[3])	
			man.ranks[4].set(m_ranks.cost_by_rank[4])	
#			man.info.set(self.vars_dialog_info.get()) 
			man.order.set(self.vars_dialog_order.get())
			man.slvl.set(self.vars_dialog_slevel.get())
			man.tlvl.set(self.vars_dialog_tlevel.get())
			man.goal.set(self.vars_dialog_goal.get())			
			
			if self.vars_dialog_hide.get() == "1":
				man.hide.set("x")
			else:
				man.hide.set("")			
			
			list.insert(int(self.vars_dialog_order.get())-1, man)
			for man in list:	
				man.order.set(i+1)
				man.ManP_Edit_Button.config(command=lambda v=i: self.Edit_Button_Onclick(v))
				man.ManP_Info_Row.grid(row=i, column=0)			
				i += 1						
			self.add_box.withdraw()				
		
		elif result == "Remove Maneuver":
			if self.maneuver_mode.get() == "Combat":
				list = globals.character.build_combat_maneuvers_list
				self.add_combat_order_menu['menu'].delete("end", "end")
				self.edit_combat_order_menu['menu'].delete("end", "end")
				self.combat_menu_size -= 1
			elif self.maneuver_mode.get() == "Shield":
				list = globals.character.build_shield_maneuvers_list
				self.add_shield_order_menu['menu'].delete("end", "end")
				self.edit_shield_order_menu['menu'].delete("end", "end")
				self.shield_menu_size -= 1
			elif self.maneuver_mode.get() == "Armor":
				list = globals.character.build_armor_maneuvers_list
				self.add_armor_order_menu['menu'].delete("end", "end")
				self.edit_armor_order_menu['menu'].delete("end", "end")
				self.armor_menu_size -= 1				
				
			list.pop(self.vars_dialog_edit_location.get()).ManP_Info_Row.grid_remove()
			for man in list:
				man.order.set(i+1)
				man.ManP_Edit_Button.config(command=lambda v=i: self.Edit_Button_Onclick(v))
				man.ManP_Info_Row.grid(row=i, column=0)			
				i += 1	
			self.add_box.withdraw()		
		
		
	def Add_Button_Onclick(self):
		prof_type = globals.character.profession.type

		self.vars_dialog_hide.set("0")
		self.vars_dialog_goal.set("")
		self.vars_dialog_slevel.set("0")
		self.vars_dialog_tlevel.set("100")	
		self.vars_dialog_errormsg.set("")

		self.add_combat_menu.grid_remove()
		self.add_shield_menu.grid_remove()
		self.add_armor_menu.grid_remove()
		self.add_combat_order_menu.grid_remove()
		self.add_shield_order_menu.grid_remove()
		self.add_armor_order_menu.grid_remove()
		self.edit_combat_order_menu.grid_remove()
		self.edit_shield_order_menu.grid_remove()
		self.edit_armor_order_menu.grid_remove()
		
		if self.add_box.component("buttonbox").button(0)["text"] == "Update Maneuver":
			self.add_box.component("buttonbox").delete("Update Maneuver")
			self.add_box.component("buttonbox").delete("Remove Maneuver")		
			self.add_box.component("buttonbox").insert("Add Maneuver", command=lambda v="Add Maneuver": self.Dialog_Box_Onclick(v))	
				
		if self.maneuver_mode.get() == "Combat":
			man = globals.combat_maneuvers_list[globals.combat_maneuvers[0]]
			self.vars_dialog_combat_maneuver.set(globals.combat_maneuvers[0])
			self.vars_dialog_order.set(self.combat_menu_size)
			self.add_combat_order_menu.grid(row=3, column=1, sticky="w")	
			self.add_combat_menu.grid(row=0, column=1, sticky="w", columnspan=4)				
		elif self.maneuver_mode.get() == "Shield":
			man = globals.shield_maneuvers_list[globals.shield_maneuvers[0]]
			self.vars_dialog_shield_maneuver.set(globals.shield_maneuvers[0])
			self.vars_dialog_order.set(self.shield_menu_size)
			self.add_shield_order_menu.grid(row=3, column=1, sticky="w")				
			self.add_shield_menu.grid(row=0, column=1, sticky="w", columnspan=4)					
		elif self.maneuver_mode.get() == "Armor":
			man = globals.armor_maneuvers_list[globals.armor_maneuvers[0]]
			self.vars_dialog_armor_maneuver.set(globals.armor_maneuvers[0])
			self.vars_dialog_order.set(self.armor_menu_size)
			self.add_armor_order_menu.grid(row=3, column=1, sticky="w")				
			self.add_armor_menu.grid(row=0, column=1, sticky="w", columnspan=4)	
			
		self.vars_dialog_info.set("%s,    %s,    %s,    %s,    %s" % (man.Get_Cost_At_Rank(0, prof_type), man.Get_Cost_At_Rank(1, prof_type), man.Get_Cost_At_Rank(2, prof_type), man.Get_Cost_At_Rank(3, prof_type), man.Get_Cost_At_Rank(4, prof_type)))		
		self.add_box.show()
		
		
	def Edit_Button_Onclick(self, location):
		prof_type = globals.character.profession.type
		
		self.add_combat_menu.grid_remove()
		self.add_shield_menu.grid_remove()
		self.add_armor_menu.grid_remove()
		self.add_combat_order_menu.grid_remove()
		self.add_shield_order_menu.grid_remove()
		self.add_armor_order_menu.grid_remove()
		self.edit_combat_order_menu.grid_remove()
		self.edit_shield_order_menu.grid_remove()
		self.edit_armor_order_menu.grid_remove()
		
		if self.maneuver_mode.get() == "Combat":
			build_man = globals.character.build_combat_maneuvers_list[int(location)]
			self.vars_dialog_combat_maneuver.set(build_man.name.get())
			self.vars_dialog_order.set(self.combat_menu_size)
			self.edit_combat_order_menu.grid(row=3, column=1, sticky="w")	
			self.add_combat_menu.grid(row=0, column=1, sticky="w", columnspan=4)				
		elif self.maneuver_mode.get() == "Shield":
			build_man = globals.character.build_shield_maneuvers_list[int(location)]
			self.vars_dialog_shield_maneuver.set(build_man.name.get())
			self.vars_dialog_order.set(self.shield_menu_size)
			self.edit_shield_order_menu.grid(row=3, column=1, sticky="w")				
			self.add_shield_menu.grid(row=0, column=1, sticky="w", columnspan=4)					
		elif self.maneuver_mode.get() == "Armor":
			build_man = globals.character.build_armor_maneuvers_list[int(location)]
			self.vars_dialog_armor_maneuver.set(build_man.name.get())
			self.vars_dialog_order.set(self.armor_menu_size)
			self.edit_armor_order_menu.grid(row=3, column=1, sticky="w")				
			self.add_armor_menu.grid(row=0, column=1, sticky="w", columnspan=4)	

		self.vars_dialog_info.set("%s,    %s,    %s,    %s,    %s" % (build_man.Get_Cost_At_Rank(0, prof_type), build_man.Get_Cost_At_Rank(1, prof_type), build_man.Get_Cost_At_Rank(2, prof_type), build_man.Get_Cost_At_Rank(3, prof_type), build_man.Get_Cost_At_Rank(4, prof_type)))		
		self.vars_dialog_order.set(build_man.order.get())
		self.vars_dialog_slevel.set(build_man.slvl.get())
		self.vars_dialog_tlevel.set(build_man.tlvl.get())
		self.vars_dialog_goal.set(build_man.goal.get())		
		self.vars_dialog_errormsg.set("")
		self.vars_dialog_edit_location.set(int(location))

		
		if self.add_box.component("buttonbox").button(0)["text"] == "Add Maneuver":
			self.add_box.component("buttonbox").delete("Add Maneuver")
			self.add_box.component("buttonbox").insert("Remove Maneuver", command=lambda v="Remove Maneuver": self.Dialog_Box_Onclick(v))	
			self.add_box.component("buttonbox").insert("Update Maneuver", command=lambda v="Update Maneuver": self.Dialog_Box_Onclick(v))	
		
		self.add_box.show()
		
		
	def Clear_Button_Onclick(self, style):
		for row in self.current_schedule_maneuvers_list:
			row.Set_To_Default()
		
		if self.maneuver_mode.get() == "Combat" or style == "All":
			for row in self.combat_schedule_maneuvers_list:
				row.Set_To_Default()
			for man in globals.character.build_combat_maneuvers_list:	
				man.ManP_Info_Row.grid_remove()
			globals.character.build_combat_maneuvers_list = []	
			if self.combat_menu_size > 1:			
				self.add_combat_order_menu['menu'].delete(1, "end")
				self.edit_combat_order_menu['menu'].delete(0, "end")
				self.combat_menu_size = 1		
			self.total_available_combat_by_level = [tkinter.IntVar() for i in range(101)]
			self.total_cost_combat_by_level = [tkinter.IntVar() for i in range(101)]
			self.total_leftover_combat_by_level = [tkinter.IntVar() for i in range(101)]
		if self.maneuver_mode.get() == "Shield" or style == "All":		
			for row in self.shield_schedule_maneuvers_list:
				row.Set_To_Default()		
			for man in globals.character.build_shield_maneuvers_list:	
				man.ManP_Info_Row.grid_remove()
			globals.character.build_shield_maneuvers_list = []	
			if self.shield_menu_size > 1:	
				self.add_shield_order_menu['menu'].delete(1, "end")
				self.edit_shield_order_menu['menu'].delete(0, "end")
				self.shield_menu_size = 1		
			self.total_available_shield_by_level = [tkinter.IntVar() for i in range(101)]
			self.total_cost_shield_by_level = [tkinter.IntVar() for i in range(101)]
			self.total_leftover_shield_by_level = [tkinter.IntVar() for i in range(101)]
		if self.maneuver_mode.get() == "Armor" or style == "All":		
			for row in self.armor_schedule_maneuvers_list:
				row.Set_To_Default()				
			for man in globals.character.build_armor_maneuvers_list:	
				man.ManP_Info_Row.grid_remove()		
			globals.character.build_armor_maneuvers_list = []
			if self.armor_menu_size > 1:				
				self.add_armor_order_menu['menu'].delete(1, "end")
				self.edit_armor_order_menu['menu'].delete(0, "end")
				self.armor_menu_size = 1	
			self.total_available_armor_by_level = [tkinter.IntVar() for i in range(101)]
			self.total_cost_armor_by_level = [tkinter.IntVar() for i in range(101)]
			self.total_leftover_armor_by_level = [tkinter.IntVar() for i in range(101)]

		self.ManP_radio_var.set(1)
		self.level_counter.setvalue(0)
		

	def Maneuver_Style_Onchange(self, result):
		i=0
		if self.maneuver_mode.get() == result:
			return			

		for row in self.current_schedule_maneuvers_list:
			row.ManP_schedule_row.grid_remove()
		self.current_schedule_maneuvers_list = []
			
		if self.maneuver_mode.get() == "Combat":
			self.maneuver_mode.set("Combat")
			for man in globals.character.build_combat_maneuvers_list:
				man.ManP_Info_Row.grid_remove()
		elif self.maneuver_mode.get() == "Shield":
			self.maneuver_mode.set("Shield")
			for man in globals.character.build_shield_maneuvers_list:	
				man.ManP_Info_Row.grid_remove()
		elif self.maneuver_mode.get() == "Armor":
			self.maneuver_mode.set("Armor") 
			for man in globals.character.build_armor_maneuvers_list:	
				man.ManP_Info_Row.grid_remove()
		
		if result == "Combat":
			self.maneuver_mode.set("Combat")	
			self.current_schedule_maneuvers_list = self.combat_schedule_maneuvers_list
			
			for man in globals.character.build_combat_maneuvers_list:	
				man.order.set(i+1)
				man.ManP_Edit_Button.config(command=lambda v=i: self.Edit_Button_Onclick(v))
				man.ManP_Info_Row.grid(row=i, column=0)			
				i += 1	
		elif result == "Shield":
			self.maneuver_mode.set("Shield")
			self.current_schedule_maneuvers_list = self.shield_schedule_maneuvers_list
			
			for man in globals.character.build_shield_maneuvers_list:	
				man.order.set(i+1)
				man.ManP_Edit_Button.config(command=lambda v=i: self.Edit_Button_Onclick(v))
				man.ManP_Info_Row.grid(row=i, column=0)		
				i += 1	
		elif result == "Armor":
			self.maneuver_mode.set("Armor") 
			self.current_schedule_maneuvers_list = self.armor_schedule_maneuvers_list
			
			for man in globals.character.build_armor_maneuvers_list:	
				man.order.set(i+1)
				man.ManP_Edit_Button.config(command=lambda v=i: self.Edit_Button_Onclick(v))
				man.ManP_Info_Row.grid(row=i, column=0)	
				i += 1	

		i = 0
		level = int(self.level_counter.getvalue())
		for row in self.current_schedule_maneuvers_list:	
			if self.ManP_radio_var.get() == 1 or (self.ManP_radio_var.get() == 2 and row.total_ranks_by_level[100].get() > 0) or (self.ManP_radio_var.get() == 3 and row.ranks_by_level[level].get() > 0):		
				if row.cost_at_level[level].get() != 0:
					row.cost.set(row.cost_at_level[level].get())
				else:
					row.cost.set("")
				row.ManP_schedule_row.grid(row=i, column=0)
			else:
				row.ManP_schedule_row.grid_remove()
			row.ranks.set(row.ranks_by_level[level].get())
			row.total_ranks.set(row.total_ranks_by_level[level].get())
			row.combined_cost.set(row.combined_cost_by_level[level].get())
			i += 1				
				

	def Create_Schedule(self, style):
		slevel = 0; tlevel = 0; ranks_taken = 0; ranks_needed = 0
		next_rank_cost = 0; available = 0; cost_at_level = 0; prev_leftover = 0
		tranks = 0; tcost = 0; new_min = 0		
		schedule_names = []
		
		total_available_array = [tkinter.IntVar() for i in range(101)]
		total_cost_array = [tkinter.IntVar() for i in range(101)]
		total_leftover_array = [tkinter.IntVar() for i in range(101)]
		
		if style == "All":
			schedule_names = ["Combat", "Shield", "Armor"]
		else:
			schedule_names = [style]			
			
		
		# Clear schedule before using it.
		for row in self.current_schedule_maneuvers_list:
			row.Set_To_Default()
			row.ManP_schedule_row.grid_remove()

		
		for type in schedule_names:
			prev_leftover = 0
			tranks = 0
			for i in range(0, 101):
				total_available_array[i].set(0)
				total_cost_array[i].set(0)
				total_leftover_array[i].set(0) 
							
			if type == "Combat":
				skill_name = "Combat Maneuvers"
				blist = globals.character.build_combat_maneuvers_list
				slist = self.combat_schedule_maneuvers_list
			elif type == "Shield":
				skill_name = "Shield Use"
				blist = globals.character.build_shield_maneuvers_list
				slist = self.shield_schedule_maneuvers_list
			elif type == "Armor":
				skill_name = "Armor Use"
				blist = globals.character.build_armor_maneuvers_list
				slist = self.armor_schedule_maneuvers_list
				
			if len(blist) == 0:
				continue
		
			for row in slist:
				row.Set_To_Default()
				
			for i in range(0, 101):
				if i > 0:
					prev_leftover = total_leftover_array[i-1].get()
				
				if skill_name in globals.character.scheduled_skills_list:
					tranks = globals.character.scheduled_skills_list[skill_name].ranks_by_level[i].get()
									
				total_available_array[i].set( prev_leftover + tranks )
				total_leftover_array[i].set( prev_leftover + tranks )					
						
			for man in blist:
				if man.hide.get() == "x":
					continue						
				
				slevel = int(man.slvl.get())
				tlevel = int(man.tlvl.get())
				ranks_needed = int(man.goal.get())
				ranks_taken = 0				
				prev_leftover = 0				
				if slevel < new_min:
					slevel = new_min					
				
				for row in slist:               #figure out a better way to do this later on					
					available = 0					
					if row.name == man.name.get():
						for lvl in range(slevel, tlevel+1):			
							# Does character have prerequisites for maneuver at this level??? logic will go here	
							available = total_leftover_array[lvl].get()							
								
							cost_at_level = 0	
							prev_leftover = 0
							next_rank_cost = row.Calcuate_Cost_At_Rank(man.ranks, row.total_ranks_by_level[lvl].get() + 1)    
							tcost = row.Calcuate_Total_Cost(man.ranks, row.total_ranks_by_level[lvl].get() + 1)
								
							while available >= next_rank_cost and lvl+1 >= tcost:
								cost_at_level += next_rank_cost
								available -= next_rank_cost
								ranks_taken += 1
								row.Calculate_Ranks_Info(lvl, 1)	
								if ranks_needed <= ranks_taken:
									break
								next_rank_cost = row.Calcuate_Cost_At_Rank(man.ranks, row.total_ranks_by_level[lvl].get()+1)
								tcost = row.Calcuate_Total_Cost(man.ranks, row.total_ranks_by_level[lvl].get() + 1)	

							if cost_at_level > 0:
								total_cost_array[lvl].set( cost_at_level + total_cost_array[lvl].get() )
								new_min = lvl
								
								for i in range(lvl, 101):
									prev_leftover = total_leftover_array[i-1].get()
							
									if skill_name in globals.character.scheduled_skills_list:	
										ranks = globals.character.scheduled_skills_list[skill_name].ranks_by_level[i].get()	
												
									total_available_array[i].set( prev_leftover + ranks )
									total_leftover_array[i].set( prev_leftover + ranks - total_cost_array[i].get() )	
									
							if ranks_needed < ranks_taken and lvl >= tlevel:
								# Error thing here
								break				
							elif ranks_needed <= ranks_taken:
								break	


			if type == "Combat":
				for i in range(101):
					self.total_available_combat_by_level[i].set(total_available_array[i].get())
					self.total_cost_combat_by_level[i].set(total_cost_array[i].get())
					self.total_leftover_combat_by_level[i].set(total_leftover_array[i].get())
			elif type == "Shield":
				for i in range(101):
					self.total_available_shield_by_level[i].set(total_available_array[i].get())
					self.total_cost_shield_by_level[i].set(total_cost_array[i].get())
					self.total_leftover_shield_by_level[i].set(total_leftover_array[i].get())
			elif type == "Armor":
				for i in range(101):
					self.total_available_armor_by_level[i].set(total_available_array[i].get())
					self.total_cost_armor_by_level[i].set(total_cost_array[i].get())
					self.total_leftover_armor_by_level[i].set(total_leftover_array[i].get())
			
			
		if globals.error_event:
			globals.error_dialogmsg.set("Skill Panel: Build becomes untrainable at lvl: %s" % i)	
			globals.error_dialog.show()	
			self.level_counter.setvalue(i)
	
		self.Update_Schedule_Frames()	

			
	def Update_Schedule_Frames(self):
		level = int(self.level_counter.getvalue())
		i = 0; combat_ranks = 0; shield_ranks = 0; armor_ranks = 0
		
		if "Combat Maneuvers" in globals.character.scheduled_skills_list:
			combat_ranks = globals.character.scheduled_skills_list["Combat Maneuvers"].ranks_by_level[level].get()
		if "Shield Use" in globals.character.scheduled_skills_list:
			shield_ranks = globals.character.scheduled_skills_list["Shield Use"].ranks_by_level[level].get()
		if "Armor Use" in globals.character.scheduled_skills_list:
			armor_ranks = globals.character.scheduled_skills_list["Armor Use"].ranks_by_level[level].get()

		for row in self.current_schedule_maneuvers_list:
			if self.ManP_radio_var.get() == 1 or (self.ManP_radio_var.get() == 2 and row.total_ranks_by_level[100].get() > 0) or (self.ManP_radio_var.get() == 3 and row.ranks_by_level[level].get() > 0):
				if row.ranks_by_level[level].get() > 0:
					row.cost.set(row.cost_at_level[level].get())
				else:
					row.cost.set("")				
				row.ranks.set(row.ranks_by_level[level].get())
				row.total_ranks.set(row.total_ranks_by_level[level].get())
				row.combined_cost.set(row.combined_cost_by_level[level].get())
				row.ManP_schedule_row.grid(row=i, column=0)
			else:
				row.ManP_schedule_row.grid_remove()
			i += 1
			
		self.vars_sfooter_combat_earned.set(combat_ranks)
		self.vars_sfooter_shield_earned.set(shield_ranks)		
		self.vars_sfooter_armor_earned.set(armor_ranks)		
		self.vars_sfooter_combat_available.set(self.total_available_combat_by_level[level].get())
		self.vars_sfooter_shield_available.set(self.total_available_shield_by_level[level].get())	
		self.vars_sfooter_armor_available.set(self.total_available_armor_by_level[level].get())	
		self.vars_sfooter_combat_total_cost.set(self.total_cost_combat_by_level[level].get())
		self.vars_sfooter_shield_total_cost.set(self.total_cost_shield_by_level[level].get())
		self.vars_sfooter_armor_total_cost.set(self.total_cost_armor_by_level[level].get())
		self.vars_sfooter_combat_leftover.set(self.total_leftover_combat_by_level[level].get())
		self.vars_sfooter_shield_leftover.set(self.total_leftover_shield_by_level[level].get())
		self.vars_sfooter_armor_leftover.set(self.total_leftover_armor_by_level[level].get())
		
		
	def ManP_Update_Maneuvers(self):		
		prof = globals.character.profession.name
		
		self.add_armor_menu['menu'].delete(0, "end")
		self.add_combat_menu['menu'].delete(0, "end")
		self.add_shield_menu['menu'].delete(0, "end")
		if self.armor_menu_size > 1:
			self.add_armor_order_menu['menu'].delete(1, "end")
			if self.armor_menu_size > 2:
				self.edit_armor_order_menu['menu'].delete(1, "end")
			self.armor_menu_size = 1	
		if self.combat_menu_size > 1:
			self.add_combat_order_menu['menu'].delete(1, "end")
			if self.armor_menu_size > 2:
				self.edit_combat_order_menu['menu'].delete(1, "end")
			self.combat_menu_size = 1	
		if self.shield_menu_size > 1:		
			self.add_shield_order_menu['menu'].delete(1, "end")
			if self.shield_menu_size > 1:		
				self.edit_shield_order_menu['menu'].delete(1, "end")
			self.shield_menu_size = 1	
		
		self.man_select_menu['menu'].delete(0, "end")	
		
		for row in self.current_schedule_maneuvers_list:
			row.ManP_schedule_row.grid_remove()
		self.current_schedule_maneuvers_list = []
		self.combat_schedule_maneuvers_list = []
		self.shield_schedule_maneuvers_list = []
		self.armor_schedule_maneuvers_list = []

		if prof == "Warrior" or prof == "Rogue" or prof == "Paladin":
			self.sfooter_shield_row.grid(row=2, column=0, padx="1")
			self.sfooter_armor_row.grid(row=3, column=0, padx="1")
			self.man_select_menu["menu"].insert_command("end", label="Combat", command=lambda s="Combat": self.Maneuver_Style_Onchange(s))
			self.man_select_menu["menu"].insert_command("end", label="Shield", command=lambda s="Shield": self.Maneuver_Style_Onchange(s))
			self.man_select_menu["menu"].insert_command("end", label="Armor", command=lambda s="Armor": self.Maneuver_Style_Onchange(s))
		else:		
			self.man_select_menu["menu"].insert_command("end", label="Combat", command=lambda s="Combat": self.Maneuver_Style_Onchange(s))
			self.sfooter_shield_row.grid_remove()
			self.sfooter_armor_row.grid_remove()
		
			
		i = 0		
		for m in globals.combat_maneuvers:
			if not m in globals.character.combat_maneuvers:
				continue
			man = globals.character.combat_maneuvers[m].name
			self.add_combat_menu['menu'].add_command(label=man, command=lambda s=man: self.Maneuvers_Menu_Onchange(s))			
			self.combat_schedule_maneuvers_list.append(Schedule_List_Maneuver(man, "Combat", self.MR_Frame))
			i += 1
			
		i = 0		
		for m in globals.shield_maneuvers:
			if not m in globals.character.shield_maneuvers:
				continue
			man = globals.character.shield_maneuvers[m].name
			self.add_shield_menu['menu'].add_command(label=man, command=lambda s=man: self.Maneuvers_Menu_Onchange(s))
			self.shield_schedule_maneuvers_list.append(Schedule_List_Maneuver(man, "Shield", self.MR_Frame))
			i += 1
			
		i = 0		
		for m in globals.armor_maneuvers:
			if not m in globals.character.armor_maneuvers:
				continue
			man = globals.character.armor_maneuvers[m].name
			self.add_armor_menu['menu'].add_command(label=man, command=lambda s=man: self.Maneuvers_Menu_Onchange(s))
			self.armor_schedule_maneuvers_list.append(Schedule_List_Maneuver(man, "Armor", self.MR_Frame))
			i += 1
			
		if self.maneuver_mode.get() == "Combat":
			self.current_schedule_maneuvers_list = self.combat_schedule_maneuvers_list		
		elif self.maneuver_mode.get() == "Shield":
			self.current_schedule_maneuvers_list = self.shield_schedule_maneuvers_list	
		elif self.maneuver_mode.get() == "Armor":
			self.current_schedule_maneuvers_list = self.armor_schedule_maneuvers_list	

		i = 0
		for row in self.current_schedule_maneuvers_list:		
			row.ManP_schedule_row.grid(row=i, column=0)
			i += 1
			
		self.ManP_radio_var.set(1)
		self.level_counter.setvalue(0)		
		self.Maneuver_Style_Onchange("Combat")		

		
	def Maneuvers_Menu_Onchange(self, name):
		prof_type = globals.character.profession.type	
	
		if self.maneuver_mode.get() == "Combat":
			man = globals.combat_maneuvers_list[name]
			self.vars_dialog_combat_maneuver.set(name)				
		elif self.maneuver_mode.get() == "Shield":
			man = globals.shield_maneuvers_list[name]
			self.vars_dialog_shield_maneuver.set(name)				
		elif self.maneuver_mode.get() == "Armor":
			man = globals.armor_maneuvers_list[name]
			self.vars_dialog_armor_maneuver.set(name)		

			
		self.vars_dialog_info.set("%s,    %s,    %s,    %s,    %s" % (man.Get_Cost_At_Rank(0, prof_type), man.Get_Cost_At_Rank(1, prof_type), man.Get_Cost_At_Rank(2, prof_type), man.Get_Cost_At_Rank(3, prof_type), man.Get_Cost_At_Rank(4, prof_type)))		

		
class Build_List_Maneuver:
	def __init__(self, parent, name, type, hidden, order, info, rank1, rank2, rank3, rank4, rank5, start, target, goal):
		self.name = tkinter.StringVar()
		self.ranks = [tkinter.StringVar() for i in range(5)]
		self.order = tkinter.StringVar()
		self.hide = tkinter.StringVar()
		self.slvl = tkinter.StringVar()
		self.tlvl = tkinter.StringVar()
		self.goal = tkinter.StringVar()
		self.ManP_Info_Row = tkinter.Frame(parent)
		self.ManP_Edit_Button = ""
		self.type = type		
		
		
		if globals.character.profession.type == "square" or self.type != "Combat":
			modifier = 1
		elif globals.character.profession.type == "semi":
			modifier = 1.5
		elif globals.character.profession.type == "pure":
			modifier = 2
		
		if rank1 != "-":
			self.ranks[0].set( math.floor(int(rank1) * modifier) )
		else:
			self.ranks[0].set("-")
			
		if rank2 != "-":
			self.ranks[1].set( math.floor(int(rank2) * modifier) )
		else:
			self.ranks[1].set("-")
			
		if rank3 != "-":
			self.ranks[2].set( math.floor(int(rank3) * modifier) )
		else:
			self.ranks[2].set("-")
			
		if rank4 != "-":
			self.ranks[3].set( math.floor(int(rank4) * modifier) )
		else:
			self.ranks[3].set("-")
			
		if rank5 != "-":
			self.ranks[4].set( math.floor(int(rank5) * modifier) )
		else:
			self.ranks[4].set("-")
			
		self.name.set(name)
		self.hide.set(hidden)
		self.order.set(order)
		self.slvl.set(start)
		self.tlvl.set(target)
		self.goal.set(goal)
				
		tkinter.Label(self.ManP_Info_Row, width=3, bg="lightgray", textvariable=self.hide).grid(row=0, column=0, sticky="w", padx="1", pady="1")
		tkinter.Label(self.ManP_Info_Row, width=6, bg="lightgray", textvariable=self.order).grid(row=0, column=2, padx="1", pady="1")
		tkinter.Label(self.ManP_Info_Row, width="26", anchor="w", bg="lightgray", textvariable=self.name).grid(row=0, column=3, padx="1", pady="1")
		tkinter.Label(self.ManP_Info_Row, width="3", bg="lightgray", textvar=self.ranks[0]).grid(row=0, column=4, padx="1", pady="1")
		tkinter.Label(self.ManP_Info_Row, width="3", bg="lightgray", textvar=self.ranks[1]).grid(row=0, column=5, padx="1", pady="1")
		tkinter.Label(self.ManP_Info_Row, width="3", bg="lightgray", textvar=self.ranks[2]).grid(row=0, column=6, padx="1", pady="1")
		tkinter.Label(self.ManP_Info_Row, width="3", bg="lightgray", textvar=self.ranks[3]).grid(row=0, column=7, padx="1", pady="1")
		tkinter.Label(self.ManP_Info_Row, width="3", bg="lightgray", textvar=self.ranks[4]).grid(row=0, column=8, padx="1", pady="1")
		tkinter.Label(self.ManP_Info_Row, width=5, bg="lightgray", textvariable=self.goal).grid(row=0, column=9, padx="1")
		tkinter.Label(self.ManP_Info_Row, width=5, bg="lightgray", textvariable=self.slvl).grid(row=0, column=10, padx="1")
		tkinter.Label(self.ManP_Info_Row, width=5, bg="lightgray", textvariable=self.tlvl).grid(row=0, column=11, padx="1")
		self.ManP_Edit_Button = tkinter.Button(self.ManP_Info_Row, text="Edit", command="")
		self.ManP_Edit_Button.grid(row=0, column=12, padx="3")		

	def Get_Cost_At_Rank(self, rank, prof_type):
		if self.ranks[rank].get() == "-":
			return "-"
			
		if prof_type == "square" or self.type != "combat":
			modifier = 1
		elif prof_type == "semi":
			modifier = 1.5
		elif prof_type == "pure":
			modifier = 2	

		return math.floor(int(self.ranks[rank].get()) * modifier)
		
		
class Schedule_List_Maneuver:
	def __init__(self, name, type, parent):
		self.name = name
		self.type = type
		self.cost = tkinter.StringVar()
		self.ranks = tkinter.IntVar()
		self.total_ranks = tkinter.IntVar()
		self.combined_cost = tkinter.IntVar()
		self.ManP_schedule_row = tkinter.Frame(parent.interior())			
		
		self.ranks_by_level = [tkinter.IntVar() for i in range(101)]
		self.cost_at_level = [tkinter.IntVar() for i in range(101)]
		self.total_ranks_by_level = [tkinter.IntVar() for i in range(101)]
		self.combined_cost_by_level = [tkinter.IntVar() for i in range(101)]	
		
		tkinter.Label(self.ManP_schedule_row, width="26", bg="lightgray", anchor="w", text=self.name).grid(row=0, column=0, padx="1", pady="1")
		tkinter.Label(self.ManP_schedule_row, width="8", bg="lightgray", textvariable=self.ranks).grid(row=0, column=1, padx="1", pady="1")		 
		tkinter.Label(self.ManP_schedule_row, width="6", bg="lightgray", textvariable=self.cost).grid(row=0, column=2, padx="1", pady="1")	 		
		tkinter.Label(self.ManP_schedule_row, width="10", bg="lightgray", textvariable=self.total_ranks).grid(row=0, column=3, padx="1", pady="1")	
		tkinter.Label(self.ManP_schedule_row, width="8", bg="lightgray", textvariable=self.combined_cost).grid(row=0, column=4, padx="1", pady="1")	
		
		self.Set_To_Default()

		
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
	
	
	def Calculate_Ranks_Info(self, level, ranks):
		tcost = 0
		if self.type == "Combat":
			blist = globals.character.build_combat_maneuvers_list		
		elif self.type == "Shield":
			blist = globals.character.build_shield_maneuvers_list
		elif self.type == "Armor":
			blist = globals.character.build_armor_maneuvers_list
			
		for m in blist:
			if self.name == m.name.get():
				man = m
				break
		
		if level == 0:
			new_total_ranks = self.ranks_by_level[level].get() + ranks			
		else:
			new_total_ranks = self.total_ranks_by_level[level-1].get() + self.ranks_by_level[level].get() + ranks	
		
		tcost =	self.Calcuate_Total_Cost(man.ranks, new_total_ranks)
		self.ranks_by_level[level].set(ranks + self.ranks_by_level[level].get())
		self.cost_at_level[level].set(man.ranks[new_total_ranks-1].get())
		
		# Set Total Ranks and Bonus for each level
		for i in range(level, 101):
			self.total_ranks_by_level[i].set(new_total_ranks)				
			self.combined_cost_by_level[i].set(tcost)
				
				
	# This functions will calculate the cost a skill using all existing ranks relative to a specific level.
	def Calcuate_Total_Cost(self, man_ranks, total_ranks):	
		total = 0
		for i in range(0, total_ranks):
			if man_ranks[i].get() == "-":
				return 9999
		
			total += int(man_ranks[i].get())
			
		return total
		
		
	def Calcuate_Cost_At_Rank(self, man_ranks, rank):				
		if man_ranks[rank-1].get() == "-":
			return -1
		
		return int(man_ranks[rank-1].get())
