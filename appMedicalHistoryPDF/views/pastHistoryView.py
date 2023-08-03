from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import models
from appMedicalHistoryPDF.models.pastHistory import PastHistory
from appMedicalHistoryPDF.serializers.pastHistorySerializer import PastHistorySerializer



@api_view(['GET','POST'])
def appointmentList(request, pk=None):
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
        appointmentSerializer =PastHistorySerializer(data=request.data)
        if appointmentSerializer.is_valid():
            appointmentSerializer.save()
            return Response(appointmentSerializer.data)
        return Response(appointmentSerializer.errors)
    
    
@api_view(['GET','PUT'])
def appointmentDetail(request, pk=None): 
    pastHistory= PastHistory.objects.filter(appointmentID = pk).first()
    if request.method =='GET':
        appointmenterializer = PastHistorySerializer(pastHistory)
        return Response(appointmenterializer.data)
    elif request.method  == 'PUT':
        appointmenterializer= PastHistorySerializer(pastHistory,data=request.data)
        if PastHistorySerializer.is_valid():
            PastHistorySerializer.save()
            return Response(PastHistorySerializer.data,status=201)
        return Response(PastHistorySerializer.errors,status=401)