from appPatients.models.patients import Patients
from appMedicalHistory.models.medicalHistory import MedicalHistory
from appMedicalHistory.serializers.medicalHistorySerializer import MedicalHistorySerializer
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    medicalHistory = MedicalHistorySerializer(required=False, allow_null=True)
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
        medical_history_data = validated_data.pop('medicalHistory', {})
        patient_instance = Patients.objects.create(**validated_data)

        # Crear la historia clínica automáticamente si se proporcionan datos
        if medical_history_data is not None:
            MedicalHistory.objects.create(patient=patient_instance, **medical_history_data)

        return patient_instance
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
                    "allergies": medicalHistory.allergies,
                    "previousDiseases": medicalHistory.previousDiseases,
                    "surgeries": medicalHistory.surgeries
                }
        }