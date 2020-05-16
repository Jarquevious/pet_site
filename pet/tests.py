from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from pets.models import Pet, Appointment
# Create your tests here.

class PetsTests(TestCase):

    def test_pet_list(self):

        user = User.objects.create()
        user.save()
        self.client.login(username='John', password='loveislove45%')

        pet = Pet.objects.create(pet_name='Nicki', species='Dog', breed='Poodle', weight_in_pounds=18, owner=user)
        pet.save()
        response = self.client.get(f'/pets/')
        self.assertEqual(response.status_code, 200)
        
        pet_info = Pet.objects.get(owner=user)
        self.assertEqual(pet_info.owner, user)
        
        pet_info = Pet.objects.get(owner=user)
        self.assertEqual(pet_info.owner, user)

    def test_pet_detail(self):

        user = User.objects.create()
        user.save()
        self.client.login(username='John', password='loveislove45%')

        pet = Pet.objects.create(pet_name='Nicki', species='Dog', breed='Poodle', weight_in_pounds=18, owner=user)
        pet.save()

        schedule = Appointment.objects.create(date_of_appointment="2020-05-28", duration_minutes=75, special_instructions="Leash is in closet immediately to your right when you walk in. The key box number 3454.", pet=pet)
        schedule.save()
        response = self.client.get(f'/pets/{pet.id}/')
        pet_info = Pet.objects.get(species="Dog")
        self.assertEqual(pet_info.species, "Dog")

    def test_pet_create(self):

        user = User.objects.create()
        user.save()
        post_data = {
            'pet_name': 'Nicki', 'species': 'Dog', 'breed': 'Poodle', 'weight_in_pounds': 18, 'owner': user.id
        }

        response = self.client.post('/pet/create/', data=post_data)
        self.assertEqual(response.status_code, 302)

        pet_info = Pet.objects.get(weight_in_pounds=18)
        self.assertEqual(pet_info.weight_in_pounds, 18)


class AppointmentTests(TestCase):

    def test_create_appointment(self):

        user = User.objects.create()
        user.save()

        pet = Pet.objects.create(pet_name='Nicki', species='Dog', breed='Poodle', weight_in_pounds=18, owner=user)
        pet.save()

        post_data = {
            'date_of_appointment': '2020-05-28',
            'duration_minutes': 60,
            'special_instructions': 'Dogs are a trigger. She gets very very agressive.',
            'pet': pet
        }

        response = self.client.post('/schedule/createtime', data=post_data)
        self.assertEqual(response.status_code, 200)
        schedule_info = Appointment.objects.get()
        self.assertEqual(schedule_info.duration_minutes, 45)
