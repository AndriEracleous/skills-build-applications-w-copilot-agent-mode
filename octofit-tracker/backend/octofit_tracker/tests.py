from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.assertEqual(str(team), 'Marvel')

    def test_create_user(self):
        team = Team.objects.create(name='DC', description='DC superheroes')
        user = User.objects.create(name='Superman', email='superman@dc.com', team=team, is_superhero=True)
        self.assertEqual(str(user), 'Superman')

    def test_create_activity(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2024-01-01')
        self.assertEqual(str(activity), 'Iron Man - Running (2024-01-01)')

    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body workout')
        self.assertEqual(str(workout), 'Pushups')

    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        user = User.objects.create(name='Hulk', email='hulk@marvel.com', team=team, is_superhero=True)
        leaderboard = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertEqual(str(leaderboard), 'Hulk - Rank 1')
