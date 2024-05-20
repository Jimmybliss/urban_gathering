# yourapp/management/commands/populate_invitations.py
import random
from django.core.management.base import BaseCommand
from invitations.models import Invitation

class Command(BaseCommand):
    help = 'Populate the Invitation model with random data'

    def handle(self, *args, **kwargs):
        first_names = ['John', 'Jane', 'Alice', 'Bob', 'Chris', 'Eve' , 'Beatrice', 'Kesia', 'Abdul', 'Peter', 'Henry', 'Dorcass', 'Brenda' ]
        last_names = ['Doe', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Crispin', 'Jonas', 'Keba', 'Mafie', 'Efatha' ]
        genders = ['Male', 'Female']
        occupations = ['Engineer', 'Artist', 'Doctor', 'Teacher', 'Musician', 'Developer', 'Nurse', 'Accountant', 'Technician', 'Sales', 'Optician']
        
        for _ in range(1000):  # Number of entries you want to create
            name = f"{random.choice(first_names)} {random.choice(last_names)}"
            age = random.randint(18, 70)
            gender = random.choice(genders)
            occupation = random.choice(occupations)
            past_attendance = random.choice([True, False])
            social_media_followers = random.randint(0, 1000000)
            interest_in_music = random.choice([True, False])
            interest_in_art = random.choice([True, False])
            interest_in_technology = random.choice([True, False])
            distance_from_venue = round(random.uniform(0.1, 100.0), 2)
            has_plus_one = random.choice([True, False])
            invited = random.choice([True, False])
            
            Invitation.objects.create(
                name=name,
                age=age,
                gender=gender,
                occupation=occupation,
                past_attendance=past_attendance,
                social_media_followers=social_media_followers,
                interest_in_music=interest_in_music,
                interest_in_art=interest_in_art,
                interest_in_technology=interest_in_technology,
                distance_from_venue=distance_from_venue,
                has_plus_one=has_plus_one,
                invited=invited
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the Invitation model with random data'))
