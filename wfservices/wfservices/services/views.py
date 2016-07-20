from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import requests
import time
import sys
import json


import ConfigParser
config = ConfigParser.ConfigParser()
config.read('/Users/8xo/software/ornl-poller/ornl-poller/eaconfig.cfg')
base_dir = config.get('settings', 'base_dir')
service_impl_dir = "/Users/8xo/software/pegasus-coupler/ScientificDataManagement/pollerPegasus"

sys.path.append(base_dir)
sys.path.append(service_impl_dir)

OUI_HOSTNAME = config.get('settings', 'oui_hostname')
OUI_PORT = config.get('settings', 'oui_port')
WFSERVICES_HOSTNAME = config.get('settings', 'wfservices_hostname')
WFSERVICES_PORT = config.get('settings', 'wfservices_port')


IN_PROGRESS_RESPONSE = config.get('settings', 'IN_PROGRESS_RESPONSE')
ERROR_RESPONSE = config.get('settings', 'ERROR_RESPONSE')
DONE_RESPONSE = config.get('settings', 'DONE_RESPONSE')

QUERY_POLL_SLEEP = 2


def get_next():
    payload = {'request': 'next'}
    url = 'http://' + OUI_HOSTNAME + ':' + str(OUI_PORT) + '/oui_backend_simulator/update/'
    r = requests.get(url, params=payload)
    
    return r
    

def post_status(status,job_id):
    
    url = 'http://' + OUI_HOSTNAME + ':' + str(OUI_PORT) + '/oui_backend_simulator/update/'
    payload = {'request' : status, 'job_id' : job_id}
    r = requests.post(url, data=payload)




def get_status(status):
    
    url = 'http://' + OUI_HOSTNAME + ':' + str(OUI_PORT) + '/oui_backend_simulator/update/'
    payload = {'request' : status}
    r = requests.get(url, params=payload)
    #print 'status: ' + str(status) + '\n' + str(r.text) + '\n'
    return r






def index(request):
  return HttpResponse("Hello, world.  You're at the services index.")

#service0
#given a new_status and an id, publish that status to the acme-web-fe
def service0(request):
  
  new_status = request.GET.get('new_status', '')
  job_id = request.GET.get('job_id','')
  
  
  print 'new_status: ' + str(new_status) + ' job_id: ' + str(job_id)
  
  #post back to oui to update status to in_progress
  r = post_status(new_status,job_id)
  
  return HttpResponse("End service0")



  
#given a 'pathToWF', call "startWorkflow" from the workflow blackbox
def service1(request):
  
    print 'in service1'
  
    #start the workflow
  
    
    #create a Pegasus WF object
    import poller
    from pollerPegasus import Pegasus
    pegasus = Pegasus()
    
    #items = ['casename', 'res', 'compiler', 'stop_n', 'project', 'mppwidth', 'user', 'stop_option', 'compset', 'mach', 'walltime']
    
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
    
    
    jsonstring = json.dumps(json_example)
    path = '/Users/8xo/software/pegasus-coupler/ScientificDataManagement/pollerPegasus'
    
    response = pegasus.startWorkflow(jsonstring,path)
    #print 'final response: ' + str(response)
    
      
    
    return HttpResponse(response)

def service2(request):

  print 'in service2'
  
  #stop the workflow
  
  return HttpResponse("In service2")

def service3(request):
    
  print 'in service3'
  
  wf_id = request.GET.get('wf_id', '')
  print 'wf_id: ' + str(wf_id)
  
  import poller
  from pollerPegasus import Pegasus
  pegasus = Pegasus()
        
  #need string representation of the response
  response = str(pegasus.queryWorkflow(wf_id))
    
  print 'query_response: ' + str(response) + ' test: ' + str(str(response) == IN_PROGRESS_RESPONSE)
        
  time.sleep(QUERY_POLL_SLEEP)
  
  return HttpResponse(response)

def service4(request):
    
  print 'in service4'
  
  #query the performance    

  return HttpResponse("In service4")

#"Service5" is the standard service for starting a wf  
def service5(request):

  print 'in service5'
        
        
  try:
      
    print 'request.body: ' + str(request.body)
    
    #get the payload and convert to the desired json_object
    from django.http import QueryDict
    import json
    q = QueryDict(request.body)
    json_example = json.dumps(q)
  
  except:
    import traceback
    tb = traceback.format_exc()
    print 'tb: ' + str(tb)
    return HttpResponse(ERROR_RESPONSE)

  
  if request.method == 'GET':
    
    print '\n...get for service5...\n'
    
    response = IN_PROGRESS_RESPONSE
    #update status by calling service0
    url = 'http://' + WFSERVICES_HOSTNAME + ':' + str(WFSERVICES_PORT) + '/services/service0?new_status=IN_PROGRESS'
    s = requests.Session()
    r = s.get(url)
    print 'after call to service0 from service5'
    
    #start a workflow by calling service1
    url = 'http://' + WFSERVICES_HOSTNAME + ':' + str(WFSERVICES_PORT) + '/services/service1/'
    s = requests.Session()
    r = s.get(url)
    service1responsetext = r.text
    service1responsejson = r.json()
    wf_id = service1responsejson['pegasusID']
    print 'response from calling service1: ' + str(response)
    print 'responsejson from calling service1: ' + str(wf_id)
    print 'after call to service1 from service5'
    
    
    response = IN_PROGRESS_RESPONSE
    #return the response from service3 when error or completion message is given
    while str(response) == IN_PROGRESS_RESPONSE:
        
        
        
        url = 'http://' + WFSERVICES_HOSTNAME + ':' + str(WFSERVICES_PORT) + '/services/service3?wf_id=' + str(wf_id)
        s = requests.Session()
        r = s.get(url)
        response = str(r.text)
        
        print 'response: ' + response
        print 'after call to service3 from service5'
        
        #change the status to "DONE" or "ERROR"
        
    if response == ERROR_RESPONSE:
        print 'ERROR_RESPONSE -> change status to ERROR'
        
        url = 'http://' + WFSERVICES_HOSTNAME + ':' + str(WFSERVICES_PORT) + '/services/service0?new_status=ERROR'
        s = requests.Session()
        r = s.get(url)
        print 'after call to service0 from service5'
        
    elif response == DONE_RESPONSE:
        print 'DONE_RESPONSE -> change status to DONE'    
        url = 'http://' + WFSERVICES_HOSTNAME + ':' + str(WFSERVICES_PORT) + '/services/service0?new_status=DONE'
        s = requests.Session()
        r = s.get(url)
        print 'after call to service0 from service5'
    
    
    print '...end get for service5...'
    return HttpResponse(response) 

  elif request.method == 'POST':
    
    
    print '\n\n\n...post for service5...\n\n\n'
    service5helper(json_example)
    
    
    
  else:
    print 'shouldnt get here...'
  
    
  return HttpResponse("In service5") 



def service5helper(json_message):
    
    print '\n\nSERVICE HELPER\n\n'
    
    response = IN_PROGRESS_RESPONSE
    #update status by calling service0
    
    print 'json_message: ' + str(json_message)
    
    
    import json
    j = json.loads(json_message)
    
    
    job_id = j['job_id']
    
    url = 'http://' + WFSERVICES_HOSTNAME + ':' + str(WFSERVICES_PORT) + '/services/service0?new_status=IN_PROGRESS&job_id=' + str(job_id)
    s = requests.Session()
    r = s.get(url)
    print 'after call to service0 from service5'
    
    
    
    #start a workflow by calling service1
    url = 'http://' + WFSERVICES_HOSTNAME + ':' + str(WFSERVICES_PORT) + '/services/service1/'
    #s = requests.Session()
    #r = s.get(url)
    
    
    #test for calling service5
    print 'calling service5'
        
    r = requests.post(url,data=json_message)
    
    #print 'r.text: ' + str(r.text)
    service1responsetext = r.text
    if r.text != ERROR_RESPONSE:
        service1responsejson = r.json()
        wf_id = service1responsejson['pegasusID']
        #print 'response from calling service1: ' + str(response)
        #print 'responsejson from calling service1: ' + str(wf_id)
        #print 'after call to service1 from service5'
    else:
        return ERROR_RESPONSE
    
    #set response to in progress
    response = IN_PROGRESS_RESPONSE
    
    print 'response: ' + str(response)
    print 'wf_id: ' + str(wf_id)
    
    
    #return the response from service3 when error or completion message is given
    while str(response) == IN_PROGRESS_RESPONSE:
        
        
        
        url = 'http://' + WFSERVICES_HOSTNAME + ':' + str(WFSERVICES_PORT) + '/services/service3?wf_id=' + str(wf_id)
        s = requests.Session()
        r = s.get(url)
        response = str(r.text)
        
        print 'response: ' + response
        print 'after call to service3 from service5'
        
        #change the status to "DONE" or "ERROR"
        
    if response == ERROR_RESPONSE:
        print 'ERROR_RESPONSE -> change status to ERROR'
        
        url = 'http://' + WFSERVICES_HOSTNAME + ':' + str(WFSERVICES_PORT) + '/services/service0?new_status=failed&job_id=' + str(job_id)
        print '\nCalling url: ' + str(url)
        s = requests.Session()
        r = s.get(url)
        print 'after call to service0 from service5'
        
    elif response == DONE_RESPONSE:
        print 'DONE_RESPONSE -> change status to DONE'    
        url = 'http://' + WFSERVICES_HOSTNAME + ':' + str(WFSERVICES_PORT) + '/services/service0?new_status=complete&job_id=' + str(job_id)
        print '\nCalling url: ' + str(url)
        s = requests.Session()
        r = s.get(url)
        print 'after call to service0 from service5'
    
    
    
    print '...end get for service5...'
    return response


def main():
    
    print 'in services main()'
    
    
    '''
    #test for calling service0
    print 'calling service0'
    new_status = 'COMPLETE'
    url = 'http://' + WFSERVICES_HOSTNAME + ':' + str(WFSERVICES_PORT) + '/services/service0?new_status=' + new_status
    s = requests.Session()
    r = s.get(url)
    '''
    
    
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
    url = 'http://' + WFSERVICES_HOSTNAME + ':' + str(WFSERVICES_PORT) + '/services/service5/'
    
    r = requests.post(url,data=json_example)
    print str(r.text)
    
    #s = requests.Session()
    #r = s.get(url)
    

if __name__ == "__main__": main()
 



