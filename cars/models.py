import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Cars(models.Model):
    carModel = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    dateAdded = models.DateTimeField('date published')
    description = models.CharField(max_length=1000, null=True, blank=True)
    shortDesc = models.CharField(max_length=500, null=True, blank=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.manufacturer + " " + self.carModel

    def wasPublishedRecently(self):
        return self.dateAdded >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        verbose_name_plural = "Cars"

class CarsImage(models.Model):
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cars Images"

class Enquiry(models.Model):
    name = models.CharField(max_length=150, null=True, blank=False)
    email = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=25, blank=False)
    remarks = models.CharField(max_length=250, blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Enquiry"

class TestDrive(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=150, null=True, blank=False)
    email = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=200, blank=False)
    phoneNumber = models.CharField(max_length=25, blank=False)
    date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Test Drive"