from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import models
from appMedicalHistory.models.medicalHistory import MedicalHistory
from appMedicalHistory.serializers.medicalHistorySerializer import MedicalHistorySerializer


@api_view(['GET','PUT','PATCH'])
def medicalHistoryDetail(request, pk=None):
    medicalHistory= MedicalHistory.objects.filter(models.Q(patient=pk)|
                                                        models.Q(historyID=pk)).first()
    if request.method =='GET':
        serializer = MedicalHistorySerializer(medicalHistory)
        return Response(serializer.data)
    elif request.method  == 'PUT':
        serializer= MedicalHistorySerializer(medicalHistory,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=401)
    elif request.method == 'PATCH':
        serializer = MedicalHistorySerializer(medicalHistory, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=401)
    
