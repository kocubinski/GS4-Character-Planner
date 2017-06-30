# INDEX OF CLASSES AND METHODS
'''
class Misc_Panel
	def __init__(self, panel)
	def Create_General_Frame(self, panel):	
	def Create_Guild_Frame(self, panel):
	def Create_Profession_Frame(self, panel):	
	def Reset_Panel(self):
	def Society_Onchange(self, name):
	def Society_Entrybox_Validate(self, d, S, s, P):
	
	
class Guild_Skill_Row
	def __init__(self, panel, number):	
	def Entrybox_Validate(self, d, S, s, P):	
	def Entrybox_On_Update(self, *args):	
	def Entrybox_On_Move(self, event):	
'''


#!/usr/bin/python

import tkinter
import Pmw
import Globals as globals
  
  
# Misc Panel will contain everything that is either too small to have it's own panel or doesn't fit with any other panel
class Misc_Panel:  
	def __init__(self, panel):			
		self.guild_skill_rows = []
		
		#Create all the sub-frames of the panel
		self.First_Frame = self.Create_General_Frame(panel)
		self.Second_Frame = self.Create_Guild_Frame(panel)
#		self.Bottom_Frame = self.Create_Profession_Frame(panel)
		
		#Make the frames visible
		self.First_Frame.grid(row=0, column=0, sticky="nw")
		self.Second_Frame.grid(row=0, column=1, sticky="nw")
#		self.Bottom_Frame.grid(row=2, column=0, sticky="nw")


		# Initialize the variables to default
		globals.character.deity.set("None")
		globals.character.elemental_attunement.set("None")
		globals.character.society.set("None")
		globals.character.society_rank.set("0")

		
	# This information is universal to all professions.
	def Create_General_Frame(self, panel):
#		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 1100, hull_height = 250)
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 335, hull_height = 165)
		myframe.component("borderframe").config(borderwidth=0)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")	
		myframe_inner = myframe.interior()
		
		tkinter.Label(myframe_inner, width="46", bg="lightgray", anchor="w", text="General Character Information").grid(row=0, column=0, sticky="w")
		
#		genframe = Pmw.ScrolledFrame(myframe_inner, usehullsize = 1, hull_width = 1093, hull_height = 228)
		genframe = Pmw.ScrolledFrame(myframe_inner, usehullsize = 1, hull_width = 328, hull_height = 143)		
		genframe.configure(hscrollmode = "none", vscrollmode = "none")	
		genframe_inner = genframe.interior()		
		genframe.grid(row=1, column=0, sticky="w")
		
		# Deity
		frame1 = tkinter.Frame(genframe_inner)
		frame1.grid(row=0, column=0, sticky="w")
		tkinter.Label(frame1, width="15", bg="lightgray", anchor="w", text="Deity").grid(row=0, column=0)
		choices = ["None", "Aeia", "Amasalen", "Andelas", "Arachne", "Charl", "Cholen", "Eonak", "Eorgina", "Fash'lo'nae", "Gosaena", "Imaera", 
		"Jastev", "Jaston", "Kai", "Kuon", "Laethe", "Leya", "Lorminstra", "Lumnis", "Luukos", "Mularos", "Marlu", "Niima", "Onar", "Phoen", 
		"Ronan", "Sheru", "The Huntress", "Tilamaire", "Tonis", "Voaris", "Voln", "V'tull", "Zelia", "Other"]
		deity_menu = tkinter.OptionMenu(frame1, globals.character.deity, *choices)
		deity_menu.config(width=18)	
		deity_menu.grid(row=0, column=1, sticky="w")		

		# Elemental Attunement
		frame2 = tkinter.Frame(genframe_inner)
		frame2.grid(row=1, column=0, sticky="w")
		tkinter.Label(frame2, width="15", bg="lightgray", anchor="w", text="Attunement").grid(row=0, column=0)
		elements = ["None", "Air", "Earth", "Fire", "Lightning", "Water"]
		elements_menu = tkinter.OptionMenu(frame2, globals.character.elemental_attunement, *elements)
		elements_menu.config(width=18, heigh=1)	
		elements_menu.grid(row=0, column=1, sticky="w")		

		# Soceity rank. 
		frame3 = tkinter.Frame(genframe_inner)
		frame3.grid(row=2, column=0, sticky="w")
		tkinter.Label(frame3, width="15", bg="lightgray", anchor="w", text="Society and Rank").grid(row=0, column=0)
		society = ["None", "Council of Light", "Guardians of Sunfist", "Order of Voln"]
		society_menu = tkinter.OptionMenu(frame3, globals.character.society, *society, command=self.Society_Onchange)
		society_menu.config(width=18, heigh=1)	
		society_menu.grid(row=0, column=1, sticky="w")	

		mycmd = (globals.root.register(self.Society_Entrybox_Validate), '%d', '%S', '%s', '%P')	
		entrybox = tkinter.Entry(frame3, width="5", justify="center", validate="key", validatecommand=mycmd, textvariable=globals.character.society_rank)
		entrybox.grid(row=0, column=2, sticky="w", padx="3")
		
		return myframe

		
	# Any guild skill the profession has will go in this frame. Any value between 0-63 is valid and an empty string is treated as a 0.
	def Create_Guild_Frame(self, panel):
#		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 1100, hull_height = 250)
		myframe = Pmw.ScrolledFrame(panel, usehullsize = 1, hull_width = 280, hull_height = 165)
		myframe.component("borderframe").config(borderwidth=0)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")	
		myframe_inner = myframe.interior()		
		
#		genframe = Pmw.ScrolledFrame(myframe_inner, usehullsize = 1, hull_width = 1093, hull_height = 228)
		genframe = Pmw.ScrolledFrame(myframe_inner, usehullsize = 1, hull_width = 173, hull_height = 143)	
		genframe.configure(hscrollmode = "none", vscrollmode = "none")	
		genframe_inner = genframe.interior()		
		
		tkinter.Label(myframe_inner, width="24", bg="lightgray", anchor="w", text="Guild Skills Ranks").grid(row=0, column=0, sticky="w")		
		genframe.grid(row=1, column=0, sticky="w")
		
		for i in range(6):
			self.guild_skill_rows.append(Guild_Skill_Row(self, genframe_inner, i))			
		
		return myframe

		
	# Placeholder. Only the Ranger's animal companion would go in this panel. I will make this one if I can find more profession specific abilities.	
	def Create_Profession_Frame(self, panel):
		pass


	def Reset_Panel(self):
		globals.character.deity.set("None")
		globals.character.elemental_attunement.set("None")
		globals.character.society.set("None")
		globals.character.society_rank.set("0")
		
		for gs in globals.character.guild_skills_ranks:
			gs.set(0)
			
		for i in range(6):
			name = globals.character.profession.guild_skills[i]
			self.guild_skill_rows[i].name.set(name)
			
			if name == "NONE":
				self.guild_skill_rows[i].frame.grid_remove()			
			else:
				self.guild_skill_rows[i].frame.grid(row=i, column=0, sticky="w")		
		
		
	# Changing the society will make sure the ranks fall in the correct bounds for the new society. GoS and CoL can have 0-20 ranks while Voln has 0-26. 
	def Society_Onchange(self, name):
		ranks = globals.character.society_rank.get()
		
		if( ranks == "" or name == "None" ):
			globals.character.society_rank.set(0)		
		elif( (name == "Council of Light" or name == "Guardians of Sunfist") and int(ranks) > 20 ):
			globals.character.society_rank.set(20)


	# Make sure the value in the box is appropriate for the society. GoS and CoL can have 0-20 ranks while Voln has 0-26.	
	def Society_Entrybox_Validate(self, d, S, s, P):
		society = globals.character.society.get()
#		print("event %s" % (d))
#		print("%s was added/deleted to entry box. Was previously %s" % (S, s))
		if( d == "1"):
			if( society == "None"):
				return False
			if( (len(s) + len(S)) > 2 ):
				return False
			try:				
				if( float(P) <= 26 and society == "Order of Voln" ):	
					return True
				elif( float(P) <= 20 and (society == "Council of Light" or society == "Guardians of Sunfist") ):
					return True
				else:
					return False
			except ValueError:
				return False
		return True

	
# This object is a row that contains the guild skill information for the profession's 6 guild skills. Profession with less than 6 declare the rest as "NONE" and are hidden
class Guild_Skill_Row:
	def __init__(self, panel, inner_frame, number):		
		self.parent = panel
		self.name = tkinter.StringVar()
		self.frame = tkinter.Frame(inner_frame)
		self.order = number
		mycmd = (globals.root.register(self.Entrybox_Validate), '%d', '%S', '%s', '%P')
		self.entrybox = tkinter.Entry(self.frame, width="5", justify="center", validate="key", validatecommand=mycmd, textvariable=globals.character.guild_skills_ranks[number])
	
		tkinter.Label(self.frame, width="15", anchor="w", bg="lightgray", textvar=self.name).grid(row=0, column=0, padx="1", pady="1")
		self.entrybox.grid(row=0, column=1, padx="1")
	
		self.entrybox.bind("<Down>", self.Entrybox_On_Move)
		self.entrybox.bind("<Up>", self.Entrybox_On_Move)		

		
	# Makes sure that the character placed in the Entry box doesn't make the length greater than 3 and that the value is less than or equal to 100. False results prevent the edit from occuring.
	def Entrybox_Validate(self, d, S, s, P):		
#		print("event %s" % (d))
#		print("%s was added/deleted to entry box. Was previously %s" % (S, s))
		if( d == "1"):
			if( (len(s) + len(S)) > 2 ):
				return False
			try:				
				if( float(P) <= 63 ):	
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
		gs_rows = self.parent.guild_skill_rows
		new_order = self.order
		
		if event.keysym == "Up":
			new_order -= 1					
		elif event.keysym == "Down":
			new_order += 1			
			
		if new_order < 0 or new_order > 5:
			return
			
		gs_rows[new_order].entrybox.focus()
		gs_rows[new_order].entrybox.icursor("end")
		
