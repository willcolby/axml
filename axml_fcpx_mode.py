from xml.etree import ElementTree
from fractions import Fraction
from random import randint
from tkinter import filedialog


def main():
    with open('TEST.fcpxml', 'rt') as f:
        tree = ElementTree.parse(f)
    
    root=tree.find('library').find('event').find('project').find('sequence').find('spine')    
    frame_duration=tree.find('resources').find('format').attrib.get('frameDuration').rstrip('s')
    original_seq_duration=tree.find('library').find('event').find('project').find('sequence').attrib.get('duration').rstrip('s')
    
    x=float(sum(Fraction(s) for s in frame_duration.split()))
    frame_rate=1/x
    frame_rate=round(frame_rate, 1)
    frame_rate=int(frame_rate)
    print(frame_rate)
    
    seq_duration=Fraction(0)

####INTERATION  
    for index, node in enumerate(root.iter('clip')):

        clipid = index+1
        seqin = node.attrib.get('offset').rstrip('s')
        duration = node.attrib.get('duration').rstrip('s')
        inpoint = node.attrib.get('start')
        if inpoint == None:
                inpoint = "0s"
                node.attrib['start']=inpoint
        inpoint = inpoint.rstrip('s')
        
        print("::::::::::::::::::")
        print("Clip ID:" + str(clipid))
        print(":::::ORIGINAL:::::")
        print("Sequence TC in:" + str(seqin))
        print("Duration:" + str(duration))
        print("Clip in point:" + str(inpoint))     

        #Randomization Module
        #x=randint(3,24)
        #x=x*1001
        #x=str(x)+"/24000"
        
        #Percentage Module
        percentage = "1/14"
        x=(Fraction(duration)*Fraction(percentage))
        
        print(x)
        
        if (Fraction(duration) > Fraction(x)):
            new_duration = x
            clip_difference = Fraction(duration)-Fraction(new_duration)
            new_seqin = seq_duration
            new_inpoint = Fraction(inpoint)+(Fraction(clip_difference)/2)
            print(new_inpoint)
        else:
            new_duration = duration
            new_seqin = seqin
            new_inpoint = inpoint
            
        seq_duration += Fraction(new_duration)
        print(new_duration)
        print(seq_duration)
        
        node.attrib['offset']=str(new_seqin)+'s'
        node.attrib['duration']=str(new_duration)+'s'
        node.attrib['start']=str(new_inpoint)+'s'
        
        
           
        print(":::::MODIFIED:::::")
        print("Sequence TC in:" + str(new_seqin))
        print("Duration:" + str(new_duration))
        print("Clip in point:" + str(new_inpoint))
        print("::::::::::::::::::")
        
    print("Original Sequence Duration:"+str(original_seq_duration))
    print("New Sequence Duration:"+str(seq_duration))
    seq_duration = str(seq_duration)+'s'
    tree.find('library').find('event').find('project').find('sequence').attrib['duration']=seq_duration
    #tree.write('output.fcpxml')

    

    
if __name__ == "__main__":
  main();


