from django.core.management.base import BaseCommand, CommandError
from core import models
from faker import Faker
from random import choice, randint

class Command(BaseCommand):
    
    def success(self, message):
        self.stdout.write(self.style.SUCCESS(message))

    def handle(self, *args, **options):
        '''
        seed the database with dummy data
        '''
        fake = Faker()
        count = 4
        for x in range(count):
            models.Organization.objects.create(
                name = fake.company(),
            )
        self.success(f"inserted {count} Organizations")
    
        count = 8
        for x in range(count):
            models.Team.objects.create(
                name = choice(["design", "accounting", "engineering", "marketing", "HR"]),
                organization = choice(models.Organization.objects.all()),
            )
        self.success(f"inserted {count} Teams")

        count = 16
        for x in range(count):
            models.Contributor.objects.create(
                username = fake.name(),
                email = fake.email(),
                bio = fake.paragraph(),
            )
        self.success(f"inserted {count} Contributors")

        count = 10
        for x in range(count):
            models.TeamMembership.objects.create(
                contributor = choice(models.Contributor.objects.all()),
                team = choice(models.Team.objects.all()),
            )
        self.success(f"inserted {count} TeamMemberships")

        count = 8
        for x in range(count):
            models.Issue.objects.create(
                author = choice(models.Contributor.objects.all()),
                organization = choice(models.Organization.objects.all()),
                title = fake.paragraph(nb_sentences=1),
                description = fake.paragraph(),
                status = choice(["Not Started", "In Progress", "Completed"]),
                severity = choice(["Low", "Medium", "High"]),
            )
        self.success(f"inserted {count} Issues")

        count = 16
        for x in range(count):
            models.Comment.objects.create(
                author = choice(models.Contributor.objects.all()),
                issue = choice(models.Issue.objects.all()),
                body = fake.paragraph(),
            )
        self.success(f"inserted {count} Comments")
        