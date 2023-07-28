from rest_framework.response import Response
from rest_framework.decorators import api_view
from appPatients.models.patients import Patients
from appPatients.serializers.patientsSerializer import PatientSerializer


@api_view([GET,POST,PUT,DELETE])
