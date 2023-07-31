from rest_framework import serializers
from appEmployees.models.employee import User

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=[
            'id',
            'username',
            'password',
            'role',
            'state',
        ]