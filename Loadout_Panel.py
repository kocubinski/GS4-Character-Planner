# INDEX OF CLASSES AND METHODS
'''
class Loadout_Panel
	def __init__(self, panel)
	def Create_Gear_Header_Frame(self, panel):
	def Create_Gear_List_Frame(self, panel):
	def Create_Effects_Header_Frame(self, panel):	
	def Create_Effects_List_Frame(self, panel):	
	def Create_Gear_Dialog_Box(self, panel, title, buttons):
	def Gear_Add_Edit_Button_Onclick(self, location):	
	def Gear_ClearAll_Button_Onclick(self):			
	def Gear_Dialog_Box_Type_Onchange(self, result):
	def Gear_Dialog_Box_Name_Onchange(self, result):	
	def Gear_Dialog_Enchantment_Entrybox_Validate(self, d, S, s, P):		
	def Gear_Dialog_Gear_Weight_Entrybox_Validate(self, d, S, s, P):
	def Gear_Dialog_Box_Onclick(self, result):	
	def Create_Effect_Dialog_Box(self, panel, title, buttons):	
	def Effects_Add_Edit_Button_Onclick(self, location):
	def Effects_ClearAll_Button_Onclick(self):
	def Effects_Dialog_Box_Type_Onchange(self, result):
	def Effects_Dialog_Box_Name_Onchange(self, result):		
	def Effects_Dialog_Box_Onclick(self, result):
	def Scroll_Gear_Build_Frame(self, event):
	def Scroll_Effects_Build_Frame(self, event):
	def Scroll_Effect_Dialog_Box_Details_Frame(self, event):
	def Scroll_Effect_Dialog_Box_Scaling_Frame(self, event):	
	
class Effect_Dialog_Scaling_Row:
	def __init__(self, parent, name, min_max_value):	
	def Entrybox_Validate(self, d, S, s, P):	
'''


#!/usr/bin/python

import tkinter
import Pmw
import collections
import Globals as globals
  
# The purpose of the Loadout panel is to allow users to specify what gear (weapons, armor, shields) and effects (spells, enhancives, etc)
# they are using on their character. Further, this panel allows the user to customize the enhancement of gear and how much each effect is
# scaled when determining their power. This panel performs no calculations by itself. Information is saved and used by the Progression
# Panel. The user can have as much gear and effects as they want because the Progression panel is responsible for determining what is being
# used what is not being used. 
class Loadout_Panel:  
	def __init__(self, panel):		
		# Shared dialog box variables
		self.vars_dialog_order = tkinter.StringVar()
		self.vars_dialog_errormsg = tkinter.StringVar()
		self.vars_dialog_edit_location = tkinter.IntVar()	
		
		# These variables are used my the gear dialog box
		self.gear_menu_size = 1
		self.vars_dialog_gear_type = tkinter.StringVar()
		self.vars_dialog_gear_name = tkinter.StringVar()
		self.vars_dialog_gear_add_order = tkinter.StringVar()
		self.vars_dialog_gear_edit_order = tkinter.StringVar()
		self.vars_dialog_gear_enchantment = tkinter.StringVar()
		self.vars_dialog_gear_weight = tkinter.StringVar()
		self.dialog_gear_display_type = ""
		self.dialog_gear_skills = ""
		self.dialog_gear_names_menu = ""
		self.dialog_gear_types_menu = ""
		self.dialog_gear_add_order_menu = ""
		self.dialog_gear_edit_order_menu = ""
		self.dialog_gear_weight_entrybox = ""	
		
		# Intitialize the gear lists
		self.dialog_gear_types = ['Brawling', 'Blunt Weapons', 'Edged Weapons', 'Polearm Weapons', 'Ranged Weapons', 'Thrown Weapons', 'Two-Handed Weapons', 'UAC Weapons', 'Armor', 'Shields']
		self.dialog_gear_names = ['temp']	
		
		# These variables are used my the effect dialog box
		self.effects_menu_size = 1
		self.effects_dialog_scaling_rows = []
		self.vars_dialog_effect_function = ""
		self.vars_dialog_effect_type = tkinter.StringVar()
		self.vars_dialog_effect_name = tkinter.StringVar()
		self.vars_dialog_effect_add_order = tkinter.StringVar()
		self.vars_dialog_effect_edit_order = tkinter.StringVar()
		self.vars_dialog_effect_details = tkinter.StringVar()
		self.vars_dialog_scaling_tags = tkinter.StringVar()
		self.vars_dialog_effect_display_type = tkinter.StringVar()
		self.vars_dialog_effect_overrides = tkinter.StringVar()
		self.dialog_effect_names_menu = ""
		self.dialog_effect_types_menu = ""
		self.dialog_effect_add_order_menu = ""
		self.dialog_effect_edit_order_menu = ""
		
		# Intitialize the effects lists
		self.dialog_effect_types = globals.LdP_effect_display_types.keys()

		self.dialog_effect_names = ['temp']			
		self.dialog_effect_scaling_frame = ""			
		
		# Create the Gear dialog box and the Effect dialog box
		self.gear_dialog_box = self.Create_Gear_Dialog_Box(panel, "Add Gear", ("Add Gear,Cancel"))
		self.effect_dialog_box = self.Create_Effect_Dialog_Box(panel, "Add Effect", ("Add Effect,Cancel"))	
		

		#Create all the sub-frames of the panel
		self.Gear_Header_Frame = self.Create_Gear_Header_Frame(panel)
		self.Gear_List_Frame = self.Create_Gear_List_Frame(panel)
		self.Effects_Header_Frame = self.Create_Effects_Header_Frame(panel)
		self.Effects_List_Frame = self.Create_Effects_List_Frame(panel)
		
		
		#Make the frames visible
		self.Gear_Header_Frame.grid(row=0, column=0, sticky="nw")
		self.Effects_Header_Frame.grid(row=0, column=1, sticky="nw")
		self.Gear_List_Frame.grid(row=1, column=0, sticky="nw")
		self.Effects_List_Frame.grid(row=1, column=1, sticky="nw")

		# Initialize defaults
		self.Gear_List_Frame.bind_class("LdP_gear", "<MouseWheel>", self.Scroll_Gear_Build_Frame)
		self.Effects_List_Frame.bind_class("LdP_effects", "<MouseWheel>", self.Scroll_Effects_Build_Frame)
		self.effect_dialog_box.bind_class("LdP_effect_dialog_scaling", "<MouseWheel>", self.Scroll_Effect_Dialog_Box_Scaling_Frame)
		self.vars_dialog_gear_type.set('Brawling')
		self.Gear_Dialog_Box_Type_Onchange('Brawling')
		self.vars_dialog_effect_type.set('Minor Spiritual (100s)')
		self.Effects_Dialog_Box_Type_Onchange('Minor Spiritual (100s)')
		self.dialog_gear_add_order_menu["menu"].insert_command("end", label=self.gear_menu_size, command=lambda v=self.gear_menu_size: self.vars_dialog_order.set(v))
		self.dialog_effect_add_order_menu["menu"].insert_command("end", label=self.effects_menu_size, command=lambda v=self.effects_menu_size: self.vars_dialog_order.set(v))	
		self.gear_dialog_box.withdraw()	
		self.effect_dialog_box.withdraw()			
		

	# The header of the Gear frame contains the add/clear buttons and the title for the build list frame
	def Create_Gear_Header_Frame(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 476, hull_height = 70)
		myframe.component("borderframe").config(borderwidth=0)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")	
		myframe_inner = myframe.interior()

		tkinter.Label(myframe_inner, bg="lightgray", anchor="w", text="Weapons, Shields, Armor, UAC Gear").grid(row=0, column=0, sticky="w")		
		
		# top frame holds the 3 buttons
		topframe = tkinter.Frame(myframe_inner)		
		topframe.grid(row=1, column=0, sticky="w")			
		tkinter.Button(topframe, height="1", text="Add Gear", command=lambda v="": self.Gear_Add_Edit_Button_Onclick(v)).grid(row=0, column=0)		
		tkinter.Button(topframe, text="Clear All", command=self.Gear_ClearAll_Button_Onclick).grid(row=0, column=2, sticky="w", pady="1")	
		
		# this is frame will hold the title of the build schedule frame. This is done to allow the other frame to scroll but not lose the title header
		title_scrollframe = Pmw.ScrolledFrame(myframe_inner, usehullsize = 1, hull_width = 457, hull_height = 26 )		
		title_scrollframe.configure(hscrollmode = "none")		
		title_scrollframe.grid(row=3, column=0, sticky="w")		
		title_scrollframe_inner = title_scrollframe.interior()						
		
		# add all labels to the title header
		tkinter.Frame(title_scrollframe_inner).grid(row=3, column=0, columnspan=3)	
		tkinter.Label(title_scrollframe_inner, width="5", bg="lightgray", text="Order").grid(row=0, column=0, padx="1")
		tkinter.Label(title_scrollframe_inner, width="22", bg="lightgray", text="Gear Name").grid(row=0, column=1, padx="1")
		tkinter.Label(title_scrollframe_inner, width="8", bg="lightgray", text="Type").grid(row=0, column=2, padx="1")
		tkinter.Label(title_scrollframe_inner, width="20", bg="lightgray", text="Details").grid(row=0, column=3, padx="1")
		tkinter.Label(title_scrollframe_inner, width="4", bg="lightgray", text="Edit").grid(row=0, column=4, padx="1")
		
		return myframe
		

	# All this frame does is hold LdP_Build_Row objects. These rows display information about each gear item and allow their attributes to be manipulated
	def Create_Gear_List_Frame(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 476, hull_height = 395)		
		myframe_inner = myframe.interior()
		myframe.configure(hscrollmode = "none", vscrollmode = "static")						
		myframe.bindtags("LdP_gear")					
#		myframe_inner.bindtags("LdP_gear")	Breaks the auto scrollbar when an row is added. Go fig.
	
		return myframe			
		
		
	# The header of the Effects frame contains the add/clear buttons and the title for the build list frame
	def Create_Effects_Header_Frame(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 624, hull_height = 70)
		myframe.component("borderframe").config(borderwidth=0)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")	
		myframe_inner = myframe.interior()

		tkinter.Label(myframe_inner, bg="lightgray", anchor="w", text="Spells, Buffs, Enhancives").grid(row=0, column=0, sticky="w")		

		# top frame holds the 3 buttons
		topframe = tkinter.Frame(myframe_inner)		
		topframe.grid(row=1, column=0, sticky="w")			
		tkinter.Button(topframe, height="1", text="Add Effect", command=lambda v="": self.Effects_Add_Edit_Button_Onclick(v)).grid(row=0, column=0)		
		tkinter.Button(topframe, text="Clear All", command=self.Effects_ClearAll_Button_Onclick).grid(row=0, column=2, sticky="w", pady="1")	
		
		# this is frame will hold the title of the build schedule frame. This is done to allow the other frame to scroll but not lose the title header
		title_scrollframe = Pmw.ScrolledFrame(myframe_inner, usehullsize = 1, hull_width = 605, hull_height = 26 )		
		title_scrollframe.configure(hscrollmode = "none")		
		title_scrollframe.grid(row=3, column=0, sticky="w")		
		title_scrollframe_inner = title_scrollframe.interior()						
		
		# add all labels to the tittle header
		tkinter.Frame(title_scrollframe_inner).grid(row=3, column=0, columnspan=3)	
		tkinter.Label(title_scrollframe_inner, width="5", bg="lightgray", text="Order").grid(row=0, column=0, padx="1")
		tkinter.Label(title_scrollframe_inner, width="15", bg="lightgray", text="Effect Name").grid(row=0, column=1, padx="1")
		tkinter.Label(title_scrollframe_inner, width="8", bg="lightgray", text="Type").grid(row=0, column=2, padx="1")
		tkinter.Label(title_scrollframe_inner, width="27", bg="lightgray", text="Effect Details").grid(row=0, column=3, padx="1")
		tkinter.Label(title_scrollframe_inner, width="20", bg="lightgray", text="Effect Scaling").grid(row=0, column=4, padx="1")
		tkinter.Label(title_scrollframe_inner, width="4", bg="lightgray", text="Edit").grid(row=0, column=5, padx="1")
		
		return myframe		
		

	# All this frame does is hold LdP_Build_Row objects. These rows display information about each gear item and allow their attributes to be manipulated
	def Create_Effects_List_Frame(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 624, hull_height = 395)		
		myframe_inner = myframe.interior()
		myframe.configure(hscrollmode = "none", vscrollmode = "static")						
		myframe.bindtags("LdP_effects")					
#		myframe_inner.bindtags("LdP_effects")	Breaks the auto scrollbar when an row is added. Go fig.
	
		return myframe			


	# The gear dialog box allows you to add/edit a Gear object
	# The user first selects what type gear they want followed by the specific name (Ranged -> Longbow)
	# The user can indicate the Gear's enhancement bonus (doesn't allow #x format only whole numbers)
	# and the gears weight (which begins as the gear's default weight)
	def Create_Gear_Dialog_Box(self, panel, title, buttons):
		dialog = Pmw.Dialog(panel,
            buttons = (buttons.split(",")),
            title = title,
            command = self.Gear_Dialog_Box_Onclick)
			
		dialog.transient(panel)	
		dialog.resizable(width=0, height=0)		
		dialog.geometry('330x280+600+300')
				
		myframe = Pmw.ScrolledFrame(dialog.interior(), usehullsize = 1, hull_width = 330, hull_height = 280)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")		
		myframe.grid(row=0, column=0, sticky="nw")	
		myframe_inner = myframe.interior()	
				
		# Add the labels that appear on the left side of the dialog box		
		tkinter.Label(myframe_inner, width="16", anchor="w", bg="lightgray", text="Gear Type").grid(row=0, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="16", anchor="w", bg="lightgray", text="Gear Name").grid(row=1, column=0, sticky="w")		
		tkinter.Label(myframe_inner, width="16", anchor="w", text="").grid(row=2, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="16", anchor="w", bg="lightgray", text="Order Number").grid(row=3, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="16", anchor="w", text="").grid(row=5, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="16", anchor="w", bg="lightgray", text="Enchantment Bonus").grid(row=6, column=0, sticky="w", pady=1)
		self.dialog_weight_label = tkinter.Label(myframe_inner, width="16", anchor="w", bg="lightgray", text="Gear Weight (lb)")
		self.dialog_weight_label.grid(row=7, column=0, sticky="w")												
		
		# The add order and edit order track the location where the Gear object is the build list
		# Add order is 1 greater than the edit order.
		self.dialog_gear_add_order_menu = tkinter.ttk.OptionMenu(myframe_inner, self.vars_dialog_order, "1", command="")
		self.dialog_gear_add_order_menu.config(width=1)	
		self.dialog_gear_add_order_menu.grid(row=3, column=1, sticky="w")		
		self.dialog_gear_edit_order_menu = tkinter.ttk.OptionMenu(myframe_inner, self.vars_dialog_order, "1", command="")
		self.dialog_gear_edit_order_menu.config(width=1)	
		
		# The gear types are categories for all the equippable gear (edged weapons, blunt weapons, armor, etc)
		self.dialog_gear_types_menu = tkinter.OptionMenu(myframe_inner, self.vars_dialog_gear_type, *self.dialog_gear_types, command=self.Gear_Dialog_Box_Type_Onchange)
		self.dialog_gear_types_menu.config(width=27, heigh=1)	
		self.dialog_gear_types_menu.grid(row=0, column=1, sticky="w", columnspan=4)
				
		# Specific names for each of gear item under chosen type (Brawling -> list of all brawling weapons)
		self.dialog_gear_names_menu = tkinter.OptionMenu(myframe_inner, self.vars_dialog_gear_name, *self.dialog_gear_names, command="")
		self.dialog_gear_names_menu.config(width=27, heigh=1)	
		self.dialog_gear_names_menu.grid(row=1, column=1, sticky="w", columnspan=4)					

		# Setup the validation hooks for the entryboxes
		enchantment_cmd = (globals.root.register(self.Gear_Dialog_Enchantment_Entrybox_Validate), '%d', '%S', '%s', '%P')
		weight_cmd = (globals.root.register(self.Gear_Dialog_Gear_Weight_Entrybox_Validate), '%d', '%S', '%s', '%P')
		
		# Create the enhancement and weight entryboxes
		tkinter.Entry(myframe_inner, width="6", justify="center", validate="key", validatecommand=enchantment_cmd, textvariable=self.vars_dialog_gear_enchantment).grid(row=6, column=1, sticky="w", padx=2)
		self.dialog_gear_weight_entrybox = tkinter.Entry(myframe_inner, width="6", justify="center", validate="key", validatecommand=weight_cmd, textvariable=self.vars_dialog_gear_weight)
		self.dialog_gear_weight_entrybox.grid(row=7, column=1, sticky="w", padx=2)
		tkinter.Label(myframe_inner, anchor="w", font="-weight bold", wraplength=330, justify="left", textvariable=self.vars_dialog_errormsg).grid(row=8, column=0, sticky="w", columnspan=4)
		
		return dialog
			
		
	# Clicking the Add Gear button or the Edit button in a gear row will call this method
	# This shows a Gear dialog box
	def Gear_Add_Edit_Button_Onclick(self, location):
		self.dialog_gear_add_order_menu.grid_remove()
		self.dialog_gear_edit_order_menu.grid_remove()
	
		# Location is set to a number if an Edit button is clicked.
		# It refers to it's location in the build list. 
		# If location isn't set, show the Add version of the dialog box
		# otherwise, show the Edit version
		if( location == "" ):				
			#self.dialog_gear_display_type = ""
			self.Gear_Dialog_Box_Type_Onchange('Brawling')
			self.vars_dialog_gear_type.set("Brawling")			
			self.vars_dialog_order.set(self.gear_menu_size)	
			self.vars_dialog_gear_enchantment.set("0")
			self.vars_dialog_gear_weight.set("0")
			self.dialog_gear_add_order_menu.grid(row=3, column=1, sticky="w")		
			
			# If the last time we used the dialog box was as an edit box, change the buttons to the add version
			if self.gear_dialog_box.component("buttonbox").button(0)["text"] == "Update Gear":
				self.gear_dialog_box.component("buttonbox").delete("Update Gear")
				self.gear_dialog_box.component("buttonbox").delete("Remove Gear")		
				self.gear_dialog_box.component("buttonbox").insert("Add Gear", command=lambda v="Add Gear": self.Gear_Dialog_Box_Onclick(v))	
		else:
			gear = globals.character.loadout_gear_build_list[location]
			self.Gear_Dialog_Box_Type_Onchange(gear.dialog_type)		
			self.vars_dialog_gear_type.set(gear.dialog_type)	
			self.vars_dialog_order.set(location+1)		
			self.vars_dialog_gear_name.set(gear.name.get())
			self.vars_dialog_gear_enchantment.set(gear.enchantment)
			self.vars_dialog_gear_weight.set(gear.weight)
			self.vars_dialog_edit_location.set(int(location))
			self.dialog_gear_edit_order_menu.grid(row=3, column=1, sticky="w")		
			self.dialog_gear_display_type = gear.display_type.get()
						
			# If the last time we used the dialog box was as an add box, change the buttons to the edit version
			if self.gear_dialog_box.component("buttonbox").button(0)["text"] == "Add Gear":
				self.gear_dialog_box.component("buttonbox").delete("Add Gear")
				self.gear_dialog_box.component("buttonbox").insert("Remove Gear", command=lambda v="Remove Gear": self.Gear_Dialog_Box_Onclick(v))	
				self.gear_dialog_box.component("buttonbox").insert("Update Gear", command=lambda v="Update Gear": self.Gear_Dialog_Box_Onclick(v))		
		
		self.gear_dialog_box.show()
		self.gear_dialog_box.grab_set()		
		
		
	# Empties the gear build list and removes all the LdP rows from the build frame	
	def Gear_ClearAll_Button_Onclick(self):		
		for row in globals.character.loadout_gear_build_list:
			row.LdP_Row.grid_remove()			
			
		# Fun fact, if you try to do delete(1, end)	on an option menue that only has no objects in it, it throws a python error. So this check is needed.
		if self.gear_menu_size > 1:
			self.dialog_gear_add_order_menu['menu'].delete(1, "end")
#			menu = [1]
#			self.dialog_gear_edit_order_menu.set_menu(1, *menu)
			self.dialog_gear_edit_order_menu['menu'].delete(0, "end")
			self.gear_menu_size = 1
		
		# A change is being made to the gear list. Set the global value to 1 so the Progression Panel knows to reset the loadout list
		globals.LdP_Gear_List_Updated = 1
		globals.character.loadout_gear_build_list = []			
		self.Gear_List_Frame.yview("moveto", 0, "units")
		
	
	# This event occurs when the user changes the gear type in the gear dialog box
	# Contacts the sql database and searches a given table for all gear of the new type
	# Clear the name menu and add in the new gear names
	def Gear_Dialog_Box_Type_Onchange(self, result):
		where = ""
		wherenot = ""
		what = "name, base_weight"
		
		# figure out what table to search
		if result == "Armor":
			table = "Armor"		
		elif result == "Shields":
			table = "Shields"	
		else:
			table = "Weapons"
			what = "name, base_weight, weapon_type"
			if result == "Brawling":
				wherenot = "AND name <> 'Closed Fist'"
			elif result == "Two-Handed Weapons":
				wherenot = "AND name <> 'Katana, One-Handed'"
			where = "WHERE weapon_type LIKE '%%%s%%' %s" % (result, wherenot)
			
		# Search the sql table for the name and base weight of all gear of the new type
		globals.db_cur.execute("SELECT %s FROM %s %s " % (what, table, where))
		globals.db_con.commit()		
		data = globals.db_cur.fetchall()
		new_choices = [item[0] for item in data]			
		
		# Clear the gear name menu and add refill it with the new names
		self.dialog_gear_names_menu['menu'].delete(0, "end")
		for choice in new_choices:
			self.dialog_gear_names_menu['menu'].add_command(label=choice, command=lambda v=choice: self.Gear_Dialog_Box_Name_Onchange(v))
		self.vars_dialog_gear_name.set(new_choices[0])
		self.vars_dialog_gear_weight.set(data[0][1])
		if result == "Armor" or result == "Shields":
			self.dialog_gear_skills = result
			self.dialog_gear_display_type = globals.LdP_gear_display_types[result]
		else:
			self.dialog_gear_skills = data[0][2]
			self.dialog_gear_display_type = globals.LdP_gear_display_types[data[0][2]]

			
	# When a new gear name is picked from the gear dialog menu, this method is called
	def Gear_Dialog_Box_Name_Onchange(self, result):	
		what = "base_weight"
		self.dialog_gear_display_type = ""
		dialog_gear_type = self.vars_dialog_gear_type.get()
				
		self.vars_dialog_gear_name.set(result)		
		
		if(dialog_gear_type == 'Armor'):
			table = 'Armor'
		elif(dialog_gear_type == 'Shields'):
			table = 'Shields'
		else:
			table = 'Weapons'
			what = "base_weight, weapon_type"					
		
		# Search the sql table for the base weight of the new gear
		globals.db_cur.execute("SELECT %s FROM %s WHERE name = '%s' " % (what, table, result))
		globals.db_con.commit()		
		data = globals.db_cur.fetchall()
		self.vars_dialog_gear_weight.set(data[0][0])	
		if dialog_gear_type == "Armor" or dialog_gear_type == "Shields":
			self.dialog_gear_skills  = dialog_gear_type
			self.dialog_gear_display_type = globals.LdP_gear_display_types[dialog_gear_type]
		else:
			if result == "Katar":
				self.vars_dialog_gear_type.set("Brawling")
			elif result == "Katana, One-Handed":
				self.vars_dialog_gear_type.set("Edged Weapons")
			else:
				self.vars_dialog_gear_type.set(data[0][1])
			self.dialog_gear_skills = data[0][1]
			self.dialog_gear_display_type = globals.LdP_gear_display_types[data[0][1]]


	# Gear enchantment values must be whole number that can be from -10 (-2x) to +50 (10x)
	def Gear_Dialog_Enchantment_Entrybox_Validate(self, d, S, s, P):		
		if( d == "1"):
			if( (len(s) + len(S)) > 3 ):
				return False
			try:				
				if( float(P) <= 50 and float(P) >= -10 ):	
					return True
				else:
					return False
			except ValueError:
				return False
		
		return True
		
		
	# Gear weight must be a whole number between 0 and 999
	def Gear_Dialog_Gear_Weight_Entrybox_Validate(self, d, S, s, P):		
		if( d == "1"):
			if( (len(s) + len(S)) > 3 ):
				return False
			try:				
				if( float(P) <= 999 and float(P) >= 0 ):	
					return True
				else:
					return False
			except ValueError:
				return False
		
		return True		

		
	# This handles button all the button events that occur in the Add/Edit gear dialog box.	
	# This will add, update, or remove a gear object from the gear build list
	def Gear_Dialog_Box_Onclick(self, result):
		i = 0

		# Occurs if the user clicks the Cancel button or the "x" in the upper right corner. Just close the box and don't do anything.
		if result is None or result == "Cancel":
			self.gear_dialog_box.withdraw()
			self.gear_dialog_box.grab_release()
			return
		
		# A change is being made to the gear list. Set the global value to 1 so the Progression Panel knows to reset the loadout list
		globals.LdP_Gear_List_Updated = 1
		
		
		# Make sure that leaving the entry boxes blank counts as 0. This would break the planner otherwise
		enchantment = self.vars_dialog_gear_enchantment.get()	
		weight = self.vars_dialog_gear_weight.get()				
		if enchantment == "":
			enchantment = 0			
		if weight == "":
			weight = 0
				
				
		# Create a new Gear object with the parameters from the gear dialog box and insert it into the gear build list
		# Make the new gear object's LdP row visible
		if result == "Add Gear":		
			self.gear_menu_size = self.gear_menu_size + 1
			
			globals.character.loadout_gear_build_list.insert(int(self.vars_dialog_order.get())-1, globals.Gear(int(self.vars_dialog_order.get())-1, self.vars_dialog_gear_name.get(), enchantment, weight, self.dialog_gear_skills, self.vars_dialog_gear_type.get()) )
						
			# Make the new Gear object's row visible
			globals.character.loadout_gear_build_list[int(self.vars_dialog_order.get())-1].Create_LdP_row(self.Gear_List_Frame.interior())						
			globals.character.loadout_gear_build_list[int(self.vars_dialog_order.get())-1].LdP_Edit_Button.config(command=lambda v=int(self.vars_dialog_order.get())-1: self.Gear_Add_Edit_Button_Onclick(v))			
			
			# Make sure the display frame has the correct information in it. 
			globals.character.loadout_gear_build_list[int(self.vars_dialog_order.get())-1].Update_Display_Details()
			# Set the traits of the gear
			globals.character.loadout_gear_build_list[int(self.vars_dialog_order.get())-1].Set_Gear_Traits("")
			
			# Update the size menu
			if self.gear_menu_size > 1:
				self.dialog_gear_edit_order_menu["menu"].insert_command("end", label=self.gear_menu_size-1, command=lambda v=self.gear_menu_size-1: self.vars_dialog_order.set(v))	
			self.dialog_gear_add_order_menu["menu"].insert_command("end", label=self.gear_menu_size, command=lambda v=self.gear_menu_size: self.vars_dialog_order.set(v))	
						
			# Update the gear build list order
			for gear in globals.character.loadout_gear_build_list:
				gear.order.set(i+1)
				gear.Update_Progression_Name()
				gear.LdP_Edit_Button.config(command=lambda v=i: self.Gear_Add_Edit_Button_Onclick(v))
				gear.LdP_Row.grid(row=i, column=0)			
				i += 1							
				
			self.gear_dialog_box.withdraw()	
			self.gear_dialog_box.grab_release()	
		
		# Updates an existing gear object. 
		# The new information for the gear is take from the Dialog box and can change every attribute of the entry
		elif result == "Update Gear":
			gear = globals.character.loadout_gear_build_list.pop(self.vars_dialog_edit_location.get())
			name = self.vars_dialog_gear_name.get()
			gear.name.set(name)
			gear.dialog_type = self.vars_dialog_gear_type.get()
			
			# Katar and Katana, One-Handed need an override for display type
			if name == "Katar":
				gear.display_type.set("OHE/BRW")
			elif name == "Katana, One-Handed":
				gear.display_type.set("OHE/THW")
			else:
				gear.display_type.set(globals.LdP_gear_display_types[self.dialog_gear_skills])
				
			gear.order.set(self.vars_dialog_order.get())
			gear.enchantment = enchantment
			gear.weight = weight
			gear.skills = self.dialog_gear_skills
			
			# Insert the Gear object into it's new location on the build list
			globals.character.loadout_gear_build_list.insert(int(self.vars_dialog_order.get())-1, gear)
			
			gear.Update_Display_Details()						
			gear.Set_Gear_Traits("") # Set the traits of the gear
			
			for gear in globals.character.loadout_gear_build_list:
				gear.order.set(i+1)
				gear.Update_Progression_Name()
				gear.LdP_Edit_Button.config(command=lambda v=i: self.Gear_Add_Edit_Button_Onclick(v))
				gear.LdP_Row.grid(row=i, column=0)			
				i += 1				
				
			self.gear_dialog_box.withdraw()	
			self.gear_dialog_box.grab_release()			
		
		# Current selected entry in the gear list is removed, the gear list is updated with the correct entry order, and the build frame is updated to reflect the removal.
		elif result == "Remove Gear":
			globals.character.loadout_gear_build_list.pop(self.vars_dialog_edit_location.get()).LdP_Row.grid_remove()
			self.gear_menu_size -= 1
			if self.gear_menu_size > 0:
				self.dialog_gear_add_order_menu['menu'].delete("end", "end")
			else:
				self.gear_menu_size = 1
			self.dialog_gear_edit_order_menu['menu'].delete("end", "end")
			for gear in globals.character.loadout_gear_build_list:
				gear.order.set(i+1)
				gear.Update_Progression_Name()
				gear.LdP_Edit_Button.config(command=lambda v=i: self.Gear_Add_Edit_Button_Onclick(v))
				gear.LdP_Row.grid(row=i, column=0)			
				i += 1	
			self.gear_dialog_box.withdraw()	
			self.gear_dialog_box.grab_release()


	# The effect dialog box allows you to add/edit a Effect object
	# The user first selects what type effect they want followed by the specific name (Maneuvers -> Surge of Strength)
	# The dialog box will generate
	def Create_Effect_Dialog_Box(self, panel, title, buttons):
		dialog = Pmw.Dialog(panel,
            buttons = (buttons.split(",")),
            title = title,
            command = self.Effects_Dialog_Box_Onclick)
			
		dialog.transient(panel)	
		dialog.resizable(width=0, height=0)		
		dialog.geometry('375x340+600+300')
				
		myframe = Pmw.ScrolledFrame(dialog.interior(), usehullsize = 1, hull_width = 375, hull_height = 340)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")		
		myframe.grid(row=0, column=0, sticky="nw")	
		myframe_inner = myframe.interior()	
				
		wrapperframe1 = tkinter.Frame(myframe_inner)	
		wrapperframe1.grid(row=0, column=0, sticky="w")
		tkinter.Label(wrapperframe1, width="16", anchor="w", bg="lightgray", text="Effect Type").grid(row=0, column=0, sticky="w")
		self.dialog_effect_types_menu = tkinter.OptionMenu(wrapperframe1, self.vars_dialog_effect_type, *self.dialog_effect_types, command=self.Effects_Dialog_Box_Type_Onchange)
		self.dialog_effect_types_menu.config(width=30, heigh=1)	
		self.dialog_effect_types_menu.grid(row=0, column=1, sticky="w", columnspan=4)		
		
		wrapperframe2 = tkinter.Frame(myframe_inner)	
		wrapperframe2.grid(row=1, column=0, sticky="w")
		tkinter.Label(wrapperframe2, width="16", anchor="w", bg="lightgray", text="Effect Name").grid(row=0, column=0, sticky="w")		
		self.dialog_effect_names_menu = tkinter.OptionMenu(wrapperframe2, self.vars_dialog_effect_name, *self.dialog_effect_names, command=self.Effects_Dialog_Box_Name_Onchange)
		self.dialog_effect_names_menu.config(width=30, heigh=1)	
		self.dialog_effect_names_menu.grid(row=0, column=1, sticky="w", columnspan=4)	
		
		tkinter.Label(myframe_inner, width="16", anchor="w", text="").grid(row=2, column=0, sticky="w")		
		
		wrapperframe3 = tkinter.Frame(myframe_inner)	
		wrapperframe3.grid(row=3, column=0, sticky="w")
		tkinter.Label(wrapperframe3, width="16", anchor="w", bg="lightgray", text="Order Number").grid(row=0, column=0, sticky="w")
		self.dialog_effect_add_order_menu = tkinter.ttk.OptionMenu(wrapperframe3, self.vars_dialog_order, "1", command="")
		self.dialog_effect_add_order_menu.config(width=1)	
		self.dialog_effect_edit_order_menu = tkinter.ttk.OptionMenu(wrapperframe3, self.vars_dialog_order, "1", command="")
		self.dialog_effect_edit_order_menu.config(width=1)	
		self.dialog_effect_add_order_menu.grid(row=0, column=1, sticky="w")		
		
		tkinter.Label(myframe_inner, width="16", anchor="w", text="").grid(row=5, column=0, sticky="w")
			
		tkinter.Label(myframe_inner, width="16", anchor="w", bg="lightgray", text="Effect Details").grid(row=6, column=0, sticky="w", pady=1)
		self.dialog_effect_details_frame = Pmw.ScrolledFrame(myframe_inner, usehullsize = 1, hull_width = 365, hull_height = 51)
		self.dialog_effect_details_frame.component("borderframe").config(borderwidth=0)
		self.dialog_effect_details_frame.configure(hscrollmode = "none", vscrollmode = "static")		
		self.dialog_effect_details_frame.grid(row=7, column=0, sticky="w")		
		details_label = tkinter.Label(self.dialog_effect_details_frame.interior(), anchor="w", wraplength=345, justify="left", textvariable=self.vars_dialog_effect_details)
		details_label.grid(row=0, column=0, sticky="w")		
		self.dialog_effect_details_frame.bindtags("LdP_effect_dialog_details")		
		details_label.bind("<MouseWheel>", self.Scroll_Effect_Dialog_Box_Details_Frame)	

		tkinter.Label(myframe_inner, width="16", anchor="w", text="").grid(row=8, column=0, sticky="w")
		
		tkinter.Label(myframe_inner, width="16", anchor="w", bg="lightgray", text="Effect Scaling").grid(row=9, column=0, sticky="w", pady=1)		
		self.dialog_effect_scaling_frame = Pmw.ScrolledFrame(myframe_inner, usehullsize = 1, hull_width = 365, hull_height = 50)
		self.dialog_effect_scaling_frame.component("borderframe").config(borderwidth=0)
		self.dialog_effect_scaling_frame.configure(hscrollmode = "none", vscrollmode = "static")			
		self.dialog_effect_scaling_frame.bindtags("LdP_effect_dialog_scaling")				
		self.dialog_effect_scaling_frame.grid(row=10, column=0, sticky="w", pady=1, columnspan=4)		
				
		return dialog
			
	# Clicking the Add Gear button or the Edit button in a effect row will call this method
	# This shows a Gear dialog box
	def Effects_Add_Edit_Button_Onclick(self, location):
		self.dialog_effect_add_order_menu.grid_remove()
		self.dialog_effect_edit_order_menu.grid_remove()
		for scale in self.effects_dialog_scaling_rows:
			scale.row.grid_remove()
		self.effects_dialog_scaling_rows = []

		# Location is set to a number if an Edit button is clicked.
		# It refers to it's location in the build list. 
		# If location isn't set, show the Add version of the dialog box
		# otherwise, show the Edit version	
		if( location == "" ):
			self.vars_dialog_effect_type.set("Minor Spiritual (100s)")
			self.Effects_Dialog_Box_Type_Onchange("Minor Spiritual (100s)")
			self.Effects_Dialog_Box_Name_Onchange("Spirit Warding I (101)")
			
			self.vars_dialog_order.set(self.effects_menu_size)	
			self.dialog_effect_add_order_menu.grid(row=0, column=1, sticky="w")		
			
			# If the last time we used the dialog box was as an edit box, change the buttons to the add version
			if self.effect_dialog_box.component("buttonbox").button(0)["text"] == "Update Effect":
				self.effect_dialog_box.component("buttonbox").delete("Update Effect")
				self.effect_dialog_box.component("buttonbox").delete("Remove Effect")		
				self.effect_dialog_box.component("buttonbox").insert("Add Effect", command=lambda v="Add Effect": self.Effects_Dialog_Box_Onclick(v))	
		else:
			effect = globals.character.loadout_effects_build_list[location]
			self.vars_dialog_effect_type.set(effect.type.get())
			self.Effects_Dialog_Box_Type_Onchange(effect.type.get())
			self.Effects_Dialog_Box_Name_Onchange(effect.name.get())
			self.vars_dialog_order.set(location+1)				
			self.vars_dialog_edit_location.set(int(location))
			self.dialog_effect_edit_order_menu.grid(row=0, column=1, sticky="w")		
				
			i = 0
			for _, value in effect.scaling_arr.items():
				if value == "D":
					self.effects_dialog_scaling_rows[i].dynamic_scaling.set(1)
					self.effects_dialog_scaling_rows[i].static_value.set(0)
				else:
					self.effects_dialog_scaling_rows[i].static_value.set(value)
				i += 1					
					
			# If the last time we used the dialog box was as an add box, change the buttons to the edit version
			if self.effect_dialog_box.component("buttonbox").button(0)["text"] == "Add Effect":
				self.effect_dialog_box.component("buttonbox").delete("Add Effect")
				self.effect_dialog_box.component("buttonbox").insert("Remove Effect", command=lambda v="Remove Effect": self.Effects_Dialog_Box_Onclick(v))	
				self.effect_dialog_box.component("buttonbox").insert("Update Effect", command=lambda v="Update Effect": self.Effects_Dialog_Box_Onclick(v))				
		
		
		self.dialog_effect_display_type = ""
		self.effect_dialog_box.show()
		self.effect_dialog_box.grab_set()		
		

	# Empties the effects build list and removes all the LdP rows from the build frame			
	def Effects_ClearAll_Button_Onclick(self):
		for row in globals.character.loadout_effects_build_list:
			row.LdP_Build_Row.grid_remove()			
			if row.ProgP_Build_Row != "":
				row.ProgP_Build_Row.grid_remove()
			
		# Fun fact, if you try to do delete(1, end)	on an option menue that only has 1 object in it, it throws a python error. So this check is needed.
		if self.effects_menu_size > 1:
			self.dialog_effect_add_order_menu['menu'].delete(1, "end")
#			menu = [1]
#			self.dialog_effect_edit_order_menu.set_menu(1, *menu)
			self.dialog_effect_edit_order_menu['menu'].delete(0, "end")
			self.effects_menu_size = 1

			
		# A change is being made to the effects list. Set the global value to 1 so the Progression Panel knows to reset the loadout list
		globals.LdP_Effects_List_Updated = 1
		globals.character.loadout_effects_build_list = []			
		self.Effects_List_Frame.yview("moveto", 0, "units")
		
		

	# When a new effect name is picked from the effect dialog menu, this method is called
	def Effects_Dialog_Box_Type_Onchange(self, result):
		type = globals.LdP_effect_display_types[result]
		self.dialog_effect_names = []
		
		# Search the sql table for the name of the new effect
		globals.db_cur.execute("SELECT name FROM Effects WHERE type = '%s' " % (type))
		globals.db_con.commit()		
		data = globals.db_cur.fetchall()		
		new_choices = [item[0] for item in data]	
				
		self.dialog_effect_names_menu['menu'].delete(0, "end")
		for choice in new_choices:
			self.dialog_effect_names_menu['menu'].add_command(label=choice, command=lambda v=choice: self.Effects_Dialog_Box_Name_Onchange(v))
		self.vars_dialog_effect_name.set(new_choices[0])
		
		self.Effects_Dialog_Box_Name_Onchange(new_choices[0])		
		
		
	# When a new effect name is picked from the gear dialog menu, this method is called
	def Effects_Dialog_Box_Name_Onchange(self, result):			
		globals.db_cur.execute("SELECT type, details, effect_tags, scaling_tags, function, override_options FROM Effects WHERE name = \"%s\" " % (result))
		globals.db_con.commit()		
		data = globals.db_cur.fetchone()
		
		# Remove all the scaling rows
		for scale in self.effects_dialog_scaling_rows:
			scale.row.grid_remove()
		self.effects_dialog_scaling_rows = []
		self.vars_dialog_effect_name.set(result)
		self.vars_dialog_effect_display_type.set(data["type"])
		self.vars_dialog_effect_details.set(data["details"])
		self.vars_dialog_effect_effect_tags = data["effect_tags"]
		self.vars_dialog_effect_function = data["function"]
		self.vars_dialog_effect_overrides = data["override_options"]		
		
		i = 0
		# If the effect has scaling, create Effect dialog rows for each one
		if( data["scaling_tags"] != 'NONE'):
			parts = data["scaling_tags"].split("|")
			for part in parts:			
				pieces = part.split(":")
				effect = Effect_Dialog_Scaling_Row(self.dialog_effect_scaling_frame.interior(), pieces[0], pieces[1])
				effect.row.grid(row=i, column=0, sticky="w")
				self.effects_dialog_scaling_rows.append(effect)
				i += 1		
	


	# This handles button all the button events that occur in the Add/Edit effect dialog box.	
	# This will add, update, or remove a effect object from the effect build list
	def Effects_Dialog_Box_Onclick(self, result):
		i = 0

		# Occurs if the user clicks the Cancel button or the "x" in the upper right corner. Just close the box and don't do anything.
		if result is None or result == "Cancel":
			self.effect_dialog_box.withdraw()
			self.effect_dialog_box.grab_release()
			return
		
		# A change is being made to the effects list. Set the global value to 1 so the Progression Panel knows to reset the loadout list
		globals.LdP_Effects_List_Updated = 1
		
		# Create a new Effect using the parameters from the Effect dialog box 
		if result == "Add Effect":		
			self.effects_menu_size = self.effects_menu_size + 1
			order = int(self.vars_dialog_order.get())-1
			scaling_arr = collections.OrderedDict()
			
			# Get all the values from scaling rows and create an array to send to the new Effect object
			for row in self.effects_dialog_scaling_rows:
				display_name = globals.LdP_effect_display_scaling[row.scaling_name.get()]
				
				if row.dynamic_scaling.get() == "1":
					value = "D"
				elif len(row.static_value.get()) == 0:
					value = row.min_value
				else:
					value = row.static_value.get()
								
				scaling_arr[display_name] = value
				
				
			# Create a new effect				
			globals.character.loadout_effects_build_list.insert(order, globals.Effect(order, self.vars_dialog_effect_name.get(), self.vars_dialog_effect_type.get(), self.vars_dialog_effect_display_type.get(), self.vars_dialog_effect_details.get(), self.vars_dialog_effect_effect_tags, scaling_arr, self.vars_dialog_effect_function, self.vars_dialog_effect_overrides, 0 ) )
						
			globals.character.loadout_effects_build_list[order].Create_LdP_row(self.Effects_List_Frame.interior())						
			globals.character.loadout_effects_build_list[order].LdP_Edit_Button.config(command=lambda v=int(self.vars_dialog_order.get())-1: self.Effects_Add_Edit_Button_Onclick(v))			
			# Update the list size			
			if self.effects_menu_size > 1:
				self.dialog_effect_edit_order_menu["menu"].insert_command("end", label=self.effects_menu_size-1, command=lambda v=self.effects_menu_size-1: self.vars_dialog_order.set(v))	
			self.dialog_effect_add_order_menu["menu"].insert_command("end", label=self.effects_menu_size, command=lambda v=self.effects_menu_size: self.vars_dialog_order.set(v))	
						
			for effect in globals.character.loadout_effects_build_list:
				effect.order.set(i+1)
				effect.LdP_Edit_Button.config(command=lambda v=i: self.Effects_Add_Edit_Button_Onclick(v))
				effect.LdP_Build_Row.grid(row=i, column=0)			
				i += 1			
			self.effect_dialog_box.withdraw()	
			self.effect_dialog_box.grab_release()	
		
		# Updates an existing Effect. 
		# The new information for the Effect is take from the Dialog box
		elif result == "Update Effect":
			effect = globals.character.loadout_effects_build_list.pop(self.vars_dialog_edit_location.get())
			effect.scaling_arr.clear()
			
			# Get all the values from scaling rows and create an array to send to the new Effect object
			for row in self.effects_dialog_scaling_rows:
				display_name = globals.LdP_effect_display_scaling[row.scaling_name.get()]
				
				if row.dynamic_scaling.get() == "1":
					value = "D"
				elif len(row.static_value.get()) == 0:
					value = row.min_value
				else:
					value = row.static_value.get()
					
				effect.scaling_arr[display_name] = value
				
				
			scaling = ""		
			if len(effect.scaling_arr) == 0:
				scaling = "NONE"
			else:
				for key, value in effect.scaling_arr.items():
					scaling += "%s: %s\n" % (key, value)
				scaling = scaling[:-1]	
				
			# Update the effect	
			effect.name.set(self.vars_dialog_effect_name.get())
			effect.type.set(self.vars_dialog_effect_type.get())
			effect.display_type.set(self.vars_dialog_effect_display_type.get())
			effect.order.set(self.vars_dialog_order.get())
			effect.scaling.set(self.vars_dialog_scaling_tags.get())
			effect.details.set(self.vars_dialog_effect_details.get())
			effect.effect_tags = self.vars_dialog_effect_effect_tags
			effect.options = self.vars_dialog_effect_overrides
			effect.function = self.vars_dialog_effect_function
			effect.scaling.set(scaling)			
			effect.hide.set('0')
			
			effect.Update_Row_Heights()
			
			globals.character.loadout_effects_build_list.insert(int(self.vars_dialog_order.get())-1, effect)
			
			# Update the list order
			for effect in globals.character.loadout_effects_build_list:
				effect.order.set(i+1)
				effect.LdP_Edit_Button.config(command=lambda v=i: self.Effects_Add_Edit_Button_Onclick(v))
				effect.LdP_Build_Row.grid(row=i, column=0)			
				i += 1				
			self.effect_dialog_box.withdraw()	
			self.effect_dialog_box.grab_release()			
		
		# Current selected entry in the gear list is removed, the gear list is updated with the correct entry order, and the build frame is updated to reflect the removal.
		elif result == "Remove Effect":
			effect = globals.character.loadout_effects_build_list.pop(self.vars_dialog_edit_location.get())
			effect.LdP_Build_Row.grid_remove()
			if effect.ProgP_Build_Row != "":
				effect.ProgP_Build_Row.grid_remove()
			self.effects_menu_size -= 1
			if self.effects_menu_size > 0:
				self.dialog_effect_add_order_menu['menu'].delete("end", "end")
			else:
				self.effects_menu_size = 1
			self.dialog_effect_edit_order_menu['menu'].delete("end", "end")		
			for effect in globals.character.loadout_effects_build_list:
				effect.order.set(i+1)
				effect.LdP_Edit_Button.config(command=lambda v=i: self.Effects_Add_Edit_Button_Onclick(v))
				effect.LdP_Build_Row.grid(row=i, column=0)			
				i += 1	
			self.effect_dialog_box.withdraw()	
			self.effect_dialog_box.grab_release()
			
		
	# This allows mouse scrolling in the build frame. Anything with the bind tag SkP_Build will allow the scrolling
	def Scroll_Gear_Build_Frame(self, event):
		self.Gear_List_Frame.yview("scroll", -1*(event.delta/120), "units")
		
		
	# This allows mouse scrolling in the build frame. Anything with the bind tag SkP_Build will allow the scrolling
	def Scroll_Effects_Build_Frame(self, event):
		self.Effects_List_Frame.yview("scroll", -1*(event.delta/120), "units")
		
		
	# This allows mouse scrolling in the build frame. Anything with the bind tag SkP_Build will allow the scrolling
	def Scroll_Effect_Dialog_Box_Details_Frame(self, event):
		self.dialog_effect_details_frame.yview("scroll", -1*(event.delta/120), "units")
		
		
	# This allows mouse scrolling in the build frame. Anything with the bind tag SkP_Build will allow the scrolling
	def Scroll_Effect_Dialog_Box_Scaling_Frame(self, event):
		self.dialog_effect_scaling_frame.yview("scroll", -1*(event.delta/120), "units")		
		
		
# In order to account for a varying and possiblely large amount of ways to scale an effect, the effect dialog box will generate as many 
# Effect_Dialog_Scaling_Row objects as needed to store the information.
# This element will track the name, min value, and max value.
class Effect_Dialog_Scaling_Row:
	def __init__(self, parent, name, min_max_value):		
		self.parent = parent
		self.row = tkinter.Frame(parent)				
		self.scaling_name = tkinter.StringVar()
		self.dynamic_scaling = tkinter.StringVar()
		self.static_value = tkinter.StringVar()
		mycmd = (globals.root.register(self.Entrybox_Validate), '%d', '%S', '%s', '%P')
		
		# Set the values to default
		self.scaling_name.set(name)
		self.static_value.set(0)	
		self.dynamic_scaling.set(0)	
		name_parts = name.split(" ")
		
		# a dash indicates that this scaling row has a specific range. Meaing a min and a max value
		# otherwise it has only a max value and the min value is set to 0
		if "-" in min_max_value:
			values = min_max_value.split("-")
			self.min_value = int(values[0])
			self.max_value = int(values[1])		
		else:
			self.min_value = 0
			self.max_value = int(min_max_value)
		
		# Create the row frame and children		
		self.row.bindtags("LdP_effect_dialog_scaling")	
		E1 = tkinter.Label(self.row, width="30", bg="lightgray", anchor="w", textvar=self.scaling_name)
		E1.grid(row=0, column=0, padx="1", pady="1", sticky="w")
		E1.bindtags("LdP_effect_dialog_scaling")	
		E2 = tkinter.Entry(self.row, width="6", justify="center", validate="key", validatecommand=mycmd, textvariable=self.static_value)
		E2.grid(row=0, column=1, padx="1", pady="1")	
		
		# Determine if the scaling needs a dynamic checkbox. This is done based on it's name. 
		if name != 'Skill ranks' and name != 'Statistic increase' and name_parts[-1] != 'Tier' and name_parts[-1] != 'bonus':
			E3 = tkinter.Label(self.row, width="1",anchor="w", text="or")
			E3.grid(row=0, column=2, padx="1", pady="1")		
			E3.bindtags("LdP_effect_dialog_scaling")	
			E4 = tkinter.Checkbutton(self.row, command="", text="Dynamic", variable=self.dynamic_scaling)
			E4.grid(row=0, column=3, sticky="w")				
			
	# The entry box will only allow a value between the minimum and maximum set for this scaling effect row.
	# This check is strong enought that another check in Effects_Dialog_Box_Onclick is unneed.
	def Entrybox_Validate(self, d, S, s, P):		
		if( d == "1"):
			try:				
				if( float(P) <= self.max_value and float(P) >= self.min_value ):	
					return True
				else:
					return False
			except ValueError:
				return False
		
		return True
	
