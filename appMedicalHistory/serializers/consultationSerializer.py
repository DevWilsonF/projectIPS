from rest_framework import serializers
from appMedicalHistory.models.consultations import Consultation


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['__ALL__',]

    
    
    
       