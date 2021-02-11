from django.db import models

# Create your models here.
class Country(models.Model):
    country_name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.country_name

class University(models.Model):
    university_name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.university_name

class Laptop(models.Model):
    laptop_name=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.laptop_name

class Student(models.Model):
    name = models.CharField(max_length=100,unique=True)
    phone=models.PositiveIntegerField(null=True)
    address=models.CharField(max_length=500,null=True)
    country=models.ManyToManyField(Country,related_name="travel_country")
    university=models.ForeignKey(University,on_delete=models.CASCADE,related_name="University",null=True)
    laptop=models.OneToOneField(Laptop,on_delete=models.CASCADE,related_name="Laptop",null=True)

    def __str__(self):
        return self.name

