
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Drop collections directly using PyMongo for a clean slate
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]
        for collection in ['user', 'team', 'activity', 'workout', 'leaderboard']:
            db[collection].drop()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Create Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)

        # Create Activities
        Activity.objects.create(user=tony, activity_type='run', duration=30, date=date(2024, 1, 1))
        Activity.objects.create(user=steve, activity_type='cycle', duration=45, date=date(2024, 1, 2))
        Activity.objects.create(user=bruce, activity_type='swim', duration=60, date=date(2024, 1, 3))
        Activity.objects.create(user=clark, activity_type='fly', duration=120, date=date(2024, 1, 4))

        # Create Workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for heroes', suggested_for='marvel')
        Workout.objects.create(name='Flight Training', description='Flight workout for Kryptonians', suggested_for='dc')

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=100, rank=1)
        Leaderboard.objects.create(user=steve, score=90, rank=2)
        Leaderboard.objects.create(user=bruce, score=80, rank=3)
        Leaderboard.objects.create(user=clark, score=70, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
