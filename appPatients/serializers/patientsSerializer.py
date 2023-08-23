from appPatients.models.patients import Patients
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Patients
        fields = ['PatientID',
                'firstName',
                'lastName',
                'registrationDate',
                'phone',
                'gender',
                'maritalStatus',
                'nationality',
                'city',
                'address',
                'documentType',
                'documentNumber',
                'birthDate',
                'email',
                'insuranceType',
                'occupation']