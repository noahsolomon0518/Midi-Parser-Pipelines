from . import *
import pickle
import os
import shutil

class Tokenizer(PipeComponent):
    def __init__(self):
        rightCompatible = []
        super().__init__(rightCompatible)


        
class OnOffTokenizer(Tokenizer):
    def __init__(self, fp):
        self.fp = fp
        self.data = []
        super().__init__()
    
    def apply(self, inp):
        for piece in inp:
            if(piece.tracks):
                dfData = []
                for event in piece.tracks[0]:
                    if(event.type in ["note_on", "note_off"]):
                        if(event.type=="note_on" and event.velocity==0):
                            dfData.append("note_off_"+str(event.note))
                            if(event.time>0):
                                dfData.append("rest_"+str(event.time))
                        else:
                            dfData.append(event.type+"_"+str(event.note))
                            if(event.time>0):
                                dfData.append("rest_"+str(event.time))
                                
                if(dfData):
                    self.data.append(dfData)
            
    def teardown(self):
        if(os.path.exists(self.fp+".pickle")):
            os.remove(self.fp+".pickle")

        f = open(self.fp+".pickle","wb")

        pickle.dump(self.data, f)
        f.close()
        