
from os import walk, path
from . import *
from mido import MidiFile
from copy import deepcopy


def findMidis(folder, r=True):
    paths = []
    if(".mid" in folder):
        paths.append(folder)
        return paths

    for (dirpath, _, filenames) in walk(folder):
        for file in filenames:
            if ".mid" in file:
                paths.append(path.join(dirpath, file))
        if not r:
            return paths
    return paths




def parseToMidos(paths):
    if(type(paths)==str):
        paths = [paths]
    return [MidiFile(_path) for _path in paths]


def applyNoteRange(mido, noteRange):
    for track in mido.tracks:
        for event in track:
            if(event.type in ["note_on", "note_off"]):
                if(event.note>noteRange[1]):
                    event.note -= ((((event.note-noteRange[1])-1)//12)+1)*12
                elif(event.note<noteRange[0]):
                    event.note += ((((noteRange[0]-event.note)-1)//12)+1)*12
    return mido



def chooseTracks(mido, tracks):
    tracks = [mido.tracks[i] for i in range(len(mido.tracks)) if i in tracks]
    mido.tracks = tracks
    return mido





#TIMING


def ticksToNorm(ticks, tpb, smallestTimeUnit):
    converted = ticks*(1/tpb)/4/smallestTimeUnit
    if(converted>0 and converted<1):
        converted=1
    return round(converted)



def normalizeMido(mido, smallestTimeUnit):
        tpb = mido.ticks_per_beat   
        for track in mido.tracks:
            for msg in track:
                msg.time = ticksToNorm(msg.time, tpb, smallestTimeUnit)
        return mido



def keyShift(mido):
    shifted = []
    #up
    for i in range(1,7):
        mf = deepcopy(mido)
        for track in mf.tracks:
            for msg in track:
                if(msg.type in ["note_on", "note_off"]):
                    msg.note+=i
        shifted.append(mf)


    for i in range(1,6):
        mf = deepcopy(mido)

        for track in mf.tracks:
            for msg in track:
                if(msg.type in ["note_on", "note_off"]):
                    msg.note-=i
        shifted.append(mf)
    
    return shifted

