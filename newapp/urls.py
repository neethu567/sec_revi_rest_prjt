from django.urls import path
from newapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns =[
    path('sample/',views.Sample.as_view(),name="sample"),
    path("student/",views.StudentListCreate.as_view()),
    path("country/",views.CountryListCreate.as_view()),
    path("laptop/",views.LaptopListCreate.as_view()),
    path("university/",views.UniversityCreate.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
