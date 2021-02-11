from rest_framework import serializers
from newapp.models import *

class LaptopSerializer(serializers.ModelSerializer):

    class Meta:
        model=Laptop
        fields=['id','laptop_name']

class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model=University
        fields=['id','university_name']

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model=Country
        fields=['id','country_name']


    # country = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # country=serializers.CharField(max_length=200,None=True)

        # fields=['id','country_name']
    #
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Country.objects.create(**validated_data)


class StudentSerializer(serializers.ModelSerializer):


    # laptop=LaptopSerializer()
    # university=UniversitySerializer()
    # country=CountrySerializer()

    class Meta:
        model=Student
        fields=['id','name','phone','address','country','university','laptop']


class StudentGetSerializer(serializers.ModelSerializer):


    laptop=LaptopSerializer()
    university=UniversitySerializer()
    country=CountrySerializer()

    class Meta:
        model=Student
        fields=['id','name','phone','address','country','university','laptop']

