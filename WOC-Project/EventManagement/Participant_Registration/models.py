from django.db import models

# Create your models here.
class Participant(models.Model):
    Name = models.CharField(max_length=50)
    Contact_No = models.PositiveIntegerField()
    Email = models.EmailField()
    Event_Name = models.CharField(max_length=100)
    Type_Of_Registration = models.CharField(max_length=50)
    No_Of_Participant = models.PositiveIntegerField()
