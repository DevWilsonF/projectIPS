from appMedicalHistoryPDF.models.pastHistory import PastHistory
from rest_framework import serializers


class PastHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=PastHistory
        fields = [
            'pastHistoryID',
            'patientID',
            'medicalHistoryID',
            'ingressDate',
            'file']