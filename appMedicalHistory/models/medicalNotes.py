from django.db import models

from .consultations import Consultation


class MedicalNotes(models.Model):
    medicalNotesID = models.AutoField(primary_key=True)
    consultationID = models.ForeignKey(Consultation, null= False,on_delete=models.PROTECT)
    noteDate = models.DateTimeField(auto_now=True, null= False)
    Description = models.CharField(max_length= 2000, null=False)