from django.test import TestCase
from .models import CustomUser

class CustomUserTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="testuser", password="password")

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
