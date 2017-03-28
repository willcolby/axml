from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):



        self.title = Label(master, text = "AXML", font = ("Futura", 24), foreground = "#2a416c", padx=200, pady=10)
        self.title.grid(row = 0, column = 0, columnspan = 3)

        self.input_label = Label(master, text = "INPUT",font = ("Futura", 20), foreground = "White", background = "#2a416c", padx=50, pady=10)
        self.input_label.grid(row =1, column = 0)
        
        self.manipulate_label = Label(master, text = "MANIPULATE",font = ("Futura", 20), foreground = "White", background = "#223557", padx=50, pady=10)
        self.manipulate_label.grid(row = 1, column = 1)
        
        self.output_label = Label(master, text = "OUTPUT",font = ("Futura", 20), foreground = "White", background = "#2a416c", padx=50, pady=10)
        self.output_label.grid(row = 1, column = 2)

        self.input_dialog = Label(master, text="?", background = "#223557")
        self.input_dialog.grid(row =1, column = 0)

def main():

    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if __name__ == "__main__": main()
