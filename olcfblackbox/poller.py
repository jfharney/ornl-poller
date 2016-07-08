#!/usr/bin/env python


# Poller interface for inheritance

from abc import * 

class Poller:

    __metaclass__ = ABCMeta
    

    #assert jsonToWF(json, pathToWF)
    #assert startWG(pathToWF)
    #assert StopWF(ID)
    #assert query(ID)

    @abstractmethod
    def jsonToWorkflow(self, json, pathToWF):
        return

    @abstractmethod
    def startWorkflow(self, pathToWF):
        return

    @abstractmethod
    def stopWorkflow(self, ID):
        return

    @abstractmethod
    def queryWorkflow(self, ID):
        return

    @abstractmethod
    def queryPerformance(self, ID):
        return
    