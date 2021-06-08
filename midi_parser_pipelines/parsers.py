from . import *


class Parser(PipeComponent):
    def __init__(self, trickle):
        rightCompatible = [MidoTransformer]
        super().__init__(rightCompatible)
        self.trickle = trickle
    
    #Input is list of path(s)
    def apply(self, inp):
        return [MidiFile(fp) for fp in inp]