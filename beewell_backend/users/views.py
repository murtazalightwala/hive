import json
from rest_framework.views import APIView
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import PatientSerializer
from .models import Patient
from django.http import HttpResponse
import io
from rest_framework.permissions import IsAuthenticated  # <-- Here


# Create your views here.    

class PatientView(APIView):

    permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        print(request.user)
        print(request.headers)
        if request.user:
            print(request.user.username)
            token = request.headers['Authorization'].split()[-1]
            print(token)
            auser = Token.objects.get(key = token)
            print(auser.user)
            patient = get_object_or_404(Patient, user = auser.user)
            patient = PatientSerializer(patient)
            return HttpResponse(JSONRenderer().render(patient.data), content_type = 'application/json')

    def post(self, request):
        json_data = request.body
        data = JSONParser().parse(io.BytesIO(json_data))
        



def patient(request):
    if request.method == 'POST':
        json_data = request.body
        data = JSONParser().parse(io.BytesIO(json_data))
        print(data)
        patient_data = PatientSerializer(data = data)
        if patient_data.is_valid():
            print("Yay!")
        else:   
            print(patient_data.errors)
        return HttpResponse(JSONRenderer().render({'message': 'Target Reached'}), content_type = 'application/json')
    elif request.method == 'GET':
        print(request.user)
        print(request.headers)
        if request.user:
            print(request.user.username)
            token = request.headers['Authorization'].split()[-1]
            print(token)
            auser = Token.objects.get(key = token)
            print(auser.user)
            patient = get_object_or_404(Patient, user = auser.user)
            patient = PatientSerializer(patient)
            return HttpResponse(JSONRenderer().render(patient.data), content_type = 'application/json')
        # patient = Patient.objects.get(user = request.user)

def sign_in(request):
    if request.method == 'POST':
        user = authenticate()
    pass

def sign_out(request):
    pass

def sign_up(request):
    pass