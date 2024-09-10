import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from home.models import Job  # Make sure the correct model is imported

class Command(BaseCommand):
    help = 'Load jobs from a JSON file into the database'

    def handle(self, *args, **kwargs):
        # Path to the JSON file
        file_path = os.path.join(settings.BASE_DIR, 'joblistings.json')

        # Load job listings from the JSON file
        with open(file_path, 'r') as file:
            jobs_data = json.load(file)

        # Iterate through each job in the JSON data and create Job objects
        for job in jobs_data:
            Job.objects.create(
                title=job['title'],
                company=job['company'],
                location=job['location'],
                description=job['description'],
                apply_link=job['applyLink']
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded job listings from the JSON file.'))