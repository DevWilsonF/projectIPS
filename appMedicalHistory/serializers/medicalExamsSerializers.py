from rest_framework import serializers
from appMedicalHistory.models.medicalExams import MedicalExams


class MedicalExamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalExams
        fields = ['__all__']
