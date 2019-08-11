from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from taxi.serializers import Taxidriver, TaxidriverList
from taxi.models import Driver
from taxi.forms import DriverForm
# Create your views here.


class CreateDriverSerialiser(generics.CreateAPIView):
    serializer_class = Taxidriver


class DriverList(generics.ListAPIView):
    serializer_class = TaxidriverList
    queryset = Driver.objects.all()


class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaxidriverList
    queryset = Driver.objects.all()


def main_page(request):
    return render(request, 'index.html', {})


def signup_manager(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


def signup_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = DriverForm()
    return render(request, 'registration/driver_create.html', {
        'form': form
    })