
import requests
import json
import sys
import time

base_dir = '/Users/8xo/software/ornl-poller/ornl-poller'
sys.path.append(base_dir)

from handlers import requesthandlers


OUI_HOSTNAME = 'localhost'
OUI_PORT = '9000'
POLLER_SLEEPER = 20



def main():
    
    print '...............'
    print 'starting poller'
    print '...............'
    
    #simulates poller
    poller()
    
    print '...............'
    print 'ending poller'
    print '...............'
    
    
#Poller 
def poller():
    
    poll = True
    counter = 0
    while(poll):
        print '\n****poll round****\n'
        if counter > 5:
            poll = False
            
        #Get a message, if any 
        request_json = get_next().json()
        
        #if there is content, forward message along
        if request_json.has_key('job_id'):
            print 'valid request'
            
            #Open message, interpret which Handler
            
            #Follow some logic here to get the name of the handler, for now hard code with Basic Handler
            name = "BasicRequest"
        
        
        
            #Send to appropriate handler if there is a valid message
            if name == "BasicRequest":
                
                #use the celery wrapper for request handlers
                from tasks import basicRequestHandlerWrapper
                
                basicRequestHandlerWrapper.delay(request_json,name)
            
        else:
            print 'no new requests'
        
        print '\n****end poll round****\n'

        time.sleep(POLLER_SLEEPER)
        counter = counter + 1


def get_next():
    payload = {'request': 'next'}
    url = 'http://' + OUI_HOSTNAME + ':' + str(OUI_PORT) + '/oui_backend_simulator/update/'
    r = requests.get(url, params=payload)
    return r
    

if __name__ == "__main__": main()





'''   
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
'''






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
    
'''
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
'''