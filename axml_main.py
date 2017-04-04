from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from xml.etree import ElementTree
from fractions import Fraction
from random import randint

class Ui:

    def __init__(self, master):
        #APP TITLE
        master.title("AXML")

        #VARIABLES FOR ENTRIES
        self.input = StringVar(master)
        self.input.set("Select your xml...")

        self.output = StringVar(master)
        self.output.set("Name your new xml...")

        self.mode = StringVar(master)
        self.mode.set("Interval")

        self.duration = StringVar(master)
        self.duration.set("120")

        #UI ELEMENTS
        #TITLE
        self.title = Label(master, text = "AXML", font = ("Futura", 24), foreground = "#2a416c", padx = 100, pady = 10)
        self.title.grid(row = 0, column = 0, columnspan = 3)

        #INPUT LABEL
        self.input_label = Label(master, text = "Input Sequence:", foreground = "#2a416c")
        self.input_label.grid(row = 1, column = 0, sticky=E)
        #INPUT ENTRY
        self.input_file = Entry(master, foreground = "#2a416c", textvariable = self.input)
        self.input_file.grid(row = 1, column = 1, sticky=W)
        #INPUT BUTTON
        self.input_button = Button(master, text = "...", foreground = "#2a416c", activebackground = "#cccccc", command = self.xml_input)
        self.input_button.grid(row = 1, column = 2, sticky=W)

        #OUTPUT LABEL
        self.output_label = Label(master, text = "Export Sequence:", foreground = "#2a416c")
        self.output_label.grid(row = 2, column = 0, sticky=E)
        #OUTPUT ENTRY
        self.output_file = Entry(master, foreground = "#2a416c", textvariable = self.output)
        self.output_file.grid(row = 2, column = 1, sticky=W)
        #OUTPUT BUTTON
        self.output_button = Button(master, text = "...", foreground = "#2a416c", activebackground = "#cccccc", command = self.xml_output)
        self.output_button.grid(row = 2, column = 2, sticky=W)

        #DURATION
        self.duration_label = Label(master, text = "Desired Duration (in seconds):", foreground = "#2a416c")
        self.duration_label.grid(row = 3, column = 0, sticky=E)

        self.duration_file = Entry(master, foreground = "#2a416c", textvariable = self.duration)
        self.duration_file.grid(row = 3, column = 1, sticky=W)

        #MODE
        self.mode_label = Label(master, text = "Mode:", foreground = "#2a416c")
        self.mode_label.grid(row = 4, column = 0, sticky=E)

        self.mode_menu = OptionMenu(master, self.mode, "Interval","Random","Relative")
        self.mode_menu.grid(row = 4, column = 1, sticky=W)

        #GO!
        self.go = Button(master, text = "GO!", font = ("Futura", 20), foreground = "#2a416c", padx = 20, pady = 10, command = self.xml_create)
        self.go.grid(row = 5, column = 0, columnspan = 2)

    def xml_input(self):
        self.input.set(filedialog.askopenfilename())
        self.sequence_input = Sequence(openXml(self.input.get()))
        print(sum(clip.duration for clip in self.sequence_input.clips)) ## debug LINE to make sure the class is working as intended

    def xml_output(self):
        self.output.set(filedialog.asksaveasfilename())

    def xml_create(self):
        mode = self.mode.get()
        duration_new = Fraction(self.duration.get())
        self.sequence_input.modify(mode, duration_new)
        print("New Sequence Length:")
        print(sum(clip.duration for clip in self.sequence_input.clips))

    def xml_write(self):
        new_name = self.output.get()


class Clip:

    def __init__(self, name, ref, seq_in, clip_in, duration):
        self.name = name
        self.ref = ref
        self.seq_in = seq_in
        self.clip_in = clip_in
        self.duration = duration

class Sequence:

    def __init__(self, spine):
        self.spine = spine #stores the XML reference
        self.clips = [] #will contain list of "Clips" that make up the sequence

        for index, node in enumerate(self.spine.iter('clip')):

            #EXTRACT VARIABLES FROM XML, Iterating through clips
            name = node.attrib.get('name')
            ref = node.find('video').attrib.get('ref')
            seqin = Fraction(node.attrib.get('offset').rstrip('s'))
            duration = Fraction(node.attrib.get('duration').rstrip('s'))
            #some instances of clips do not have a start point explicitly stated
            #this is fine for FCPX, but our code needs it explicitly stated, so we add it here
            if node.attrib.get('start') == None:
                inpoint = "0"
                node.attrib['start']=inpoint+'s'
            else:
                inpoint = Fraction(node.attrib.get('start').rstrip('s'))
            inpoint = Fraction(inpoint)

            #APPEND CLIP TO SEQUENCE
            self.clips.append(Clip(name, ref, seqin, inpoint, duration))

    def modify(self, mode, duration):
        if mode == "Interval":
            for index, clip in enumerate(self.clips):
                midpoint = clip.duration/2
                clip.duration = duration/(len(self.clips))
                clip.seq_in = index*duration
                clip.clip_in = midpoint - (clip.duration/2)

            print(mode + "Working")
            #Set each clip to same duration so that the sequence is designated length

        if mode == "Random":
            print(mode + "Working")
            print(duration)
            #Set each clip to a random duration that is 10% a deviation from the interval length to ensure the sequence is the desired length

        if mode == "Relative":
            print(mode + "Working")
            print(duration)
            #set each clip to a legth proportionately equal to the ratio of the new sequence:old sequence

def openXml(xml):

    with open(xml, 'rt') as f:
        tree = ElementTree.parse(f)

    spine = tree.find('library').find('event').find('project').find('sequence').find('spine')

    return spine

def main():

    root = Tk()
    app = Ui(root)
    root.mainloop()

if __name__ == "__main__": main()
