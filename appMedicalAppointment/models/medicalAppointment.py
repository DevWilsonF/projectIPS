from django.db import models
from appPatients.models.patients import Patients
from appEmployees.models.employee import User
class MedicalAppointment(models.Model):
    appointmentID = models.AutoField(primary_key= True)
    patientID = models.ForeignKey(Patients, on_delete= models.PROTECT)
    appointmentDate = models.DateField('apointmentDate',null= False)
    appointmentTime = models.TimeField('appointmentTime',null=False)
    state = models.BooleanField(default=True)
    employeeID = models.ForeignKey(User, on_delete= models.PROTECT)