# Generated by Django 4.2.4 on 2023-09-06 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appPatients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('consultationID', models.AutoField(primary_key=True, serialize=False)),
                ('consultationDate', models.DateField(verbose_name='consultationDate')),
                ('state', models.BooleanField(default=True)),
                ('diagnosis', models.CharField(max_length=3000, verbose_name='Diagnosis')),
                ('treatment', models.CharField(max_length=3000, verbose_name='Treatment')),
                ('employeeID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VitalSings',
            fields=[
                ('vitalSingsID', models.AutoField(primary_key=True, serialize=False)),
                ('recordignDate', models.DateTimeField(auto_now=True)),
                ('bloodPressure', models.CharField(max_length=100)),
                ('heartRate', models.CharField(max_length=4)),
                ('temperature', models.CharField(max_length=3)),
                ('weight', models.CharField(max_length=3)),
                ('height', models.CharField(max_length=3)),
                ('consultationID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appMedicalHistory.consultation')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalNotes',
            fields=[
                ('medicalNotesID', models.AutoField(primary_key=True, serialize=False)),
                ('noteDate', models.DateTimeField(auto_now=True)),
                ('Description', models.CharField(max_length=2000)),
                ('consultationID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appMedicalHistory.consultation')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('historyID', models.AutoField(primary_key=True, serialize=False)),
                ('allergies', models.CharField(max_length=3000, null=True)),
                ('previousDiseases', models.CharField(max_length=3000, null=True)),
                ('surgeries', models.CharField(max_length=3000, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='medicalHistory', to='appPatients.patients')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalExams',
            fields=[
                ('medicalExamsID', models.AutoField(primary_key=True, serialize=False)),
                ('medicalExamsDate', models.DateField()),
                ('examType', models.CharField(max_length=2000)),
                ('Results', models.CharField(max_length=2000)),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPatients.patients')),
                ('consultationID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appMedicalHistory.consultation')),
            ],
        ),
        migrations.AddField(
            model_name='consultation',
            name='historyID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appMedicalHistory.medicalhistory'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='patientID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPatients.patients'),
        ),
    ]
