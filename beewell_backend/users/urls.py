from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.PatientView.as_view(), name = "Patient View"),
    path('get_token/', obtain_auth_token)
    
]
