from rest_framework import serializers
from appMedicalHistory.models.vitalSigns import VitalSings


class VitalSingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalSings
        fields = [
            'vitalSingsID',
            'consultationID',
            'recordignDate',
            'bloodPressure',
            'heartRate',
            'temperature',
            'weight',
            'height'
        ]