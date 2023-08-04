from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import models
from appMedicalHistoryPDF.models.pastHistory import PastHistory
from appMedicalHistoryPDF.serializers.pastHistorySerializer import PastHistorySerializer



@api_view(['GET','POST'])
def pastHistoryList(request, pk=None):
    if request.method ==  'GET':
        if pk is not None:
            pastHistory= PastHistory.objects.filter(models.Q(medicalHistoryID__icontains=pk)|
                                                           models.Q(pastHistoryID__icontains=pk)|
                                                           models.Q(patientID__icontains=pk))
        else:
            pastHistory= PastHistory.objects.all()
        serializer = PastHistorySerializer(pastHistory,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        pastHistorySerializer =PastHistorySerializer(data=request.data)
        if pastHistorySerializer.is_valid():
            pastHistorySerializer.save()
            return Response(pastHistorySerializer.data)
        return Response(pastHistorySerializer.errors)
    
    
@api_view(['GET','PUT'])
def pastHistoryDetail(request, pk=None): 
    pastHistory= PastHistory.objects.filter(pastHistoryID = pk).first()
    if request.method =='GET':
        pastHistoryerializer = PastHistorySerializer(pastHistory)
        return Response(pastHistoryerializer.data)
    elif request.method  == 'PUT':
        pastHistoryerializer= PastHistorySerializer(pastHistory,data=request.data)
        if PastHistorySerializer.is_valid():
            PastHistorySerializer.save()
            return Response(PastHistorySerializer.data,status=201)
        return Response(PastHistorySerializer.errors,status=401)