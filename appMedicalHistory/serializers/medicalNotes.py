from rest_framework import serializers
from appMedicalHistory.models.medicalNotes import MedicalNotes


class MedicalNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model= MedicalNotes
        fields = ['__all__']