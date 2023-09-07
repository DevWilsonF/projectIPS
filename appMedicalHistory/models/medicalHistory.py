from django.db import models
from appPatients.models.patients import Patients


class MedicalHistory(models.Model):
    historyID = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patients,null=False,on_delete= models.PROTECT,related_name='medicalHistory')
    allergies = models.CharField(null=True, max_length=3000)
    previousDiseases = models.CharField(null= True,max_length=3000)
    surgeries = models.CharField(null=True,max_length=3000)








