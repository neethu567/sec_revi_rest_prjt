from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import View, APIView
from django.http import HttpResponse
from rest_framework.response import Response

from newapp import serializers
from newapp.models import Student,Laptop,University,Country
from newapp.serializers import StudentSerializer,LaptopSerializer,CountrySerializer,UniversitySerializer
# from rest_framework.views
# Create your views here.
#
class Sample(View):
    def get(self,request):
        return HttpResponse("sample newapp code")

class CountryListCreate(generics.ListCreateAPIView):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class LaptopListCreate(generics.ListCreateAPIView):

    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer

class UniversityCreate(generics.ListCreateAPIView):

    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class StudentListCreate(generics.ListCreateAPIView):

    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.StudentSerializer
        return serializers.StudentGetSerializer