from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    pass_date = serializers.DateTimeField()

    # to insert/create a data
    def create(self, validated_data):
        print(10*'%%')

        print(validated_data)
        
        return Student.objects.create(**validated_data)