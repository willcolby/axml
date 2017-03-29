import xml.etree.ElementTree as ET

def autoXml():
    
    tree=ET.parse('TEST.xml')
    
    root=tree.find('sequence')

    sequenceLength=(root.find('duration').text)
    print(root.find('duration').text)

    sequenceFrameRate=(root.find('rate').find('timebase').text)
    print(root.find('rate').find('timebase').text)

    sequenceName=(root.find('name').text)
    print((root.find('name').text))
    
    root=root.find('media')
    root=root.find('video')
    root=root.find('track')
    
    for index, node in enumerate(root.iter('clipitem')):
        
        #parse all needed variables
        
        clipid = node.attrib.get('id')
        duration = node.find('duration')
        inpoint = node.find('in')
        outpoint = node.find('out')
        seqin = node.find('start')
        seqout = node.find('end')
        
        #determine new variables // build this as a module


        
        new_duration = 96
        clip_midpoint = (int(duration.text))/2
        new_seqin = index*new_duration
        new_seqout = (index+1)*new_duration
        new_inpoint = clip_midpoint-(new_duration/2)
        new_outpoint = clip_midpoint+(new_duration/2)
        



        
        print("Clip ID:" + clipid)
        print(":::::ORIGINAL:::::")
        print("Sequence TC in:" + seqin.text)
        print("Sequence TC out:" + seqout.text)
        print("Duration:" + duration.text)
        print("Clip in point:" + inpoint.text)
        print("Clip out point:" + outpoint.text)
        
        duration.text = str(new_duration)
        seqin.text = str(new_seqin)
        seqout.text = str(new_seqout)
        inpoint.text = str(new_inpoint)
        outpoint.text = str(new_outpoint)
        
        print(":::::MODIFIED:::::")
        print("Clip ID:" + clipid)
        print("Sequence TC in:" + seqin.text)
        print("Sequence TC out:" + seqout.text)
        print("Duration:" + duration.text)
        print("Clip in point:" + inpoint.text)
        print("Clip out point:" + outpoint.text)
        print("::::::::::::::::::")
        
    tree.write(sequenceName+'-processed.xml')
    print("DONE")
