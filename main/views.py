from django.shortcuts import render, redirect
from .forms import UserRegister
from .models import Schedule, Doctor

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = UserRegister()

    return render(request, 'main/register.html', {"form": form})

def doctors(request):
    doctors = Doctor.objects.all()
    context = {
        "doctors": doctors,
    }

    return render(request, 'main/doctors.html', context)

def book(request, doctor_name):
    doctor_name = request.path_info
    doctor_name = str(doctor_name)[9:len(doctor_name)]
    schedules = Schedule.objects.filter(doctor_name=doctor_name)
    context = {
        "schedules": schedules,
    }

    return render(request, 'main/book.html', context)