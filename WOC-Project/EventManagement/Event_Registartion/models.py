from django.db import models

# Create your models here.

class Event(models.Model):
    EventName = models.CharField(max_length=100)
    Description = models.TextField(max_length=2000)
    Location = models.CharField(max_length=100)
    Link_of_Poster = models.URLField()
    From_Date = models.DateField()
    From_Time = models.TimeField()
    To_Date = models.DateField()
    To_Time = models.TimeField()
    Dead_Date = models.DateField()
    Dead_Time = models.TimeField()
    Host_Name = models.CharField(max_length=100)
    Host_Email = models.EmailField()
    Password = models.CharField(max_length=50)
    Status = models.CharField(max_length=50)





