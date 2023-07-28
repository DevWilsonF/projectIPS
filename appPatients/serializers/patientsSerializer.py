from appPatients.models.patients import Patients
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Patients
        fields = ['__all__']