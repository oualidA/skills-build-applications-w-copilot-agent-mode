from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(id=ObjectId(), email='student1@example.com', name='Student One', created_at=datetime.now()),
            User(id=ObjectId(), email='student2@example.com', name='Student Two', created_at=datetime.now()),
            User(id=ObjectId(), email='student3@example.com', name='Student Three', created_at=datetime.now()),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(id=ObjectId(), name='Team Alpha', created_at=datetime.now())
        team2 = Team(id=ObjectId(), name='Team Beta', created_at=datetime.now())
        team1.save()
        team2.save()

        # Utilise la méthode set() pour définir les membres des équipes
        team1.members.set([users[0], users[1]])
        team2.members.set([users[2]])
        team1.save()
        team2.save()

        # Create activities
        activities = [
            Activity(id=ObjectId(), user=users[0], type='Running', duration=30, date=datetime.now().date()),
            Activity(id=ObjectId(), user=users[1], type='Cycling', duration=45, date=datetime.now().date()),
            Activity(id=ObjectId(), user=users[2], type='Swimming', duration=60, date=datetime.now().date()),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(id=ObjectId(), team=team1, score=100, updated_at=datetime.now()),
            Leaderboard(id=ObjectId(), team=team2, score=80, updated_at=datetime.now()),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(id=ObjectId(), name='Morning Run', description='A 5km run to start the day', duration=30),
            Workout(id=ObjectId(), name='Cycling Session', description='A 20km cycling session', duration=45),
            Workout(id=ObjectId(), name='Swimming Laps', description='30 laps in the pool', duration=60),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))