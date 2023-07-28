from rest_framework import serializers
from appEmployees.models.users import User

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['__all__']