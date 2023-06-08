from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Schedule(models.Model):
    name = models.CharField(max_length=64, default="")
    description = models.CharField(max_length=1000, default="")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null = True, blank= True)

class Timeslot(models.Model):
    start = models.DateTimeField(null = True, blank= True)
    end =  models.DateTimeField(null = True, blank= True)
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE, null = True, blank= True)