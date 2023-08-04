from rest_framework import serializers
from appMedicalHistory.models.medicalExams import MedicalExams


class MedicalExamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalExams
        fields = [
            'medicalExamsID',
            'consultationID',
            'PatientID',
            'medicalExamsDate',
            'examType',
            'Results'
        ]
