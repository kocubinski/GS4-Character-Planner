# TODO LIST
# Consider adding more to ShowPage and HidePage functions that will cleanup, load. unload information.
# Error Dialog Box needs at least 2 buttons to be createable. Figure out what button2 should be called and what it should do. 


#!/usr/bin/python

import sys
import os
import sqlite3
import tkinter
import Pmw
import Globals as globals
import Character as char
import Statistics_Panel as StP
import Skills_Panel as SkP


# Planner is the main object in script.
class Planner:
	def __init__(self, parent):
#		tkinter.Frame.__init__(self, parent)	
		self.parent = parent
		self.pages = {}
		self.panels_loaded = 0
		
		globals.character = char.Character()
		globals.db_cur.execute("SELECT * FROM Races WHERE name='%s'" % 'Human')
		globals.db_con.commit()		
		data = globals.db_cur.fetchone()
		globals.character.race = globals.Race(data)	
		globals.db_cur.execute("SELECT * FROM Professions WHERE name='%s'" % 'Warrior')
		globals.db_con.commit()		
		data = globals.db_cur.fetchone()
		globals.character.profession = globals.Profession(data)	
		globals.db_cur.execute("SELECT name FROM Skills" )
		globals.db_con.commit()		
		data = globals.db_cur.fetchall()		
		for skill in data:
			globals.skills.append(skill[0])				
			
		
		self.Planner_Create_Menu()
		self.MakeNotebook(self)
		globals.error_dialog = self.Create_Error_Dialog()
		globals.error_dialog.withdraw()
		
	# This error dialog box is used by all panels to display errors that occur in the planner.
	def Create_Error_Dialog(self):
		width = 400; height = 250; xpos = 450; ypos = 300
		dialog = Pmw.Dialog(self.parent,
            buttons = ("Okay", "Not Okay"),
            title = "Error",
            command = self.Dialog_Box_Onclick)
			
		dialog.transient(self.parent)	
		dialog.resizable(width=0, height=0)		
		dialog.geometry('%sx%s+%s+%s' % (width, height, xpos, ypos))

		myframe = Pmw.ScrolledFrame(dialog.interior(), usehullsize = 1, hull_width = width, hull_height = height)
		myframe.configure(hscrollmode = "none", vscrollmode = "none")		
		myframe.grid(row=0, column=0, sticky="nw")	
		myframe_inner = myframe.interior()			
		tkinter.Label(myframe_inner, anchor="w", font="-weight bold", wraplength=width, justify="left", textvariable=globals.error_dialogmsg).grid(row=0, column=0, sticky="w")
		
		return dialog

	# Handles the button click events for the error dialog box	
	def Dialog_Box_Onclick(self, result):
		globals.error_dialog.withdraw()
		globals.error_dialogmsg.set("")	
		globals.error_event = 0

	# Makes the top menu that appears horizontally across the top of the planner
	def Planner_Create_Menu(self):
		menubar = tkinter.Menu(self.parent)
		self.parent.config(menu=menubar)
		filemenu = tkinter.Menu(menubar, tearoff=0)
		menubar.add_cascade(label="File", menu=filemenu)
		filemenu.add_command(label="New", command=self.donothing)
		filemenu.add_command(label="Open", command=self.donothing)
		filemenu.add_command(label="Save as...", command=self.donothing)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.parent.quit)

	# Python megawidget that creates and holds all the panels	
	def MakeNotebook(self, parent):
		self.notebook = Pmw.NoteBook(self.parent,
                tabpos = 'n',
         #       createcommand = PrintOne('Create'),
                lowercommand = self.HidePage,
                raisecommand = self.ShowPage,
                hull_width = 300,
                hull_height = 300,
                )
				
		self.notebook.pack(fill = 'both', expand = 1, padx = 5, pady = 5)
		page1 = self.notebook.add('Statistics')		
		page2 = self.notebook.add('Skills')				
		page3 = self.notebook.add('Maneuvers')		
		self.pages['Statistics'] = tkinter.Frame(page1, background="white")
		globals.panels['Statistics'] = StP.Statistics_Panel(self.parent, self.pages['Statistics'])		
		self.pages['Skills'] = tkinter.Frame(page2, background="white")
		globals.panels['Skills'] = SkP.Skills_Panel(self.parent, self.pages['Skills'])
		
		self.pages['Statistics'].grid(row=0, column=0)
		self.pages['Skills'].grid(row=0, column=1)
	
		# sets up defaults for each panel
		globals.character.Update_Skills(globals.character.profession.name)
		globals.panels['Statistics'].Change_Race("Human")
		globals.panels['Skills'].Create_Schedule()              
#		self.panels_loaded = 1
#		self.notebook.selectpage('Maneuvers')						# Debug option	

	# Temporary until the top menu options are made
	def donothing(self):
		pass		

		
	def ShowPage(self, caller):	
		if self.panels_loaded == 1:
			print("show")
			self.pages[caller].grid(row=0, column=0)

			
	def HidePage(self, caller):	
		if self.panels_loaded == 1:
			print("hide")
			self.pages[caller].grid_remove()
		
		
if __name__ == "__main__":
	if not os.path.isfile(globals.db_file):	
		print("ERROR: GS4_Planner.db file not found.")
		sys.exit(1)
	else:
		globals.db_con = sqlite3.connect(globals.db_file)
		globals.db_con.row_factory = sqlite3.Row
		globals.db_cur = globals.db_con.cursor()
		globals.root.title("Gemstone IV Character Planner %s" % globals.version);
		globals.root.geometry("1200x600")
		planner = Planner(globals.root)	
		globals.root.mainloop();		
