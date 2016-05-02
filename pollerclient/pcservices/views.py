from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.http import JsonResponse
import json

from django.views.generic import View

from .models import UserRuns


# Create your views here.
def index(request):
    u = UserRuns.objects.all()
    print 'in pcservices'
    return HttpResponse("Hello pcservices")



class UserRunsView(View):
    
    def put(self, request, name):
      print 'put'
      return HttpResponse("UserRunsView Put\n")
  
  
  
  
    #@csrf_protect
    def post(self, request, name):
      print 'post'
      
      try:
          
        data = json.loads(request.body)
      
        print 'data: ' + str(data)
      
        fields = data['fields']
      
        for key in fields:
            print 'key: ' + str(key)
        new_run = UserRuns.objects.create(user=fields['user'], runspec=fields['runspec'], status='new')
      
        #da = Published.objects.filter(dataset_name=dataset_name)
      
      except Exception as e:
        import traceback
        #print_debug(e)
        print str(traceback.print_exc())
        return HttpResponse(status=500)
      
      
      #new_run = UserRuns.objects.create(user=data['user'], runspec=data['runspec'], status='new')
      #new_run.save

      
      return HttpResponse("UserRunsView Post\n")
      
      
      
      
    def get(self, request, name):
      print 'get'
      
      try:
        
        status = request.GET.get('status')
        user = request.GET.get('user')
        print 'user: ' + str(user)
        print 'status: ' + str(status)
        
      except Exception as e:
        import traceback
        #print_debug(e)
        print str(traceback.print_exc())
        return HttpResponse(status=500)    
      
      
      return HttpResponse("UserRunsView Get\n")
