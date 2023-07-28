from rest_framework import serializers
from appMedicalHistory.models.medicalHistory import MedicalHistory


class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = ['__all__']