from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import models
from appMedicalHistory.models.medicalNotes import MedicalNotes
from appMedicalHistory.serializers.medicalNotesSerializer import MedicalNotesSerializer


@api_view(['GET','POST'])
def medicalNotesList(request, pk=None):
    if request.method ==  'GET':
        if pk is not None:
            medicalNotes= MedicalNotes.objects.filter(models.Q(consultationID__icontains=pk)|
                                                        models.Q(medicalNotesID__icontains=pk))
        else:
            medicalNotes= MedicalNotes.objects.all()
        serializer = MedicalNotesSerializer(medicalNotes,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =MedicalNotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(['GET','PUT'])
def medicalNotesDetail(request, pk=None): 
    medicalNotes= MedicalNotes.objects.filter(medicalNotesID = pk).first()
    if request.method =='GET':
        serializer = MedicalNotesSerializer(medicalNotes)
        return Response(serializer.data)
    elif request.method  == 'PUT':
        serializer= MedicalNotesSerializer(medicalNotes,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=401)