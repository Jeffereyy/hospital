from django.shortcuts import render, redirect
from .forms import UserRegister
from .models import Schedule, Doctor
from django.views.generic import TemplateView

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
    args = {
        "doctors": doctors,
    }

    return render(request, 'main/doctors.html', args)

class Book(TemplateView):

    template_name = 'main/book.html'

    def get(self, request, doctor_name):
        doctor_name = request.path_info
        doctor_name = str(doctor_name)[9:len(doctor_name)]
        schedules = Schedule.objects.filter(doctor_name=doctor_name)
        args = {
            "schedules": schedules,
        }
        return render(request, self.template_name, args)

    def post(self, request, doctor_name):
        schedule_id = int(request.POST['schedule_id'][0])
        patient_name = request.POST['patient_name']
        if Schedule.objects.get(id=schedule_id).vacant == True:
            schedule = Schedule.objects.get(id=schedule_id)
            schedule.vacant = False
            schedule.patient_name = patient_name
            schedule.save()

            args = {
                "message": "You have succesfully reserved an appointment",
            }
        else:
            args = {
                "message": "Sorry this one is already reserved",
            }
        return render(request, self.template_name, args)