from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Cars, CarsImage
from .forms import TestDriveForm, EnquiryForm

# Create your views here.
def index(request):
    carList = Cars.objects.order_by('-dateAdded').exclude(sold='True')
    return render(request, 'cars/index.htm', {'carList': carList,})

def details(request, cars_id):
    cars = get_object_or_404(Cars, pk = cars_id)
    carsImage = CarsImage.objects.all().filter(cars_id = cars_id)
    return render(request, 'cars/details.htm', {'cars': cars, 'carsImage': carsImage})

def enquiry(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cars:submitenquiry'))
    else:
        form = EnquiryForm()    
    return render(request, 'cars/enquiry.htm', {'form': form,})

def submitenquiry(request):
    return render(request, 'cars/submitenquiry.htm',)

def submittestdrive(request):
    #cars = get_object_or_404(Cars, pk = cars_id)
    return render(request, 'cars/submittestdrive.htm',)

@login_required
def testdrive(request):
    cars = Cars.objects.all()
    form = TestDriveForm

    if request.method == "POST":
        form = TestDriveForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cars:submittestdrive'))
    return render(request, 'cars/testdrive.htm', {'form': form, 'cars': cars})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('cars:index'))
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.htm', {'form': form})