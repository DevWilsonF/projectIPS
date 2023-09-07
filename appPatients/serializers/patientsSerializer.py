from appPatients.models.patients import Patients
from appMedicalHistory.models.medicalHistory import MedicalHistory
from appMedicalHistory.serializers.medicalHistorySerializer import MedicalHistorySerializer
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    medicalHistory = MedicalHistorySerializer()
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
                'documentType',
                'documentNumber',
                'birthDate',
                'email',
                'insuranceType',
                'occupation',
                'medicalHistory']
        
    def create(self, validated_data):
        medicalHistoryData = validated_data.pop('medicalHistory')
        patientInstance = Patients.objects.create(**validated_data)
        MedicalHistory.objects.create(patient=patientInstance, **medicalHistoryData)
        return patientInstance
    def to_representation(self, obj):
        patient =Patients.objects.get(PatientID = obj.PatientID)
        medicalHistory = MedicalHistory.objects.get(patient=obj.PatientID)
        
        return {
                "PatientID": patient.PatientID,
                "firstName": patient.firstName,
                "lastName": patient.lastName,
                "registrationDate": patient.registrationDate,
                "phone": patient.phone,
                "gender": patient.gender,
                "maritalStatus": patient.maritalStatus,
                "nationality": patient.nationality,
                "documentType": patient.documentType,
                "documentNumber": patient.documentNumber,
                "birthDate": patient.birthDate,
                "email": patient.email,
                "insuranceType": patient.insuranceType,
                "occupation": patient.occupation,
                "medicalHistory": {
                    "allergies": "Pollen, Peanuts",
                    "previousDiseases": "Hypertension",
                    "surgeries": "Appendectomy"
                }
        }