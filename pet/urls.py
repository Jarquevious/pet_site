from . import views
from django.urls import path
from pet.views import Home, PetCreateView, Pet_List_Page, PetDetailView, AppointmentScheduler, CalendarView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('pets/', Pet_List_Page.as_view(), name='pets-list-page'),
    path('pet/create/', PetCreateView.as_view(), name='pet-create-page'),
    path('pets/<int:pet_id>/', PetDetailView.as_view(), name='pet-detail-page'),
    path('schedule/', CalendarView.as_view(), name='calendar-list'),
    path('schedule/createtime', AppointmentScheduler.as_view(), name='calendar-create'),
]