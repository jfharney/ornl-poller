from __future__ import unicode_literals

from django.db import models

# Create your models here.
#[{"fields": {"status": "new", "destination": "", "created": "2016-03-14T22:57:04.957Z", "user": "acmetest", "runspec": "/User Documents/acmetest/newfiletest.txt", "casename": "F1850C5.ne30.6mos", "mppwidth": 144, "stop_option": "ndays", "stop_n": "60, 60", "walltime": "60, 60", "mach": "titan", "compset": "F1850C5", "res": "ne30_g16", "project": "cli115", "compiler":"intel"}, "model": "poller.userruns", "pk": 1},

class UserRuns(models.Model):
    status = models.CharField(max_length=100)
    json_message = models.CharField(max_length=100)
    

class UserRunsOUI(models.Model):
    status = models.CharField(max_length=100)
    created = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    config_options = models.CharField(max_length=1000)
    
class UserRunsFinal(models.Model):
    user = models.CharField(max_length=30)
    config_options = models.TextField()
    status = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)