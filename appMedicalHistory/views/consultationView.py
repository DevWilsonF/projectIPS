from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import models
from appMedicalHistory.models.consultations import Consultation
from appMedicalHistory.serializers.consultationSerializer import ConsultationSerializer



@api_view(['GET','POST'])
def consultationList(request, pk=None):
    if request.method ==  'GET':
        if pk is not None:
            consultation= Consultation.objects.filter(models.Q(consultationID__icontains=pk)|
                                                        models.Q(patientID__icontains=pk)|
                                                        models.Q(employeeID__icontains=pk)|
                                                        models.Q(historyID__icontains=pk))
        else:
            consultation= Consultation.objects.all()
        serializer = ConsultationSerializer(consultation,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =ConsultationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
@api_view(['GET'])    
def consultationStateDetail(request, pk=None): 
    consultation= Consultation.objects.filter(state = pk)
    if request.method =='GET':
        serializer = ConsultationSerializer(consultation,many=True)
        return Response(serializer.data)   


@api_view(['GET','PUT'])
def consultationDetail(request, pk=None): 
    consultation= Consultation.objects.filter(consultationID = pk).first()
    if request.method =='GET':
        serializer = ConsultationSerializer(consultation)
        return Response(serializer.data)
    elif request.method  == 'PUT':
        serializer= ConsultationSerializer(consultation,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=401)