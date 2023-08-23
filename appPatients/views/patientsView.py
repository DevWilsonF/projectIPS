from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import models
from appPatients.models.patients import Patients
from appPatients.serializers.patientsSerializer import PatientSerializer



@api_view(['GET','POST'])
def patientsList(request, pk=None):
    if request.method ==  'GET':
        if pk is not None:
            patients= Patients.objects.filter(models.Q(firstName__icontains=pk)|
                                models.Q(documentNumber__icontains=pk)|
                                models.Q(lastName__icontains=pk))
        else:
            patients= Patients.objects.all()
        serializer = PatientSerializer(patients,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        patientsSerializer =PatientSerializer(data=request.data)
        if patientsSerializer.is_valid():
            patientsSerializer.save()
            return Response(patientsSerializer.data)
        return Response(patientsSerializer.errors)
    
    
@api_view(['GET','PUT'])
def patientsDetail(request, pk=None): 
    patients= Patients.objects.filter(PatientID = pk).first()
    if request.method =='GET':
        patientSerializer = PatientSerializer(patients)
        return Response(patientSerializer.data)
    elif request.method  == 'PUT':
        patientSerializer= PatientSerializer(patients,data=request.data)
        if patientSerializer.is_valid():
            patientSerializer.save()
            return Response(patientSerializer.data,status=201)
        return Response(patientSerializer.errors,status=401)


    
