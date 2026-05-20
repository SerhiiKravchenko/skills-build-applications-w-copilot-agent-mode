from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Define models if not already defined elsewhere
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='test', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='test', first_name='Peter', last_name='Parker'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='test', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='test', first_name='Clark', last_name='Kent'),
        ]

        # Create activities
        Activity.objects.create(user='ironman', type='run', duration=30)
        Activity.objects.create(user='spiderman', type='cycle', duration=45)
        Activity.objects.create(user='batman', type='swim', duration=60)
        Activity.objects.create(user='superman', type='run', duration=50)

        # Create leaderboard
        Leaderboard.objects.create(user='ironman', points=100)
        Leaderboard.objects.create(user='spiderman', points=80)
        Leaderboard.objects.create(user='batman', points=90)
        Leaderboard.objects.create(user='superman', points=110)

        # Create workouts
        Workout.objects.create(name='Super Strength', description='Lift heavy weights')
        Workout.objects.create(name='Web Sling', description='Agility and flexibility')
        Workout.objects.create(name='Bat Training', description='Martial arts and gadgets')
        Workout.objects.create(name='Kryptonian Cardio', description='High intensity running')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
