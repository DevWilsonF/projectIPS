from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import models
from appMedicalHistory.models.medicalExams import MedicalExams
from appMedicalHistory.serializers.medicalExamsSerializers import MedicalExamsSerializer


@api_view(['GET','POST'])
def medicalExamsList(request, pk=None):
    if request.method ==  'GET':
        if pk is not None:
            medicalExams= MedicalExams.objects.filter(models.Q(patientID__icontains=pk)|
                                                        models.Q(medicalExamsID__icontains=pk))
        else:
            medicalExams= MedicalExams.objects.all()
        serializer = MedicalExamsSerializer(medicalExams,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =MedicalExamsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(['GET','PUT'])
def medicalExamsDetail(request, pk=None): 
    medicalExams= MedicalExams.objects.filter(consultationID = pk).first()
    if request.method =='GET':
        serializer = MedicalExamsSerializer(medicalExams)
        return Response(serializer.data)
    elif request.method  == 'PUT':
        serializer= MedicalExamsSerializer(medicalExams,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=401)