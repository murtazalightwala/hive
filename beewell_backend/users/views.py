import json

from django.views.decorators import csrf
from rest_framework.views import APIView
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import PatientSerializer, UserSerializer
from .models import Patient
from django.http import HttpResponse
import io
from rest_framework.permissions import IsAuthenticated, AllowAny  # <-- Here


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
        return Http404("Page does not exist")



# def patient(request):
#     if request.method == 'POST':
#         json_data = request.body
#         data = JSONParser().parse(io.BytesIO(json_data))
#         print(data)
#         patient_data = PatientSerializer(data = data)
#         if patient_data.is_valid():
#             print("Yay!")
#         else:   
#             print(patient_data.errors)
#         return HttpResponse(JSONRenderer().render({'message': 'Target Reached'}), content_type = 'application/json')
#     elif request.method == 'GET':
#         print(request.user)
#         print(request.headers)
#         if request.user:
#             print(request.user.username)
#             token = request.headers['Authorization'].split()[-1]
#             print(token)
#             auser = Token.objects.get(key = token)
#             print(auser.user)
#             patient = get_object_or_404(Patient, user = auser.user)
#             patient = PatientSerializer(patient)
#             return HttpResponse(JSONRenderer().render(patient.data), content_type = 'application/json')
#         # patient = Patient.objects.get(user = request.user)

class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request): 
        json_data = request.body
        data = JSONParser().parse(io.BytesIO(json_data))
        print(data)
        user_data = UserSerializer(data = data)
        if user_data.is_valid():
            user_data.save()
            print("Signed Up")
            print(user_data.data)
            
            user = User.objects.get(username = user_data.data['username'])
            print(user)
            token = Token.objects.create(user=user)
            patient = PatientSerializer(data = data)
            if patient.is_valid():
                patient = patient.save()
                patient.user = user
                patient.save()
                print("Patient Created")
            else:
                print(patient.errors)            
        else:
            print(user_data.errors)
        body = {}
        body['token'] = token.key
        return HttpResponse(JSONRenderer().render(body), content_type = 'application/json')

class SignInView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request): 
        json_data = request.body
        data = JSONParser().parse(io.BytesIO(json_data))
        print(data)
        body = {}

        user = authenticate(request, username = data['username'], password = data['password'])
        print(user)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            print(token)
            body['token'] = token.key
            body['user'] = token.user.username
            body['email'] = token.user.email
        else:
            body['message'] = "Authentication Failed"
        return HttpResponse(JSONRenderer().render(body), content_type = 'application/json')

class SignInView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request): 
        json_data = request.body
        data = JSONParser().parse(io.BytesIO(json_data))
        print(data)
        body = {}

        user = authenticate(request, username = data['username'], password = data['password'])
        print(user)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            print(token)
            body['token'] = token.key
            body['user'] = token.user.username
            body['email'] = token.user.email
        else:
            body['message'] = "Authentication Failed"
        return HttpResponse(JSONRenderer().render(body), content_type = 'application/json')
