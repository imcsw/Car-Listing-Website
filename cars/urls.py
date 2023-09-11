from django.urls import path, include

from . import views

app_name = "cars"

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('<int:cars_id>', views.details, name='details'),
    path('enquiry', views.enquiry, name='enquiry'),
    path('testdrive', views.testdrive, name='testdrive'),
    path('submitenquiry', views.submitenquiry, name='submitenquiry'),
    path('submittestdrive', views.submittestdrive, name='submittestdrive'),
]