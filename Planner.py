#!/usr/bin/python

import sys
from cx_Freeze import setup, Executable
from tkinter import *
import Pmw
import Globals as globals
import Character as char
import Statistics_Panel as StP

#base = None
#if sys.platform == "win32":
#	base = "Win32GUI"
	
#setup(name="Testing", version="2.0", description="GS4 Character Planner", executables=[Executable("Planner.py", base=base)])


class Planner(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)		
		self.parent = parent
		self.character = char.Character()
		
		self.character.StP_Init_Statistics(globals.statistics_list)		
		self.Planner_Create_Menu()
		self.MakeNotebook(self)
		
	def initialize(self):
		self.grid()
		self.button = Button(self)
		self.button["text"] = "click me"
		self.button.grid(row = 1, column = 1, sticky = W)

	def Planner_Create_Menu(self):
		menubar = Menu(self.parent)
		self.parent.config(menu=menubar)
		filemenu = Menu(menubar, tearoff=0)
		menubar.add_cascade(label="File", menu=filemenu)
		filemenu.add_command(label="New", command=self.donothing)
		filemenu.add_command(label="Open", command=self.donothing)
		filemenu.add_command(label="Save as...", command=self.donothing)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.parent.quit)
	
	def MakeNotebook(self, parent):
		self.notebook = Pmw.NoteBook(self.parent,
                tabpos = 'n',
         #       createcommand = PrintOne('Create'),
         #       lowercommand = PrintOne('Lower'),
       #         raisecommand = PrintOne('Raise'),
                hull_width = 300,
                hull_height = 300,
                )
				
		self.notebook.pack(fill = 'both', expand = 1, padx = 5, pady = 5)
		page1 = self.notebook.add('Statistics')		
		page2 = self.notebook.add('Skills')				
		page3 = self.notebook.add('Maneuvers')		
		self.notebook.tab('Statistics').focus_set()
		frame1 = Frame(page1, background="white")
		frame1.grid(row=0, column=0)
		StP.Statistics_Panel(self.parent, frame1, parent.character)
		
		
	def donothing(self):
		pass		
		
		
if __name__ == "__main__":
	#root = Tk();
	globals.root.title("Gemstone IV Character Planner");
	globals.root.geometry("1200x600")
	planner = Planner(globals.root)	
	globals.root.mainloop();	
	
