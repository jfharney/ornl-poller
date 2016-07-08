from abc import *

class AbstractWF:
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def jsonToWorkflow(self,json,pathToWF):
        return
    
    @abstractmethod
    def startWorkflow(self,pathToWF):
        return
    
    @abstractmethod
    def stopWorkflow(self,ID):
        return
    
    @abstractmethod
    def queryWorkflow(self,ID):
        return
    
    @abstractmethod
    def queryPerformance(self,ID):
        return
    
    