from django.test import TestCase
from .models import User, UserProfile
from mixer.backend.django import mixer
import pytest

pytest_mark = pytest.mark.django_db


# Create your tests here.
class TestUserModel(TestCase):
    def setUp(self):
        self.user = mixer.blend(User, email="monique@wright.com")
        print(self.user.__dict__)

    def test_user_created(self):
        assert self.user.email == "monique@wright.com"

    def test_self_dot_email(self):
        assert str(self.user) == "monique@wright.com"
