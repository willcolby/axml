from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class HelloApp:

    def __init__(self, master):

        #VARIABLES FOR ENTRIES
        self.input = StringVar(master)
        self.input.set("Select your xml...")

        self.output = StringVar(master)
        self.output.set("Name your new xml...")
        
        self.mode = StringVar(master)
        self.mode.set("Interval")
        
        self.duration = StringVar(master)
        self.duration.set("00:02:00:00")

        #UI ELEMENTS
        #TITLE
        self.title = Label(master, text = "AXML", font = ("Futura", 24), foreground = "#2a416c", padx = 100, pady = 10)
        self.title.grid(row = 0, column = 0, columnspan = 3)

        #INPUT
        self.input_label = Label(master, text = "Input Sequence:", foreground = "#2a416c")
        self.input_label.grid(row = 1, column = 0, sticky=E)

        self.input_file = Entry(master, foreground = "#2a416c", textvariable = self.input)
        self.input_file.grid(row = 1, column = 1, sticky=W)

        self.input_button = Button(master, text = "...", foreground = "#2a416c")
        self.input_button.grid(row = 1, column = 2, sticky=W)

        #OUTPUT
        self.output_label = Label(master, text = "Export Sequence:", foreground = "#2a416c")
        self.output_label.grid(row = 2, column = 0, sticky=E)

        self.output_file = Entry(master, foreground = "#2a416c", textvariable = self.output)
        self.output_file.grid(row = 2, column = 1, sticky=W)

        self.output_button = Button(master, text = "...", foreground = "#2a416c")
        self.output_button.grid(row = 2, column = 2, sticky=W)

        #DURATION
        self.duration_label = Label(master, text = "New Sequence Duration:", foreground = "#2a416c")
        self.duration_label.grid(row = 3, column = 0, sticky=E)

        self.duration_file = Entry(master, foreground = "#2a416c", textvariable = self.duration)
        self.duration_file.grid(row = 3, column = 1, sticky=W)

        #MODE
        self.mode_label = Label(master, text = "Mode:", foreground = "#2a416c")
        self.mode_label.grid(row = 4, column = 0, sticky=E)

        self.mode_menu = OptionMenu(master, self.mode, "Interval","Random","Rhythmic","Hyper","Draw")
        self.mode_menu.grid(row = 4, column = 1, sticky=W)

        #GO!
        self.go = Button(master, text = "GO!", font = ("Futura", 20), foreground = "#2a416c", padx = 20, pady = 10)
        self.go.grid(row = 5, column = 0, columnspan = 2)

def main():

    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if __name__ == "__main__": main()
