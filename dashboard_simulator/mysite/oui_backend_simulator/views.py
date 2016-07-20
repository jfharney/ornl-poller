from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View
from oui_backend_simulator.models import UserRuns
from oui_backend_simulator.models import UserRunsFinal

import traceback
import json

from django.http import JsonResponse

# Create your views here.
def index(request):
  return HttpResponse("Hello world.  You're at the oui_backend_simulator")


def update(request):
    if request.method == 'GET':
        print 'in update service GET'
        try:
            request_type = request.GET.get('request')
            user = request.GET.get('user')
            
            print 'request_type: ' + str(request_type) 
            print 'user: ' + str(user) 
            
            if request_type:
                if request_type == 'all':
                    print 'all'
                    
                    if user:
                        data = UserRunsFinal.objects.filter(user=user)
                    else:
                        data = UserRunsFinal.objects.all()
                    
            
                elif request_type == 'next':
                    print 'next'
                    data = UserRunsFinal.objects.filter(status='new').order_by('created')
                    
                    if not data:
                        return JsonResponse({}, safe=False)
                    else:
                        data = data[0]
                        config = json.loads(data.config_options)
                        r = {}
                        r['job_id'] = data.id
                        r['user'] = data.user
                        r.update(config)
                        return JsonResponse(r, safe=False)
                
                
                elif request_type in ['new', 'in_progress', 'complete', 'failed']:
                    if user:
                        data = UserRunsFinal.objects.filter(status=request_type, user=user)
                    else:
                        data = UserRunsFinal.objects.filter(status=request_type)
                        
                        
                elif request_type == 'job':
                    job_id = request.GET.get('job_id')  # todo: write tests for this
                    if job_id and job_id.isdigit():
                        try:
                            data = UserRunsFinal.objects.get(id=job_id)
                            config = json.loads(data.config_options)
                            obj = {
                                'job_id': data.id,
                                'user': data.user,
                                'status': data.status,
                            }
                            obj.update(config)
                            return JsonResponse(obj, safe=False)
                        except UserRuns.DoesNotExist:
                            return JsonResponse({}, status=200)
                    else:
                        return HttpResponse(status=400)
                else:
                    return HttpResponse(status=400)
                
                
                if not data:
                    return JsonResponse({}, status=200)
                obj_list = []
                for obj in data:
                    config = json.loads(obj.config_options)
                    obj_dict = {}
                    obj_dict['job_id'] = obj.id
                    obj_dict['user'] = obj.user
                    obj_dict['status'] = obj.status
                    obj_dict.update(config)
                    obj_list.append(obj_dict)
                return JsonResponse(obj_list, safe=False)
            
            
            else:
                return HttpResponse(status=400)  
                
                
                
                
                
        except Exception as e:
            print 'except'
    
    
    
    
     
    if request.method == 'POST':      
            
        print 'in POST'
        try:
            request_type = request.POST.get('request')
            user = request.POST.get('user')
            status = request.POST.get('status')
            
            print 'request_type: ' + str(request_type)
            print 'user: ' + str(user)
            print 'status: ' + str(status)
                 
            if request_type == 'all':
                print 'all'
                
                
            if request_type == 'new':
                print 'new'
                
                
                if user:
                    print 'user'
                    config = {}
                    for key in request.POST:
                        print 'key: ' + str(key)
                        value = request.POST.get(key)
                        config.update({key: value})
                  
                    del config['user']
                    del config['request']
                    
                    config = json.dumps(config)
                    new_run = UserRunsFinal.objects.create(
                        status='new',
                        config_options=config,
                        user=user
                    )
                    
                    new_run.save()
                    
                    
                    
                    return JsonResponse({'job_id': new_run.id})
                else:
                    
                    print 'not user'
                    
                    return HttpResponse(status=400)
             
            if request_type == 'delete':
                try:
                    job_id = request.POST.get('job_id')
                    if not job_id:
                        raise KeyError
                    else:
                        UserRuns.objects.get(id=job_id).delete()
                        return HttpResponse(status=200)
                except (KeyError, AttributeError, UserRuns.DoesNotExist):
                    return HttpResponse(status=400)   
                  
                  
            if request_type in ['in_progress', 'complete', 'failed']:
                job_id = request.POST.get('job_id')
                if job_id:
                    try:
                        job = UserRunsFinal.objects.get(id=job_id)
                        job.status = request_type
                        job.save()
                        return HttpResponse(status=200)
                    except ObjectDoesNotExist:
                        return HttpResponse(status=400)
            else:
                return HttpResponse(status=400)  # Unrecognized request    
                 
                 
                 
                 
        except Exception as e:
            print str(traceback.print_exc())
            print 'except'

    return HttpResponse("In update")















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
    
    




        