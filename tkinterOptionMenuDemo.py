# File name: tkinterOptionMenuDemo.py
# Changing/adding/deleting options to OptionMenu on the fly
# Author: S.Prasanna

from Tkinter import *
import tkMessageBox

def displayOption():
    """ Display the OptionMenu selection. """

    global optionMenuWidget, DEFAULTVALUE_OPTION

    if (optionMenuWidget.cget("text") == DEFAULTVALUE_OPTION):
        tkMessageBox.showerror("Tkinter OptionMenu Widget", "Select a valid option.")
    else:
        tkMessageBox.showinfo("Tkinter OptionMenu Widget", "OptionMenu value = " + optionMenuWidget.cget("text"))

def addMenuOptions():
    """ Add Menu options dynamically """

    global optionMenuWidget

    optionMenuWidget["menu"].delete(0, END)
    # Add options from 1 to 5
    for i in range(1, 6):
        optionMenuWidget["menu"].add_command(label=i, command=lambda temp = i: optionMenuWidget.setvar(optionMenuWidget.cget("textvariable"), value = temp))
                
if __name__ == "__main__":

    root = Tk()
    DEFAULTVALUE_OPTION = "Select an option."    
    
    root.title("Tkinter OptionMenu Widget")
    root["padx"] = 40
    root["pady"] = 20       

    # Create an Option frame to hold the option Label and the optionMenu widget
    optionFrame = Frame(root)
    
    #Create a Label in textFrame
    optionLabel = Label(optionFrame)
    optionLabel["text"] = "OptionsMenu demo"
    optionLabel.pack(side=LEFT)

    # Create an optionMenu Widget in the optionFrame
    optionTuple = ("",)
    
    defaultOption = StringVar()
    optionMenuWidget = apply(OptionMenu, (optionFrame, defaultOption) + optionTuple)
    addMenuOptions()
    defaultOption.set(DEFAULTVALUE_OPTION)
    optionMenuWidget["width"] = 15
    optionMenuWidget.pack(side=LEFT)

    optionFrame.pack()

    button = Button(root, text="Submit", command=displayOption)
    button.pack() 
    
    root.mainloop()
