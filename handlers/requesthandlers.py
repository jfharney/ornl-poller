from abc import *


wfservices_hostname = 'localhost'
wfservices_port = '9001'

WFSERVICES_HOSTNAME = 'localhost'
WFSERVICES_PORT = '9001'

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
        print '\n\nlaunching BasicRequestHandler service\n\n'
        
        import requests
        import json
        
        json_example = message
    
        #test for calling service5
        #print 'calling service5'
        url = 'http://' + wfservices_hostname + ':' + wfservices_port + '/services/service5/'
        
        r = requests.post(url,data=json_example)
        #print str(r.text)
        
        
     
        