from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    Gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other','Other'),
    ]

    Relationship_status_choices = [
        ('married', 'Married'),
        ('unmarried','Unmarried'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(choices = Gender_choices, max_length=10)
    relationship_status = models.CharField(choices = Relationship_status_choices, max_length= 20)
    children = models.IntegerField()
    address = models.CharField(max_length= 400)
    profession = models.CharField(max_length= 20)
    blood_group = models.CharField(max_length= 10)
    height = models.CharField(max_length= 10)
    weight = models.CharField(max_length= 10)
    blood_pressure = models.CharField(max_length= 20)
    allergies = models.CharField(max_length= 200)
    sugar_level = models.CharField(max_length= 20)
    routine_medications = models.CharField(max_length= 200)
    surgical_history = models.CharField(max_length= 200)
    other_details = models.CharField(max_length= 200)
    em_contact_name = models.CharField(max_length= 100)
    em_phone = models.CharField(max_length= 20)
    is_in_healthcare = models.BooleanField()
    healthcare_catagory = models.CharField(max_length= 20)
    


