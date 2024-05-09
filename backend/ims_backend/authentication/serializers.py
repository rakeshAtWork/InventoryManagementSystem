from rest_framework import serializers

from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['name', 'age']
        # exclude = ['id']
        fields = '__all__'

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError("Age should be greater than 18")
        return data
