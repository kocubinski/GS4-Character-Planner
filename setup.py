# This file create the .exe file and the other necessary files that allow computers without Python installed to run the Planner.

# How to generate the .exe (needs Python 3.4 installed with the cx_Freeze module)
# Run "py setup.py build" in the command prompt
# If GS4_Planner.db doesn't exist, run "py Create_Database.py" in the command prompt
# Copy the database file into the folder with the .exe file
# Make a folder called Characters in the main directory as well. This is where Character files are saved/loaded by default
# The Planner should now run


#!/usr/bin/python

import sys
from cx_Freeze import setup, Executable

#base = None
if sys.platform == "win32":
	base = "Win32GUI"	
setup(name="GS4 Character Planner", version="2.3", description="GS4 Character Planner", executables=[Executable("Planner.py", base=base)])
