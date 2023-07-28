from django.db import models

from .consultations import Consultation


class MedicalExams(models.Model):
    medicalExamsID = models.AutoField(primary_key=True)
    consultationID = models.ForeignKey(Consultation,on_delete=models.PROTECT, null= False)
    examType = models.CharField(max_length=2000, null= False)
    Results = models.CharField(max_length= 2000, null=False)