# INDEX OF CLASSES AND METHODS

# TODO LIST
# Allow +30 AS for ranged weapons if using a crossbow with the Lying Down or Kneeling effect
# Need clarification on Steely Resolve shield maneuver. Block DS? Is that like Shield Use ranks? Phantom Shield Use ranks?
# Symbol of the Proselyte (340) use a unique CS calculation and needs special code to get it to work



'''
class Progression_Panel
	def __init__(self, panel)
	def Create_Gear_List_Frame(self, panel):
	def Create_Effect_Header_Frame(self, panel):	
	def Create_Effect_List_Frame(self, panel):
	def Create_Graph_Plot_Frame(self, panel):
	def Plot_Graph_Clear(self):	
	def Plot_Graph_Data(self):
	def Graph_Marker_Onclick(self, event):
	def Graph_Option_Category_OnChange(self, choice):
	def Graph_Option_Subcategory_OnChange(self, choice):
	def Gear_List_Populate_Lists(self):
	def Gear_List_Onchange(self, type, gear_name):	
	def Get_Gear_By_Order(self, gear_name):		
	def Effects_List_Populate_List(self):		
	def Effects_Toggle_Button_Onclick(self):
	def Scroll_Effects_Frame(self, event):
	def Scroll_Tooltip_Frame(self, event):
	def Find_Effects_By_Tags(self, effect_tags):	
	def Combine_Effects(self, level, arr, tag, action_type, convert_var, indenting):	
	def Formula_Attack_Strength(self, twc_mode, gear_name, gear_skills_names, main_enchantment, other_enchantment, calc_style):	
	def Formula_Defense_Strength(self, vs_type, main_gear, other_hand_gear, armor_gear, gloves_gear, calc_style):
	def Formula_Casting_Strength(self, display_spell_circles, statistic_names, calc_style):
	def Formula_Target_Defense(self, calc_style):
	
	
class Graph_Data_Line_Container:	
	def __init__(self):			
	def Reset_Graph_Data(self):		
'''


#!/usr/bin/python

import tkinter
import math
import Pmw
import Globals as globals
import Calculations as calculations

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


# The Progression Panel combines the data entered into the Statistics, Misc, Skills, Maneuvers,
# Postcap, and Loadout Panels to display how a character grows in regards to
# various game mechanics such as Attack Strength and Target Defense. The results are presented 
# as a line graph that the user can interact with to display more detailed information.
class Progression_Panel:  
	def __init__(self, panel):		
		self.gear_main_weapon = tkinter.StringVar()
		self.gear_other_hand = tkinter.StringVar()
		self.gear_armor = tkinter.StringVar()
		self.gear_uac_gloves = tkinter.StringVar()
		self.gear_uac_boots = tkinter.StringVar()		
		self.graph_figure = ""
		self.graph_tooltip_frame = ""
		self.graph_tooltip_text = tkinter.StringVar()
		self.graph_option_category = tkinter.StringVar()
		self.graph_option_subcategory = tkinter.StringVar()		
		self.graph_radio_var = tkinter.IntVar()
		self.effects_list_toggle = 0
		
		# These are the default gear options that are always included in the Gear List Frame
		self.base_main_weapon = globals.Gear(0, "Closed Fist", 0, 0, "Brawling", "")
		self.base_main_weapon.gear_traits = {"base_speed": 1, "minimum_speed": 3}		
		self.base_other_hand = globals.Gear(0, "Empty", 0, 0, "None", "")
		self.base_armor = globals.Gear(0, "No Armor", 0, 0, "None", "")
		self.base_armor.dialog_type = "Armor"
		self.base_armor.Set_Gear_Traits("Clothing")
		self.base_uac_gloves = globals.Gear(0, "No Gloves", 0, 0, "None", "")
		self.base_uac_boots = globals.Gear(0, "No Boots", 0, 0, "None", "")	
		
		# Set the default gear to be the default option selected
		self.gear_main_weapon.set(self.base_main_weapon.name.get())
		self.gear_other_hand.set(self.base_other_hand.name.get())
		self.gear_armor.set(self.base_armor.name.get())
		self.gear_uac_gloves.set(self.base_uac_gloves.name.get())
		self.gear_uac_boots.set(self.base_uac_boots.name.get())		
		
#		self.subcategory_list_physical = ["Attack Strength (Main Weapon)", "Attack Strength (Other Hand Weapon)", "Unarmed Attack Factor (UAF)", "Defense Strength (vs Melee)", "Defense Strength (vs Ranged)", "Defense Strength (vs Bolt Spell)", "Roundtime"]	
		self.subcategory_list_physical = ["Attack Strength (Main Weapon)", "Attack Strength (Other Hand Weapon)", "Defense Strength (vs Melee)", "Defense Strength (vs Ranged)", "Defense Strength (vs Bolt Spell)"]			
		self.subcategory_list_magical = [
		"Attack Strength (Spell Aiming)", "Casting Strength (Bard - MnE, Bard)", "Casting Strength (Cleric - MnS, MjS, Cleric)", "Casting Strength (Empath - MnS, MjS, Empath)", 
		"Casting Strength (Monk - MnS, MnM)", "Casting Strength (Paladin - MnS, Paladin)", "Casting Strength (Ranger - MnS, Ranger)", "Casting Strength (Rogue/Warrior - MnS, MnE)", 
#		"Casting Strength (Savant - MnM, MjM, Savant)", 
		"Casting Strength (Sorcerer - MnS, MnE, Sorc)", "Casting Strength (Wizard - MnE, MjE, Wizard)", "Casting Strength (Arcane Circle)", "Target Defense"]		
		self.subcategory_list_skills = ["Armor Use - AAP, Hindrance, Roundtime", "Multi-Opponent Combat - FoF, Mstrike",
		"Arcane Symbols - Modifiers per Sphere", "Arcane Symbols - Max Spell, Spell Duration", "Magic Item Use - Modifiers per Sphere",
		"Magic Item Use - Max Spell, Spell Duration", "First Aid - Herb Roundtime Reduction"]		
		self.subcategory_list_other = ["Spellsong Renewal Time", "Mana Regeneration", "Stamina Regeneration", "Mana Pulse uses per day", "Mana Spellup uses per day", "Spellburst"]
			
		
		# Create each section of the Progression Panel
		self.Gear_List_Frame = self.Create_Gear_List_Frame(panel)
		self.Effect_Header_Frame = self.Create_Effect_Header_Frame(panel)
		self.Effect_List_Frame = self.Create_Effect_List_Frame(panel)		
		self.Graph_Plot_Frame = self.Create_Graph_Plot_Frame(panel)

		
		# Make the frames visible
		self.Gear_List_Frame.grid(row=1, column=0, sticky="nw")
		self.Effect_Header_Frame.grid(row=2, column=0, sticky="nw")
		self.Effect_List_Frame.grid(row=3, column=0, sticky="nw")		
		self.Graph_Plot_Frame.grid(row=0, column=1, rowspan=4, sticky="nw")		
		
		
		# Initialize defaults
		self.graph_information = Graph_Data_Line_Container()
		self.graph_radio_var.set(1)		
		self.graph_option_category.set("Physical Combat")
		self.Graph_Option_Category_OnChange("Physical Combat")
		self.Effect_List_Frame.bind_class("ProgP_effects", "<MouseWheel>", self.Scroll_Effects_Frame)
		self.graph_tooltip_frame.bind_class("ProgP_tooltip", "<MouseWheel>", self.Scroll_Tooltip_Frame)
		self.Plot_Graph_Clear()
		
		
	# Creates the frame that holds the equipped gear used by the character. These lists are populated by the Gear_List_Populate_Lists method	
	def Create_Gear_List_Frame(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 369, hull_height = 200)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")	
		myframe_inner = myframe.interior()
		
		tkinter.Label(myframe_inner, width="13", anchor="w", bg="lightgray", text="Main Weapon").grid(row=0, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="13", anchor="w", bg="lightgray", text="Other Hand").grid(row=1, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="13", anchor="w", bg="lightgray", text="Armor").grid(row=2, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="13", anchor="w", bg="lightgray", text="UAC Gloves").grid(row=3, column=0, sticky="w")
		tkinter.Label(myframe_inner, width="13", anchor="w", bg="lightgray", text="UAC Boots").grid(row=4, column=0, sticky="w")
		
		self.gear_main_weapon_menu = tkinter.OptionMenu(myframe_inner, self.gear_main_weapon, self.gear_main_weapon.get() )
		self.gear_main_weapon_menu.config(width=33, heigh=1)	
		self.gear_other_hand_menu = tkinter.OptionMenu(myframe_inner, self.gear_other_hand, self.gear_other_hand.get() )
		self.gear_other_hand_menu.config(width=33, heigh=1)	
		self.gear_armor_menu = tkinter.OptionMenu(myframe_inner, self.gear_armor, self.gear_armor.get() )
		self.gear_armor_menu.config(width=33, heigh=1)	
		self.gear_uac_gloves_menu = tkinter.OptionMenu(myframe_inner, self.gear_uac_gloves, self.gear_uac_gloves.get() )
		self.gear_uac_gloves_menu.config(width=33, heigh=1)	
		self.gear_uac_boots_menu = tkinter.OptionMenu(myframe_inner, self.gear_uac_boots, self.gear_uac_boots.get() )
		self.gear_uac_boots_menu.config(width=33, heigh=1)	
		
		# Make the frames visible
		self.gear_main_weapon_menu.grid(row=0, column=1, sticky="w")	
		self.gear_other_hand_menu.grid(row=1, column=1, sticky="w")	
		self.gear_armor_menu.grid(row=2, column=1, sticky="w")	
		self.gear_uac_gloves_menu.grid(row=3, column=1, sticky="w")	
		self.gear_uac_boots_menu.grid(row=4, column=1, sticky="w")	
				
		return myframe

	
	# Creates a frame to hold the column titles for the Effects List Frame. This is done to allow scrolling, without losing the titles.
	def Create_Effect_Header_Frame(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 369, hull_height = 53)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")	
		myframe_inner = myframe.interior()
		
		
		# top frame holds the 3 buttons
		topframe = tkinter.Frame(myframe_inner)		
		topframe.grid(row=1, column=0, sticky="w")			
		tkinter.Button(topframe, text="Toggle All Effects", command=self.Effects_Toggle_Button_Onclick).grid(row=0, column=0, sticky="w", pady="1")	
		
		# this is frame will hold the title of the build schedule frame. This is done to allow the other frame to scroll but not lose the title header
		title_scrollframe = Pmw.ScrolledFrame(myframe_inner, usehullsize = 1, hull_width = 348, hull_height = 26 )		
		title_scrollframe.configure(hscrollmode = "none")		
		title_scrollframe.grid(row=3, column=0, sticky="w")		
		title_scrollframe_inner = title_scrollframe.interior()						
		
		# add all labels to the tittle header
		tkinter.Frame(title_scrollframe_inner).grid(row=3, column=0, columnspan=3)	
		tkinter.Label(title_scrollframe_inner, width="3", bg="lightgray", text="Hide").grid(row=0, column=0, padx="1")
		tkinter.Label(title_scrollframe_inner, width="15", bg="lightgray", text="Effect Name").grid(row=0, column=2, padx="1")
		tkinter.Label(title_scrollframe_inner, width="8", bg="lightgray", text="Type").grid(row=0, column=3, padx="1")
		tkinter.Label(title_scrollframe_inner, width="20", bg="lightgray", text="Effect Scaling").grid(row=0, column=4, padx="1")		
		
		return myframe

		
	# Frame dedicated to holding the effects the character is using. The effects are supplied by the Loadout Panel.
	# Displays: Hide, Effect Name, Scaling
	def Create_Effect_List_Frame(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 369, hull_height = 290)
		myframe.configure(hscrollmode = "none", vscrollmode = "static")	
		myframe_inner = myframe.interior()
		
		return myframe
		

	# This method creates 3 important frames:
	# - tkinter drawing area. Composed of Figure and a single plot that displays data in a table in line format.
	# - option frame below the drawing area. The options determine what data will be display on the data plot.
	# - tooltip frame to the right of the options frame. Clicking the graph after ploting data will display
	#    a message in the tooltip frame that breaks down how the data for a specific level/postcap experience 
	#    interval was calculated.
	def Create_Graph_Plot_Frame(self, panel):
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 731, hull_height = 543)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")	
		myframe_inner = myframe.interior()
		
#		plt.ion()
		# Creates the figure and plot contained in the canvas that data can be plotted on
		self.graph_figure = Figure(figsize=(7.25, 3.80), dpi=100, tight_layout={'pad':3})
		a = self.graph_figure.add_subplot(111)
			
		# a tk.DrawingArea
		canvas = FigureCanvasTkAgg(self.graph_figure, master=myframe_inner)
		canvas.show()
		canvas.get_tk_widget().grid(row=0, column=0, columnspan=2, sticky="nw")
		
		# Creates the toolbar for the figure. At this time, the toolbar is the default one used Matplotlib. In the future, I might customize this
		toolbar_frame = tkinter.Frame(myframe_inner)
		toolbar_frame.grid(row=1, column=0, sticky="nw")
		toolbar = NavigationToolbar2TkAgg(canvas, toolbar_frame)
		toolbar.update()
		

		# The lower frame where the type of plot data can be specified
		options_frame = tkinter.Frame(myframe_inner, width=10)

		tkinter.Label(options_frame, width="13", anchor="w", bg="lightgray", text="Category").grid(row=0, column=0, sticky="w")
		tkinter.Label(options_frame, width="13", anchor="w", bg="lightgray", text="Subcategory").grid(row=1, column=0, sticky="w")
		
#		choices = ["Physical Combat", "Magical Combat", "Skills Calculations", "Other Calculations"]
		choices = ["Physical Combat", "Magical Combat"]		
		self.graph_option_category_menu = tkinter.OptionMenu(options_frame, self.graph_option_category, *choices, command=self.Graph_Option_Category_OnChange)
		self.graph_option_category_menu.config(width=40, heigh=1)				
		self.graph_option_subcategory_menu = tkinter.OptionMenu(options_frame, self.graph_option_subcategory, "", command=self.Graph_Option_Subcategory_OnChange)
		self.graph_option_subcategory_menu.config(width=40, heigh=1)			
		tkinter.Radiobutton(options_frame, anchor="w", text="Pre-Cap", command="", var=self.graph_radio_var, value=1).grid(row=2, column=0, sticky="w", pady="1")
		tkinter.Radiobutton(options_frame, anchor="w", text="Post-Cap", command="", var=self.graph_radio_var, value=2).grid(row=2, column=1, sticky="w", pady="1")			
		tkinter.Button(options_frame, text="Generate Graph", command=self.Plot_Graph_Data).grid(row=3, column=0, sticky="w", pady="1")	
		
		self.graph_option_category_menu.grid(row=0, column=1, sticky="w")	
		self.graph_option_subcategory_menu.grid(row=1, column=1, sticky="w")		
		options_frame.grid(row=2, column=0, sticky="nw")

		# Tooltip frame				
		self.graph_tooltip_frame = Pmw.ScrolledFrame(myframe_inner, usehullsize = 1, hull_width = 345, hull_height = 158)
		self.graph_tooltip_frame.configure(hscrollmode = "none", vscrollmode = "static")		
		self.graph_tooltip_frame.bindtags("ProgP_tooltip")
		tooltip_label = tkinter.Label(self.graph_tooltip_frame.interior(), justify="left", anchor="nw", width=100, wraplength=310, textvariable=self.graph_tooltip_text)	
		tooltip_label.bindtags("ProgP_tooltip")
		
		tooltip_label.grid(row=0, column=0, sticky="nw", padx="1") 
		self.graph_tooltip_frame.grid(row=1, column=1, sticky="nw", rowspan=2)					
		
		return myframe		
		
	
	# Clears the graph figure of whatever data was shown. Used to "reset" the figure after 
	def Plot_Graph_Clear(self):		
		self.graph_information.Reset_Graph_Data()
	
		a = self.graph_figure.axes[0]
		a.cla()		
		a.grid()   						 # This isn't a tkinter grid, this makes it SHOW a grid format on the graph figure
		a.set_picker(True)
		
		# major ticks every 10, minor ticks every 1                                      
		major_ticks = np.arange(0, 101, 10)                                              
		minor_ticks = np.arange(0, 101, 1)       
		
		a.set_xlabel("Level Axis")
		a.set_ylabel("Value Axis")
		
		self.graph_figure.canvas.show()
		self.graph_tooltip_text.set("")
	
	
	# This method is used to plot data depending on the options selected by the user.
	# The choice option determines which formula is called. This formula will populated
	# the graph_information object which is used as the data for the figure's plot
	def Plot_Graph_Data(self):		

		# Reset the graphing data 
		self.graph_information.Reset_Graph_Data()
		self.graph_tooltip_text.set("Click the data points on the graph for more information.")
		
		a = self.graph_figure.axes[0]
		a.cla()		
		a.grid()   						 # This isn't a tkinter grid, this makes it SHOW a grid format
		a.set_picker(True)
		
		# Yes, this DOES need to be done everytime data is plotted. Changing the graphed information, removes the button press event
		self.graph_figure.canvas.mpl_connect('button_press_event', self.Graph_Marker_Onclick)			
					
		choice = self.graph_option_subcategory.get()
		
		if choice == "Attack Strength (Main Weapon)":	
			main_gear = self.Get_Gear_By_Order(self.gear_main_weapon.get())
			other_gear = self.Get_Gear_By_Order(self.gear_other_hand.get())
			ammo_enchantment = 0
			if main_gear.skills == "Ranged Weapons" and other_gear.name.get() == "Arrows/Bolts":
				ammo_enchantment = int(other_gear.enchantment)
			
			self.Formula_Attack_Strength(0, main_gear, ammo_enchantment, self.graph_radio_var.get())
				
		elif choice == "Attack Strength (Other Hand Weapon)":		
			other_gear = self.Get_Gear_By_Order(self.gear_other_hand.get())
			name = other_gear.name.get() 
			
			# Invalid off-hand gear, abort ploting
			if name == "Empty" or name == "Small Shield" or name == "Medium Shield" or name == "Large Shield" or name == "Tower Shield":
				self.Plot_Graph_Clear()
				return
			
			self.Formula_Attack_Strength(1, other_gear, 0, self.graph_radio_var.get())		
				
		elif choice == "Attack Strength (Spell Aiming)":	
			dummy_gear = globals.Gear(0, "Bolt Spell", 0, 0, "Spell Aiming", "")
			self.Formula_Attack_Strength(0, dummy_gear, 0, self.graph_radio_var.get())
				
		elif choice == "Defense Strength (vs Melee)":	
			gear = self.Get_Gear_By_Order(self.gear_main_weapon.get())
			other = self.Get_Gear_By_Order(self.gear_other_hand.get())
			armor = self.Get_Gear_By_Order(self.gear_armor.get())
			gloves = self.Get_Gear_By_Order(self.gear_uac_gloves.get())
			
			self.Formula_Defense_Strength("Melee", gear, other, armor, gloves, self.graph_radio_var.get())
				
		elif choice == "Defense Strength (vs Ranged)":	
			gear = self.Get_Gear_By_Order(self.gear_main_weapon.get())
			other = self.Get_Gear_By_Order(self.gear_other_hand.get())
			armor = self.Get_Gear_By_Order(self.gear_armor.get())
			gloves = self.Get_Gear_By_Order(self.gear_uac_gloves.get())
			
			self.Formula_Defense_Strength("Ranged", gear, other, armor, gloves, self.graph_radio_var.get())
				
		elif choice == "Defense Strength (vs Bolt Spell)":	
			gear = self.Get_Gear_By_Order(self.gear_main_weapon.get())
			other = self.Get_Gear_By_Order(self.gear_other_hand.get())
			armor = self.Get_Gear_By_Order(self.gear_armor.get())
			gloves = self.Get_Gear_By_Order(self.gear_uac_gloves.get())
			
			self.Formula_Defense_Strength("Bolt", gear, other, armor, gloves, self.graph_radio_var.get())
				
		elif choice == "Casting Strength (Bard - MnE, Bard)":
			spell_circles = ["Minor Elemental", "Bard"]
			statistic_names = ["Aura"]		
				
			self.Formula_Casting_Strength(spell_circles, statistic_names, self.graph_radio_var.get())
				
		elif choice == "Casting Strength (Cleric - MnS, MjS, Cleric)":
			spell_circles = ["Minor Spiritual", "Major Spiritual", "Cleric"]
			statistic_names = ["Wisdom"]	
				
			self.Formula_Casting_Strength(spell_circles, statistic_names, self.graph_radio_var.get())
					
		elif choice == "Casting Strength (Empath - MnS, MjS, Empath)":
			spell_circles = ["Minor Spiritual", "Major Spiritual", "Empath"]
			statistic_names = ["Wisdom"]	
				
			self.Formula_Casting_Strength(spell_circles, statistic_names, self.graph_radio_var.get())
					
		elif choice == "Casting Strength (Monk - MnS, MnM)":
			spell_circles = ["Minor Spiritual", "Minor Mental"]
			statistic_names = ["Logic", "Wisdom"]	
				
			self.Formula_Casting_Strength(spell_circles, statistic_names, self.graph_radio_var.get())
					
		elif choice == "Casting Strength (Paladin - MnS, Paladin)":
			spell_circles = ["Minor Spiritual", "Paladin"]
			statistic_names = ["Wisdom"]	
				
			self.Formula_Casting_Strength(spell_circles, statistic_names, self.graph_radio_var.get())
					
		elif choice == "Casting Strength (Ranger - MnS, Ranger)":
			spell_circles = ["Minor Spiritual", "Ranger"]
			statistic_names = ["Wisdom"]	
				
			self.Formula_Casting_Strength(spell_circles, statistic_names, self.graph_radio_var.get())
					
		elif choice == "Casting Strength (Rogue/Warrior - MnS, MnE)":
			spell_circles = ["Minor Spiritual", "Minor Elemental"]
			statistic_names = ["Aura", "Wisdom"]	
				
			self.Formula_Casting_Strength(spell_circles, statistic_names, self.graph_radio_var.get())
					
		elif choice == "Casting Strength (Savant - MnM, MjM, Savant)":
			spell_circles = ["Minor Mental", "Major Mental", "Savant"]
			statistic_names = ["Discipline", "Influence", "Logic"]			
				
			self.Formula_Casting_Strength(spell_circles, statistic_names, self.graph_radio_var.get())
			
		elif choice == "Casting Strength (Sorcerer - MnS, MnE, Sorc)":
			spell_circles = ["Minor Spiritual", "Minor Elemental", "Sorcerer"]
			statistic_names = ["Aura", "Wisdom"]			
				
			self.Formula_Casting_Strength(spell_circles, statistic_names, self.graph_radio_var.get())
			
		elif choice == "Casting Strength (Wizard - MnE, MjE, Wizard)":
			spell_circles = ["Minor Elemental", "Major Elemental", "Wizard"]
			statistic_names = ["Aura"]			
				
			self.Formula_Casting_Strength(spell_circles, statistic_names, self.graph_radio_var.get())
			
		elif choice == "Casting Strength (Arcane Circle)":
			spell_circles = ["Arcane"]
			statistic_names = ["Aura", "Logic", "Wisdom"]			
				
			self.Formula_Casting_Strength(spell_circles, statistic_names, self.graph_radio_var.get())	
			
				
		elif choice == "Target Defense":
			self.Formula_Target_Defense(self.graph_radio_var.get())						
				
		else:
			print("ERROR!!! Progression choice is not implemented!")
			self.Plot_Graph_Clear()
			return


		
		# Plot the data stored in the graph_information object
		for i in range(self.graph_information.graph_num_lines):
			a.plot(self.graph_information.graph_xaxis_tick_range, self.graph_information.graph_data_lists[i], self.graph_information.graph_legend_styles[i], label=self.graph_information.graph_legend_labels[i])			
		
		# Set up the graph figure's look before showing it
#		a.tick_params(labelsize=8)   													#both x and y
		a.xaxis.set_tick_params(labelsize=self.graph_information.graph_xlabel_size) 	# just x		

		# major ticks every 10, minor ticks every 1                                       
		mtick = math.floor(len(self.graph_information.graph_xaxis_tick_range)/10)
		if mtick == 0:
			mtick = 1
		major_ticks = np.arange(0, len(self.graph_information.graph_xaxis_tick_range), mtick)     				
		minor_ticks = np.arange(0, len(self.graph_information.graph_xaxis_tick_range), 1)                                               

		a.set_xticklabels(self.graph_information.graph_xaxis_tick_labels, rotation=self.graph_information.graph_xaxis_rotation)
		a.set_xticks(major_ticks)                                                       
		a.set_xticks(minor_ticks, minor=True)     			
			
		# Create the graph legend
		handles, labels = a.get_legend_handles_labels()		
		a.legend(handles, labels, ncol=self.graph_information.graph_legend_columns, loc='upper left', prop={'size':9}, bbox_to_anchor=(0, 1.25))
		
		a.set_ylim(self.graph_information.graph_yaxis_min, self.graph_information.graph_yaxis_max)
		a.set_xlabel(self.graph_information.graph_xlabel, fontsize=self.graph_information.graph_xaxis_size)
		a.set_ylabel(self.graph_information.graph_ylabel)
		

		# Finally, show the the graph figure
		self.graph_figure.canvas.show()


	# Clicking any part of the graph will set the tooltip variable and display information in the tooltip frame
	def Graph_Marker_Onclick(self, event):
		if event.xdata == None or len(self.graph_information.tooltip_array) == 0:
			return
			
#		print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' % (event.button, event.x, event.y, event.xdata, event.ydata))
		xloc = int(round(event.xdata))

		if len(self.graph_information.tooltip_array) > xloc:
			self.graph_tooltip_text.set(self.graph_information.tooltip_array[xloc])
		else: 
			self.graph_tooltip_text.set(self.graph_information.tooltip_array[-1])		
		
		self.graph_tooltip_frame.yview("moveto", 0, "units")	
		
	
	# When the user picks a new category, change the subcategory list to reflect the new choice
	def Graph_Option_Category_OnChange(self, choice):
		self.graph_option_subcategory_menu["menu"].insert_command("end", label="buffer")
		self.graph_option_subcategory_menu['menu'].delete(0, "end")
		
		if choice == "Physical Combat":
			self.graph_option_subcategory.set(self.subcategory_list_physical[0])
			for i in self.subcategory_list_physical:				
				self.graph_option_subcategory_menu["menu"].insert_command("end", label=i, command=lambda v=i: self.Graph_Option_Subcategory_OnChange(v))			
		elif choice == "Magical Combat":
			self.graph_option_subcategory.set(self.subcategory_list_magical[0])
			for i in self.subcategory_list_magical:	
				self.graph_option_subcategory_menu["menu"].insert_command("end", label=i, command=lambda v=i: self.Graph_Option_Subcategory_OnChange(v))
		elif choice == "Skills Calculations":
			self.graph_option_subcategory.set(self.subcategory_list_skills[0])
			for i in self.subcategory_list_skills:	
				self.graph_option_subcategory_menu["menu"].insert_command("end", label=i, command=lambda v=i: self.Graph_Option_Subcategory_OnChange(v))
		elif choice == "Other Calculations":
			self.graph_option_subcategory.set(self.subcategory_list_other[0])
			for i in self.subcategory_list_other:	
				self.graph_option_subcategory_menu["menu"].insert_command("end", label=i, command=lambda v=i: self.Graph_Option_Subcategory_OnChange(v))

	
	# Sets the drop menu to display the user's choice
	def Graph_Option_Subcategory_OnChange(self, choice):
		self.graph_option_subcategory.set(choice)
		
		
	def Gear_List_Populate_Lists(self):		
		globals.character.loadout_gear_build_list 
		globals.character.loadout_effects_build_list
		
		# Delete all the existing items from each list. The inserting of the "temp" command prevents delete(0, end) from throwing an error if the list is empty
		self.gear_main_weapon_menu['menu'].insert_command("end", label="temp")
		self.gear_other_hand_menu['menu'].insert_command("end", label="temp")
		self.gear_armor_menu['menu'].insert_command("end", label="temp")
		self.gear_uac_gloves_menu['menu'].insert_command("end", label="temp")
		self.gear_uac_boots_menu['menu'].insert_command("end", label="temp")		
		self.gear_main_weapon_menu['menu'].delete(0, "end")
		self.gear_other_hand_menu['menu'].delete(0, "end")
		self.gear_armor_menu['menu'].delete(0, "end")
		self.gear_uac_gloves_menu['menu'].delete(0, "end")
		self.gear_uac_boots_menu['menu'].delete(0, "end")	
			
		# Insert the default gear items and set them to be the currently equipped gear
		self.gear_main_weapon_menu['menu'].insert_command("end", label=self.base_main_weapon.name.get(), command=lambda v=self.base_main_weapon.name.get(): self.gear_main_weapon.set(v))
		self.gear_other_hand_menu['menu'].insert_command("end", label=self.base_other_hand.name.get(), command=lambda v=self.base_other_hand.name.get(): self.gear_other_hand.set(v))
		self.gear_armor_menu['menu'].insert_command("end", label=self.base_armor.name.get(), command=lambda v=self.base_armor.name.get(): self.gear_armor.set(v))
		self.gear_uac_gloves_menu['menu'].insert_command("end", label=self.base_uac_gloves.name.get(), command=lambda v=self.base_uac_gloves.name.get(): self.gear_uac_gloves.set(v))
		self.gear_uac_boots_menu['menu'].insert_command("end", label=self.base_uac_boots.name.get(), command=lambda v=self.base_uac_boots.name.get(): self.gear_uac_boots.set(v))	
		self.gear_main_weapon.set(self.base_main_weapon.name.get())
		self.gear_other_hand.set(self.base_other_hand.name.get())
		self.gear_armor.set(self.base_armor.name.get())
		self.gear_uac_gloves.set(self.base_uac_gloves.name.get())
		self.gear_uac_boots.set(self.base_uac_boots.name.get())	

		# Go through the loadout gear list and add all the items the appropriate lists
		for gear in globals.character.loadout_gear_build_list:
			type = gear.display_type.get()
			name = gear.ProgP_display_name		
			
			if type == "Armor":
				self.gear_armor_menu['menu'].insert_command("end", label=name, command=lambda v=name: self.Gear_List_Onchange("Armor", v))
			elif type == "Shield":
				self.gear_other_hand_menu['menu'].insert_command("end", label=name, command=lambda v=name: self.Gear_List_Onchange("Other Hand", v))
			elif type == "UAC" and "UAC Gloves" in name:
				self.gear_uac_gloves_menu['menu'].insert_command("end", label=name, command=lambda v=name: self.Gear_List_Onchange("UAC Gloves", v))
			elif type == "UAC" and "UAC Boots" in name: 
				self.gear_uac_boots_menu['menu'].insert_command("end", label=name, command=lambda v=name: self.Gear_List_Onchange("UAC Boots", v))
			elif type == "THW" or type == "Ranged" or type == "OHE/THW" or name == "Whip-blade" or (name != "Trident, One-Handed" and type == "Polearm"):
				self.gear_main_weapon_menu['menu'].insert_command("end", label=name, command=lambda v=name: self.Gear_List_Onchange("Main Weapon", v))
			elif type == "Brawling" or type == "OHE" or type == "OHB" or type == "Thrown" or type == "OHE/BRW" or name == "Trident, One-Handed":
				self.gear_main_weapon_menu['menu'].insert_command("end", label=name, command=lambda v=name: self.Gear_List_Onchange("Main Weapon", v))
				self.gear_other_hand_menu['menu'].insert_command("end", label=name, command=lambda v=name: self.Gear_List_Onchange("Other Hand", v))
				
	
	# When a choice in a gear drop down menu is selected, set it as equipped gear for that menu
	def Gear_List_Onchange(self, type, gear_name):
		if type == "Armor":
			self.gear_armor.set(gear_name)			
		elif type == "UAC Gloves":
			self.gear_uac_gloves.set(gear_name)			
		elif type == "UAC Boots":
			self.gear_uac_boots.set(gear_name)
		elif type == "Main Weapon":
			self.gear_main_weapon.set(gear_name)
			if gear_name != "Closed Fist":
				main_weapon = self.Get_Gear_By_Order(self.gear_main_weapon.get())
				
				if self.gear_other_hand.get() != "Empty":
					other_hand = self.Get_Gear_By_Order(self.gear_other_hand.get())
					display = main_weapon.display_type.get()
					if main_weapon.order.get() == other_hand.order.get() or display == "THW" or (display == "Ranged" and other_hand.name.get() != "Arrows/Bolts") or (main_weapon.ProgP_display_name != "Trident, One-Handed" and display == "Polearm"):
						self.gear_other_hand.set("Empty")						
		elif type == "Other Hand":
			self.gear_other_hand.set(gear_name)		
			if gear_name != "Empty":
				other_hand = self.Get_Gear_By_Order(self.gear_other_hand.get())				
				
				if self.gear_main_weapon.get() != "Closed Fist":
					main_weapon = self.Get_Gear_By_Order(self.gear_main_weapon.get())
					display = main_weapon.display_type.get()
					if main_weapon.order.get() == other_hand.order.get() or display == "THW" or (display == "Ranged" and other_hand.name.get() != "Arrows/Bolts") or (other_hand.ProgP_display_name != "Trident, One-Handed" and display == "Polearm"):
						self.gear_main_weapon.set("Closed Fist")
	
	
	# Gets gear by it's the order number which is it's location in the Loadout Panel's gear list. Default gear items just return themselves
	def Get_Gear_By_Order(self, gear_name):	
		if gear_name == "Closed Fist":
			return self.base_main_weapon
		elif gear_name == "Empty":
			return self.base_other_hand
		elif gear_name == "No Armor":
			return self.base_armor
		elif gear_name == "No Gloves":
			return self.base_uac_gloves
		elif gear_name == "No Boots":
			return self.base_uac_boots
			
		order = int(gear_name.split(".")[0]) - 1		
		return globals.character.loadout_gear_build_list[order]
		
	
	# Goes through the Effects List created by the Loadout Panel and creates (or adds back) the ProP_row of each effect object.
	# Effects must be unique. Only the first effect with a given is used. Duplicates are skipped.
	def Effects_List_Populate_List(self):	
		effects_list = globals.character.loadout_effects_build_list
		added_effect_names = []
		
		i = 0
		for effect in effects_list:
			if effect.name.get() in added_effect_names:
				if effect.ProgP_Build_Row != "":
					effect.ProgP_Build_Row.grid_remove()				
				continue
			
			added_effect_names.append(effect.name.get())
			
			if effect.ProgP_Build_Row == "":
				effect.Create_ProgP_row(self.Effect_List_Frame.interior())
				effect.ProgP_Build_Row.grid(row=i, column=0)
			else:
				effect.ProgP_Build_Row.grid_remove()
				effect.ProgP_Build_Row.grid(row=i, column=0)
				
			i += 1
				
		self.Gear_List_Frame.yview("moveto", 0, "units")
		

	# Toggles the hide buttons of all effects in the Effects List frame
	def Effects_Toggle_Button_Onclick(self):
		self.effects_list_toggle = (self.effects_list_toggle + 1) % 2
		effects_list = globals.character.loadout_effects_build_list
		
		for effect in effects_list:
			effect.hide.set(self.effects_list_toggle)
		

	# This allows mouse scrolling in the build frame. Anything with the bind tag ProgP_Effect will allow the scrolling
	def Scroll_Effects_Frame(self, event):
		self.Effect_List_Frame.yview("scroll", -1*(event.delta/120), "units")				

		
	# This allows mouse scrolling in the build frame. Anything with the bind tag ProgP_Effect will allow the scrolling
	def Scroll_Tooltip_Frame(self, event):
		self.graph_tooltip_frame.yview("scroll", -1*(event.delta/120), "units")				
						
		
	# Part of sorting effects, this method will figure out which effects in the loadout effects list are "active" on the Progression Panel and 
	# add each effect to one or more keys in the dict, matching_arr. The effect_tags list determines what effects we are looking for
	def Find_Effects_By_Tags(self, effect_tags):
		effects_list = globals.character.loadout_effects_build_list		
		matching_arr = {}
		
		for tag in effect_tags:
			matching_arr[tag] = []		
		
		# Ignore effects that are not visible or in the Progression Panel's effects list frame
		for effect in effects_list:
			if effect.hide.get() == "1" or effect.ProgP_Build_Row == "" or (effect.ProgP_Build_Row != "" and len(effect.ProgP_Build_Row.grid_info()) == 0):
				continue
			
			tag_list = effect.effect_tags.split("|")	
			
			for etag in tag_list:
				for tag in effect_tags:
					if etag == tag:
						matching_arr[tag].append(effect)				

		return matching_arr
					
	
	# Given a specific tag to look for, an effects_arr to search through, and an action_type to format the return data:
	# Combine_Effects will get the total bonus for an effect from all the effects in effects_arr. Calculate_Tag_Bonus
	# is called on each effect to execute a specfic internal method to calculate the data. This always returns an list
	# of 2 elements: 1st being the bonus and the 2nd being the type of the bonus
	def Combine_Effects(self, level, effects_arr, tag, action_type, convert_var, indenting):
		temp_arr = []
		temp_value = 0
		sum = 0
		tooltip = ""
		
		if len(effects_arr) > 0:
			for effect in effects_arr:
				temp_arr = effect.Calculate_Tag_Bonus(tag, level)
				if temp_arr[0] == 0:           						# skip effects that give no bonus/penalty
					continue
					
				if action_type == "stat_inc_to_bonus":
					tooltip += "%s%s bonus  (%+d %s)\n" % ( indenting,  ("%+d" % (temp_arr[0]/2)).rjust(4),   temp_arr[0],   temp_arr[1])
					sum += temp_arr[0]/2
				elif action_type == "effect_display":	
					tooltip += "%s%s %s  (%s)\n" % (indenting,  ("%+d" % temp_arr[0]).rjust(4),  temp_arr[1],  effect.name.get())
					sum += temp_arr[0]	
				elif action_type == "skill_bonus_to_ranks":	
					temp_value = calculations.Convert_Bonus_To_New_Ranks(convert_var, temp_arr[0])
					tooltip += "%s%s ranks  (%+d %s)\n" % (indenting,  ("%+d" % temp_value).rjust(4), temp_arr[0], temp_arr[1])
					sum += temp_value	
				elif action_type == "skill_ranks_to_bonus":	
					temp_value = calculations.Convert_Ranks_To_New_Bonus(convert_var, temp_arr[0])
					tooltip += "%s%s bonus  (%d %s)\n" % (indenting,  ("%+d" % temp_value).rjust(4), temp_arr[0], temp_arr[1])
					sum += temp_value				
				elif action_type == "ranks_display":
					tooltip += "%s%s ranks  (%s)\n" % ( indenting,  ("%+d" % temp_arr[0]).rjust(4), temp_arr[1])
					sum += temp_arr[0]					
				elif action_type == "float_format":
					tooltip += "%s%s bonus  (%s)\n" % ( indenting,  ("%+.2f" % temp_arr[0]).rjust(4), temp_arr[1])
					sum += temp_arr[0]				
				else:
					tooltip += "%s%s  bonus  (%s)\n" % ( indenting,  ("%+d" % temp_arr[0]).rjust(4), temp_arr[1])
					sum += temp_arr[0]		
				
		return (sum, tooltip)

	
	# This massive method is used to calculate the Attack Strength (AS) of a character from level 0-100 or across
	# postcap training. It can calculate the AS for any weapon type including weapons that use multiple skills
	# like the Katar. It can also calculate Bolt AS and TWC AS as well. All statistics, skills, and effects that
	# increase skills, statistics, or AS itself are included in this calculation.	
	def Formula_Attack_Strength(self, twc_mode, main_gear, ammo_enchantment, calc_style):	
		index = 0
		loop_range = [i for i in range(101)]
		base_stat_arr = {}
		base_ranks_arr = {}
		base_bonus_arr = {}
		postcap_intervals = []
		lists_of_effects_by_tag = {}		
		
		off_hand_text = ""			
		main_enchantment = int(main_gear.enchantment)
		weapon_types = main_gear.skills.split("/")	
			
		off_stance_totals = []
		adv_stance_totals = []
		for_stance_totals = []
		neu_stance_totals = []
		gua_stance_totals = []
		def_stance_totals = []		
		
		# Setup the lists for what skills and stats are relavent for calculate AS
		if weapon_types[0] == "Spell Aiming":
			effects_list = ["Statistic_Dexterity", "Statistic_Bonus_Dexterity", "AS_All", "AS_Bolt"]	
			statistic_names = ["Dexterity"]
			skill_names = []
			effect_type = "AS_Bolt"
		elif weapon_types[0] == "Ranged Weapons":
			effects_list = ["Statistic_Dexterity", "Statistic_Bonus_Dexterity", "Skill_Bonus_Ambush", "Skill_Ranks_Ambush", "Skill_Bonus_Perception", "Skill_Ranks_Perception", "AS_All", "AS_Ranged"]	
			statistic_names = ["Dexterity"]
			skill_names = ["Ambush", "Perception"]
			effect_type = "AS_Ranged"
		elif weapon_types[0] == "Thrown Weapons":
			effects_list = ["Statistic_Strength", "Statistic_Bonus_Strength", "Statistic_Dexterity", "Statistic_Bonus_Dexterity", "Skill_Bonus_Perception", "Skill_Ranks_Perception", "Skill_Phantom_Ranks_Combat_Maneuvers", "Skill_Bonus_Combat_Maneuvers", "Skill_Ranks_Combat_Maneuvers", "AS_All", "AS_Ranged"]	
			statistic_names = ["Dexterity", "Strength"]
			skill_names = ["Combat Maneuvers", "Perception"]
			effect_type = "AS_Ranged"
		else:				
			effects_list = ["Statistic_Strength", "Statistic_Bonus_Strength", "Skill_Phantom_Ranks_Combat_Maneuvers", "Skill_Bonus_Combat_Maneuvers", "Skill_Ranks_Combat_Maneuvers", "AS_All", "AS_Melee"]	
			statistic_names = ["Strength"]
			skill_names = ["Combat Maneuvers"]
			effect_type = "AS_Melee"
		
		# TWC is considered an extra step in the calculation process and needs to add extra skills and effects to calculate it 
		if twc_mode == 1:
			off_hand_text = "Off-hand "
			skill_names.append("Two Weapon Combat")
			effects_list.extend(("Skill_Bonus_Two_Weapon_Combat", "Skill_Ranks_Two_Weapon_Combat"))
			if "Dexterity" not in statistic_names:
				statistic_names.append("Dexterity")
				effects_list.extend(("Statistic_Dexterity", "Statistic_Bonus_Dexterity"))
		
					
		# This is a quicker way to add weapon skill effects to the effects list
		for skill in weapon_types:
			skill_names.append(skill)
			effects_list.append("Skill_Ranks_%s" % skill.replace(" ", "_").replace("-", "_").replace(",", ""))
			effects_list.append("Skill_Bonus_%s" % skill.replace(" ", "_").replace("-", "_").replace(",", ""))
			
		lists_of_effects_by_tag = self.Find_Effects_By_Tags(effects_list)				
		
		# In Postcap mode, loop_range is not 0-100, instead its whatever postcap intervals that have training in the relevant skills
		if calc_style == 2:
			interval = 7575000
			for interval, training in globals.character.postcap_skill_training_by_interval.items():
				for skill in skill_names:
					if skill in training:
						postcap_intervals.append(interval)
						break										
							
			# If no intervals are found, add one so we have at least 2 points to plot		
			if len(postcap_intervals) == 0:
				postcap_intervals.append(7572500)
				postcap_intervals.append(interval)
			elif postcap_intervals[0] != 7572500:
				postcap_intervals.insert(0, 7572500)			
			
			if postcap_intervals[-1] != interval:
				postcap_intervals.append(interval)		
							
			loop_range = postcap_intervals
					
		# Begin the big loop to calculate all the data		
		for i in loop_range:
			skill_phantom = 0
			skill_inc_ranks = 0
			skill_inc_bonus = 0		
			skill_rank_count = 0
			effects_total = 0
			combined_weapons_bonus = 0
			combined_statistic_bonus = 0
			
			weapon_enhancive_totals = []
			stat_enhancive_totals = []
			
			stat_tooltip_text = ""
			skill_phantom_tooltip = ""
			skill_tooltip = ""
			weapon_tooltip_text = ""
			effects_tooltip_text = ""
			weapon_tooltip_arr = []
			
			# Get the base ranks and bonus for each relevant statistic and skill for this level/interval
			if calc_style == 1:
				tooltip = "Level %s: %sAttack Strength with %s\n" % (i, off_hand_text, main_gear.skills)
				for stat in statistic_names:				
					base_stat_arr[stat] = globals.character.statistics_list[stat].bonuses_by_level[i].get()	
				
				for skill in skill_names:
					base_ranks_arr[skill] = globals.character.skills_list[skill].total_ranks_by_level[i].get()
					base_bonus_arr[skill] = globals.character.skills_list[skill].bonus_by_level[i].get()		
					
			elif calc_style == 2:	
				tooltip = "Postcap Experience Interval %s: %sAttack Strength with %s\n" % ("{:,}".format(i), off_hand_text, main_gear.skills)
				for stat in statistic_names:				
					base_stat_arr[stat] = globals.character.statistics_list[stat].bonuses_by_level[100].get()	
				
				for skill in skill_names:
					base_ranks_arr[skill] = globals.character.skills_list[skill].total_ranks_by_level[100].get()
					base_bonus_arr[skill] = globals.character.skills_list[skill].bonus_by_level[100].get()
					
					base_ranks_arr[skill] += globals.character.skills_list[skill].Postcap_Get_Total_Ranks_Closest_To_Interval(i)
					base_bonus_arr[skill] += globals.character.skills_list[skill].Postcap_Get_Bonus_Closest_To_Interval(i)	
		

			# Calculate Statistic bonus	
			# TWC has a different way of calculating than the rest of the weapons
			if twc_mode == 1:		
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Statistic_Bonus_Dexterity"], "Statistic_Bonus_Dexterity", "", 0, "            ")
				stat_enh_bonus = ce_total
				stat_tooltip_text = ce_tooltip + stat_tooltip_text
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Statistic_Dexterity"], "Statistic_Dexterity", "stat_inc_to_bonus", 0, "            ")
				stat_enh_bonus += ce_total
				stat_tooltip_text = ce_tooltip + stat_tooltip_text						
				
				if stat_enh_bonus > 0:
					stat_tooltip_text = "       %s  enhancive Dexterity bonus (%s vs max +20)\n" % (("%+d" % min(20, stat_enh_bonus)).rjust(4), "%+d" % (stat_enh_bonus)) + stat_tooltip_text
				stat_tooltip_text = "       %s  Dexterity base bonus\n" % (("%+d" % base_stat_arr["Dexterity"]).rjust(4)) + stat_tooltip_text		
				
				combined_dexterity_bonus = base_stat_arr["Dexterity"] + min(50, stat_enh_bonus)		
				

				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Statistic_Bonus_Strength"], "Statistic_Bonus_Strength", "", 0, "            ")
				stat_enh_bonus = ce_total
				stat_tooltip_text = ce_tooltip + stat_tooltip_text
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Statistic_Strength"], "Statistic_Strength", "stat_inc_to_bonus", 0, "            ")
				stat_enh_bonus += ce_total
				stat_tooltip_text = ce_tooltip + stat_tooltip_text						
				
				if stat_enh_bonus > 0:
					stat_tooltip_text = "       %s  enhancive Strength bonus (%s vs max +20)\n" % (("%+d" % min(20, stat_enh_bonus)).rjust(4), "%+d" % (stat_enh_bonus)) + stat_tooltip_text
				stat_tooltip_text = "       %s  Strength base bonus\n" % (("%+d" % base_stat_arr["Strength"]).rjust(4)) + stat_tooltip_text		
				
				combined_strength_bonus = base_stat_arr["Strength"] + min(50, stat_enh_bonus)				

				
				stat_tooltip_text = "  %s  Statistic bonus: min(Strength %+d vs Dexterity %+d)\n" % (("%+d" % min(combined_strength_bonus, combined_dexterity_bonus)).rjust(4), combined_strength_bonus, combined_dexterity_bonus) + stat_tooltip_text	
			# Statistic calculations for every other weapon style	
			else:
				for stat in statistic_names:
					ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Statistic_Bonus_%s" % stat], "Statistic_Bonus_%s" % stat, "", 0, "            ")
					stat_enh_bonus = ce_total
					stat_tooltip_text = ce_tooltip + stat_tooltip_text
					
					ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Statistic_%s" % stat], "Statistic_%s" % stat, "stat_inc_to_bonus", 0, "            ")
					stat_enh_bonus += ce_total
					stat_tooltip_text = ce_tooltip + stat_tooltip_text				
					
					stat_enhancive_totals.append(base_stat_arr[stat] + min(50, stat_enh_bonus) )				
					
					if stat_enh_bonus > 0:
						stat_tooltip_text = "       %s  enhancive %s bonus (%s vs max +20)\n" % (("%+d" % min(20, stat_enh_bonus)).rjust(4), stat, "%+d" % (stat_enh_bonus)) + stat_tooltip_text
					stat_tooltip_text = "       %s  %s base bonus\n" % (("%+d" % base_stat_arr[stat]).rjust(4), stat) + stat_tooltip_text		
					
					combined_statistic_bonus += base_stat_arr[stat] + min(50, stat_enh_bonus)
								
				combined_statistic_bonus /= len(statistic_names)							

								
				if len(statistic_names) > 1:	
					mutli_tooltip = ""
					for j in range(len(statistic_names)):
						mutli_tooltip = " %s (%s)," % (statistic_names[j], "%+d" % stat_enhancive_totals[j]) + mutli_tooltip
					stat_tooltip_text = "  %s  Statistic bonus avg: %s\n" % (("%+d" % combined_statistic_bonus).rjust(4), mutli_tooltip[:-1]) + stat_tooltip_text
				else:						
					stat_tooltip_text = "  %s  %s bonus\n" % (("%+d" % combined_statistic_bonus).rjust(4), statistic_names[0]) + stat_tooltip_text
			
			if weapon_types[0] == "Spell Aiming":
				pass       # Yes, do nothing. Need to do this because the "else" below to calculate every other style aside from Ranged Weapons and Thrown Weapons
				
			elif weapon_types[0] == "Ranged Weapons":
				# Calculate Perception ranks
				skill_rank_count = base_ranks_arr["Perception"]			
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Bonus_Perception"], "Skill_Bonus_Perception", "skill_bonus_to_ranks", skill_rank_count, "            ")
				skill_inc_bonus += ce_total
				skill_tooltip = ce_tooltip + skill_tooltip
				skill_rank_count += ce_total			
						
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Ranks_Perception"], "Skill_Ranks_Perception", "ranks_display", skill_rank_count, "            ")
				skill_inc_ranks = ce_total
				skill_tooltip = ce_tooltip + skill_tooltip
						
				
				if skill_inc_ranks > 0 or skill_inc_bonus > 0:
					skill_tooltip = "       %s  enhancive Perception ranks (%s vs max +50)\n" % (("%+d" % min(50, skill_inc_bonus+skill_inc_ranks)).rjust(4), "%+d" % (skill_inc_bonus+skill_inc_ranks)) + skill_tooltip
					
				perception_total = base_ranks_arr["Perception"] + min(50, skill_inc_bonus+skill_inc_ranks)		
				skill_tooltip = "       %s  Perception base ranks\n" % (("%+d" % base_ranks_arr["Perception"]).rjust(4)) + skill_tooltip										

				skill_tooltip = "  %s  Perception ranks  ((%s - 40) / 4) vs min +0)\n" % (("%+d" % ( max(0, math.floor(0/4) + math.floor((perception_total - 40) / 4) )) ).rjust(4), perception_total) + skill_tooltip									
								
								
				# Calculate Ambush ranks
				skill_rank_count = base_ranks_arr["Ambush"]		
						
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Bonus_Ambush"], "Skill_Bonus_Ambush", "skill_bonus_to_ranks", skill_rank_count, "            ")
				skill_inc_bonus += ce_total
				skill_tooltip = ce_tooltip + skill_tooltip		
				skill_rank_count += ce_total			
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Ranks_Ambush"], "Skill_Ranks_Ambush", "ranks_display", skill_rank_count, "            ")
				skill_inc_ranks = ce_total
				skill_tooltip = ce_tooltip + skill_tooltip				
						
				
				if skill_inc_ranks > 0 or skill_inc_bonus > 0:
					skill_tooltip = "       %s  enhancive Ambush ranks (%s vs max +50)\n" % (("%+d" % min(50, skill_inc_bonus+skill_inc_ranks)).rjust(4), "%+d" % (skill_inc_bonus+skill_inc_ranks)) + skill_tooltip
					
				ambush_total = base_ranks_arr["Ambush"] + min(50, skill_inc_bonus+skill_inc_ranks)			
				skill_tooltip = "       %s  Ambush base ranks\n" % (("%+d" % base_ranks_arr["Ambush"]).rjust(4)) + skill_tooltip			
				
				skill_tooltip = "  %s  Ambush ranks  ((%s - 40) / 4) vs min +0)\n" % (("%+d" % ( max(0, math.floor(0/4) + math.floor((ambush_total - 40) / 4) )) ).rjust(4), ambush_total) + skill_tooltip	
				
			elif weapon_types[0] == "Thrown Weapons":
				# Calculate Perception ranks
				skill_rank_count = base_ranks_arr["Perception"]			
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Bonus_Perception"], "Skill_Bonus_Perception", "skill_bonus_to_ranks", skill_rank_count, "            ")
				skill_inc_bonus = ce_total
				skill_tooltip = ce_tooltip + skill_tooltip
				skill_rank_count += ce_total			
						
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Ranks_Perception"], "Skill_Ranks_Perception", "ranks_display", skill_rank_count, "            ")
				skill_inc_ranks = ce_total
				skill_tooltip = ce_tooltip + skill_tooltip						
				
				if skill_inc_ranks > 0 or skill_inc_bonus > 0:
					skill_tooltip = "       %s  enhancive Perception ranks (%s vs max +50)\n" % (("%+d" % min(50, skill_inc_bonus+skill_inc_ranks)).rjust(4), "%+d" % (skill_inc_bonus+skill_inc_ranks)) + skill_tooltip
					
				perception_total = base_ranks_arr["Perception"] + min(50, skill_inc_bonus+skill_inc_ranks)		
				skill_tooltip = "       %s  Perception base ranks\n" % (("%+d" % base_ranks_arr["Perception"]).rjust(4)) + skill_tooltip		
								
								
				# Calculate Combat Maneuver ranks
				skill_rank_count = base_ranks_arr["Combat Maneuvers"]		
						
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Bonus_Combat_Maneuvers"], "Skill_Bonus_Combat_Maneuvers", "skill_bonus_to_ranks", skill_rank_count, "            ")
				skill_inc_bonus = ce_total
				skill_tooltip = ce_tooltip + skill_tooltip		
				skill_rank_count += ce_total			
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Ranks_Combat_Maneuvers"], "Skill_Ranks_Combat_Maneuvers", "ranks_display", skill_rank_count, "            ")
				skill_inc_ranks = ce_total
				skill_tooltip = ce_tooltip + skill_tooltip		
						
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Phantom_Ranks_Combat_Maneuvers"], "Skill_Phantom_Ranks_Combat_Maneuvers", "effect_display", 0, "            ")
				skill_phantom += ce_total
				skill_phantom_tooltip = ce_tooltip	
						
				
				if skill_inc_ranks > 0 or skill_inc_bonus > 0:
					skill_tooltip = "       %s  enhancive Combat Maneuvers ranks (%s vs max +50)\n" % (("%+d" % min(50, skill_inc_bonus+skill_inc_ranks)).rjust(4), "%+d" % (skill_inc_bonus+skill_inc_ranks)) + skill_tooltip
					
				cman_total = base_ranks_arr["Combat Maneuvers"] + skill_phantom + min(50, skill_inc_bonus+skill_inc_ranks)				
				
				if skill_phantom_tooltip != "":
					skill_tooltip = "       %s  Combat Maneuver phantom ranks\n" % (("%+d" % skill_phantom).rjust(4)) + skill_phantom_tooltip + skill_tooltip
				skill_tooltip = "       %s  Combat Maneuver base ranks\n" % (("%+d" % base_ranks_arr["Combat Maneuvers"]).rjust(4)) + skill_tooltip
				
				skill_tooltip = "  %s  Combat Maneuvers + Perception ranks  ((%s + %s) / 4)\n" % (("%+d" % ( math.floor((cman_total + perception_total) / 4) )).rjust(4), cman_total, perception_total) + skill_tooltip	
				
			else:
				# Calculate Combat Maneuvers ranks
				skill_rank_count = base_ranks_arr["Combat Maneuvers"]	
						
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Bonus_Combat_Maneuvers"], "Skill_Bonus_Combat_Maneuvers", "skill_bonus_to_ranks", skill_rank_count, "            ")
				skill_inc_bonus = ce_total
				skill_tooltip = ce_tooltip + skill_tooltip			
				skill_rank_count += ce_total			
						
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Ranks_Combat_Maneuvers"], "Skill_Ranks_Combat_Maneuvers", "ranks_display", skill_rank_count, "            ")
				skill_inc_ranks = ce_total
				skill_tooltip = ce_tooltip + skill_tooltip	
				skill_rank_count += ce_total				
						
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Phantom_Ranks_Combat_Maneuvers"], "Skill_Phantom_Ranks_Combat_Maneuvers", "effect_display", 0, "            ")
				skill_phantom += ce_total
				skill_phantom_tooltip = ce_tooltip	
				
				if skill_inc_ranks > 0 or skill_inc_bonus > 0:
					skill_tooltip = "       %s  enhancive ranks (%s vs max +50)\n" % (("%+d" % min(50, skill_inc_bonus+skill_inc_ranks)).rjust(4), "%+d" % (skill_inc_bonus+skill_inc_ranks)) + skill_tooltip
					
				cman_total = base_ranks_arr["Combat Maneuvers"] + skill_phantom + min(50, skill_inc_bonus+skill_inc_ranks)				
				
				if skill_phantom_tooltip != "":
					skill_tooltip = "       %s  phantom ranks\n" % (("%+d" % skill_phantom).rjust(4)) + skill_phantom_tooltip + skill_tooltip
				skill_tooltip = "       %s  base ranks\n" % (("%+d" % base_ranks_arr["Combat Maneuvers"]).rjust(4)) + skill_tooltip
				skill_tooltip = "  %s  Combat Maneuver ranks  (%s / 2)\n" % (("%+d" % (cman_total/2)).rjust(4), cman_total) + skill_tooltip
				
					
			# Calculate Weapon Skill bonus. Takes several weapons skills into account in the case of Katana, Katar, or similar
			for skill in weapon_types:				
				weapon_enhancive_bonus = 0
				weapon_inc_bonus = 0															
				
				tag_name_sub = skill.replace(" ", "_").replace("-", "_").replace(",", "")																	
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Bonus_%s" % tag_name_sub], "Skill_Bonus_%s" % tag_name_sub,  "", 0, "            ")
				weapon_inc_bonus = ce_total			
				weapon_tooltip_text = ce_tooltip + weapon_tooltip_text
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Ranks_%s" % tag_name_sub], "Skill_Ranks_%s" % tag_name_sub,  "skill_ranks_to_bonus", base_bonus_arr[skill], "            ")
				weapon_inc_bonus += ce_total			
				weapon_tooltip_text = ce_tooltip + weapon_tooltip_text							
						
				weapon_enhancive_totals.append(base_bonus_arr[skill] + min(50, weapon_inc_bonus) )

				if weapon_inc_bonus > 0:
					weapon_tooltip_text = "       %s  enhancive %s bonus (%s vs max +50)\n" % (("%+d" % min(50, weapon_inc_bonus)).rjust(4), skill, "%+d" % weapon_inc_bonus) + weapon_tooltip_text
				weapon_tooltip_text = "       %s bonus from %s %s base ranks\n" % (("%+d" % base_bonus_arr[skill]).rjust(4), base_ranks_arr[skill], skill) + weapon_tooltip_text
				combined_weapons_bonus += base_bonus_arr[skill] + min(50, weapon_inc_bonus) 
				
			combined_weapons_bonus /= len(weapon_types)							

			# In TWC mode, we need to calculate the TWC bonus
			if twc_mode == 1:		
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Bonus_Two_Weapon_Combat"], "Skill_Bonus_Two_Weapon_Combat",  "", 0, "            ")
				weapon_inc_bonus = ce_total			
				weapon_tooltip_text = ce_tooltip + weapon_tooltip_text
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Ranks_Two_Weapon_Combat"], "Skill_Ranks_Two_Weapon_Combat",  "skill_ranks_to_bonus", weapon_inc_bonus, "            ")
				twc_inc_bonus = ce_total			
				weapon_tooltip_text = ce_tooltip + weapon_tooltip_text									

				if twc_inc_bonus > 0:
					weapon_tooltip_text = "       %s  enhancive Two Weapon Combat bonus (%s vs max +50)\n" % (("%+d" % min(50, twc_inc_bonus)).rjust(4), "%+d" % twc_inc_bonus) + weapon_tooltip_text
				weapon_tooltip_text = "       %s bonus from %s Two Weapon Combat base ranks\n" % (("%+d" % base_bonus_arr["Two Weapon Combat"]).rjust(4), base_ranks_arr["Two Weapon Combat"]) + weapon_tooltip_text
				combined_twc_bonus = base_bonus_arr["Two Weapon Combat"] + min(50, twc_inc_bonus) 		
				
				
			
			# Create the tooltip for the weapons part
			if len(weapon_types) > 1:	
				mutli_tooltip = ""
				for j in range(len(weapon_types)):
					mutli_tooltip = " %s (%s)," % (weapon_types[j], "%+d" % weapon_enhancive_totals[j]) + mutli_tooltip
					
				if twc_mode == 1:
					weapon_tooltip_text = "       %s  Skill bonus avg: %s\n" % (("%+d" % combined_weapons_bonus).rjust(4), mutli_tooltip[:-1]) + weapon_tooltip_text
					weapon_tooltip_text = "  %s  Off-hand %s skill bonus (3/5 * %+d) + (2/5 * %+d) \n" % (("%+d" % ((3/5 * combined_weapons_bonus) + (2/5 * combined_twc_bonus)) ).rjust(4), main_gear.skills,  combined_weapons_bonus, combined_twc_bonus) + weapon_tooltip_text
				else:
					weapon_tooltip_text = "  %s  Skill bonus avg: %s\n" % (("%+d" % combined_weapons_bonus).rjust(4), mutli_tooltip[:-1]) + weapon_tooltip_text
					
			elif twc_mode == 1:
				weapon_tooltip_text = "  %s  Off-hand %s skill bonus (3/5 * %+d) + (2/5 * %+d) \n" % (("%+d" % ((3/5 * combined_weapons_bonus) + (2/5 * combined_twc_bonus)) ).rjust(4), weapon_types[0],  combined_weapons_bonus, combined_twc_bonus) + weapon_tooltip_text
			else:
				weapon_tooltip_text = "  %s  %s skill bonus\n" % (("%+d" % combined_weapons_bonus).rjust(4), weapon_types[0]) + weapon_tooltip_text
			
			
			weapon_tooltip_arr.append(weapon_tooltip_text)	

			
			# Calculate total of AS_All
			ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["AS_All"], "AS_All",  "effect_display", 0, "       ")
			effects_total = ce_total
			effects_tooltip_text += ce_tooltip		
			
			# Calculate total AS_Bolt effects								
			ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag[effect_type], effect_type,  "effect_display", 0, "       ")
			effects_total += ce_total
			effects_tooltip_text += ce_tooltip						
			
			if effects_tooltip_text != "":
					effects_tooltip_text = "  %s  bonus from Attack Strength effects\n" % (("%+d" % effects_total).rjust(4)) + effects_tooltip_text								
						
									
			# Calculate the AS in each stance
			if twc_mode == 1:
				value = min(combined_strength_bonus, combined_dexterity_bonus) + math.floor( ((3/5 * combined_weapons_bonus) + (2/5 * combined_twc_bonus)) ) + math.floor(cman_total / 2) + main_enchantment + effects_total	
			elif weapon_types[0] == "Spell Aiming":		
				value = combined_statistic_bonus + math.floor(combined_weapons_bonus) + effects_total				
			elif weapon_types[0] == "Thrown Weapons":
				value = combined_statistic_bonus + math.floor(combined_weapons_bonus) + math.floor((cman_total + perception_total) / 4) + effects_total	
			elif weapon_types[0] == "Ranged Weapons":	
				value = combined_statistic_bonus + math.floor(combined_weapons_bonus) + max(0, math.floor(0/4) + math.floor((ambush_total - 40) / 4) ) + max(0, math.floor((perception_total - 40) / 4)) + min(50, main_enchantment+ammo_enchantment) + effects_total				
			else:										
				value = combined_statistic_bonus + math.floor(combined_weapons_bonus) + math.floor(cman_total / 2) + main_enchantment + effects_total		
				
			off_stance_totals.append(value * 1.0)
			neu_stance_totals.append(value * 0.7)
			adv_stance_totals.append(value * 0.9)
			gua_stance_totals.append(value * 0.6)
			for_stance_totals.append(value * 0.8)
			def_stance_totals.append(value * 0.5)
			
			# Create Tooltip
			tooltip += "%+s = %+d * 1.0  (Offensive Stance)\n" % (("%+d" % off_stance_totals[index]).rjust(4), value)
			tooltip += "%+s = %+d * 0.9  (Advanced Stance)\n" % (("%+d" % adv_stance_totals[index]).rjust(4), value)
			tooltip += "%+s = %+d * 0.8  (Forward Stance)\n" % (("%+d" % for_stance_totals[index]).rjust(4), value)
			tooltip += "%+s = %+d * 0.7  (Neutral Stance)\n" % (("%+d" % neu_stance_totals[index]).rjust(4), value)
			tooltip += "%+s = %+d * 0.6  (Guarded Stance)\n" % (("%+d" % gua_stance_totals[index]).rjust(4), value)
			tooltip += "%+s = %+d * 0.5  (Defensive Stance)\n" % (("%+d" % def_stance_totals[index]).rjust(4), value)
			tooltip += "%+d calculated with:\n" % value
			if weapon_types[0] == "Ranged Weapons":			
				tooltip += "  %s  Combined enchantment bonus (%+d vs max +50)\n" % (("%+d" % min(50, main_enchantment+ammo_enchantment)).rjust(4), main_enchantment+ammo_enchantment)
				tooltip += "      %s  Enchantment bonus of %s\n" % (("%+d" % main_enchantment).rjust(4), main_gear.name.get())
				tooltip += "      %s  Enchantment bonus of Arrows/Bolts\n" % (("%+d" % ammo_enchantment).rjust(4))
			elif weapon_types[0] != "Spell Aiming":
				tooltip += "  %s  Enchantment bonus of %s\n" % (("%+d" % main_enchantment).rjust(4), main_gear.name.get())
			tooltip += stat_tooltip_text			
			for text in weapon_tooltip_arr:
				tooltip += text
			tooltip += skill_tooltip		
			tooltip += effects_tooltip_text
			self.graph_information.tooltip_array.append(tooltip[:-1])					

			index += 1
					

					
		# Loop is done, set up the graph_infomation object	
		if calc_style == 1:
			self.graph_information.graph_xlabel = "%s %sAS by Stance per Level" % (main_gear.skills, off_hand_text)
			self.graph_information.graph_xaxis_rotation = 0
			self.graph_information.graph_xlabel_size = 12
			self.graph_information.graph_xaxis_size = 12
			self.graph_information.graph_xaxis_tick_range = loop_range
			self.graph_information.graph_xaxis_tick_labels = [0,10,20,30,40,50,60,70,80,90,100]		
		elif calc_style == 2:
			self.graph_information.graph_xlabel = "%s AS by Stance per Postcap Experience Interval" % main_gear.skills
			self.graph_information.graph_xaxis_rotation = 30
			self.graph_information.graph_xlabel_size = 10
			self.graph_information.graph_xaxis_size = 9			
			self.graph_information.graph_xaxis_tick_range = [i for i in range(index)]
			
			if len(postcap_intervals) <= 10:
				self.graph_information.graph_xaxis_tick_labels = [i for i in postcap_intervals]	
			else:
				temp = math.floor(len(postcap_intervals)/10)
				i = 0
								
				for interval in postcap_intervals:
					if i % temp == 0:
						self.graph_information.graph_xaxis_tick_labels.append(interval)
					i += 1								
					
					
		if def_stance_totals[0] < off_stance_totals[0]:			
			self.graph_information.graph_yaxis_min = def_stance_totals[0] - 5
		else:	
			self.graph_information.graph_yaxis_min = off_stance_totals[0] - 5
		self.graph_information.graph_yaxis_max = off_stance_totals[-1] + 5	
		self.graph_information.graph_data_lists.append(off_stance_totals)
		self.graph_information.graph_data_lists.append(adv_stance_totals)
		self.graph_information.graph_data_lists.append(for_stance_totals)
		self.graph_information.graph_data_lists.append(neu_stance_totals)
		self.graph_information.graph_data_lists.append(gua_stance_totals)
		self.graph_information.graph_data_lists.append(def_stance_totals)

		# Legend Information
		self.graph_information.graph_num_lines = 6
		self.graph_information.graph_legend_columns = 3
		self.graph_information.graph_legend_labels.append("Offensive Stance")
		self.graph_information.graph_legend_styles.append("r^-")
		self.graph_information.graph_legend_labels.append("Neutral Stance")
		self.graph_information.graph_legend_styles.append("g*-")
		self.graph_information.graph_legend_labels.append("Advanced Stance")
		self.graph_information.graph_legend_styles.append("mD-")
		self.graph_information.graph_legend_labels.append("Guarded Stance")
		self.graph_information.graph_legend_styles.append("cH-")
		self.graph_information.graph_legend_labels.append("Forward Stance")
		self.graph_information.graph_legend_styles.append("yd-")
		self.graph_information.graph_legend_labels.append("Defensive Stance")
		self.graph_information.graph_legend_styles.append("bs-")

		self.graph_information.graph_ylabel = "Attack Strength"					
	
	
	# This huge method is used to Defense Strength (DS) of a character from level 0-100 or across postcap training. 
	# The user picks between melee and ranged defense and the DS is calculated depending on their gear's combat style.
	# All three parts of the DS formula, Parry, Block, and Evade are calculated seperately and added up to show the
	# total DS gained. Off-Hand Parry DS is also done if a weapon is in the off-hand. All statistics, skills, and 
	# effects that increase skills, statistics, or AS itself are included in this calculation.	
	def Formula_Defense_Strength(self, vs_type, main_gear, other_hand_gear, armor_gear, gloves_gear, calc_style):
		index = 0
		loop_range = [i for i in range(101)]
		base_stat_arr = {}
		base_ranks_arr = {}
		base_bonus_arr = {}
		postcap_intervals = []
		lists_of_effects_by_tag = {}	
		
		main_enchantment = int(main_gear.enchantment)
		other_name = other_hand_gear.name.get()
		other_enchantment = int(other_hand_gear.enchantment)
		armor_enchantment = int(armor_gear.enchantment)
		gloves_enchantment = int(gloves_gear.enchantment)
		weapon_types = main_gear.skills.split("/")
		shield_factor = 1
		shield_size_penalty = 0
		shield_size = "none"	
		runestaff_rank_conversions = [0, 0.15, 0.30, 0.45, 0.60, 0.70, 0.80, 0.90, 1, 1.1, 1.2, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55]
		
		off_stance = []
		adv_stance = []
		for_stance = []
		neu_stance = []
		gua_stance = []
		def_stance = []			
		
		# Setup the lists for what skills and stats are relavent for calculate DS by fighting style
		if main_gear.name.get() == "Runestaff":
			effects_list = ["Skill_Ranks_Arcane_Symbols", "Skill_Ranks_Magic_Item_Use", "Skill_Ranks_Harness_Power", "Skill_Ranks_Spell_Aiming",
							"Skill_Ranks_Elemental_Mana_Control", "Skill_Ranks_Mental_Mana_Control", "Skill_Ranks_Spiritual_Mana_Control",
							"Skill_Ranks_Elemental_Lore_Air", "Skill_Ranks_Elemental_Lore_Earth", "Skill_Ranks_Elemental_Lore_Fire", "Skill_Ranks_Elemental_Lore_Water",
							"Skill_Ranks_Spiritual_Lore_Blessings", "Skill_Ranks_Spiritual_Lore_Summoning", "Skill_Ranks_Spiritual_Lore_Religion",
							"Skill_Ranks_Mental_Lore_Divination", "Skill_Ranks_Mental_Lore_Manipulation", "Skill_Ranks_Mental_Lore_Telepathy", "Skill_Ranks_Mental_Lore_Transference", "Skill_Ranks_Mental_Lore_Transformation",
							"Skill_Ranks_Sorcerous_Lore_Demonology", "Skill_Ranks_Sorcerous_Lore_Necromancy", "Skill_Ranks_Spell_Research_Minor_Spiritual", "Skill_Ranks_Spell_Research_Major_Spiritual", "Skill_Ranks_Spell_Research_Cleric", "Skill_Ranks_Spell_Research_Minor_Elemental", "Skill_Ranks_Spell_Research_Major_Elemental", "Skill_Ranks_Spell_Research_Ranger", "Skill_Ranks_Spell_Research_Sorcerer", "Skill_Ranks_Spell_Research_Wizard","Skill_Ranks_Spell_Research_Savant", "Skill_Ranks_Spell_Research_Minor_Mental", "Skill_Ranks_Spell_Research_Major_Mental", "Skill_Ranks_Spell_Research_Paladin",
							"Skill_Bonus_Arcane_Symbols", "Skill_Bonus_Magic_Item_Use", "Skill_Bonus_Harness_Power", "Skill_Bonus_Spell_Aiming",
							"Skill_Bonus_Elemental_Mana_Control", "Skill_Bonus_Mental_Mana_Control", "Skill_Bonus_Spiritual_Mana_Control",
							"Skill_Bonus_Elemental_Lore_Air", "Skill_Bonus_Elemental_Lore_Earth", "Skill_Bonus_Elemental_Lore_Fire", "Skill_Bonus_Elemental_Lore_Water",
							"Skill_Bonus_Spiritual_Lore_Blessings", "Skill_Bonus_Spiritual_Lore_Summoning", "Skill_Bonus_Spiritual_Lore_Religion",
							"Skill_Bonus_Mental_Lore_Divination", "Skill_Bonus_Mental_Lore_Manipulation", "Skill_Bonus_Mental_Lore_Telepathy", "Skill_Bonus_Mental_Lore_Transference", "Skill_Bonus_Mental_Lore_Transformation",
							"Skill_Bonus_Sorcerous_Lore_Demonology", "Skill_Bonus_Sorcerous_Lore_Necromancy", "Skill_Bonus_Spell_Research_Minor_Spiritual", "Skill_Bonus_Spell_Research_Major_Spiritual", "Skill_Bonus_Spell_Research_Cleric", "Skill_Bonus_Spell_Research_Minor_Elemental", "Skill_Bonus_Spell_Research_Major_Elemental", "Skill_Bonus_Spell_Research_Ranger", "Skill_Bonus_Spell_Research_Sorcerer", "Skill_Bonus_Spell_Research_Wizard","Skill_Bonus_Spell_Research_Savant", "Skill_Bonus_Spell_Research_Minor_Mental", "Skill_Bonus_Spell_Research_Major_Mental", "Skill_Bonus_Spell_Research_Paladin",
							"Statistic_Strength", "Statistic_Bonus_Strength", "Statistic_Dexterity", "Statistic_Bonus_Dexterity", "Statistic_Intuition", "Statistic_Bonus_Intuition", "Statistic_Agility", "Statistic_Bonus_Agility", "DS_All"]	
			statistic_names = ["Intuition", "Agility", "Dexterity", "Strength"]
			skill_names = ["Arcane Symbols", "Magic Item Use", "Harness Power", "Spell Aiming",
							"Elemental Mana Control", "Mental Mana Control", "Spiritual Mana Control", 
							"Elemental Lore, Air", "Elemental Lore, Earth", "Elemental Lore, Fire", "Elemental Lore, Water",
							"Spiritual Lore, Blessings", "Spiritual Lore, Summoning", "Spiritual Lore, Religion",
							"Mental Lore, Divination", "Mental Lore, Manipulation", "Mental Lore, Telepathy", "Mental Lore, Transference", "Mental Lore, Transformation", 
							"Sorcerous Lore, Demonology", "Sorcerous Lore, Necromancy",
							"Spell Research, Minor Spiritual", "Spell Research, Major Spiritual", "Spell Research, Cleric", "Spell Research, Minor Elemental", "Spell Research, Major Elemental", "Spell Research, Ranger", "Spell Research, Sorcerer", "Spell Research, Wizard", "Spell Research, Savant", "Spell Research, Minor Mental", "Spell Research, Major Mental", "Spell Research, Paladin"
						]
						
		elif weapon_types[0] == "Ranged Weapons":
			effects_list = ["Statistic_Intuition", "Statistic_Bonus_Intuition", "Statistic_Agility", "Statistic_Bonus_Agility", "Skill_Bonus_Ambush", "Skill_Ranks_Ambush", "Skill_Bonus_Perception", "Skill_Ranks_Perception", "DS_All"]	
			statistic_names = ["Intuition", "Agility"]
			skill_names = ["Ambush", "Perception"]

		else:				
			effects_list = ["Statistic_Strength", "Statistic_Bonus_Strength", "Statistic_Dexterity", "Statistic_Bonus_Dexterity", "Statistic_Intuition", "Statistic_Bonus_Intuition", "Statistic_Agility", "Statistic_Bonus_Agility", "DS_All"]	
			statistic_names = ["Intuition", "Agility", "Dexterity", "Strength"]
			skill_names = []
			
		
		if other_name == "Small Shield" or other_name == "Medium Shield" or other_name == "Large Shield" or other_name == "Tower Shield":
			effects_list.extend( ("Skill_Bonus_Shield_Use", "Skill_Ranks_Shield_Use", "Shield_Factor") )
			shield_size = other_hand_gear.gear_traits["size"]
			shield_melee_size_modifer = other_hand_gear.gear_traits["melee_size_modifer"]
			shield_ranged_size_modifer = other_hand_gear.gear_traits["ranged_size_modifer"]
			shield_ranged_size_bonus = other_hand_gear.gear_traits["ranged_size_bonus"]
			shield_size_penalty = other_hand_gear.gear_traits["dodging_size_penalty"]	
			shield_factor = other_hand_gear.gear_traits["dodging_shield_factor"]				
			skill_names.append("Shield Use")
			
		elif ( weapon_types[0] != "Ranged Weapons" and other_name != "Empty" ) or ( weapon_types[0] == "Brawling" and other_name == "Empty" ):
			effects_list.extend( ("Skill_Bonus_Two_Weapon_Combat", "Skill_Ranks_Two_Weapon_Combat") )
			skill_names.append("Two Weapon Combat")

			
		# Evade DS setup
		dodge_armor_hindrance = armor_gear.gear_traits["dodging_hindrance_factor"]	
		effects_list.extend( ("Skill_Bonus_Dodging", "Skill_Ranks_Dodging", "Skill_Phantom_Ranks_Dodging") )
		skill_names.append("Dodging")
		
		
		if vs_type == "Melee":
			effects_list.append("DS_Melee")
		elif vs_type == "Ranged":
			effects_list.append("DS_Ranged")
		elif vs_type == "Bolt":		
			effects_list.append("DS_Bolt")
		
						
		# Don't need THW skill when using a Runestaff
		if main_gear.name.get() != "Runestaff":
			for skill in weapon_types:
				skill_names.append(skill)
				effects_list.append("Skill_Ranks_%s" % skill.replace(" ", "_").replace("-", "_").replace(",", ""))
				effects_list.append("Skill_Bonus_%s" % skill.replace(" ", "_").replace("-", "_").replace(",", ""))
			
		lists_of_effects_by_tag = self.Find_Effects_By_Tags(effects_list)				


		# In Postcap mode, loop_range is not 0-100, instead its whatever postcap intervals that have training in the relevant skills
		if calc_style == 2:
			interval = 7575000
			for interval, training in globals.character.postcap_skill_training_by_interval.items():
				for skill in skill_names:
					if skill in training:
						postcap_intervals.append(interval)
						break										
							
			if len(postcap_intervals) == 0:
				postcap_intervals.append(7572500)
				postcap_intervals.append(interval)
			elif postcap_intervals[0] != 7572500:
				postcap_intervals.insert(0, 7572500)			
			
			if postcap_intervals[-1] != interval:
				postcap_intervals.append(interval)		
							
			loop_range = postcap_intervals
			

		# Begin the big loop to calculate all the data	
		for i in loop_range:	
			skill_phantom = 0
			skill_inc_ranks = 0
			skill_inc_bonus = 0		
			skill_rank_count = 0
			effects_total = 0
			combined_weapons_bonus = 0
			combined_statistic_bonus = 0			
			weapon_enhancive_totals = []
			stat_enhancive_totals = {}
			stat_tooltip_arr = {}
			skill_tooltip_arr = {}			
			skill_phantom_tooltip = ""
			skill_tooltip = ""
			weapon_tooltip_text = ""
			effects_tooltip_text = ""
			parry_tooltip_text = ""
			off_hand_tooltip_text = ""
			shield_tooltip_text = ""
			evade_tooltip_text = ""
			weapon_tooltip_arr = []		
			
			parry_totals_arr = []
			shield_totals_arr = []
			evade_totals_arr = []
			
			if calc_style == 1:
				tooltip = "Level %s: Defense Strength vs %s\n" % (i, vs_type)
				for stat in statistic_names:				
					base_stat_arr[stat] = globals.character.statistics_list[stat].bonuses_by_level[i].get()	
				
				for skill in skill_names:
					base_ranks_arr[skill] = globals.character.skills_list[skill].total_ranks_by_level[i].get()
					base_bonus_arr[skill] = globals.character.skills_list[skill].bonus_by_level[i].get()		
					
			elif calc_style == 2:	
				tooltip = "Postcap Experience Interval %s: Defense Strength vs %s\n" % ("{:,}".format(i), vs_type)
				for stat in statistic_names:				
					base_stat_arr[stat] = globals.character.statistics_list[stat].bonuses_by_level[100].get()	
				
				for skill in skill_names:
					base_ranks_arr[skill] = globals.character.skills_list[skill].total_ranks_by_level[100].get()
					base_bonus_arr[skill] = globals.character.skills_list[skill].bonus_by_level[100].get()
					
					base_ranks_arr[skill] += globals.character.skills_list[skill].Postcap_Get_Total_Ranks_Closest_To_Interval(i)
					base_bonus_arr[skill] += globals.character.skills_list[skill].Postcap_Get_Bonus_Closest_To_Interval(i)	
		

			# Calculate Statistic bonus	
			for stat in statistic_names:
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Statistic_Bonus_%s" % stat], "Statistic_Bonus_%s" % stat, "", 0, "            ")
				stat_enh_bonus = ce_total
				stat_tooltip_text = ce_tooltip
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Statistic_%s" % stat], "Statistic_%s" % stat, "stat_inc_to_bonus", 0, "            ")
				stat_enh_bonus += ce_total
				stat_tooltip_text = ce_tooltip + stat_tooltip_text				
				
				stat_enhancive_totals[stat] = base_stat_arr[stat] + min(50, stat_enh_bonus)				
				
				if stat_enh_bonus > 0:
					stat_tooltip_text = "       %s  enhancive %s bonus (%s vs max +20)\n" % (("%+d" % min(20, stat_enh_bonus)).rjust(4), stat, "%+d" % (stat_enh_bonus)) + stat_tooltip_text
				stat_tooltip_text = "       %s  %s base bonus\n" % (("%+d" % base_stat_arr[stat]).rjust(4), stat) + stat_tooltip_text						
				stat_tooltip_arr[stat] = stat_tooltip_text
								
						

			# Calculate Parry DS	
			if main_gear.name.get() == "Runestaff":		
				combined_weapons_ranks = 0
				for skill in skill_names:		
					if skill == "Dodging" or skill == "Two Weapon Combat":
						continue
												
					tag_name_sub = skill.replace(" ", "_").replace("-", "_").replace(",", "")																	
					
					ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Bonus_%s" % tag_name_sub], "Skill_Bonus_%s" % tag_name_sub,  "skill_bonus_to_ranks", base_ranks_arr[skill], "            ")
					skill_inc_bonus = ce_total			
					weapon_tooltip_text = ce_tooltip 
					
					ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Ranks_%s" % tag_name_sub], "Skill_Ranks_%s" % tag_name_sub,  "", base_ranks_arr[skill]+ce_total, "            ")
					skill_inc_bonus += ce_total			
					weapon_tooltip_text = ce_tooltip + weapon_tooltip_text							
							
					weapon_enhancive_totals.append(base_ranks_arr[skill] + min(50, skill_inc_bonus) )

					if skill_inc_bonus > 0:
						weapon_tooltip_text = "       %s  enhancive %s bonus (%s vs max +50)\n" % (("%+d" % min(50, skill_inc_bonus)).rjust(4), skill, "%+d" % skill_inc_bonus) + weapon_tooltip_text
					weapon_tooltip_text = "       %s %s base ranks\n" % (("%+d" % base_ranks_arr[skill]).rjust(4), skill) + weapon_tooltip_text
					combined_weapons_ranks += base_ranks_arr[skill] + min(50, skill_inc_bonus) 
					skill_tooltip_arr[skill] = weapon_tooltip_text	

				
				if (i > 0 and i*8 > combined_weapons_ranks) or (i == 0 and combined_weapons_ranks < 8):
					if i == 0:
						parry_tooltip_text = "--Parry DS by Stance--\n+0 Parry DS.  Character has insuficent Runestaff magical ranks (%s vs %s).\n" % (combined_weapons_ranks, 8)
					else:
						parry_tooltip_text = "--Parry DS by Stance--\n+0 Parry DS.  Character has insuficent Runestaff magical ranks (%s vs %s).\n" % (combined_weapons_ranks, 8*i)
					parry_totals_arr = [0 for i in range(6)]	
				else:
					if i > 0:	 # Stupid divide by zero errors...
						conversion_rate = min(16, int(math.floor(combined_weapons_ranks/i)))
						parry_ranks = int(math.floor( runestaff_rank_conversions[conversion_rate] * i ))
					else:
						conversion_rate = min(16, combined_weapons_ranks)
						parry_ranks = int(math.floor( runestaff_rank_conversions[conversion_rate] ))
						


					parry_tooltip_text = "--Parry DS by Stance--\n"			
					parry_base_value = int(parry_ranks + math.floor(stat_enhancive_totals["Strength"]/4) + math.floor(stat_enhancive_totals["Dexterity"]/4))

					stance_mod = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]			 	
					stance_bonus = [0, 10, 20, 30, 40, 50]
					stance_arr = ["Offensive", "Advanced", "Forward", "Neutral", "Guarded", "Defensive"]
					for j in range(6):
						value = math.floor(parry_base_value * stance_mod[j])
						value = math.floor(value * 1.5)
						
						if vs_type == "Melee":
							value += main_enchantment
							value += stance_bonus[j]
						else:
							value = math.floor(value/2)
							value += math.floor(main_enchantment/2)
							value += math.floor(stance_bonus[j]/2)
						
						parry_totals_arr.append(value)	
												
						if vs_type == "Melee":
							parry_tooltip_text += "%+d = (%s  x  %.2f)  x  1.5  +  %s  +  %s  (%s)\n" % (value, parry_base_value, stance_mod[j], main_enchantment, stance_bonus[j], stance_arr[j]) 
						else:
							parry_tooltip_text += "%+d = ((%s  x  %.2f)  x  1.5)/2  +  %s  +  %s  (%s)\n" % (value, parry_base_value, stance_mod[j], int(math.floor(main_enchantment/2)), int(stance_bonus[j]/2),  stance_arr[j]) 
													

					parry_tooltip_text += "%+d (Parry Base Value) calculated with:\n" % parry_base_value	
					if i == 0:
						parry_tooltip_text += "  %s  Parry Ranks (%s vs %s -> %s(%s) = %s * %s)\n" % (("%+d" % parry_ranks).rjust(4), combined_weapons_ranks, 8, conversion_rate,  runestaff_rank_conversions[conversion_rate], runestaff_rank_conversions[conversion_rate], 1)					
					else:					
						parry_tooltip_text += "  %s  Parry Ranks (%s vs %s -> %s(%s) = %s * %s)\n" % (("%+d" % parry_ranks).rjust(4), combined_weapons_ranks, i*8, conversion_rate,runestaff_rank_conversions[conversion_rate], runestaff_rank_conversions[conversion_rate], i)					
					for skill in skill_names:	
						if skill == "Dodging" or skill == "Two Weapon Combat":
							continue
						parry_tooltip_text += skill_tooltip_arr[skill]
					parry_tooltip_text += "  %s    Strength bonus  (%+d / 4)\n" % (("%+d" % math.floor(stat_enhancive_totals["Strength"]/4)).rjust(4), stat_enhancive_totals["Strength"])		
					parry_tooltip_text += stat_tooltip_arr["Strength"]		
					parry_tooltip_text += "  %s    Dexterity bonus  (%+d / 4)\n" % (("%+d" % math.floor(stat_enhancive_totals["Dexterity"]/4)).rjust(4), stat_enhancive_totals["Dexterity"])		
					parry_tooltip_text += stat_tooltip_arr["Dexterity"]		
					if vs_type == "Melee":
						parry_tooltip_text += "  %s  Enchantment bonus of %s\n" % (("%+d" % main_enchantment).rjust(3), main_gear.name.get())	
					else:
						parry_tooltip_text += "  %s  Enchantment bonus of %s  (%d / 2)\n" % (("%+d" % int(math.floor(main_enchantment/2))).rjust(3), main_gear.name.get(), main_enchantment)		
						
			# Ranged Parry DS	
			elif weapon_types[0] == "Ranged Weapons":				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Bonus_Ranged_Weapons"], "Skill_Bonus_Ranged_Weapons",  "", 0, "            ")
				skill_inc_bonus = ce_total			
				weapon_tooltip_text = ce_tooltip + weapon_tooltip_text
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Ranks_Ranged_Weapons"], "Skill_Ranks_Ranged_Weapons",  "skill_ranks_to_bonus", base_bonus_arr["Ranged Weapons"], "            ")
				skill_inc_bonus += ce_total			
				weapon_tooltip_text = ce_tooltip + weapon_tooltip_text							
						
				weapon_enhancive_totals.append(base_bonus_arr["Ranged Weapons"] + min(50, skill_inc_bonus) )

				if skill_inc_bonus > 0:
					weapon_tooltip_text = "       %s  enhancive Ranged Weapons bonus (%s vs max +50)\n" % (("%+d" % min(50, skill_inc_bonus)).rjust(4), "%+d" % skill_inc_bonus) + weapon_tooltip_text
				weapon_tooltip_text = "       %s bonus from %s Ranged Weapons base ranks\n" % (("%+d" % base_bonus_arr["Ranged Weapons"]).rjust(4), base_ranks_arr["Ranged Weapons"]) + weapon_tooltip_text
				weapons_bonus = base_bonus_arr["Ranged Weapons"] + min(50, skill_inc_bonus) 				
				weapon_tooltip_text = "  %s  %s skill bonus\n" % (("%+d" % weapons_bonus).rjust(4), weapon_types[0]) + weapon_tooltip_text
				

				# Calculate Perception ranks
				skill_rank_count = base_ranks_arr["Perception"]			
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Bonus_Perception"], "Skill_Bonus_Perception", "skill_bonus_to_ranks", skill_rank_count, "            ")
				skill_inc_bonus = ce_total
				skill_tooltip = ce_tooltip
				skill_rank_count += ce_total			
						
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Ranks_Perception"], "Skill_Ranks_Perception", "ranks_display", skill_rank_count, "            ")
				skill_inc_ranks += ce_total
				skill_tooltip = ce_tooltip + skill_tooltip
						
				
				if skill_inc_ranks > 0 or skill_inc_bonus > 0:
					skill_tooltip = "       %s  enhancive Perception ranks (%s vs max +50)\n" % (("%+d" % min(50, skill_inc_bonus+skill_inc_ranks)).rjust(4), "%+d" % (skill_inc_bonus+skill_inc_ranks)) + skill_tooltip
					
				perception_total = base_ranks_arr["Perception"] + min(50, skill_inc_bonus+skill_inc_ranks)		
				skill_tooltip = "       %s  Perception base ranks\n" % (("%+d" % base_ranks_arr["Perception"]).rjust(4)) + skill_tooltip										

				skill_tooltip = "  %s  Perception ranks  (%s / 2)\n" % (("%+d" % ( math.floor(perception_total / 2 ) ) ).rjust(4), perception_total) + skill_tooltip
				skill_tooltip_arr["Perception"] = skill_tooltip				
	
	
				# Calculate Ambush ranks
				skill_rank_count = base_ranks_arr["Ambush"]		
						
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Bonus_Ambush"], "Skill_Bonus_Ambush", "skill_bonus_to_ranks", skill_rank_count, "            ")
				skill_inc_bonus = ce_total
				skill_tooltip = ce_tooltip	
				skill_rank_count += ce_total			
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Ranks_Ambush"], "Skill_Ranks_Ambush", "ranks_display", skill_rank_count, "            ")
				skill_inc_ranks += ce_total
				skill_tooltip = ce_tooltip + skill_tooltip						
						
				
				if skill_inc_ranks > 0 or skill_inc_bonus > 0:
					skill_tooltip = "       %s  enhancive Ambush ranks (%s vs max +50)\n" % (("%+d" % min(50, skill_inc_bonus+skill_inc_ranks)).rjust(4), "%+d" % (skill_inc_bonus+skill_inc_ranks)) + skill_tooltip
					
				ambush_total = base_ranks_arr["Ambush"] + min(50, skill_inc_bonus+skill_inc_ranks)			
				skill_tooltip = "       %s  Ambush base ranks\n" % (("%+d" % base_ranks_arr["Ambush"]).rjust(4)) + skill_tooltip			
				
				skill_tooltip = "  %s  Ambush ranks  (%s / 2)\n" % (("%+d" % ( math.floor((ambush_total / 2) )) ).rjust(4), ambush_total) + skill_tooltip	
				skill_tooltip_arr["Ambush"] = skill_tooltip		



				# Calculate Parry DS
				if weapons_bonus == 0:
					parry_tooltip_text = "--Parry DS by Stance--\n+0 Parry DS.  Character has no ranks in %s.\n" % main_gear.skills
					parry_totals_arr = [0 for i in range(6)]	
				else:
					# Ranged Parry DS calculations				
					parry_tooltip_text = "--Parry DS by Stance--\n"			
					parry_base_value = int(weapons_bonus + math.floor(perception_total/2) + math.floor(ambush_total/2))	
					
					
					if main_gear.name.get() == "Heavy Crossbow" or main_gear.name.get() == "Light Crossbow":
						stance_mod = [0.12, 0.17, 0.22, 0.27, 0.32, 0.37]		
					else:
						stance_mod = [0.15, 0.21, 0.27, 0.33, 0.39, 0.45]	
					stance_bonus = [0, 10, 20, 30, 40, 50]
					stance_arr = ["Offensive", "Advanced", "Forward", "Neutral", "Guarded", "Defensive"]
					for j in range(6):
						if vs_type == "Melee":
							value = math.floor(parry_base_value * stance_mod[j]) + stance_bonus[j]
						else:
							value = math.floor(parry_base_value * stance_mod[j])	

						value += main_enchantment
						
						parry_totals_arr.append(value)	
						
						if vs_type == "Melee":		
							parry_tooltip_text += "%+d = (%s  x  %.2f)  +  %s  + %s  (%s)\n" % (value, parry_base_value, stance_mod[j], main_enchantment, stance_bonus[j], stance_arr[j]) 
						else:
							parry_tooltip_text += "%+d = (%s  x  %.2f)  +  %s  (%s)\n" % (value, parry_base_value, stance_mod[j], main_enchantment, stance_arr[j]) 	


					parry_tooltip_text += "%+d (Parry Base Value) calculated with:\n" % parry_base_value		
					parry_tooltip_text += weapon_tooltip_text	
					parry_tooltip_text += skill_tooltip_arr["Perception"]			
					parry_tooltip_text += skill_tooltip_arr["Ambush"]		
					parry_tooltip_text += "%s  Enchantment bonus of %s\n" % (("%+d" % main_enchantment).rjust(3), main_gear.name.get())			
			
			# THW Parry DS
			elif weapon_types[0] == "Two-Handed Weapons" or (weapon_types[0] == "Polearm Weapons" and (main_gear.name.get() != "Pilum" and main_gear.name.get() != "Spear, One-Handed")):
				tag_name_sub = weapon_types[0].replace(" ", "_").replace("-", "_").replace(",", "")
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Bonus_%s" % tag_name_sub], "Skill_Bonus_%s" % tag_name_sub,  "", 0, "            ")
				skill_inc_bonus = ce_total			
				weapon_tooltip_text = ce_tooltip + weapon_tooltip_text
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Ranks_%s" % tag_name_sub], "Skill_Ranks_%s" % tag_name_sub,  "skill_ranks_to_bonus", base_bonus_arr[weapon_types[0]], "            ")
				skill_inc_bonus += ce_total			
				weapon_tooltip_text = ce_tooltip + weapon_tooltip_text							
						
				weapon_enhancive_totals.append(base_bonus_arr[weapon_types[0]] + min(50, skill_inc_bonus) )

				if skill_inc_bonus > 0:
					weapon_tooltip_text = "       %s  enhancive %s bonus (%s vs max +50)\n" % (("%+d" % min(50, skill_inc_bonus)).rjust(4), weapon_types[0], "%+d" % skill_inc_bonus) + weapon_tooltip_text
				weapon_tooltip_text = "       %s bonus from %s %s base ranks\n" % (("%+d" % base_bonus_arr[weapon_types[0]]).rjust(4), base_ranks_arr[weapon_types[0]], weapon_types[0]) + weapon_tooltip_text
				weapons_bonus = base_bonus_arr[weapon_types[0]] + min(50, skill_inc_bonus) 				
				weapon_tooltip_text = "  %s  %s skill bonus\n" % (("%+d" % weapons_bonus).rjust(4), weapon_types[0]) + weapon_tooltip_text				
			
				# No skill, no parry DS
				if weapons_bonus == 0:
					parry_tooltip_text = "--Parry DS by Stance--\n+0 Parry DS.  Character has no ranks in %s.\n" % main_gear.skills
					parry_totals_arr = [0 for i in range(6)]	
				else:			
					# Two-Handed Weapons and Two-Handed Polearms Parry DS calculations				
					parry_tooltip_text = "--Parry DS by Stance--\n"			
					parry_base_value = int(weapons_bonus + math.floor(stat_enhancive_totals["Strength"]/4) + math.floor(stat_enhancive_totals["Dexterity"]/4)) + main_enchantment
					
					
					if weapon_types[0] == "Two-Handed Weapons":
						stance_mod = [0.30, 0.45, 0.60, 0.75, 0.90, 1.05]				
						stance_bonus = [0, 10, 20, 30, 40, 50]
					else:
						stance_mod = [0.27, 0.41, 0.54, 0.68, 0.81, 0.94]			 	
						stance_bonus = [15, 28, 41, 54, 67, 80]
					stance_arr = ["Offensive", "Advanced", "Forward", "Neutral", "Guarded", "Defensive"]
					for j in range(6):
						if vs_type == "Melee":
							value = math.floor(parry_base_value * stance_mod[j]) + stance_bonus[j]
						else:
							value = math.floor(parry_base_value * stance_mod[j])	
						
						parry_totals_arr.append(value)	
						
						if vs_type == "Melee":		
							parry_tooltip_text += "%+d = (%s  x  %.2f)  + %s  (%s)\n" % (value, parry_base_value, stance_mod[j], stance_bonus[j], stance_arr[j]) 
						else:
							parry_tooltip_text += "%+d = (%s  x  %.2f)  (%s)\n" % (value, parry_base_value, stance_mod[j], stance_arr[j]) 
													

					parry_tooltip_text += "%+d (Parry Base Value) calculated with:\n" % parry_base_value		
					parry_tooltip_text += weapon_tooltip_text	
					parry_tooltip_text += "  %s    Strength bonus  (%+d / 4)\n" % (("%+d" % math.floor(stat_enhancive_totals["Strength"]/4)).rjust(4), stat_enhancive_totals["Strength"])		
					parry_tooltip_text += stat_tooltip_arr["Strength"]		
					parry_tooltip_text += "  %s    Dexterity bonus  (%+d / 4)\n" % (("%+d" % math.floor(stat_enhancive_totals["Dexterity"]/4)).rjust(4), stat_enhancive_totals["Dexterity"])		
					parry_tooltip_text += stat_tooltip_arr["Dexterity"]		
					parry_tooltip_text += "  %s  Enchantment bonus of %s\n" % (("%+d" % main_enchantment).rjust(3), main_gear.name.get())		
			
			# Every other weapon for Parry DS (one handed and possible off-hand)
			else:			
				for skill in weapon_types:			
					weapon_inc_bonus = 0															
					
					tag_name_sub = skill.replace(" ", "_").replace("-", "_").replace(",", "")																	
					
					ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Bonus_%s" % tag_name_sub], "Skill_Bonus_%s" % tag_name_sub,  "skill_bonus_to_ranks", 0, "            ")
					weapon_inc_bonus = ce_total			
					weapon_tooltip_text = ce_tooltip + weapon_tooltip_text
					
					ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Ranks_%s" % tag_name_sub], "Skill_Ranks_%s" % tag_name_sub,  "", base_ranks_arr[skill]+weapon_inc_bonus, "            ")
					weapon_inc_bonus += ce_total			
					weapon_tooltip_text = ce_tooltip + weapon_tooltip_text							
							
					weapon_enhancive_totals.append(base_ranks_arr[skill] + min(50, weapon_inc_bonus) )

					if weapon_inc_bonus > 0:
						weapon_tooltip_text = "       %s  enhancive %s bonus (%s vs max +50)\n" % (("%+d" % min(50, weapon_inc_bonus)).rjust(4), skill, "%+d" % weapon_inc_bonus) + weapon_tooltip_text
					weapon_tooltip_text = "       %s %s base ranks\n" % (("%+d" % base_ranks_arr[skill]).rjust(4), skill) + weapon_tooltip_text
					combined_weapons_bonus += base_ranks_arr[skill] + min(50, weapon_inc_bonus) 
						
				combined_weapons_bonus /= len(weapon_types)					


				if len(weapon_types) > 1:	
					mutli_tooltip = ""
					for j in range(len(weapon_types)):
						mutli_tooltip = " %s (%s)," % (weapon_types[j], "%+d" % weapon_enhancive_totals[j]) + mutli_tooltip
					weapon_tooltip_text = "  %s  Skill ranks avg: %s\n" % (("%+d" % combined_weapons_bonus).rjust(4), mutli_tooltip[:-1]) + weapon_tooltip_text
				else:	
					weapon_tooltip_text = "  %s  %s Skill ranks\n" % (("%+d" % combined_weapons_bonus).rjust(4), weapon_types[0]) + weapon_tooltip_text


				# No skill bonus, no parry DS
				if combined_weapons_bonus == 0:
					parry_tooltip_text = "--Parry DS by Stance--\n+0 Parry DS.  Character has no ranks in %s.\n" % main_gear.skills
					parry_totals_arr = [0 for i in range(6)]	
				else:									
					if main_gear.name.get() == "Closed Fist" and gloves_gear.name.get() != "No Gloves":
						parry_weapon = gloves_gear
						enchantment = gloves_enchantment
					else:
						parry_weapon = main_gear
						enchantment = main_enchantment
						
					# Main Hand Parry DS calculations				
					parry_tooltip_text = "--Parry DS by Stance--\n"			
					parry_base_value = int(combined_weapons_bonus + math.floor(stat_enhancive_totals["Strength"]/4) + math.floor(stat_enhancive_totals["Dexterity"]/4))+ int(math.floor(enchantment/2))
					
					
					stance_mod = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]			 	
					stance_bonus = [0, 10, 20, 30, 40, 50]
					stance_arr = ["Offensive", "Advanced", "Forward", "Neutral", "Guarded", "Defensive"]
					for j in range(6):
						value = math.floor(parry_base_value * stance_mod[j]) + stance_bonus[j]
						
						parry_totals_arr.append(value)							

						parry_tooltip_text += "%+d = (%s  x  %.2f)  + %s  (%s)\n" % (value, parry_base_value, stance_mod[j], stance_bonus[j], stance_arr[j]) 
						
						'''
						if vs_type == "Melee":		
							parry_tooltip_text += "%+d = (%s  x  %.2f)  + %s  (%s)\n" % (value, parry_base_value, stance_mod[j], stance_bonus[j], stance_arr[j]) 
						else:
							parry_tooltip_text += "%+d = (%s  x  %.2f)  (%s)\n" % (value, parry_base_value, stance_mod[j], stance_arr[j])						
						'''							

					parry_tooltip_text += "%+d (Parry Base Value) calculated with:\n" % parry_base_value		
					parry_tooltip_text += weapon_tooltip_text	
					parry_tooltip_text += "  %s    Strength bonus  (%+d / 4)\n" % (("%+d" % math.floor(stat_enhancive_totals["Strength"]/4)).rjust(4), stat_enhancive_totals["Strength"])		
					parry_tooltip_text += stat_tooltip_arr["Strength"]		
					parry_tooltip_text += "  %s    Dexterity bonus  (%+d / 4)\n" % (("%+d" % math.floor(stat_enhancive_totals["Dexterity"]/4)).rjust(4), stat_enhancive_totals["Dexterity"])		
					parry_tooltip_text += stat_tooltip_arr["Dexterity"]		
					parry_tooltip_text += "  %s  Enchantment bonus of %s  (%+d / 2)\n" % (("%+d" % int(math.floor(enchantment/2))).rjust(3), parry_weapon.name.get(), enchantment)	
			
			
				# Checked for off-hand Parry. If not using a shield		
				if shield_factor == 1:	
					ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Bonus_Two_Weapon_Combat"], "Skill_Bonus_Two_Weapon_Combat",  "skill_bonus_to_ranks", 0, "            ")
					weapon_inc_bonus = ce_total			
					off_hand_tooltip_text = ce_tooltip + off_hand_tooltip_text
					
					ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Ranks_Two_Weapon_Combat"], "Skill_Ranks_Two_Weapon_Combat",  "", base_ranks_arr["Two Weapon Combat"]+weapon_inc_bonus, "            ")
					weapon_inc_bonus += ce_total			
					off_hand_tooltip_text = ce_tooltip + off_hand_tooltip_text							
							
					weapon_enhancive_totals.append(base_ranks_arr["Two Weapon Combat"] + min(50, weapon_inc_bonus) )

					if weapon_inc_bonus > 0:
						off_hand_tooltip_text = "       %s  enhancive Two Weapon Combat bonus (%s vs max +50)\n" % (("%+d" % min(50, weapon_inc_bonus)).rjust(4), "%+d" % weapon_inc_bonus) + off_hand_tooltip_text
					off_hand_tooltip_text = "       %s Two Weapon Combat base ranks\n" % (("%+d" % base_ranks_arr["Two Weapon Combat"]).rjust(4)) + off_hand_tooltip_text
					weapons_bonus = base_ranks_arr["Two Weapon Combat"] + min(50, weapon_inc_bonus) 	
					off_hand_tooltip_text = "  %s  Two Weapon Combat ranks\n" % (("%+d" % weapons_bonus).rjust(4)) + off_hand_tooltip_text
					skill_tooltip_arr["Two Weapon Combat"] = off_hand_tooltip_text	

					# No skill bonus, no off-hand parry DS
					if weapons_bonus == 0:
						off_hand_tooltip_text = "--Off-Hand Parry DS by Stance--\n+0 Off-Hand Parry DS.  Character has no ranks in Two Weapon Combat.\n"
					else:			
						# Off-Hand Parry DS DS calculations				
						off_hand_tooltip_text = "--Off-Hand Parry DS by Stance--\n"			
						parry_base_value = int(weapons_bonus + math.floor(stat_enhancive_totals["Strength"]/4) + math.floor(stat_enhancive_totals["Dexterity"]/4))+ int(math.floor(other_enchantment/2))
						
						
						stance_mod = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35]	
						if other_hand_gear.name.get() == "Sai" or other_hand_gear.name.get() == "Main Gauche" or (other_hand_gear.name.get() == "Empty" and weapons_bonus > i/2):
							bonus = 15
						else:
							bonus = 5
						stance_arr = ["Offensive", "Advanced", "Forward", "Neutral", "Guarded", "Defensive"]
						for j in range(6):
							value = math.floor(parry_base_value * stance_mod[j]) + bonus
							
							parry_totals_arr[j] += value
							
							off_hand_tooltip_text += "%+d = (%s  x  %.2f)  + %s  (%s)\n" % (value, parry_base_value, stance_mod[j], bonus, stance_arr[j]) 
							
							'''
							if vs_type == "Melee":		
								off_hand_tooltip_text += "%+d = (%s  x  %.2f)  + %s  (%s)\n" % (value, parry_base_value, stance_mod[j], stance_bonus[j], stance_arr[j]) 
							else:
								off_hand_tooltip_text += "%+d = (%s  x  %.2f)  (%s)\n" % (value, parry_base_value, stance_mod[j], stance_arr[j])						
							'''

						off_hand_tooltip_text += "%+d (Off-Hand Parry Base Value) calculated with:\n" % parry_base_value		
						off_hand_tooltip_text += skill_tooltip_arr["Two Weapon Combat"]
						off_hand_tooltip_text += "  %s    Strength bonus  (%+d / 4)\n" % (("%+d" % math.floor(stat_enhancive_totals["Strength"]/4)).rjust(4), stat_enhancive_totals["Strength"])		
						off_hand_tooltip_text += stat_tooltip_arr["Strength"]		
						off_hand_tooltip_text += "  %s    Dexterity bonus  (%+d / 4)\n" % (("%+d" % math.floor(stat_enhancive_totals["Dexterity"]/4)).rjust(4), stat_enhancive_totals["Dexterity"])		
						off_hand_tooltip_text += stat_tooltip_arr["Dexterity"]		
						off_hand_tooltip_text += "  %s  Enchantment bonus of %s  (%+d / 2)\n" % (("%+d" % int(math.floor(other_enchantment/2))).rjust(3), other_hand_gear.name.get(), other_enchantment)				
					

			
			# Calculate Block DS
			if shield_factor == 1:
				shield_tooltip_text = "--Block DS by Stance--\n+0 Block DS.  Character is not using a shield.\n"
				shield_totals_arr = [0 for i in range(6)]	
			else:
				skill_rank_count = base_ranks_arr["Shield Use"]	
						
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Bonus_Shield_Use"], "Skill_Bonus_Shield_Use", "skill_bonus_to_ranks", skill_rank_count, "            ")
				skill_inc_bonus += ce_total
				skill_tooltip_arr["Shield Use"] = ce_tooltip		
				skill_rank_count += ce_total			
						
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Ranks_Shield_Use"], "Skill_Ranks_Shield_Use", "ranks_display", skill_rank_count, "            ")
				skill_inc_ranks += ce_total
				skill_tooltip_arr["Shield Use"] = ce_tooltip + skill_tooltip_arr["Shield Use"]	
										
				if skill_inc_ranks > 0 or skill_inc_bonus > 0:
					skill_tooltip_arr["Shield Use"] = "       %s  enhancive ranks (%s vs max +50)\n" % (("%+d" % min(50, skill_inc_bonus+skill_inc_ranks)).rjust(4), "%+d" % (skill_inc_bonus+skill_inc_ranks)) + skill_tooltip_arr["Shield Use"]
					
				shield_total = base_ranks_arr["Shield Use"] + min(50, skill_inc_bonus+skill_inc_ranks)				
				
				skill_tooltip_arr["Shield Use"] = "       %s  base ranks\n" % (("%+d" % base_ranks_arr["Shield Use"]).rjust(4)) + skill_tooltip_arr["Shield Use"]
				skill_tooltip_arr["Shield Use"] = "  %s  Shield Use ranks  \n" % (("%+d" % shield_total).rjust(4)) + skill_tooltip_arr["Shield Use"]			
				
				
				# Block DS calculations				
				shield_tooltip_text = "--Block DS by Stance--\n"			
				shield_base_value = int(shield_total + math.floor(stat_enhancive_totals["Strength"]/4) + math.floor(stat_enhancive_totals["Dexterity"]/4))	
				
				stance_mod = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]					
				stance_arr = ["Offensive", "Advanced", "Forward", "Neutral", "Guarded", "Defensive"]
				for j in range(6):
					if vs_type == "Melee":
						value = math.floor(shield_base_value * shield_melee_size_modifer * stance_mod[j])
					else:
						value = math.floor((math.floor(shield_base_value * shield_ranged_size_modifer) + shield_ranged_size_bonus) * stance_mod[j])

					value = int(math.floor(value / 1.5))
					value += 20 + other_enchantment
					
					shield_totals_arr.append(value)		
					
					if vs_type == "Melee":		
						shield_tooltip_text += "%+d = %s  x  %.2f  x  %s  /  1.5  +  20  + %s  (%s)\n" % (value, shield_base_value, shield_melee_size_modifer, stance_mod[j], other_enchantment, stance_arr[j]) 
					else:
						shield_tooltip_text += "%+d = (%s  x  %.2f  +  %s)  x  %s  /  1.5  +  20  + %s  (%s)\n" % (value, shield_base_value, shield_ranged_size_modifer, shield_ranged_size_bonus, stance_mod[j], other_enchantment, stance_arr[j]) 
				
				shield_tooltip_text += "%+d (Shield Base Value) calculated with:\n" % shield_base_value			
				shield_tooltip_text += skill_tooltip_arr["Shield Use"]		
				shield_tooltip_text += "  %s    Strength bonus  (%+d / 4)\n" % (("%+d" % math.floor(stat_enhancive_totals["Strength"]/4)).rjust(4), stat_enhancive_totals["Strength"])
				shield_tooltip_text += stat_tooltip_arr["Strength"]		
				shield_tooltip_text += "  %s    Dexterity bonus  (%+d / 4)\n" % (("%+d" % math.floor(stat_enhancive_totals["Dexterity"]/4)).rjust(4), stat_enhancive_totals["Dexterity"])	
				shield_tooltip_text += stat_tooltip_arr["Dexterity"]	
				if vs_type == "Melee":		
					shield_tooltip_text += "%+.2f (Melee Shield Size Modifier) calculated with:\n" % shield_melee_size_modifer		
					shield_tooltip_text += "    %+.2f base modifier of %s :\n" % (shield_melee_size_modifer, other_hand_gear.name.get())
				else:
					shield_tooltip_text += "%+.2f (Ranged Shield Size Modifier) calculated with:\n" % shield_ranged_size_modifer		
					shield_tooltip_text += "    %+.2f base modifier of %s\n" % (shield_ranged_size_modifer, other_hand_gear.name.get())
					shield_tooltip_text += "%+d (Ranged Shield Size Bonus) calculated with:\n" % shield_ranged_size_bonus		
					shield_tooltip_text += "    %+d base modifier of %s\n" % (shield_ranged_size_bonus, other_hand_gear.name.get())
				
				shield_tooltip_text += "+20  Base shield DS\n"
				shield_tooltip_text += "%s  Enchantment bonus of %s\n" % (("%+d" % other_enchantment).rjust(3), other_hand_gear.name.get())
			
				
			# Calculate Evade DS
			
			# Calculate Dodging ranks
			skill_rank_count = base_ranks_arr["Dodging"]	
					
			ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Bonus_Dodging"], "Skill_Bonus_Dodging", "skill_bonus_to_ranks", skill_rank_count, "            ")
			skill_inc_bonus = ce_total
			skill_tooltip_arr["Dodging"] = ce_tooltip		
			skill_rank_count += ce_total			
					
			ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Ranks_Dodging"], "Skill_Ranks_Dodging", "ranks_display", skill_rank_count, "            ")
			skill_inc_ranks = ce_total
			skill_tooltip_arr["Dodging"] = ce_tooltip + skill_tooltip_arr["Dodging"]	
			skill_rank_count += ce_total				
					
			ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Skill_Phantom_Ranks_Dodging"], "Skill_Phantom_Ranks_Dodging", "effect_display", 0, "            ")
			skill_phantom = ce_total
			phantom_tooltip_text = ce_tooltip	
			
			if skill_inc_ranks > 0 or skill_inc_bonus > 0:
				skill_tooltip_arr["Dodging"] = "       %s  enhancive ranks (%s vs max +50)\n" % (("%+d" % min(50, skill_inc_bonus+skill_inc_ranks)).rjust(4), "%+d" % (skill_inc_bonus+skill_inc_ranks)) + skill_tooltip_arr["Dodging"]
				
			dodge_total = base_ranks_arr["Dodging"] + skill_phantom + min(50, skill_inc_bonus+skill_inc_ranks)				
			
			if phantom_tooltip_text != "":
				skill_tooltip_arr["Dodging"] = "       %s  phantom ranks\n" % (("%+d" % skill_phantom).rjust(4)) + phantom_tooltip_text + skill_tooltip_arr["Dodging"]
			skill_tooltip_arr["Dodging"] = "       %s  base ranks\n" % (("%+d" % base_ranks_arr["Dodging"]).rjust(4)) + skill_tooltip_arr["Dodging"]
			skill_tooltip_arr["Dodging"] = "  %s  Dodging ranks\n" % (("%+d" % dodge_total).rjust(4)) + skill_tooltip_arr["Dodging"]

			

			# Calculate Evade DS				
			evade_tooltip_text = "--Evade DS by Stance--\n"			
			dodge_base_value = int(dodge_total + stat_enhancive_totals["Agility"] + math.floor(stat_enhancive_totals["Intuition"]/4))					
			
			if shield_size == "small" or shield_size == "medium":
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Shield_Factor"], "Shield_Factor", "float_format", 0, "    ")	
				
			else:
				ce_tooltip = ""
				ce_total = 0
			
			s_factor = shield_factor + ce_total
			stance_mod = [0.75, 0.80, 0.85, 0.9, 0.95, 1.0]				
			stance_arr = ["Offensive", "Advanced", "Forward", "Neutral", "Guarded", "Defensive"]
			for j in range(6):
				if vs_type == "Melee":
					value = math.floor(dodge_base_value * dodge_armor_hindrance) 
					value = math.floor(value * s_factor) - shield_size_penalty 
					value = int(math.floor(value * stance_mod[j]))
					
				else:
					value = math.floor(dodge_base_value * dodge_armor_hindrance) 
					value = math.floor(value * s_factor)
					value = math.floor(value * stance_mod[j])
					value = int(math.floor(value * 1.5))					
					
				evade_totals_arr.append(value)		
				
				if vs_type == "Melee":		
					evade_tooltip_text += "%+d = ((%s  x  %s  x  %.2f)  -  %s)  x  %.2f  (%s)\n" % (value, dodge_base_value, dodge_armor_hindrance, s_factor, shield_size_penalty, stance_mod[j], stance_arr[j]) 
				else:
					evade_tooltip_text += "%+d = %s  x  %s  x  %.2f   x  %.2f  x  1.5  (%s)\n" % (value, dodge_base_value, dodge_armor_hindrance, s_factor, stance_mod[j], stance_arr[j]) 
			
			evade_tooltip_text += "%+d (Dodge Base Value) calculated with:\n" % dodge_base_value			
			evade_tooltip_text += skill_tooltip_arr["Dodging"]		
			evade_tooltip_text += "    %s  Agility bonus\n" % (("%+d" % stat_enhancive_totals["Agility"]).rjust(4))
			evade_tooltip_text += stat_tooltip_arr["Agility"]		
			evade_tooltip_text += "    %s  Intuition bonus  (%+d / 4)\n" % (("%+d" % math.floor(stat_enhancive_totals["Intuition"]/4)).rjust(4), stat_enhancive_totals["Intuition"])		
			evade_tooltip_text += stat_tooltip_arr["Intuition"]				
			evade_tooltip_text += "%.2f (Armor Hindrance) calculated with:\n" % dodge_armor_hindrance		
			evade_tooltip_text += "    %+.2f  base modifier of %s\n" % (dodge_armor_hindrance, armor_gear.name.get())
			evade_tooltip_text += "%.2f (Shield Factor) calculated with:\n" % s_factor		
			evade_tooltip_text += "    %+.2f  base modifier of %s\n" % (shield_factor, other_hand_gear.name.get())
			evade_tooltip_text += ce_tooltip
			if vs_type == "Melee":		
				evade_tooltip_text += "%d (Shield Size Penalty) calculated with:\n" % shield_size_penalty		
				evade_tooltip_text += "  -%d base modifier of %s\n" % (shield_size_penalty, other_hand_gear.name.get())			
			
			
			
			
			# Calculate Effects values			
		
			# Calculate total of DS_All
			ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["DS_All"], "DS_All",  "effect_display", 0, "       ")
			effects_total = ce_total
			effects_tooltip_text += ce_tooltip		
			
			# Calculate total of attack type effects								
			if vs_type == "Melee":	
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["DS_Melee"], "DS_Melee",  "effect_display", 0, "       ")
				effects_total += ce_total
				effects_tooltip_text += ce_tooltip						
			elif vs_type == "Ranged":	
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["DS_Ranged"], "DS_Ranged",  "effect_display", 0, "       ")
				effects_total += ce_total
				effects_tooltip_text += ce_tooltip		
			elif vs_type == "Bolt":	
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["DS_Bolt"], "DS_Bolt",  "effect_display", 0, "       ")
				effects_total += ce_total
				effects_tooltip_text += ce_tooltip					
			
			if effects_tooltip_text != "":
					effects_tooltip_text = "  %s  bonus from Defense Strength effects\n" % (("%+d" % effects_total).rjust(4)) + effects_tooltip_text		
					
			effects_tooltip_text = "  %s  Enchantment bonus of %s\n" % (("%+d" % armor_enchantment).rjust(3), armor_gear.name.get()) + effects_tooltip_text	
			effects_total += armor_enchantment		
			effects_tooltip_text = "--Effects DS--\n" + effects_tooltip_text	
						
			# Calculate DS totals 						
			off_stance.append(parry_totals_arr[0] + shield_totals_arr[0] + evade_totals_arr[0] + effects_total)
			neu_stance.append(parry_totals_arr[1] + shield_totals_arr[1] + evade_totals_arr[1] + effects_total)
			adv_stance.append(parry_totals_arr[2] + shield_totals_arr[2] + evade_totals_arr[2] + effects_total)
			gua_stance.append(parry_totals_arr[3] + shield_totals_arr[3] + evade_totals_arr[3] + effects_total)
			for_stance.append(parry_totals_arr[4] + shield_totals_arr[4] + evade_totals_arr[4] + effects_total)
			def_stance.append(parry_totals_arr[5] + shield_totals_arr[5] + evade_totals_arr[5] + effects_total)
			
			# Create Tooltip info
			tooltip += "%s = %d  +  %d  +  %d  +  %d  (Offensive Stance)\n" % (("%+d" % off_stance[index]).rjust(4), parry_totals_arr[0], shield_totals_arr[0], evade_totals_arr[0], effects_total)
			tooltip += "%s = %d  +  %d  +  %d  +  %d  (Advanced Stance)\n" % (("%+d" % adv_stance[index]).rjust(4), parry_totals_arr[1], shield_totals_arr[1], evade_totals_arr[1], effects_total)
			tooltip += "%s = %d  +  %d  +  %d  +  %d  (Forward Stance)\n" % (("%+d" % for_stance[index]).rjust(4), parry_totals_arr[2], shield_totals_arr[2], evade_totals_arr[2], effects_total)
			tooltip += "%s = %d  +  %d  +  %d  +  %d  (Neutral Stance)\n" % (("%+d" % neu_stance[index]).rjust(4), parry_totals_arr[3], shield_totals_arr[3], evade_totals_arr[3], effects_total)
			tooltip += "%s = %d  +  %d  +  %d  +  %d  (Guarded Stance)\n" % (("%+d" % gua_stance[index]).rjust(4), parry_totals_arr[4], shield_totals_arr[4], evade_totals_arr[4], effects_total)
			tooltip += "%s = %d  +  %d  +  %d  +  %d  (Defensive Stance)\n" % (("%+d" % def_stance[index]).rjust(4), parry_totals_arr[5], shield_totals_arr[5], evade_totals_arr[5], effects_total)

			tooltip += parry_tooltip_text
			tooltip += off_hand_tooltip_text
			tooltip += shield_tooltip_text
			tooltip += evade_tooltip_text	
			tooltip += effects_tooltip_text
			
			self.graph_information.tooltip_array.append(tooltip[:-1])	
			index += 1
					
		# Setup graph_information object with new data
		if calc_style == 1:
			self.graph_information.graph_xlabel = "DS vs %s by Stance per Level" % (vs_type)
			self.graph_information.graph_xaxis_rotation = 0
			self.graph_information.graph_xlabel_size = 12
			self.graph_information.graph_xaxis_size = 12
			self.graph_information.graph_xaxis_tick_range = loop_range
			self.graph_information.graph_xaxis_tick_labels = [0,10,20,30,40,50,60,70,80,90,100]		
		elif calc_style == 2:
			self.graph_information.graph_xlabel = "DS vs %s by Stance per Postcap Experience Interval" % vs_type
			self.graph_information.graph_xaxis_rotation = 30
			self.graph_information.graph_xlabel_size = 10
			self.graph_information.graph_xaxis_size = 9			
			self.graph_information.graph_xaxis_tick_range = [i for i in range(index)]
			
			if len(postcap_intervals) <= 10:
				self.graph_information.graph_xaxis_tick_labels = [i for i in postcap_intervals]	
			else:
				temp = math.floor(len(postcap_intervals)/10)
				i = 0
								
				for interval in postcap_intervals:
					if i % temp == 0:
						self.graph_information.graph_xaxis_tick_labels.append(interval)
					i += 1		
					
		if off_stance[0] < def_stance[0]:			
			self.graph_information.graph_yaxis_min = off_stance[0] - 5
		else:	
			self.graph_information.graph_yaxis_min = def_stance[0] - 5
		self.graph_information.graph_yaxis_max = def_stance[-1] + 5	
		self.graph_information.graph_data_lists.append(off_stance)
		self.graph_information.graph_data_lists.append(adv_stance)
		self.graph_information.graph_data_lists.append(for_stance)
		self.graph_information.graph_data_lists.append(neu_stance)
		self.graph_information.graph_data_lists.append(gua_stance)
		self.graph_information.graph_data_lists.append(def_stance)
				
		self.graph_information.graph_num_lines = 6
		self.graph_information.graph_legend_columns = 3
		self.graph_information.graph_legend_labels.append("Offensive Stance")
		self.graph_information.graph_legend_styles.append("r^-")
		self.graph_information.graph_legend_labels.append("Neutral Stance")
		self.graph_information.graph_legend_styles.append("g*-")
		self.graph_information.graph_legend_labels.append("Advanced Stance")
		self.graph_information.graph_legend_styles.append("mD-")
		self.graph_information.graph_legend_labels.append("Guarded Stance")
		self.graph_information.graph_legend_styles.append("cH-")
		self.graph_information.graph_legend_labels.append("Forward Stance")
		self.graph_information.graph_legend_styles.append("yd-")
		self.graph_information.graph_legend_labels.append("Defensive Stance")
		self.graph_information.graph_legend_styles.append("bs-")

		self.graph_information.graph_ylabel = "Defense Strength"	


	# This method is used to calculate the character's Casting Strength (CS) from level 0-100 or across postcap training.
	# CS is calculated based on spell circles and due to the large amount of spell circles that exist in game, only 1-3 
	# spell circles are calculated at once and this is determined by the profession (or just Arcane) picked by the user.
	# All statistics skills, and effects that increase statistics or CS itself are included in these calculations.		
	def Formula_Casting_Strength(self, display_spell_circles, statistic_names, calc_style):
		index = 0
		loop_range = [i for i in range(101)]
		base_stat_arr = {}
		base_ranks_arr = {}
		postcap_intervals = []
		lists_of_effects_by_tag = {}	
		skill_names = []
		
		cs_effects_per_display = {}
		cs_tooltips_per_display = {}
		cs_tooltips_primary_secondary = ""
		casting_strength_totals = {}
		casting_strength_per_display_per_character = {}		
		character_spell_circles = globals.character.profession.spell_circles
		effects_list = ["CS_All", "CS_Elemental", "CS_Mental", "CS_Spiritual", "CS_Sorcerer"]

		# Populate the dictionaries with spell circle keys	
		for circle in display_spell_circles:
			self.graph_information.graph_legend_labels.append(circle)
			casting_strength_totals[circle] = []
			cs_effects_per_display[circle] = []
			cs_tooltips_per_display[circle] = []
			casting_strength_per_display_per_character[circle] = {}
			
		# Populate relevant skills and statistics	
		for circle in character_spell_circles:
			skill_names.append("Spell Research, %s" % circle)		
			for display in display_spell_circles:
				casting_strength_per_display_per_character[display][circle] = []
			
		for stat in statistic_names:
			effects_list.append("Statistic_Bonus_%s" % stat)
			effects_list.append("Statistic_%s" % stat)				
			
		lists_of_effects_by_tag = self.Find_Effects_By_Tags(effects_list)	
		

		# In Postcap mode, loop_range is not 0-100, instead its whatever postcap intervals that have training in the relevant skills
		if calc_style == 2:
			interval = 7575000
			for interval, training in globals.character.postcap_skill_training_by_interval.items():
				for skill in skill_names:
					if skill in training:
						postcap_intervals.append(interval)
						break										
							
			if len(postcap_intervals) == 0:
				postcap_intervals.append(7572500)
				postcap_intervals.append(interval)
			elif postcap_intervals[0] != 7572500:
				postcap_intervals.insert(0, 7572500)			
			
			if postcap_intervals[-1] != interval:
				postcap_intervals.append(interval)		
							
			loop_range = postcap_intervals


		# Begin the big loop to calculate all the data	
		for i in loop_range:
			stat_enh_bonus = 0
			effects_total = 0
			stat_enhancive_totals = {}
			stat_tooltip_text = ""
			stat_tooltip_arr = {}
			effects_tooltip_text = ""
						
						
			if calc_style == 1:
				tooltip = "Level %s: Casting Strength\n" % (i)
				for stat in statistic_names:				
					base_stat_arr[stat] = globals.character.statistics_list[stat].bonuses_by_level[i].get()	
				
				for skill in skill_names:
					base_ranks_arr[skill] = globals.character.skills_list[skill].total_ranks_by_level[i].get()
					
			elif calc_style == 2:	
				tooltip = "Postcap Experience Interval %s: Casting Strength\n" % ("{:,}".format(i))
				for stat in statistic_names:				
					base_stat_arr[stat] = globals.character.statistics_list[stat].bonuses_by_level[100].get()	
				
				for skill in skill_names:
					base_ranks_arr[skill] = globals.character.skills_list[skill].total_ranks_by_level[100].get()					
					base_ranks_arr[skill] += globals.character.skills_list[skill].Postcap_Get_Total_Ranks_Closest_To_Interval(i)
		

			# Calculate Statistic bonus	
			for stat in statistic_names:
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Statistic_Bonus_%s" % stat], "Statistic_Bonus_%s" % stat, "", 0, "            ")
				stat_enh_bonus = ce_total
				stat_tooltip_text = ce_tooltip
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Statistic_%s" % stat], "Statistic_%s" % stat, "stat_inc_to_bonus", 0, "            ")
				stat_enh_bonus += ce_total
				stat_tooltip_text = ce_tooltip + stat_tooltip_text				
				
				stat_enhancive_totals[stat] = base_stat_arr[stat] + min(50, stat_enh_bonus)				
				
				if stat_enh_bonus > 0:
					stat_tooltip_text = "       %s  enhancive %s bonus (%s vs max +20)\n" % (("%+d" % min(20, stat_enh_bonus)).rjust(4), stat, "%+d" % (stat_enh_bonus)) + stat_tooltip_text
				stat_tooltip_text = "       %s  %s base bonus\n" % (("%+d" % base_stat_arr[stat]).rjust(4), stat) + stat_tooltip_text						
				stat_tooltip_arr[stat] = stat_tooltip_text		
		
			# Calculate CS. Cycle through the spell circles we are showing and compare to each character user spell circles. 
			# Treat as primary if the match or secondary if not
			base_cs = min(300, i*3)
			current_cs = 0.0	
			total_cs = 0
			cs_stat = 0
			level = min(i, 100)
			level_secondary_var = math.ceil(i * 2/3)
			 
			for display_circle in display_spell_circles:
				total_cs = base_cs
				cs_tooltips_primary_secondary = ""
				for char_circle in character_spell_circles:
					ranks = base_ranks_arr["Spell Research, %s" % char_circle]
					current_cs = 0.0	
					# Do calculations if char_circle is the primary circle 
					if display_circle == char_circle:
						while ranks > 0:							
							if ranks <= level:
								current_cs += 1
							elif ranks <= (level+20):
								current_cs += 0.75
							elif ranks <= (level+60):
								current_cs += 0.5
							elif ranks <= (level+100):
								current_cs += 0.25
							else:
								current_cs += 0.125								
								
							ranks -= 1
						current_cs = int(math.ceil(current_cs))
						cs_tooltips_primary_secondary = "%s  Bonus from Primary Circle\n          %s  %s base ranks\n" % (("%+d" % current_cs).rjust(4), base_ranks_arr["Spell Research, %s" % char_circle], char_circle) + cs_tooltips_primary_secondary
						
					# Otherwise calculate it as a secondary circle
					else: 
						while ranks > 0:							
							if ranks <= level_secondary_var:
								current_cs += 0.333
							elif ranks <= level:
								current_cs += 0.1
							else:
								current_cs += 0.5								
								
							ranks -= 1
						current_cs = int(math.ceil(current_cs))
						cs_tooltips_primary_secondary += "%s  Bonus from Secondary Circle\n" % (("%+d" % current_cs).rjust(4))
						cs_tooltips_primary_secondary += "          %s %s base ranks\n" % (base_ranks_arr["Spell Research, %s" % char_circle], char_circle) 
						
					casting_strength_per_display_per_character[display_circle][char_circle] = current_cs					
					total_cs += current_cs

					
				# Calculate CS Effects values			
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["CS_All"], "CS_All",  "effect_display", 0, "       ")
				effects_total = ce_total
				effects_tooltip_text = ce_tooltip		
				
				if display_circle == "Bard" or display_circle == "Minor Elemental" or display_circle == "Major Elemental" or display_circle == "Wizard":
					ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["CS_Elemental"], "CS_Elemental",  "effect_display", 0, "       ")
				elif display_circle == "Monk" or display_circle == "Minor Mental" or display_circle == "Major Mental" or display_circle == "Savant":
					ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["CS_Mental"], "CS_Mental",  "effect_display", 0, "       ")
				elif display_circle == "Sorcerer" or display_circle == "Arcane":
					ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["CS_Sorcerer"], "CS_Sorcerer",  "effect_display", 0, "       ")
				else:
					ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["CS_Spiritual"], "CS_Spiritual",  "effect_display", 0, "       ")
						
				effects_total += ce_total
				effects_tooltip_text += ce_tooltip		
				if effects_tooltip_text != "":
						effects_tooltip_text = "%s  Bonus from Casting Strength effects\n" % (("%+d" % effects_total).rjust(4)) + effects_tooltip_text		
						
				cs_effects_per_display[display_circle] = effects_total				
				cs_tooltips_per_display[display_circle] = "%s  Base Casting Strength\n" % ("%+d" % base_cs).rjust(4)				
			
			
				# Find the relevant CS stat for the current spell circle and add it to the total CS
				if display_circle == "Bard" or display_circle == "Minor Elemental" or display_circle == "Major Elemental" or display_circle == "Wizard":
					cs_stat = int(stat_enhancive_totals["Aura"])					
					cs_tooltips_per_display[display_circle] += "%s  Bonus from Aura (%+d)\n" % (("%+d" % cs_stat).rjust(4), stat_enhancive_totals["Aura"])
					cs_tooltips_per_display[display_circle] += stat_tooltip_arr["Aura"]
				elif display_circle == "Monk" or display_circle == "Minor Mental":
					cs_stat = int(stat_enhancive_totals["Logic"])
					cs_tooltips_per_display[display_circle] += "%s  Bonus from Logic (%+d)\n" % (("%+d" % cs_stat).rjust(4), stat_enhancive_totals["Logic"])
					cs_tooltips_per_display[display_circle] += stat_tooltip_arr["Logic"]	
				elif display_circle == "Major Mental":
					cs_stat = math.ceil((stat_enhancive_totals["Influence"] + stat_enhancive_totals["Logic"]) / 2) 
					cs_tooltips_per_display[display_circle] += "%s  Avg of Influence (%+d), Logic (%+d)\n" % (("%+d" % cs_stat).rjust(4), stat_enhancive_totals["Influence"], stat_enhancive_totals["Logic"])
					cs_tooltips_per_display[display_circle] += stat_tooltip_arr["Influence"]	
					cs_tooltips_per_display[display_circle] += stat_tooltip_arr["Logic"]	
				elif display_circle == "Savant":
					cs_stat = math.ceil((stat_enhancive_totals["Discipline"] + stat_enhancive_totals["Logic"]) / 2) 
					cs_tooltips_per_display[display_circle] += "%s  Avg of Discipline (%+d), Logic (%+d)\n" % (("%+d" % cs_stat).rjust(4), stat_enhancive_totals["Discipline"], stat_enhancive_totals["Logic"])
					cs_tooltips_per_display[display_circle] += stat_tooltip_arr["Discipline"]	
					cs_tooltips_per_display[display_circle] += stat_tooltip_arr["Logic"]	
				elif display_circle == "Sorcerer":
					cs_stat = math.ceil((stat_enhancive_totals["Aura"] + stat_enhancive_totals["Wisdom"]) / 2) 
					cs_tooltips_per_display[display_circle] += "%s  Avg of Aura (%+d), Logic (%+d)\n" % (("%+d" % cs_stat).rjust(4), stat_enhancive_totals["Aura"], stat_enhancive_totals["Wisdom"])
					cs_tooltips_per_display[display_circle] += stat_tooltip_arr["Aura"]	
					cs_tooltips_per_display[display_circle] += stat_tooltip_arr["Wisdom"]	
				elif display_circle == "Arcane":
					cs_stat = math.ceil((stat_enhancive_totals["Wisdom"] + stat_enhancive_totals["Aura"] + stat_enhancive_totals["Logic"]) / 3) 
					cs_tooltips_per_display[display_circle] += "%s  Avg of Aura (%+d), Logic (%+d), Wisdom( %+d)\n" % (("%+d" % cs_stat).rjust(4), stat_enhancive_totals["Aura"], stat_enhancive_totals["Logic"], stat_enhancive_totals["Wisdom"])
					cs_tooltips_per_display[display_circle] += stat_tooltip_arr["Aura"]	
					cs_tooltips_per_display[display_circle] += stat_tooltip_arr["Logic"]	
					cs_tooltips_per_display[display_circle] += stat_tooltip_arr["Wisdom"]	
				else:
					cs_stat = int(stat_enhancive_totals["Wisdom"])			
					cs_tooltips_per_display[display_circle] += "%s  Bonus from Wisdom (%+d)\n" % (("%+d" % cs_stat).rjust(4), stat_enhancive_totals["Wisdom"])
					cs_tooltips_per_display[display_circle] += stat_tooltip_arr["Wisdom"]			
				
				cs_tooltips_per_display[display_circle] += cs_tooltips_primary_secondary
				cs_tooltips_per_display[display_circle] += "  " + effects_tooltip_text

				total_cs += cs_stat + effects_total
				casting_strength_totals[display_circle].append(total_cs)
				cs_tooltips_per_display[display_circle] = ("%+d calculated with:\n" % total_cs) + cs_tooltips_per_display[display_circle]
				cs_tooltips_per_display[display_circle] = "-- %s CS --\n" % (display_circle) + cs_tooltips_per_display[display_circle]
				
				
			# Create Tooltip info
			for display_circle in display_spell_circles:			
				tooltip += "  %+d = %d + %d + " % (casting_strength_totals[display_circle][index], base_cs, cs_stat)
				for char_circle in character_spell_circles:
					tooltip += "%d + " % (casting_strength_per_display_per_character[display_circle][char_circle])
				tooltip += "%d  (%s)\n" % (effects_total, display_circle)
			
			for display_circle in display_spell_circles:		
				tooltip += cs_tooltips_per_display[display_circle]
					
			self.graph_information.tooltip_array.append(tooltip[:-1])	
			index += 1
					
			
		self.graph_information.graph_ylabel = "Casting Strength"	
		if calc_style == 1:
			self.graph_information.graph_xlabel = "CS by Spell Circle per Level"
			self.graph_information.graph_xaxis_rotation = 0
			self.graph_information.graph_xlabel_size = 12
			self.graph_information.graph_xaxis_size = 12
			self.graph_information.graph_xaxis_tick_range = loop_range
			self.graph_information.graph_xaxis_tick_labels = [0,10,20,30,40,50,60,70,80,90,100]		
		elif calc_style == 2:
			self.graph_information.graph_xlabel = "CS by Spell Circle per Postcap Experience Interval"
			self.graph_information.graph_xaxis_rotation = 30
			self.graph_information.graph_xlabel_size = 10
			self.graph_information.graph_xaxis_size = 9			
			self.graph_information.graph_xaxis_tick_range = [i for i in range(index)]
			
			if len(postcap_intervals) <= 10:
				self.graph_information.graph_xaxis_tick_labels = [i for i in postcap_intervals]	
			else:
				temp = math.floor(len(postcap_intervals)/10)
				i = 0
								
				for interval in postcap_intervals:
					if i % temp == 0:
						self.graph_information.graph_xaxis_tick_labels.append(interval)
					i += 1			

		
		self.graph_information.graph_num_lines = len(display_spell_circles)
		self.graph_information.graph_legend_columns = len(display_spell_circles)
		
		legend_styles = ["r^-", "g*-", "mD-"]
		for style in legend_styles:
			self.graph_information.graph_legend_styles.append(style)					

		ymin = 5000
		ymax = 0
		for circle in display_spell_circles:
			ymin = min(ymin, casting_strength_totals[circle][0])
			ymax = max(ymax, casting_strength_totals[circle][0])
			ymin = min(ymin, casting_strength_totals[circle][-1])
			ymax = max(ymax, casting_strength_totals[circle][-1])
			self.graph_information.graph_data_lists.append(casting_strength_totals[circle])
		self.graph_information.graph_yaxis_min = ymin - 5	
		self.graph_information.graph_yaxis_max = ymax + 5	
		
	
	# This method is used to calculate the character's Target Defense (TD) from level 0-100 or across postcap training.
	# It calculates all four types of TD (elemental, mental, spiritual, sorcerer) at the same time. All statistics, and
	# effects that increase statistics or TD itself are included in this calculation.
	def Formula_Target_Defense(self, calc_style):
		char_race = globals.character.race
		racial_td = {"Elemental":int(char_race.elemental_td), "Mental":int(char_race.mental_td), "Spiritual":int(char_race.spiritual_td), "Sorcerer":int(char_race.sorc_td)}
		legend_styles = ["r^-", "g*-", "mD-"]
		effects_list = ["TD_All", "TD_Elemental", "TD_Mental", "TD_Spiritual", "TD_Sorcerer"]
		td_types = ["Elemental", "Mental", "Spiritual", "Sorcerer"]
		statistic_names = ["Aura", "Discipline", "Wisdom", ]
		td_totals_by_type = {}
		td_effects_per_type = {}
		td_tooltips_per_type = {}
		td_stat_per_type = {}
		index = 0
		loop_range = [i for i in range(101)]
		base_stat_arr = {}
		postcap_intervals = []
		lists_of_effects_by_tag = {}			
			
		# Setup the effects lists and td lists	
		for stat in statistic_names:
			effects_list.append("Statistic_Bonus_%s" % stat)
			effects_list.append("Statistic_%s" % stat)
			
		for type in td_types:
			td_totals_by_type[type] = []
			td_effects_per_type[type] = []
			td_stat_per_type[type] = []
			td_tooltips_per_type[type] = []
				
		lists_of_effects_by_tag = self.Find_Effects_By_Tags(effects_list)				

		# In Postcap mode, loop_range is not 0-100, instead its the first and last time the character trained in something
		if calc_style == 2:
			last_interval = 7575000

			for interval, training in globals.character.postcap_skill_training_by_interval.items():
				last_interval = interval
				
			postcap_intervals.append(7572500)	
			postcap_intervals.append(last_interval)				
							
			loop_range = postcap_intervals


		# Begin the big loop to calculate all the data	
		for i in loop_range:	
			ce_tooltip = ""					
			ce_total = 0
			stat_enh_stat = 0
			stat_enh_bonus = 0
			effects_total = 0
			stat_enhancive_totals = {}
			stat_tooltip_text = ""
			stat_tooltip_arr = {}
			skill_tooltip_arr = {}
			effects_tooltip_text = ""
		
			# Only a minor change depending on calc_style
			if calc_style == 1:
				tooltip = "Level %s: Target Defense\n" % (i)
				for stat in statistic_names:				
					base_stat_arr[stat] = globals.character.statistics_list[stat].bonuses_by_level[i].get()	
					
			elif calc_style == 2:	
				tooltip = "Postcap Experience Interval %s: Target Defense\n" % ("{:,}".format(i))
				for stat in statistic_names:				
					base_stat_arr[stat] = globals.character.statistics_list[stat].bonuses_by_level[100].get()					
		

			# Calculate Statistic bonus	
			for stat in statistic_names:
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Statistic_Bonus_%s" % stat], "Statistic_Bonus_%s" % stat, "", 0, "            ")
				stat_enh_bonus = ce_total
				stat_tooltip_text = ce_tooltip
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["Statistic_%s" % stat], "Statistic_%s" % stat, "stat_inc_to_bonus", 0, "            ")
				stat_enh_bonus += ce_total
				stat_tooltip_text = ce_tooltip + stat_tooltip_text				
				
				stat_enhancive_totals[stat] = base_stat_arr[stat] + min(50, stat_enh_bonus)				
				
				if stat_enh_bonus > 0:
					stat_tooltip_text = "       %s  enhancive %s bonus (%s vs max +20)\n" % (("%+d" % min(20, stat_enh_bonus)).rjust(4), stat, "%+d" % (stat_enh_bonus)) + stat_tooltip_text
				stat_tooltip_text = "       %s  %s base bonus\n" % (("%+d" % base_stat_arr[stat]).rjust(4), stat) + stat_tooltip_text						
				stat_tooltip_arr[stat] = stat_tooltip_text				
			
			# Calculate each type of TD
			td_base = min(300, i*3)
			level = min(100, i)
			for type in td_types:
				td_tooltips_per_type[type] = "%s  Base Target Defense\n" % ("%+d" % td_base).rjust(4)	

				td_tooltips_per_type[type] += "%s  %s racial bonus\n" % (("%+d" % racial_td[type]).rjust(4), char_race.name)
						
				# Add the relevant statistics to the TD
				if type == "Elemental":							
					td_stat_per_type[type] = stat_enhancive_totals["Aura"]
					td_tooltips_per_type[type] += "%s  Bonus from Aura (%+d)\n" % (("%+d" % td_stat_per_type[type]).rjust(4), stat_enhancive_totals["Aura"])
					td_tooltips_per_type[type] += stat_tooltip_arr["Aura"]
				elif type == "Mental":					
					td_stat_per_type[type] = stat_enhancive_totals["Discipline"]
					td_tooltips_per_type[type] += "%s  Bonus from Discipline (%+d)\n" % (("%+d" % td_stat_per_type[type]).rjust(4), stat_enhancive_totals["Discipline"])
					td_tooltips_per_type[type] += stat_tooltip_arr["Discipline"]
				elif type == "Spiritual":					
					td_stat_per_type[type] = stat_enhancive_totals["Wisdom"]
					td_tooltips_per_type[type] += "%s  Bonus from Wisdom (%+d)\n" % (("%+d" % td_stat_per_type[type]).rjust(4), stat_enhancive_totals["Wisdom"])
					td_tooltips_per_type[type] += stat_tooltip_arr["Wisdom"]
				elif type == "Sorcerer":					
					td_stat_per_type[type] = math.ceil((stat_enhancive_totals["Aura"] + stat_enhancive_totals["Wisdom"]) / 2)
					td_tooltips_per_type[type] += "%s  Avg of Aura (%+d), Wisdom (%+d)\n" % (("%+d" % td_stat_per_type[type]).rjust(4), stat_enhancive_totals["Aura"], stat_enhancive_totals["Wisdom"])
					td_tooltips_per_type[type] += stat_tooltip_arr["Aura"]
					td_tooltips_per_type[type] += stat_tooltip_arr["Wisdom"]
			
			
				# Calculate TD Effects values			
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["TD_All"], "TD_All",  "effect_display", 0, "       ")
				effects_total = ce_total
				effects_tooltip_text = ce_tooltip						
				
				ce_total, ce_tooltip = self.Combine_Effects(i, lists_of_effects_by_tag["TD_%s" % type], "TD_%s" % type,  "effect_display", 0, "       ")
						
				effects_total += ce_total
				effects_tooltip_text += ce_tooltip		
				if effects_tooltip_text != "":
						effects_tooltip_text = "%s  Bonus from Target Defense effects\n" % (("%+d" % effects_total).rjust(4)) + effects_tooltip_text		
						
				td_effects_per_type[type] = effects_total	
				td_totals_by_type[type].append(td_base + td_stat_per_type[type] + effects_total)
				td_tooltips_per_type[type] += "  " + effects_tooltip_text
				
				td_tooltips_per_type[type] = ("%+d calculated with:\n" % td_totals_by_type[type][index]) + td_tooltips_per_type[type]
				td_tooltips_per_type[type] = "-- %s TD --\n" % (type) + td_tooltips_per_type[type]
			
			
			# Create Tooltip info
			for type in td_types:			
				tooltip += "  %+d = %d + %d + %d + %d  (%s)\n" % (td_totals_by_type[type][index], td_base, racial_td[type], td_stat_per_type[type], td_effects_per_type[type], type)
			
			for type in td_types:		
				tooltip += td_tooltips_per_type[type]			
			
			self.graph_information.tooltip_array.append(tooltip[:-1])	

			index += 1
					
		
		# Loop is done, set up the graph_infomation object		
		self.graph_information.graph_ylabel = "Target Defense"	
		if calc_style == 1:
			self.graph_information.graph_xlabel = "TD by type per Level"
			self.graph_information.graph_xaxis_rotation = 0
			self.graph_information.graph_xlabel_size = 12
			self.graph_information.graph_xaxis_size = 12
			self.graph_information.graph_xaxis_tick_range = loop_range
			self.graph_information.graph_xaxis_tick_labels = [0,10,20,30,40,50,60,70,80,90,100]		
		elif calc_style == 2:
			self.graph_information.graph_xlabel = "TD by type per Postcap Experience Interval"
			self.graph_information.graph_xaxis_rotation = 30
			self.graph_information.graph_xlabel_size = 10
			self.graph_information.graph_xaxis_size = 9			
			self.graph_information.graph_xaxis_tick_range = [i for i in range(index)]
			
			if len(postcap_intervals) <= 10:
				self.graph_information.graph_xaxis_tick_labels = [i for i in postcap_intervals]	
			else:
				temp = math.floor(len(postcap_intervals)/10)
				i = 0
								
				for interval in postcap_intervals:
					if i % temp == 0:
						self.graph_information.graph_xaxis_tick_labels.append(interval)
					i += 1			

		ymin = 5000
		ymax = 0
		for type in td_types:
			ymin = min(ymin, td_totals_by_type[type][0])
			ymax = max(ymax, td_totals_by_type[type][0])
			ymin = min(ymin, td_totals_by_type[type][-1])
			ymax = max(ymax, td_totals_by_type[type][-1])
			self.graph_information.graph_data_lists.append(td_totals_by_type[type])
		self.graph_information.graph_yaxis_min = ymin - 5	
		self.graph_information.graph_yaxis_max = ymax + 5		

		# Setup the Legend
		self.graph_information.graph_num_lines = 4
		self.graph_information.graph_legend_columns = 4
		self.graph_information.graph_legend_labels.append("Elemental TD")
		self.graph_information.graph_legend_styles.append("r^-")
		self.graph_information.graph_legend_labels.append("Mental TD")
		self.graph_information.graph_legend_styles.append("g*-")
		self.graph_information.graph_legend_labels.append("Spiritual TD")
		self.graph_information.graph_legend_styles.append("mD-")
		self.graph_information.graph_legend_labels.append("Sorcerer TD")
		self.graph_information.graph_legend_styles.append("cH-")			
		
		

# This class is used in a single global object that tracks ALL that data needed to be graphed on the Figure
# The Formula methods will populate the object as the data calculated
class Graph_Data_Line_Container:	
	def __init__(self):		
		self.graph_num_lines = 0   				# How many lines do we need to graph?	
		
		self.graph_xlabel = ""					# Vertical left label
		self.graph_xlabel_size = 12
		self.graph_ylabel = ""					# Horizonal bottom label
		self.graph_yaxis_min = 0				# x-axis always has a set range. y will need to specified
		self.graph_yaxis_max = 0
		self.graph_xaxis_tick_range = []		
		self.graph_xaxis_tick_labels = []
		self.graph_xaxis_rotation = 0			# This is changed
		self.graph_xaxis_size = 12
		
		self.graph_legend_columns = 1
		self.graph_legend_labels = []
		self.graph_legend_styles = []
		
		self.graph_data_lists = []				# Where the calculated information is stored in a 100 sized array for precap or variable sized for postcap
		self.tooltip_array = []					# Tooltip text detailing how the above data was calculated. Same size as graph_data_lists
	
	# Resets the object back to default so it can be reused by a new Formula method
	def Reset_Graph_Data(self):	
		self.graph_num_lines = 0   		
		
		self.graph_xlabel = ""
		self.graph_xlabel_size = 12
		self.graph_ylabel = ""	
		self.graph_yaxis_min = 0
		self.graph_yaxis_max = 0
		self.graph_xaxis_tick_range = []
		self.graph_xaxis_tick_labels = []
		self.graph_xaxis_rotation = 0
		self.graph_xaxis_size = 12
		
		self.graph_legend_columns = 1
		self.graph_legend_labels = []
		self.graph_legend_styles = []
		
		self.graph_data_lists = []	
		self.tooltip_array = []	
	
		
		
