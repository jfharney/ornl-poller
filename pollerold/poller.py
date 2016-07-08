
import requests
import json

hostname = 'localhost'
port = '9000'
base_dir = '/Users/8xo/software/ornl-poller/ornl-poller'
import sys
sys.path.append(base_dir)
from handlers import requesthandlers

import time
#
def main():
    
    
    print '\n...............'
    print 'starting poller'
    print '...............\n'
    
    #simulates poller
    poller()
    
    print '\n...............'
    print 'ending poller'
    print '...............\n'
    
    

def poller():
    
    poll = True
    counter = 0
    while(poll):
        print '\n****poll round****\n'
        if counter > -1:
            poll = False
        
        
        
        
        #Get a message, if any 
        request_json = get('7')
        request_id = request_json['id']
        
        request_json = { 
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
    
        
        
        #Open message, interpret which Handler
        #Follow some logic here to get the name of the handler
        name = "BasicRequest"
        
        
        
        #For now, if the request_id sent back is -1, then there are no new messages
        if request_id != '-1':
            print '\ngetting new request'
            
            
            #Send to appropriate handler if there is a valid message
            if name == "BasicRequest":
                
                
                #use the celery wrapper for request handlers
                from tasks import basicRequestHandlerWrapper
                
                basicRequestHandlerWrapper.delay(request_json,name)
                
                #handler = requesthandlers.BasicRequestHandler(name)
                #handler.launch(request_json)
        
    
    
        
            
        time.sleep(1)
        counter = counter + 1
        
        print '\n****end poll round****\n'


    
def put(id,status):
    
    print '----IN PUT----'
    url = 'http://' + hostname + ':' + port + '/oui_backend_simulator/about/' + str(id) + '/'
    print 'calling PUT url...' + str(url)
    
    print 'in put...id: ' + str(id) + ' status: ' + str(status)    
    payload_put = {'id':str(id),'status':str(status)}
    
    #r = requests.put('http://localhost:9000/oui_backend_simulator/about/4/',data=payload_put)
    
    print '----END PUT----'
    
    

def get(id='7'):
    
    print '----IN GET----'
    
    
    url = 'http://' + hostname + ':' + port + '/oui_backend_simulator/about/' + str(id) + '/'
    
    print 'calling GET url...' + str(url)
    
    s = requests.Session()
    #url = 'http://localhost:8000/pcservices/userruns/name/?user=user&status=new'
        
    r = s.get(url)
    #print 'response: ' + r.text
    response_json = r.json()
    
    print '----END GET----'
    
    return response_json






if __name__ == "__main__": main()

'''
        request_id = request_json['id']
        request_status = request_json['status']
        print 'request_id: ' + str(request_id) + ' request_status: ' + str(request_status)
    
        if request_id != '-1':
            print '\ngetting new request'
            if request_status == 'new':
                
              put(str(request_id),str(request_status))
            
        else:
            print '\nno new requests'
        
'''