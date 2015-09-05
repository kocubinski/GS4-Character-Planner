# TODO LIST
# Entering a specific number of ranks to take over a level range will try to train them all at the start level
#   This is intentional. The goal will be to make the planner smart enough to know where to place the skill ranks. This will be worked on in the future.
# Skills do not take other subskills of the same type (Spell Research, Elemental Lore, etc) in to account when trying to determine training cost.
# Add a small message to the build header indicating if the build is valid. This will update if the user changes stats, race, professions to invalid.


#!/usr/bin/python

import tkinter
import re
import Pmw
import math
import Globals as globals
  
class Skills_Panel:  
	def __init__(self, parent, panel):		
		self.parent = parent
		self.schedule_skills_list = []
		self.SkP_radio_var = tkinter.IntVar()				
		
		# Dialog Box vars
		self.add_order_menu = ""
		self.add_skills_menu = ""
		self.edit_order_menu = ""
		self.edit_skills_menu = ""
		self.menu_size = 1
		self.dialog_max_ranks = 0
		self.vars_dialog_skill = tkinter.StringVar()
		self.vars_dialog_order = tkinter.StringVar()
		self.vars_dialog_info = tkinter.StringVar()
		self.vars_dialog_hide = tkinter.StringVar()
		self.vars_dialog_goal = tkinter.StringVar()
		self.vars_dialog_slevel = tkinter.StringVar()
		self.vars_dialog_tlevel = tkinter.StringVar()
		self.vars_dialog_errormsg = tkinter.StringVar()
		self.vars_dialog_edit_location = tkinter.IntVar()		
		
		# Schedule Level Calculation
		self.total_regained_ptp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_regained_mtp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_available_ptp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_available_mtp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_cost_ptp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_cost_mtp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_converted_ptp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_converted_mtp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_leftover_ptp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_leftover_mtp_by_level = [tkinter.IntVar() for i in range(101)]
		
		# Schedule Footer vars
		self.vars_sfooter_ptp_earned = tkinter.IntVar()
		self.vars_sfooter_mtp_earned = tkinter.IntVar()
		self.vars_sfooter_ptp_regained = tkinter.IntVar()
		self.vars_sfooter_mtp_regained = tkinter.IntVar()
		self.vars_sfooter_ptp_available = tkinter.IntVar()
		self.vars_sfooter_mtp_available = tkinter.IntVar()
		self.vars_sfooter_ptp_total_cost = tkinter.IntVar()
		self.vars_sfooter_mtp_total_cost = tkinter.IntVar()
		self.vars_sfooter_ptp_converted = tkinter.IntVar()
		self.vars_sfooter_mtp_converted = tkinter.IntVar()
		self.vars_sfooter_ptp_leftover = tkinter.IntVar()
		self.vars_sfooter_mtp_leftover = tkinter.IntVar()	
			
		self.add_box = self.Create_Dialog_Box(panel, "Add Skill", ("Add Skill,Cancel"))
		self.edit_box = self.Create_Dialog_Box(panel, "Edit Skill", ("Update Skill,Remove Skill,Cancel"))		
		
		self.level_counter = ""     #Becomes a Pmw.counter later on
			
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
		self.edit_box.withdraw()
		self.SkP_radio_var.set(1)
		self.level_counter.setvalue(0)
#		self.Update_Schedule_Frames()
							

	def Create_Build_Header(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 547, hull_height = 50)
		myframe.component("borderframe").config(borderwidth=0)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")	
		myframe_inner = myframe.interior()

		topframe = tkinter.Frame(myframe_inner)		
		topframe.grid(row=0, column=0, sticky="w")	
		tkinter.Button(topframe, height="1", text="Add Skill", command=self.Add_Button_Onclick).grid(row=0, column=0)		
		tkinter.Button(topframe, height="1", text="Calculate Build", command=self.Create_Schedule).grid(row=0, column=1)	
		tkinter.Button(topframe, text="Clear All", command=self.ClearAll_Button_Onclick).grid(row=0, column=2, sticky="w", pady="1")	
		
		title_scrollframe = Pmw.ScrolledFrame(myframe_inner, usehullsize = 1, hull_width = 530, hull_height = 26 )		
		title_scrollframe.configure(hscrollmode = "none")		
		title_scrollframe.grid(row=3, column=0, sticky="w")		
		title_scrollframe_inner = title_scrollframe.interior()						
		
		tkinter.Frame(title_scrollframe_inner).grid(row=3, column=0, columnspan=3)	
		tkinter.Label(title_scrollframe_inner, width="3", bg="lightgray", text="Hide").grid(row=0, column=0, padx="1")
		tkinter.Label(title_scrollframe_inner, width="6", bg="lightgray", text="Order").grid(row=0, column=1, padx="1")
		tkinter.Label(title_scrollframe_inner, width="26", bg="lightgray", text="Skill Name").grid(row=0, column=2, padx="1")
		tkinter.Label(title_scrollframe_inner, width="12", bg="lightgray", text="Cost & Ranks").grid(row=0, column=3, padx="1")
		tkinter.Label(title_scrollframe_inner, width="5", bg="lightgray", text="Goal").grid(row=0, column=4, padx="1")
		tkinter.Label(title_scrollframe_inner, width="5", bg="lightgray", text="S.lvl").grid(row=0, column=5, padx="1")
		tkinter.Label(title_scrollframe_inner, width="5", bg="lightgray", text="T.lvl").grid(row=0, column=6, padx="1")
		tkinter.Label(title_scrollframe_inner, width="4", bg="lightgray", text="Edit").grid(row=0, column=7, padx="1")
		
		return myframe
		
		
	def Create_Build_Frame(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 547, hull_height = 444)			
		myframe.configure(hscrollmode = "none")					
		
		return myframe			
		
		
	def Create_Schedule_Header(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 530, hull_height = 50)
		myframe.component("borderframe").config(borderwidth=0)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")			
		myframe_inner = myframe.interior()		
						
		topframe = tkinter.Frame(myframe_inner)	
		topframe.grid(row=0, column=0, sticky="w")	
		tlvl_frame = tkinter.Frame(topframe)
		tlvl_frame.grid(row=0, column=0, sticky="w", padx=3, pady="1")	
		self.level_counter = Pmw.Counter(tlvl_frame, entryfield_entry_width = 3, entryfield_validate = { 'validator':'numeric', 'min':0, 'max':100 }, labelpos = 'w', label_text = 'Training at Level', entryfield_value = 0, datatype = "numeric", entryfield_modifiedcommand=self.Update_Schedule_Frames )
		self.level_counter.grid(row=0, column=0, sticky="w", pady="1")
		
		tkinter.Radiobutton(topframe, anchor="w", text="Show All Skills", command=self.Update_Schedule_Frames, var=self.SkP_radio_var, value=1).grid(row=0, column=1)	
		tkinter.Radiobutton(topframe, anchor="w", text="Show All Trained", command=self.Update_Schedule_Frames, var=self.SkP_radio_var, value=2).grid(row=0, column=2)		
		tkinter.Radiobutton(topframe, anchor="w", text="Show Trained this Level", command=self.Update_Schedule_Frames, var=self.SkP_radio_var, value=3).grid(row=0, column=3)

		title_scrollframe = Pmw.ScrolledFrame(myframe_inner, usehullsize = 1, hull_width = 510, hull_height = 28 )		
		title_scrollframe.configure(hscrollmode = "none")		
		title_scrollframe.grid(row=3, column=0, sticky="w")	
		title_scrollframe_inner = title_scrollframe.interior()							
		
		tkinter.Frame(title_scrollframe_inner).grid(row=1, column=2, sticky="w", pady="1")	
		tkinter.Label(title_scrollframe_inner, width="26", bg="lightgray", text="Skill Name").grid(row=0, column=0, padx="1")
		tkinter.Label(title_scrollframe_inner, width="8", bg="lightgray", text="Ranks").grid(row=0, column=1, padx="1")
		tkinter.Label(title_scrollframe_inner, width="12", bg="lightgray", text="Cost").grid(row=0, column=2, padx="1")
		tkinter.Label(title_scrollframe_inner, width="10", bg="lightgray", text="Total Ranks").grid(row=0, column=3, padx="1")
		tkinter.Label(title_scrollframe_inner, width="11", bg="lightgray", text="Total Bonus").grid(row=0, column=4, padx="1")
	
		return myframe		
		
		
	def Create_Schedule_Frame(self, panel):
		self.training_middle_scrollframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 530, hull_height = 369)		
		self.training_middle_scrollframe_inner = self.training_middle_scrollframe.interior()
		self.training_middle_scrollframe.configure(hscrollmode = "none")		
	
		return self.training_middle_scrollframe		
	

	def Create_Schedule_Footer(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 530, hull_height = 75)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")			
		myframe_inner = myframe.interior()									
		
		tkinter.Label(myframe_inner, width="10", bg="lightgray", text="Earned").grid(row=0, column=1, padx="1")
		tkinter.Label(myframe_inner, width="10", bg="lightgray", text="Regained").grid(row=0, column=2, padx="1")
		tkinter.Label(myframe_inner, width="10", bg="lightgray", text="Available").grid(row=0, column=3, padx="1")
		tkinter.Label(myframe_inner, width="10", bg="lightgray", text="Total Cost").grid(row=0, column=4, padx="1")
		tkinter.Label(myframe_inner, width="10", bg="lightgray", text="Converted").grid(row=0, column=5, padx="1")
		tkinter.Label(myframe_inner, width="10", bg="lightgray", text="Leftover").grid(row=0, column=6, padx="1")

		tkinter.Label(myframe_inner, width=5, text="").grid(row=0, column=0, sticky="w", padx="1", pady="1")		
		tkinter.Label(myframe_inner, width="5", bg="lightgray", text="PTP").grid(row=1, column=0, padx="2", pady="1")
		tkinter.Label(myframe_inner, width="5", bg="lightgray", text="MTP").grid(row=2, column=0, padx="2", pady="1")	
		
		tkinter.Label(myframe_inner, width="10", bg="lightgray", textvar=self.vars_sfooter_ptp_earned).grid(row=1, column=1, padx="1")
		tkinter.Label(myframe_inner, width="10", bg="lightgray", textvar=self.vars_sfooter_mtp_earned).grid(row=2, column=1, padx="1")	
		tkinter.Label(myframe_inner, width="10", bg="lightgray", textvar=self.vars_sfooter_ptp_regained).grid(row=1, column=2, padx="1")
		tkinter.Label(myframe_inner, width="10", bg="lightgray", textvar=self.vars_sfooter_mtp_regained).grid(row=2, column=2, padx="1")	
		tkinter.Label(myframe_inner, width="10", bg="lightgray", textvar=self.vars_sfooter_ptp_available).grid(row=1, column=3, padx="1")	
		tkinter.Label(myframe_inner, width="10", bg="lightgray", textvar=self.vars_sfooter_mtp_available).grid(row=2, column=3, padx="1")
		tkinter.Label(myframe_inner, width="10", bg="lightgray", textvar=self.vars_sfooter_ptp_total_cost).grid(row=1, column=4, padx="1")
		tkinter.Label(myframe_inner, width="10", bg="lightgray", textvar=self.vars_sfooter_mtp_total_cost).grid(row=2, column=4, padx="1")		
		tkinter.Label(myframe_inner, width="10", bg="lightgray", textvar=self.vars_sfooter_ptp_converted).grid(row=1, column=5, padx="1")	
		tkinter.Label(myframe_inner, width="10", bg="lightgray", textvar=self.vars_sfooter_mtp_converted).grid(row=2, column=5, padx="1")
		tkinter.Label(myframe_inner, width="10", bg="lightgray", textvar=self.vars_sfooter_ptp_leftover).grid(row=1, column=6, padx="1")
		tkinter.Label(myframe_inner, width="10", bg="lightgray", textvar=self.vars_sfooter_mtp_leftover).grid(row=2, column=6, padx="1")		
					
		return myframe	
		
		
	def Create_Dialog_Box(self, panel, title, buttons):
		dialog = Pmw.Dialog(panel,
            buttons = (buttons.split(",")),
            title = title,
            command = self.Dialog_Box_Onclick)
			
		dialog.transient(panel)	
		dialog.resizable(width=0, height=0)		
		dialog.geometry('300x280+600+300')
				
		myframe = Pmw.ScrolledFrame(dialog.interior(), usehullsize = 1, hull_width = 300, hull_height = 280)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")		
		myframe.grid(row=0, column=0, sticky="nw")	
		myframe_inner = myframe.interior()	
				
		tkinter.Label(myframe_inner, width="12", anchor="w", bg="lightgray", text="Skill Name").grid(row=0, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="12", anchor="w", bg="lightgray", text="Cost & Ranks").grid(row=1, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="12", anchor="w", textvar=self.vars_dialog_info).grid(row=1, column=1, sticky="w")
		tkinter.Label(myframe_inner, width="12", anchor="w", text="").grid(row=2, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="12", anchor="w", bg="lightgray", text="Training Order").grid(row=3, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="12", anchor="w", bg="lightgray", text="Hide").grid(row=4, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="12", anchor="w", text="").grid(row=5, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="12", anchor="w", bg="lightgray", text="Goal").grid(row=6, column=0, sticky="w", pady=1)
		tkinter.Label(myframe_inner, width="12", anchor="w", bg="lightgray", text="Level Range").grid(row=7, column=0, sticky="w")			
								
		tkinter.Checkbutton(myframe_inner, command="", variable=self.vars_dialog_hide).grid(row=4, column=1, sticky="w")		
	
		if title == "Add Skill":
			self.add_order_menu = tkinter.OptionMenu(myframe_inner, self.vars_dialog_order, "1", command="")
			self.add_order_menu.config(width=1, heigh=1)	
			self.add_order_menu.grid(row=3, column=1, sticky="w")
			self.add_skills_menu = tkinter.OptionMenu(myframe_inner, self.vars_dialog_skill, "", command="")
			self.add_skills_menu.config(width=27, heigh=1)	
			self.add_skills_menu.grid(row=0, column=1, sticky="w", columnspan=4)		
		elif title == "Edit Skill":
			self.edit_order_menu = tkinter.OptionMenu(myframe_inner, self.vars_dialog_order, "1", command="")
			self.edit_order_menu.grid(row=3, column=1, sticky="w")
			self.edit_order_menu.config(width=1, heigh=1)
			self.edit_skills_menu = tkinter.OptionMenu(myframe_inner, self.vars_dialog_skill, "", command="")
			self.edit_skills_menu.config(width=27, heigh=1)	
			self.edit_skills_menu.grid(row=0, column=1, sticky="w", columnspan=4)				
				
		lvlframe = tkinter.Frame(myframe_inner)
		lvlframe.grid(row=7, column=1, sticky="w", columnspan=4)	
		Pmw.Counter(lvlframe, entryfield_entry_width = 3, entryfield_validate = { 'validator':'numeric', 'min':0, 'max':100 }, labelpos = 'w', label_text = 'Start', entryfield_value = 0, datatype = "numeric", entryfield_entry_textvariable=self.vars_dialog_slevel).grid(row=0, column=0, sticky="w")
		Pmw.Counter(lvlframe, entryfield_entry_width = 3, entryfield_validate = { 'validator':'numeric', 'min':0, 'max':100 }, labelpos = 'w', label_text = 'Target', entryfield_value = 0, datatype = "numeric", entryfield_entry_textvariable=self.vars_dialog_tlevel).grid(row=0, column=1, sticky="w", columnspan=2)
		goal_box = tkinter.Entry(myframe_inner, width="6", justify="center", validate="key", validatecommand="", textvariable=self.vars_dialog_goal).grid(row=6, column=1, sticky="w", padx=2)
		tkinter.Label(myframe_inner, anchor="w", font="-weight bold", wraplength=300, justify="left", textvariable=self.vars_dialog_errormsg).grid(row=8, column=0, sticky="w", columnspan=4)
				
			
		return dialog
				
		
	def Dialog_Box_Onclick(self, result):
		i = 0

		if result is None or result == "Cancel":
			self.add_box.withdraw()
			self.edit_box.withdraw()
			return
			
		# Error checking for Add/Edit Skill choices
		elif result == "Add Skill" or result == "Update Skill":
			if int(self.vars_dialog_slevel.get()) > int(self.vars_dialog_tlevel.get()):
				self.vars_dialog_errormsg.set("ERROR: Start level cannot be greater than target level." )
				return
			elif len(self.vars_dialog_goal.get()) == 0 or self.vars_dialog_goal.get() == "0" or not re.search(r"(^[1-9]\d{0,2}$)|(^[1-3]x$)|(^[0-2]\.[0-9]{1,3}x$)", self.vars_dialog_goal.get()):
				self.vars_dialog_errormsg.set("ERROR: Goal must be number greater than 0 or a rate (2x, 0.5x, 0.25x, etc).")
				return				
			elif self.vars_dialog_goal.get()[-1] == "x" and float(self.vars_dialog_goal.get()[:-1]) > self.dialog_max_ranks:
				self.vars_dialog_errormsg.set("ERROR: Goal rate cannot be greater than the skill's max ranks per level.")
				return				
			elif self.vars_dialog_goal.get()[-1] != "x" and	int(self.vars_dialog_goal.get()) > self.dialog_max_ranks	* (1 + int(self.vars_dialog_tlevel.get()) - int(self.vars_dialog_slevel.get()) ):
				self.vars_dialog_errormsg.set("ERROR: Goal ranks cannot be achieved within level range.")
				return					

				
		if result == "Add Skill":				
			skill = globals.character.skills[self.vars_dialog_skill.get()]
			hide = "" 
			if self.vars_dialog_hide.get() == "1":
				hide = "x"
			self.menu_size = self.menu_size + 1
				
			globals.character.build_skills_list.insert(int(self.vars_dialog_order.get())-1, Build_List_Skill(self.ML_Frame.interior(), self.vars_dialog_skill.get(), hide, self.vars_dialog_order.get(), 
			"%s / %s (%s)" % (skill.ptp_cost,skill.mtp_cost, skill.max_ranks), self.vars_dialog_slevel.get(), self.vars_dialog_tlevel.get(), self.vars_dialog_goal.get()))						
			globals.character.build_skills_list[int(self.vars_dialog_order.get())-1].SkP_Edit_Button.config(command=lambda v=int(self.vars_dialog_order.get())-1: self.Edit_Button_Onclick(v))
			
			if self.menu_size-1 > 1:
				self.edit_order_menu["menu"].insert_command("end", label=self.menu_size-1, command=lambda v=self.menu_size-1: self.vars_dialog_order.set(v))				
			self.add_order_menu["menu"].insert_command("end", label=self.menu_size, command=lambda v=self.menu_size: self.vars_dialog_order.set(v))	
			
			for skill in globals.character.build_skills_list:
				skill.order.set(i+1)
				skill.SkP_Edit_Button.config(command=lambda v=i: self.Edit_Button_Onclick(v))
				skill.SkP_Info_Row.grid(row=i, column=0)			
				i += 1			
			self.add_box.withdraw()		
		
		elif result == "Update Skill":
			skill = globals.character.build_skills_list.pop(self.vars_dialog_edit_location.get())
			skill.name.set(self.vars_dialog_skill.get())
			skill.info.set(self.vars_dialog_info.get())
			skill.order.set(self.vars_dialog_order.get())
			skill.slvl.set(self.vars_dialog_slevel.get())
			skill.tlvl.set(self.vars_dialog_tlevel.get())
			skill.goal.set(self.vars_dialog_goal.get())			
			
			if self.vars_dialog_hide.get() == "1":
				skill.hide.set("x")
			else:
				skill.hide.set("")			
			
			globals.character.build_skills_list.insert(int(self.vars_dialog_order.get())-1, skill)
			for skill in globals.character.build_skills_list:	
				skill.order.set(i+1)
				skill.SkP_Edit_Button.config(command=lambda v=i: self.Edit_Button_Onclick(v))
				skill.SkP_Info_Row.grid(row=i, column=0)			
				i += 1						
			self.edit_box.withdraw()				
		
		elif result == "Remove Skill":
			globals.character.build_skills_list.pop(self.vars_dialog_edit_location.get()).SkP_Info_Row.grid_remove()
			self.add_order_menu['menu'].delete("end", "end")
			self.edit_order_menu['menu'].delete("end", "end")
			self.menu_size -= 1
			for skill in globals.character.build_skills_list:
				skill.order.set(i+1)
				skill.SkP_Edit_Button.config(command=lambda v=i: self.Edit_Button_Onclick(v))
				skill.SkP_Info_Row.grid(row=i, column=0)			
				i += 1	
			self.edit_box.withdraw()		
		
		
	def Add_Button_Onclick(self):
		skill = globals.skills_list["Armor Use"]
		self.vars_dialog_skill.set("Armor Use")
		self.vars_dialog_info.set("%s/%s (%s)" % (skill.ptp_cost, skill.mtp_cost, skill.max_ranks))
		self.vars_dialog_order.set(self.menu_size)
		self.vars_dialog_hide.set("0")
		self.vars_dialog_goal.set("")
		self.vars_dialog_slevel.set("0")
		self.vars_dialog_tlevel.set("100")	
		self.vars_dialog_errormsg.set("")
		self.dialog_max_ranks = skill.max_ranks
		self.add_box.show()
		
		
	def Edit_Button_Onclick(self, location):
		build_skill = globals.character.build_skills_list[int(location)]
		skill = globals.skills_list[build_skill.name.get()]
		self.vars_dialog_skill.set(build_skill.name.get())
		self.vars_dialog_info.set("%s/%s (%s)" % (skill.ptp_cost, skill.mtp_cost, skill.max_ranks))
		self.vars_dialog_order.set(build_skill.order.get())
		self.vars_dialog_slevel.set(build_skill.slvl.get())
		self.vars_dialog_tlevel.set(build_skill.tlvl.get())
		self.vars_dialog_goal.set(build_skill.goal.get())		
		self.vars_dialog_errormsg.set("")
		self.vars_dialog_edit_location.set(int(location))
		self.dialog_max_ranks = skill.max_ranks
		self.edit_box.show()
		
		
	def ClearAll_Button_Onclick(self):		
		for row in self.schedule_skills_list:
			row.Set_To_Default()
			row.SkP_schedule_row.grid_remove()
			
		for skill in globals.character.build_skills_list:	
			skill.SkP_Info_Row.grid_remove()
			
		if self.menu_size > 1:
			self.add_order_menu['menu'].delete(1, "end")
			self.edit_order_menu['menu'].delete(1, "end")
			self.menu_size = 1
		
		globals.character.build_skills_list = []		
		self.total_regained_ptp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_regained_mtp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_cost_ptp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_cost_mtp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_converted_ptp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_converted_mtp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_leftover_ptp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_leftover_mtp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_available_ptp_by_level = [tkinter.IntVar() for i in range(101)]
		self.total_available_mtp_by_level = [tkinter.IntVar() for i in range(101)]
		
		self.SkP_radio_var.set(1)
		self.level_counter.setvalue(0)
		self.Update_Schedule_Frames()

		
	def Create_Schedule(self):		
		goal = 0; tranks = 0; estimated_ranks = 0
		
		# Clear schedule before using it.
		for row in self.schedule_skills_list:
			row.Set_To_Default()
			row.SkP_schedule_row.grid_remove()
				
		for bskill in globals.character.build_skills_list:
			if bskill.hide.get() == "x":
				continue
				
			for row in self.schedule_skills_list:               #figure out a better way to do this later on
#				print("%s %s" % (row.name, bskill.name))
				if row.name == bskill.name.get():
					break
					
			if bskill.goal.get()[-1] == "x":
				goal = float(bskill.goal.get()[:-1])
				start = int(bskill.slvl.get())
				end = int(bskill.tlvl.get()) + 1
				for i in range(start, end):
					tranks = row.total_ranks_by_level[i].get()
					estimated_ranks = goal * (i+1)
					mod_ranks = estimated_ranks % 1
					mod_goal = goal % 1
					if ( mod_ranks == .9 or 
						mod_ranks == .99 or 
						mod_ranks == .999
					   ) and  ( mod_goal == .3 or 
						mod_goal == .33 or 
						mod_goal == .333					   
					   ):
						estimated_ranks = int(math.ceil(estimated_ranks))					   
					else:
						estimated_ranks = int(math.floor(estimated_ranks))
#					print("%s %s" % (estimated_ranks, tranks))
					row.Calculate_Ranks_Info(i, estimated_ranks-tranks-start)			
			else:
				row.Calculate_Ranks_Info(int(bskill.slvl.get()), int(bskill.goal.get()))
#				goal = int(bskill.goal.get())
#				taken = 0
#				start_lvl = int(bskill.slvl.get())
#				ptp_arr = []
#				mtp_arr = []
#				while(taken < goal):
#					for i in range(start_lvl, 101):
#						ptp_arr[i] = self.total_leftover_ptp_by_level[i].get()
#						mtp_arr[i] = self.total_leftover_mtp_by_level[i].get()
						
#					for i in range(start_lvl, int(bskill.tlvl.get()) + 1):
				# TODO
				# This isn't do able at the moment since I can't get an up to date count of ptp/mtp left after taking a rank.
				# It also needs to calculate out to 100 just to be sure it doesn't go negative later on.
				# I may need to redo design to get this to work but I am going to leave it along for now
				#
				# Place ranks up to a certain number
				# favor spreading ranks over the entire level range and
				# front load ranks. By that I mean take ranks earlier in the level range and multiple ranks if need be.
				# hardest part will be deciding if it is possible to take a rank on a level with low TP. 1.5x could break a build unless accounted for, for example
				
		
			
		# Calculate the values for the Schedule Footer
#		abr_skill_list = []
#		for row in self.schedule_skills_list:
#			if row.total_ranks_by_level[100].get() > 0:				
#				abr_skill_list.append(row)
			
		for i in range(0, 101):
			pcost = 0; mcost = 0; pregain = 0; mregain = 0; prev_pleftover = 0; prev_mleftover = 0; ava_ptp = 0; ava_mtp = 0; convert_ptp = 0; convert_mtp = 0
			prev_pconverted = 0; prev_mconverted = 0
						
			for row in self.schedule_skills_list:
				if row.total_ranks_by_level[100].get() == 0:							
					continue
#			for row in abr_skill_list:
				pregain += row.ptp_regained_at_level[i].get()
				mregain += row.mtp_regained_at_level[i].get()
				pcost += row.ptp_cost_at_level[i].get()
				mcost += row.mtp_cost_at_level[i].get()
			
			if i > 0:
				prev_pleftover = self.total_leftover_ptp_by_level[i-1].get()
				prev_mleftover = self.total_leftover_mtp_by_level[i-1].get()
				prev_pconverted = self.total_converted_ptp_by_level[i-1].get()
				prev_mconverted = self.total_converted_mtp_by_level[i-1].get()
				pregain += prev_pconverted
				mregain += prev_mconverted
				
			ava_ptp = prev_pleftover + globals.character.ptp_by_level[i].get() + pregain
			ava_mtp = prev_mleftover + globals.character.mtp_by_level[i].get() + mregain 
			
#			print(ava_mtp)
#			print(mcost)
#			if ava_ptp < pcost and ava_mtp < mcost:
#				print("jere")
#				globals.error_dialogmsg.set("Skill Panel: Build becomes untrainable at lvl: " % i)	
#				globals.error_dialog.show()	
			if ava_ptp < pcost:
				while ava_mtp - convert_mtp > 1 and convert_mtp/2 + ava_ptp < pcost:
					convert_mtp += 2			
				if ava_mtp - convert_mtp <= 1:
					globals.error_event = 1
			elif ava_mtp < mcost:
				while ava_ptp - convert_ptp > 1 and convert_ptp/2 + ava_mtp < mcost:
					convert_ptp += 2			
				if ava_ptp - convert_ptp <= 1:
					globals.error_event = 1
					
			self.total_regained_ptp_by_level[i].set(pregain)
			self.total_regained_mtp_by_level[i].set(mregain)
			self.total_cost_ptp_by_level[i].set(pcost)
			self.total_cost_mtp_by_level[i].set(mcost)			
			self.total_available_ptp_by_level[i].set(ava_ptp)
			self.total_available_mtp_by_level[i].set(ava_mtp)	
			self.total_converted_ptp_by_level[i].set(convert_ptp)
			self.total_converted_mtp_by_level[i].set(convert_mtp)		
			self.total_leftover_ptp_by_level[i].set(ava_ptp - pcost + convert_mtp/2 - convert_ptp)
			self.total_leftover_mtp_by_level[i].set(ava_mtp - mcost + convert_ptp/2 - convert_mtp)
			
			if globals.error_event:
				break
			
		if globals.error_event:
			globals.error_dialogmsg.set("Skill Panel: Build becomes untrainable at lvl: %s" % i)	
			globals.error_dialog.show()	
			self.level_counter.setvalue(i)
	
		self.Update_Schedule_Frames()
		globals.character.StP_Update_Resources()

			
	def Update_Schedule_Frames(self):
		level = int(self.level_counter.getvalue())
		i = 0
#		print(self.SkP_radio_var.get())
		for row in self.schedule_skills_list:
			if self.SkP_radio_var.get() == 1 or (self.SkP_radio_var.get() == 2 and row.total_ranks_by_level[100].get() > 0) or (self.SkP_radio_var.get() == 3 and row.ranks_by_level[level].get() > 0):
				if row.ranks_by_level[level].get() > 0:
					row.cost.set("%s / %s" % (row.ptp_cost_at_level[level].get(), row.mtp_cost_at_level[level].get()))
				else:
					row.cost.set("")				
				row.ranks.set(row.ranks_by_level[level].get())
				row.total_ranks.set(row.total_ranks_by_level[level].get())
				row.bonus.set(row.bonus_by_level[level].get())
				row.SkP_schedule_row.grid(row=i, column=0)
			else:
				row.SkP_schedule_row.grid_remove()
			i += 1
			
		self.vars_sfooter_ptp_earned.set(globals.character.ptp_by_level[level].get())
		self.vars_sfooter_mtp_earned.set(globals.character.mtp_by_level[level].get())
		self.vars_sfooter_ptp_regained.set(self.total_regained_ptp_by_level[level].get())
		self.vars_sfooter_mtp_regained.set(self.total_regained_mtp_by_level[level].get())			
		self.vars_sfooter_ptp_available.set(self.total_available_ptp_by_level[level].get())
		self.vars_sfooter_mtp_available.set(self.total_available_mtp_by_level[level].get())	
		self.vars_sfooter_ptp_total_cost.set(self.total_cost_ptp_by_level[level].get())
		self.vars_sfooter_mtp_total_cost.set(self.total_cost_mtp_by_level[level].get())
		self.vars_sfooter_ptp_converted.set(self.total_converted_ptp_by_level[level].get())
		self.vars_sfooter_mtp_converted.set(self.total_converted_mtp_by_level[level].get()) 
		self.vars_sfooter_ptp_leftover.set(self.total_leftover_ptp_by_level[level].get())
		self.vars_sfooter_mtp_leftover.set(self.total_leftover_mtp_by_level[level].get())
		
		
	def SkP_Update_Skills(self):	
		self.add_skills_menu['menu'].delete(0, "end")
		self.edit_skills_menu['menu'].delete(0, "end")
		i = 0
		
		for row in self.schedule_skills_list:
			row.SkP_schedule_row.grid_remove()
		self.schedule_skills_list = []
		
		for s in globals.skills:
			if globals.character.skills[s] == "":
				continue
			skill = globals.character.skills[s].name
			self.add_skills_menu['menu'].add_command(label=skill, command=lambda s=skill: self.Skills_Menu_Onchange(s))
			self.edit_skills_menu['menu'].add_command(label=skill, command=lambda s=skill: self.Skills_Menu_Onchange(s))
			self.schedule_skills_list.append(Schedule_List_Skill(globals.character.skills[s].name, self.MR_Frame))
			self.schedule_skills_list[i].SkP_schedule_row.grid(row=i, column=0)
			i += 1
			
		self.level_counter.setvalue(0)
		self.Create_Schedule()
		

	def Skills_Menu_Onchange(self, name):
		skill = globals.skills_list[name]
		self.vars_dialog_skill.set(name)
		self.vars_dialog_info.set("%s/%s (%s)" % (skill.ptp_cost, skill.mtp_cost, skill.max_ranks))
		self.dialog_max_ranks = skill.max_ranks
	
	
	def Get_Skill_By_Name(self, name):
		for row in self.schedule_skills_list:
			if row.name == name:
				return row
				
		return None		
		
	
class Build_List_Skill:
	def __init__(self, parent, name, hidden, order, info, start, target, goal):
		self.name = tkinter.StringVar()
		self.info = tkinter.StringVar()
		self.order =tkinter.StringVar()
		self.hide = tkinter.StringVar()
		self.slvl = tkinter.StringVar()
		self.tlvl = tkinter.StringVar()
		self.goal = tkinter.StringVar()
		self.SkP_Info_Row = tkinter.Frame(parent)
		self.SkP_Edit_Button = ""
				
		self.name.set(name)
		self.hide.set(hidden)
		self.order.set(order)
		self.info.set(info)
		self.slvl.set(start)
		self.tlvl.set(target)
		self.goal.set(goal)
		
		tkinter.Label(self.SkP_Info_Row, width=3, bg="lightgray", textvariable=self.hide).grid(row=0, column=0, sticky="w", padx="1", pady="1")
		tkinter.Label(self.SkP_Info_Row, width=6, bg="lightgray", textvariable=self.order).grid(row=0, column=2, padx="1", pady="1")
		tkinter.Label(self.SkP_Info_Row, width="26", anchor="w", bg="lightgray", textvariable=self.name).grid(row=0, column=3, padx="1", pady="1")
		tkinter.Label(self.SkP_Info_Row, width="12", bg="lightgray", textvar=self.info).grid(row=0, column=4, padx="1", pady="1")
		tkinter.Label(self.SkP_Info_Row, width=5, bg="lightgray", textvariable=self.goal).grid(row=0, column=5, padx="1")
		tkinter.Label(self.SkP_Info_Row, width=5, bg="lightgray", textvariable=self.slvl).grid(row=0, column=6, padx="1")
		tkinter.Label(self.SkP_Info_Row, width=5, bg="lightgray", textvariable=self.tlvl).grid(row=0, column=7, padx="1")
		self.SkP_Edit_Button = tkinter.Button(self.SkP_Info_Row, text="Edit", command="")
		self.SkP_Edit_Button.grid(row=0, column=8, padx="3")		

		
class Schedule_List_Skill:
	def __init__(self, name, parent):
		self.name = name
		self.cost = tkinter.StringVar()
		self.ranks = tkinter.IntVar()
		self.total_ranks = tkinter.IntVar()
		self.bonus = tkinter.IntVar()
		self.SkP_schedule_row = tkinter.Frame(parent.interior())			
		
		tkinter.Label(self.SkP_schedule_row, width="26", bg="lightgray", anchor="w", text=self.name).grid(row=0, column=0, padx="1", pady="1")
		tkinter.Label(self.SkP_schedule_row, width="8", bg="lightgray", textvariable=self.ranks).grid(row=0, column=1, padx="1", pady="1")		 
		tkinter.Label(self.SkP_schedule_row, width="12", bg="lightgray", textvariable=self.cost).grid(row=0, column=2, padx="1", pady="1")	 		
		tkinter.Label(self.SkP_schedule_row, width="10", bg="lightgray", textvariable=self.total_ranks).grid(row=0, column=3, padx="1", pady="1")	
		tkinter.Label(self.SkP_schedule_row, width="11", bg="lightgray", textvariable=self.bonus).grid(row=0, column=4, padx="1", pady="1")	

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
		
	def Calculate_Ranks_Info(self, level, ranks):
		skill = globals.skills_list[self.name]		
		pcost = 0	
		mcost = 0			
		if level == 0:
			prev_total_ranks = 0			
		else:
			prev_total_ranks = self.total_ranks_by_level[level-1].get()
			self.Calcuate_Total_Cost(level-1, prev_total_ranks)

#		self.ranks_by_level[level].set(ranks)			
		self.ranks_by_level[level].set(self.ranks_by_level[level].get() + ranks)					
			
		# Set Total Ranks and Bonus for each level
		for i in range(level, 101):
			self.total_ranks_by_level[i].set(ranks + prev_total_ranks)
			self.bonus_by_level[i].set(self.Calculate_Skill_Bonus(ranks + prev_total_ranks))
								
				
		# Calculate the PTP and MTP cost for training in the skill. 
		for x in range(1, ranks+1):
#			print("%s vs %s" % (prev_total_ranks+x, level+1))
			if x + prev_total_ranks > 2 * (level + 1):
#				print("triple: %s" % (skill.ptp_cost * 4))
				pcost += skill.ptp_cost * 4
				mcost += skill.mtp_cost * 4
			elif x + prev_total_ranks > (level + 1):
#				print("double: %s" % (skill.ptp_cost * 2))
				pcost += skill.ptp_cost * 2
				mcost += skill.mtp_cost * 2
			else:
#				print("single: %s" % skill.ptp_cost)
				pcost += skill.ptp_cost
				mcost += skill.mtp_cost		
				
		self.ptp_cost_at_level[level].set(pcost)
		self.mtp_cost_at_level[level].set(mcost)
				
		self.Calcuate_Total_Cost(level, prev_total_ranks)
		
		self.ptp_regained_at_level[level].set(max(0, self.total_ptp_cost_at_level[level-1].get() - self.total_ptp_cost_at_level[level].get()))
		self.mtp_regained_at_level[level].set(max(0, self.total_mtp_cost_at_level[level-1].get() - self.total_mtp_cost_at_level[level].get()))
				
	def Calculate_Skill_Bonus(self, ranks):
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
				
	# This functions will calculate the cost a skill using all existing ranks relative to a specific level.
	def Calcuate_Total_Cost(self, level, total_ranks):
		skill = globals.skills_list[self.name]
		triple_train = max(0, total_ranks - 2 * (level + 1))
		double_train = max(0, total_ranks - triple_train - (level + 1))
		single_train = max(0, total_ranks - triple_train - double_train)		

		self.total_ptp_cost_at_level[level].set(skill.ptp_cost * single_train  +  2 * skill.ptp_cost * double_train  +  4 * skill.ptp_cost * triple_train)
		self.total_mtp_cost_at_level[level].set(skill.mtp_cost * single_train  +  2 * skill.mtp_cost * double_train  +  4 * skill.mtp_cost * triple_train)
#		print("level %s: regained PTP/MTP %s/%s" % (level, self.ptp_regained_at_level[level].get(), self.mtp_regained_at_level[level].get()))
#		print(" %s, %s, %s" % (single_train, double_train, triple_train))
#		print("cost now %s: cost prev %s" % (self.total_ptp_cost_at_level[level].get(), self.total_ptp_cost_at_level[level-1].get()))
		
		
#	def Get_Next_Rank_Type(self, level):
		# Returns 1 if single train, 2 if double train, 3 if triple train
#		if self.total_ranks_by_level[level] + 1 > 2*(level+1):
#			return 3
#		elif self.total_ranks_by_level[level] + 1 > (level+1):
#			return 2
#		else:		
#			return 1
