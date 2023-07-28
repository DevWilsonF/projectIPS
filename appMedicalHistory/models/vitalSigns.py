from django.db import models

from .consultations import Consultation


class VitalSings(models.Model):
    vitalSingsID = models.AutoField(primary_key=True)
    consultationID = models.ForeignKey(Consultation, null= False, on_delete=models.PROTECT)
    recordignDate = models.DateTimeField(auto_now=True, null= False)
    bloodPressure = models.CharField(max_length= 100, null=False)
    heartRate = models.CharField(max_length= 4, null=False)
    temperature = models.CharField(max_length=3,null= False)
    weight = models.CharField(max_length= 3 , null= False)
    height = models.CharField(max_length= 3,null=False)

