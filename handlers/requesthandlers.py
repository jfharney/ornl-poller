from abc import *


wfservices_hostname = 'localhost'
wfservices_port = '9001'

class RequestHandler(object):
    
    __metaclass__ = ABCMeta
    
    def __init__(self,name):
        print 'in request handler constructor'
        self.description = 'RequestHandlers determine which services to use'
        self.name = name
        
    @abstractmethod
    def launch(self,message):
        return

class BasicRequestHandler(RequestHandler):
    
    def __init__(self,name):
        RequestHandler.__init__(self,name)
        print 'in basic request handler constructor'
        self.description = '\nThe BasicRequestHandler is the standard request handler used in launching a single workflow and updating the \n'
        #print 'self.name: ' + str(self.name) + ' self.description: ' + str(self.description)

    
    def launch(self,message):
        print 'launching BasicRequestHandler service'
        
        import requests
        import json
        
        json_example = { 
            'casename' : 'case1',
            'res' : 'res1',
            'compiler' : 'compiler1',
            'stop_n' : 'stop_n1',
            'project' : 'project1',
            'mppwidth' : 'mppwidth1',
            'user' : 'user1',
            'stop_option' : 'stop_option1',
            'compset' : 'compset1',
            'mach' : 'mach1',
            'walltime' : 'walltime1'
            }
    
        #test for calling service5
        print 'calling service5'
        url = 'http://' + wfservices_hostname + ':' + wfservices_port + '/services/service5/'
        
        r = requests.post(url,data=json_example)
        print str(r.text)
        
        
        