from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import models
from appMedicalAppointment.models.medicalAppointment import MedicalAppointment
from appMedicalAppointment.serializers.appointmentSerializer import AppointmentSerializer



@api_view(['GET','POST'])
def appointmentList(request, pk=None):
    if request.method ==  'GET':
        if pk is not None:
            apointments= MedicalAppointment.objects.filter(models.Q(appointmentID__icontains=pk)|
                                                           models.Q(employeeID__icontains=pk)|
                                                           models.Q(patientID__icontains=pk))
        else:
            apointments= MedicalAppointment.objects.all()
        serializer = AppointmentSerializer(apointments,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        appointmentSerializer =AppointmentSerializer(data=request.data)
        if appointmentSerializer.is_valid():
            appointmentSerializer.save()
            return Response(appointmentSerializer.data)
        return Response(appointmentSerializer.errors)
    
    
@api_view(['GET','PUT'])
def appointmentDetail(request, pk=None): 
    apointments= MedicalAppointment.objects.filter(appointmentID = pk).first()
    if request.method =='GET':
        appointmenterializer = AppointmentSerializer(apointments)
        return Response(appointmenterializer.data)
    elif request.method  == 'PUT':
        appointmenterializer= AppointmentSerializer(apointments,data=request.data)
        if AppointmentSerializer.is_valid():
            AppointmentSerializer.save()
            return Response(AppointmentSerializer.data,status=201)
        return Response(AppointmentSerializer.errors,status=401)
