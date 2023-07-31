from django.db import models
from appPatients.models.patients import Patients
from appEmployees.models.employee import User
from .medicalHistory import MedicalHistory
   
class Consultation(models.Model):
    consultationID = models.AutoField(primary_key= True)
    patientID = models.ForeignKey(Patients, on_delete= models.PROTECT)
    consultationDate = models.DateField('consultationDate',null= False)
    state = models.BooleanField(default=True)
    diagnosis = models.CharField('Diagnosis', max_length= 3000,null=False)
    treatment = models.CharField('Treatment', max_length= 3000, null=False)
    employeeID = models.ForeignKey(User, on_delete= models.PROTECT)
    historyID = models.ForeignKey(MedicalHistory, on_delete= models.PROTECT)