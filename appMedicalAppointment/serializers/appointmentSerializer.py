from appMedicalAppointment.models.medicalAppointment import MedicalAppointment
from rest_framework import serializers


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicalAppointment
        fields = [
            'appointmentID',
            'patientID',
            'appointmentDate',
            'appointmentTime',
            'state',
            'employeeID']