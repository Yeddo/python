# Import Libraries
import os, sys
from Tkinter import *           # Import the Tkinter library

#declare variables
APPLCIATIONS = "/Applications"

#begin
#print os.listdir(APPLCIATIONS)

root = Tk()                    # Create a background window object
li = os.listdir(APPLCIATIONS)  # Create list based on directory listing of /Applications
listb  = Listbox(root)          # Create listbox widget
for item in li:                 # Insert each item inside li into the listb
    listb.insert(0,item)

listb.pack()                    # Pack listbox into the main window
root.mainloop()                 # Invoke the main event handling loop