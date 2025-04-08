from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class UserTests(APITestCase):
    def test_create_user(self):
        data = {"email": "test@example.com", "name": "Test User", "age": 25}
        response = self.client.post("/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamTests(APITestCase):
    def test_create_team(self):
        data = {"name": "Team A", "members": []}
        response = self.client.post("/teams/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        data = {"type": "Running", "duration": 30, "date": "2025-04-08"}
        response = self.client.post("/activity/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTests(APITestCase):
    def test_create_leaderboard(self):
        data = {"score": 100}
        response = self.client.post("/leaderboard/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        data = {"name": "Workout A", "description": "Test workout", "duration": 45}
        response = self.client.post("/workouts/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
