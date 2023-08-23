from django.db import models

   
class Patients(models.Model):
    PatientID = models.AutoField(primary_key=True)
    firstName = models.CharField('Name', max_length=30, null=False)
    lastName = models.CharField('Lastname', max_length=30, null=False)
    registrationDate = models.DateTimeField('RegistrationDate', auto_now_add= True, null= False)
    phone = models.CharField('Phone', max_length=30, null=False)
    gender = models.CharField('Gender', max_length=30, null=False)
    maritalStatus = models.CharField('MaritalStatus',max_length= 15, null= False)
    nationality = models.CharField('Nationality', max_length= 15, null=False)
    city = models.CharField('City', max_length=30, null=False)
    address = models.CharField('Address', max_length=120, null=False)
    documentType = models.CharField('DocumentType', max_length=30, null=False)
    documentNumber = models.CharField('DocumentNumber', max_length=30, null=False)
    birthDate = models.DateField('BirthDate', null=False)
    email = models.EmailField('Email', max_length=30, null=False)
    insuranceType = models.CharField('InsuranceType', max_length=15, null= False)
    occupation = models.CharField('Occupation', max_length=30, null= False)

    def __str__(self):
        return f"{self.PatientID}: {self.firstName} {self.lastName}"