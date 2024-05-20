from django.core.management.base import BaseCommand
from invitations.models import Invitation
import csv

class Command(BaseCommand):
    help = 'Export invitations data to CSV'

    def handle(self, *args, **kwargs):
        try:
            with open('invitations_data.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['age', 'gender', 'occupation', 'past_attendance', 'social_media_followers',
                                 'interest_in_music', 'interest_in_art', 'interest_in_technology', 'distance_from_venue',
                                 'has_plus_one', 'invited'])
                for invitation in Invitation.objects.all():
                    writer.writerow([
                        invitation.age, 
                        invitation.gender, 
                        invitation.occupation, 
                        invitation.past_attendance, 
                        invitation.social_media_followers, 
                        invitation.interest_in_music, 
                        invitation.interest_in_art, 
                        invitation.interest_in_technology, 
                        invitation.distance_from_venue, 
                        invitation.has_plus_one, 
                        invitation.invited
                    ])
            self.stdout.write(self.style.SUCCESS('Successfully exported invitations data to invitations_data.csv'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error exporting data: {e}'))
