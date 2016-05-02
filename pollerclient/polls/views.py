from django.shortcuts import render

from django.http import HttpResponse

from .models import Question

# Create your views here.
def index(request):
    q = Question.objects.all()
    print 'in polls'
    return HttpResponse("Hello")
