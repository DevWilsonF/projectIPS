from django.db import models
from appPatients.models.patients import Patients


class MedicalHistory(models.Model):
    historyID = models.AutoField(primary_key=True)
    patientID = models.ForeignKey(Patients,null=False,on_delete= models.PROTECT)
    allergies = models.CharField(null=True, max_length=3000)
    previousDiseases = models.CharField(null= True,max_length=3000)
    surgeries = models.CharField(null=True,max_length=3000)








