from . import *



       
class MidoTransformer(PipeComponent):
    def __init__(self):
        rightCompatible = [MidoTransformer, Tokenizer]
        super().__init__(rightCompatible)


class TrackChooser(MidoTransformer):
    def __init__(self, tracks):
        self.tracks = tracks
        super().__init__()
        
    def apply(self, inp):
        return [chooseTracks(mido, self.tracks) for mido in inp]
    
    
class TrackIDCondenser(MidoTransformer):
    def __init__(self):
    
        self.curID = 0
        super().__init__()
        
    def apply(self, inp):
        return [self.nextID(mido) for mido in inp]
    
    
    def nextID(self, mido):
        self.curID += 1
        mido.filename = "piece_"+str(self.curID)
        return mido
    
class NoteRangeConverter(MidoTransformer):
    def __init__(self, noteRange):
        self.noteRange = noteRange
        super().__init__()
    
    #Input is list of midos
    def apply(self, inp):
        return [applyNoteRange(mido, self.noteRange) for mido in inp]




class TimeNormalizer(MidoTransformer):
    def __init__(self, smallestTimeUnit):
        self.smallestTimeUnit = smallestTimeUnit
        super().__init__()

    def apply(self,inp):
        return [normalizeMido(mido, self.smallestTimeUnit) for mido in inp]





class KeyShiftAdder(MidoTransformer):
    def __init__(self):
        super().__init__()

    def apply(self,inp):
        keyShifted = []
        for piece in inp:
            keyShifted.extend(keyShift(piece))
        return keyShifted









    