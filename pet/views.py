from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.utils import timezone
from django.http import HttpResponse 
from pet.models import Pet, Appointment

# Create your views here.
class Home(ListView):
    def get(self, request):
        return render(request, 'home.html')

class Pet_List_Page(ListView):
    model = Pet
    
    def get(self, request):
        pets = self.get_queryset().all()
        return render(request, 'pet/PetsList.html', {'pets': pets})

class PetCreateView(CreateView):
    model = Pet
    fields = ['owner', 'pet_name', 'species', 'breed', 'weight_in_lbs']
    template_name = 'pet/Create_Pet.html'

class PetDetailView(DetailView):
    def get(self, request, pet_id):
        return render(request, 'pet/Pet_Detail.html', {'pet': Pet.objects.get(id=pet_id)})

class AppointmentScheduler(CreateView):
    model = Appointment
    fields = ['date_of_appointment', 'duration_minutes', 'special_instructions', 'pet']
    template_name = 'schedule/ScheduleAppointmentPage.html'


class CalendarView(ListView):
    model = Appointment

    def get(self, request):
        appointments = self.get_queryset().all()
        return render(request, 'schedule/Appointment_List.html', {'appointments': appointments.filter(
            date_of_appointment__gte=timezone.now()
        ).order_by('date_of_appointment', 'duration_minutes')})
