"""
URL configuration for authIPSPrevenir project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from appEmployees.views.employeeView import (UserGetView,UserPostView)
from appPatients.views.patientsView import (patientsList,patientsDetail)
from appMedicalAppointment.views.appointmentView import(appointmentDetail,appointmentList)
from appMedicalHistory.views import *
from appMedicalHistoryPDF.views.pastHistoryView import (pastHistoryDetail,pastHistoryList)
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('user/',UserPostView.as_view()),
    path('user/<int:pk>',UserGetView.as_view()),
    path('patients/',patientsList),
    path('patients/<str:pk>',patientsList),
    path('patientsDetail/<int:pk>',patientsDetail),
    path('appointmentDetail/<int:pk>',appointmentDetail),
    path('appointmentList/<int:pk>',appointmentList),
    path('appointmentList/',appointmentList),
    path('pastHistoryDetail/<int:pk>',pastHistoryDetail),
    path('pastHistoryList/<int:pk>',pastHistoryList),
    path('pastHistoryList/',pastHistoryList),
    path('consultationDetail/<int:pk>',consultationDetail),
    path('consultationList/<int:pk>',consultationList),
    path('consultationList/',consultationList),
    path('consultationStateDetail/<int:pk>',consultationStateDetail),
    path('medicalExamsDetail/<int:pk>',medicalExamsDetail),
    path('medicalExamsList/',medicalExamsList),
    path('medicalExamsList/<int:pk>',medicalExamsList),
    path('medicalHistoryDetail/<int:pk>',medicalHistoryDetail),
    path('medicalHistoryList/',medicalHistoryList),
    path('medicalHistoryList/<int:pk>',medicalHistoryList),
    path('medicalNotesDetail/<int:pk>',medicalNotesDetail),
    path('medicalNotesList/<int:pk>',medicalNotesList),
    path('medicalNotesList/',medicalNotesList),
    path('vitalSignsDetail/<int:pk>',vitalSingsDetail),
    path('vitalSingsList/<int:pk>',vitalSingsList),
    path('vitalSingsList/',vitalSingsList),
]
