from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import models
from appMedicalHistory.models.medicalHistory import MedicalHistory
from appMedicalHistory.serializers.medicalHistorySerializer import MedicalHistorySerializer


@api_view(['GET','POST'])
def medicalHistoryList(request, pk=None):
    if request.method ==  'GET':
        if pk is not None:
            medicalHistory= MedicalHistory.objects.filter(models.Q(patientID__icontains=pk)|
                                                        models.Q(historyID__icontains=pk))
        else:
            medicalHistory= MedicalHistory.objects.all()
        serializer = MedicalHistorySerializer(medicalHistory,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =MedicalHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(['GET','PUT'])
def medicalHistoryDetail(request, pk=None): 
    medicalHistory= MedicalHistory.objects.filter(consultationID = pk).first()
    if request.method =='GET':
        serializer = MedicalHistorySerializer(medicalHistory)
        return Response(serializer.data)
    elif request.method  == 'PUT':
        serializer= MedicalHistorySerializer(medicalHistory,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=401)