from mido import MidiFile, MidiTrack, Message
import fluidsynth
import os
sf2 = os.path.abspath("C:/Users/noahs/Local Python Libraries/soundfonts/piano.sf2")
import time

def tokenizedOnOffToMido(piece):
    m = MidiFile()
    track = MidiTrack()
    m.tracks.append(track)
    for i,msg in enumerate(piece):
        msg = msg.split("_")
        if("rest" not in msg):
            c = 1
            dt = 0
            while i<len(piece)-1 and "rest" in piece[i+c]:
                print(piece[i+c])
                dt += int(piece[i+c].split("_")[1])
                c += 1
        if(msg[1]=="on"):
            track.append(Message("note_on", note = int(msg[2]), velocity = 90, time = dt))
        if(msg[1]=="off"):
            track.append(Message("note_off", note = int(msg[2]), time = dt))
    return m



def playMido(mido, smallestTimeUnit, tempo = 120):
    assert len(mido.tracks)==1
    timeUnitSeconds =  (smallestTimeUnit/(1/4))*(60/tempo)     #How many beats in smallest time unit
    sf2 = os.path.abspath("C:/Users/noahs/Local Python Libraries/soundfonts/piano.sf2")
    fs = fluidsynth.Synth()
    fs.start()
    sfid = fs.sfload(sf2)
    fs.program_select(0, sfid, 0, 0)
    for msg in mido.tracks[0]:
        if(msg.type == "note_on"):
            print(msg)
            fs.noteon(0, msg.note, 100)
        elif(msg.type == "note_off"):
            print(msg)
            fs.noteoff(0, msg.note)
        time.sleep(msg.time*timeUnitSeconds)
    