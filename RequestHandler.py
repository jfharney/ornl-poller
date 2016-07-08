from abc import ABCMeta, abstractmethod
from _pyio import __metaclass__

class RequestHandler(object):
    '''A RequestHandler for incoming request pulled by the poller
    Attributes:
        name: Name of the request handler
    '''
    
    __metaclass__ = ABCMeta
    
    
    def __init__(self,name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    @abstractmethod
    def launch(self):
        '''
        """"Perform behaviors for the specific handler""""
        '''
        pass
    
    
    