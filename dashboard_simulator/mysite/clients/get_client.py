
import requests
import json

hostname = 'localhost'
port = '9000'

import time


def main():
    print 'in main'
    
    
    #simulates poller
    poller()
    
    
    

def poller():
    
    poll = True
    counter = 0
    while(poll):
        print '\n****poll round****\n'
        if counter > 1:
            poll = False
        
        #Get a message, if any 
        request_json = get('7')
        
        #Open message, interpret which Handler
        request_id = request_json['id']
        
        #For now, if the request_id sent back is -1, then there are no new messages
        if request_id != '-1':
            print '\ngetting new request'
            
            #Send to appropriate handler if there is a valid message
        
            r_handler = BasicRequestHandler()
        
        
    
    
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


class RequestHandler(object):
    
    def __init__(self):
        self.description = 'RequestHandlers determine which services to use'
        print 'in request handler constructor'


class BasicRequestHandler(RequestHandler):
    
    def __init__(self):
        print 'in basic request handler constructor'
        print 'self.description: ' + str(self.description)







if __name__ == "__main__": main()