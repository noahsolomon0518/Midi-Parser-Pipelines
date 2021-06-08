from . import *
from .utils import *


class Pipeline:
    def __init__(self, components):
        self.components = components
        self.check()
    
    
    
    
    def check(self):
        for i,comp in enumerate(self.components):
            try:
                assert isinstance(comp, PipeComponent)
            except:
                raise Exception("List of PipeComponents must be passed into Pipeline")

            if(i<len(self.components)-1):
                nextComponent = self.components[i+1]
                compatible = False
                for rightCompatible in comp.rightCompatible:
                    if(isinstance(nextComponent, rightCompatible)):
                        compatible = True
                if(not compatible):
                    raise Exception("Component "+ str(type(comp))+ " not compatible with "+ str(type(nextComponent)))
            
            
            
        
    def apply(self, inp):
        paths = findMidis(inp)
        nPaths = len(paths)
        if(self.components[0].trickle == True):
            for i,path in enumerate(paths):
                self._pipelineFunc([path])
                print(str(i+1)+"/"+str(nPaths)+" completed", end = "\r")
        else:
            self._pipelineFunc(paths)
        
        for comp in self.components:
            comp.teardown()
                
                
    def _pipelineFunc(self, inp):
        currentData = inp
        for comp in self.components:
            currentData = comp.apply(currentData)
        
        
        

#General class for objects that are in pipeline
class PipeComponent:
    def __init__(self, rightCompatible):
        self.rightCompatible = rightCompatible
               
    def apply(self, inp):
        raise NotImplementedError("Must implement apply(self, inp) function.")
    
    
    def teardown(self):
        pass