from functools import partial
import io
from django.db.models import manager
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Student

@csrf_exempt
def student(request):
    """
    Here accepts data from .py file not from POSTMAN
    """
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id is not None:
            st = Student.objects.get(id=id)
            sr = StudentSerializer(st)
            json_data = JSONRenderer().render(sr.data)
            return HttpResponse(json_data, content_type='application/json')
            
        st = Student.objects.all()
        sr = StudentSerializer(st, many=True)
        json_data = JSONRenderer().render(sr.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        sr = StudentSerializer(data=python_data)
        if sr.is_valid():
            sr.save()
            res = {'message': 'Data Uploaded Successfully'}
            json_res = JSONRenderer().render(res)
        else:
            json_res = JSONRenderer().render(sr.errors)

        return HttpResponse(json_res, content_type='application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        st = Student.objects.get(id=python_data.get('id'))
        # For complete update
        # sr = StudentSerializer(st, data=python_data)
        # For partial update
        sr = StudentSerializer(st, data=python_data, partial=True)
        if sr.is_valid():
            sr.save()
            res = {'message': 'Data Updated Successfully'}
            json_res = JSONRenderer().render(res)
        else:
            json_res = JSONRenderer().render(sr.errors)

        return HttpResponse(json_res, content_type='application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        st = Student.objects.filter(id=id).first()
        if st is not None:
            st.delete()
            res = {'message': 'Student deleted successfully'}
        else:    
            res = {'message': 'Please enter valid id'}
        json_res = JSONRenderer().render(res)   
        return HttpResponse(json_res, content_type='application/json')

        