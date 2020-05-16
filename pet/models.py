from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
    pet_name = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    weight_in_lbs = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, help_text='The user who posted this question.')

    def __str__(self):
        self.pet_name

class Appointment(models.Model):
    date_of_appointment = models.DateTimeField('Appointment Date')
    duration_minutes = models.IntegerField(default=0)
    special_instructions = models.CharField(max_length=600)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        self.pet.pet_name