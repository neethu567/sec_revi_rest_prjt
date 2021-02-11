from django.contrib import admin
from newapp.models import Student,Laptop,University,Country
# Register your models here.
admin.site.register(Student)
admin.site.register(Laptop)
admin.site.register(Country)
admin.site.register(University)