from django.shortcuts import render
from rest_framework import serializers
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

def student_detail(request, pk):
    std = Student.objects.get(id=pk)
    serializer = StudentSerializer(std)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
    # or
    # return JsonResponse(serializer.data)


def student_all(request):
    std = Student.objects.all()
    serializer = StudentSerializer(std, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    # or
    return JsonResponse(serializer.data, safe=False)
    # if we have many data then we need to spcify safe=False

# process of deserialization
@csrf_exempt
def student_create(request):
    # This want work using postman agent
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'message': 'Data Created Succesfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')