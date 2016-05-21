# INDEX OF CLASSES AND METHODS
'''
class Planner
	def _init__(self, parent)
	def Create_Top_Menubar(self):	
	def Menubar_Option_New_Character(self):
	def Menubar_Option_Load_Character(self):
	def Menubar_Option_Save_Character(self):
	def Create_Notebook(self, parent):
	def Notebook_OnShowPage(self, caller):	
	def Notebook_OnHidePage(self, caller):
'''

#!/usr/bin/python

import sys
import os
import sqlite3
import tkinter
import Pmw
import Globals as globals
import Statistics_Panel as StP
import Skills_Panel as SkP
import Maneuvers_Panel as ManP
import PostCap_Panel as PcP


# Planner is the primary window in the program that holds everything else.
# Planner is responsible for creating top Menubar and the Notebook used to store each Panel
class Planner:
	def __init__(self, parent):	
		self.parent = parent
		self.pages = {}
		self.panels_loaded = 0		
			
		# Create top Menubar used to Save and Load character builds
		self.Create_Top_Menubar()
		
		# Create the Notebook used to hold all the Panels and then create each Panel to be held in the Notebook
		self.Create_Notebook(self)

		
	# Makes the top menu that appears horizontally across the top of the planner
	def Create_Top_Menubar(self):
		menubar = tkinter.Menu(self.parent)
		self.parent.config(menu=menubar)
		filemenu = tkinter.Menu(menubar, tearoff=0)
		menubar.add_cascade(label="File", menu=filemenu)
		filemenu.add_command(label="New Character", command=self.Menubar_Option_New_Character)              # Reset planner to default 
		filemenu.add_command(label="Load Character", command=self.Menubar_Option_Load_Character)             # Open and load a character save file into the planner
		filemenu.add_command(label="Save Character as...", command=self.Menubar_Option_Save_Character)       # Save an existing build to file
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.parent.quit)


	def Menubar_Option_New_Character(self):
		globals.char_name = "New Character"
		for stat, obj in globals.character.statistics_list.items():
			obj.Set_To_Default()
		globals.panels['Skills'].ClearAll_Button_Onclick()
		globals.panels['Maneuvers'].Clear_Button_Onclick("All")
		globals.panels['Post Cap'].Clear_Button_Onclick("All")
		globals.root.title("%s %s - %s" % (globals.title, globals.version, globals.char_name))


	def Menubar_Option_Load_Character(self):
		globals.character.Load_Character()

		
	def Menubar_Option_Save_Character(self):
		globals.character.Save_Character()
		
		
	# Method uses a Python megawidget, Notebook, to create and hold all the Panels	
	def Create_Notebook(self, parent):
		globals.notebook = Pmw.NoteBook(self.parent,
                tabpos = 'n',
         #       createcommand = PrintOne('Create'),
         #       lowercommand = self.Notebook_OnHidePage,
         #       raisecommand = self.Notebook_OnShowPage,
                hull_width = 300,
                hull_height = 300,
                )				
		globals.notebook.pack(fill = 'both', expand = 1, padx = 5, pady = 5)
		
		# Create the pages (tabs) for each panel and add them to the notebook
		page1 = globals.notebook.add('Statistics')		
		page2 = globals.notebook.add('Skills')				
		page3 = globals.notebook.add('Maneuvers')				
		page4 = globals.notebook.add('Post Cap')	
		self.pages['Statistics'] = tkinter.Frame(page1, background="white")
		self.pages['Skills'] = tkinter.Frame(page2, background="white")
		self.pages['Maneuvers'] = tkinter.Frame(page3, background="white")
		self.pages['Post Cap'] = tkinter.Frame(page4, background="white")
		self.pages['Statistics'].grid(row=0, column=0)
		self.pages['Skills'].grid(row=0, column=1)
		self.pages['Maneuvers'].grid(row=0, column=2)
		self.pages['Post Cap'].grid(row=0, column=3)
		
		# Create each Panel. Each is added to the a global list so they can be referenced later
		globals.panels['Statistics'] = StP.Statistics_Panel(self.pages['Statistics'])		
		globals.panels['Skills'] = SkP.Skills_Panel(self.pages['Skills'])	
		globals.panels['Maneuvers'] = ManP.Maneuvers_Panel(self.pages['Maneuvers'])
		globals.panels['Post Cap'] = PcP.PostCap_Panel(self.pages['Post Cap'])
	
		# Set up defaults
		globals.panels['Statistics'].Change_Race("Human")
		globals.panels['Statistics'].Change_Profession("Warrior")  		

	
	# Temporary. This might be used to quickly load calculations for some Panels
	def Notebook_OnShowPage(self, caller):	
		if self.panels_loaded == 1:
			print("show")
			self.pages[caller].grid(row=0, column=0)

			
	# Temporary. This might be used to quickly hide or erase data from a Panel when it is hidden	
	def Notebook_OnHidePage(self, caller):	
		if self.panels_loaded == 1:
			print("hide")
			self.pages[caller].grid_remove()
			

# Start of the program. Unless the SQLite database exist it will exit. Otherwise, setup the database and create the Planner.			
if __name__ == "__main__":
	if not os.path.isfile(globals.db_file):	
		print("ERROR: GS4_Planner.db file not found.")
		sys.exit(1)
	
	globals.db_con = sqlite3.connect(globals.db_file)
	globals.db_con.row_factory = sqlite3.Row
	globals.db_cur = globals.db_con.cursor()
	globals.root.title("%s %s - %s" % (globals.title, globals.version, globals.char_name))
	globals.root.geometry("1140x600")
	globals.root.resizable(0,0)
	planner = Planner(globals.root)	
	globals.root.mainloop();		
