from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Patient

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only = True, style = {'input_type': 'password'} )

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        
        user.set_password(validated_data['password'])
        user.save()

        return user


class PatientSerializer(serializers.Serializer):
    dob = serializers.DateField()
    gender = serializers.CharField()
    relationship_status = serializers.CharField()
    children = serializers.IntegerField()
    address = serializers.CharField()
    profession = serializers.CharField()
    blood_group = serializers.CharField()
    height = serializers.CharField()
    weight = serializers.CharField()
    blood_pressure = serializers.CharField()
    allergies = serializers.CharField()
    sugar_level = serializers.CharField()
    routine_medications = serializers.CharField()
    surgical_history = serializers.CharField()
    other_details = serializers.CharField()
    em_contact_name = serializers.CharField()
    em_phone = serializers.CharField()
    is_in_healthcare = serializers.BooleanField()
    healthcare_catagory = serializers.CharField()

    def create(self, validated_data):
        patient = Patient.objects.create(**validated_data)
        return patient

    def update(self, instance, validated_data):
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.relationship_status = validated_data.get('relationship_status', instance.relationship_status)
        instance.children = validated_data.get('children', instance.children)
        instance.address = validated_data.get('address', instance.address)
        instance.profession = validated_data.get('profession', instance.profession)
        instance.blood_group = validated_data.get('blood_group', instance.blood_group)
        instance.height = validated_data.get('height', instance.height)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.blood_pressure = validated_data.get('blood_pressure', instance.blood_pressure)
        instance.allergies = validated_data.get('allergies', instance.allergies)
        instance.sugar_level = validated_data.get('sugar_level', instance.sugar_level)
        instance.routine_medications = validated_data.get('routine_medications', instance.routine_medications)
        instance.surgical_history = validated_data.get('age', instance.age)
        instance.other_details = validated_data.get('age', instance.age)
        instance.em_contact_name = validated_data.get('age', instance.age)
        instance.em_phone = validated_data.get('age', instance.age)
        instance.is_in_healthcare = validated_data.get('age', instance.age)
        instance.healthcare_catagory = validated_data.get('age', instance.age)