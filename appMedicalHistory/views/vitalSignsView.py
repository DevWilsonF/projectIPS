from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import models
from appMedicalHistory.models.vitalSigns import VitalSings
from appMedicalHistory.serializers.vitalSingsSerializers import VitalSingsSerializer


@api_view(['GET','POST'])
def vitalSingsList(request, pk=None):
    if request.method ==  'GET':
        if pk is not None:
            vitalSigns= VitalSings.objects.filter(models.Q(consultationID__icontains=pk)|
                                                        models.Q(vitalSingsID__icontains=pk))
        else:
            vitalSigns= VitalSings.objects.all()
        serializer = VitalSingsSerializer(vitalSigns,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =VitalSingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(['GET','PUT'])
def vitalSingsDetail(request, pk=None): 
    vitalSigns= VitalSings.objects.filter(vitalSingsID = pk).first()
    if request.method =='GET':
        serializer = VitalSingsSerializer(vitalSigns)
        return Response(serializer.data)
    elif request.method  == 'PUT':
        serializer= VitalSingsSerializer(vitalSigns,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=401)