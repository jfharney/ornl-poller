from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View
from oui_backend_simulator.models import UserRuns

import traceback
import json

# Create your views here.
def index(request):
  return HttpResponse("Hello world.  You're at the oui_backend_simulator")

class UserRunsView(View):
    
    def delete(self, request, wf_id):
        
        print '\nDELETEing... ' + str(wf_id)
        
        wf = UserRuns.objects.filter(id=wf_id)
        
        if not wf:
            print 'wf is not in the db'
            
        else:
            print 'wf: ' + str(wf[0])
            
            workflow = wf[0]
            print workflow.id
            
            workflow.delete()
       
         
        return HttpResponse("DELETE Done\n")   
    
    
    def put(self, request, wf_id):
    
        from django.http import QueryDict
        
        print 'request.body: ' + str(request.body)
        
        try:
        
            q = QueryDict(request.body)
            q = json.dumps(q)
            
            #need to get the status and ids to update the db
            status = ''
            request_id = ''
            
            #hackjob to get the id and status... why is the json object being loaded this way????
            json_data = json.loads(q)
            
            request_id = json_data['id']
            status = json_data['status']
            '''
            for key in json_data:
                print 'key: ' + str(key)
                j = json.loads(key)
                request_id = j['id']
                status = j['status']
            '''
            
            print 'id: ' + str(request_id)
            print 'status: ' + str(status)
        
            
            userrun = UserRuns.objects.filter(id=request_id)
        
            if userrun != None:
                u = userrun[0]
            
                print 'old status: ' + str(u.status)
            
                status_from_poller = status
                current_status = u.status
                
                if current_status == "new":
                    if status_from_poller == 'in_progress':
                        u.status = status
                        u.save()
                
                if current_status == "in_progress":
                    if status_from_poller == 'done':
                        u.status = status
                        u.save()
                    elif status_from_poller == 'error':
                        u.status = status
                        u.save()
                
                print 'new status: ' + str(u.status)
        
            return HttpResponse("PUT Done\n")  
        
        
        except:
            tb = traceback.format_exc()
            print 'tb: ' + str(tb)
            return HttpResponse("error")
        
         
    
    
    def post(self, request, wf_id):
        
      
        print '\nPOSTing...'
  
        from django.http import QueryDict
        print 'request.body: ' + str(request.body)
        
        try:
        
            q = QueryDict(request.body)
            q = json.dumps(q)
            
            #need to get the status and ids to update the db
            new_message = ''
            
            
            
            #hackjob to get the id and status... why is the json object being loaded this way????
            json_data = json.loads(q)
            
            new_message = json_data['json_message']
            '''
            for key in json_data:
                print 'key: ' + str(key)
                j = json.loads(key)
                new_message = j['json_message']
            '''
            
            
            new_status = 'new'
            
            userrun = UserRuns(status=new_status,json_message=new_message)
            userrun.save()
            
            print 'id: ' + str(userrun.id)
            
           
            
            
            return HttpResponse("POST Done\n")   
        
        
        except:
            tb = traceback.format_exc()
            print 'tb: ' + str(tb)
            #logger.debug('tb: ' + tb)
            return HttpResponse("error")
        
         
        
    
    def get(self, request, wf_id):
        
        
        print '\nGETing... ' + str(wf_id)
        
        data = {'id' : '-1' }
        newRunFound = False
            
        try:
            user_runs = UserRuns.objects.all()
            print str(user_runs)
            for user_run in user_runs:
                status = user_run.status
                #print 'status: ' + str(status) + ' len: ' + str(len(str(status))) + ' new'
                if status == 'new':
                    newRunFound = True
                    data = {'id' : user_run.id, 'status' : status, 'json_message' : user_run.json_message }
                    
            
        except:
            tb = traceback.format_exc()
            print 'tb: ' + str(tb)
            #logger.debug('tb: ' + tb)
            return HttpResponse("error")
        
        
        print 'data: ' + str(data)
        data_string = json.dumps(data,sort_keys=False,indent=2)
        print 'data_string: ' + str(data_string)
        
        return HttpResponse(data_string + "\n")   
        