from django.contrib import admin
from appMedicalHistory.models import *
# Register your models here.
admin.site.register(Consultation)
admin.site.register(MedicalExams)
admin.site.register(MedicalHistory)
admin.site.register(MedicalNotes)
admin.site.register(VitalSings)