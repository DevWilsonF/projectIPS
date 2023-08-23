from django.db import models
from appPatients.models.patients import Patients
from appMedicalHistory.models.medicalHistory import MedicalHistory

class PastHistory(models.Model):
    pastHistoryID = models.AutoField(primary_key=True)
    patientID = models.ForeignKey(Patients,null= False, on_delete=models.PROTECT)
    medicalHistoryID = models.ForeignKey(MedicalHistory,null= False,on_delete=models.PROTECT)
    ingressDate = models.DateTimeField(null=False)
    file = models.BinaryField()
