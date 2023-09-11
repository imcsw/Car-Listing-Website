from django.contrib import admin
from .models import Cars, CarsImage, Enquiry, TestDrive

# Register your models here.
admin.site.register(Cars)
admin.site.register(Enquiry)
admin.site.register(TestDrive)
admin.site.register(CarsImage)