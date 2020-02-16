from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import UserManager
import uuid
from django.core.validators import RegexValidator


# Create your models here.


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name='email address', blank=False, max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        ordering = ('email',)
        verbose_name = ('user',)
        verbose_name_plural = ('users',)
        app_label = 'accounts'

        """
        to set table name in database
        """
        db_table = "user"


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    phone_regex = RegexValidator(
        regex=r'^\+?|d{9,14}$',
        message="Phone number must be entered in the format: '+99999'. Up to 14 digits allowed."
    )
    phone_number = models.CharField(max_length=15, validators=[phone_regex], unique=True, null=False, blank=True)
    username = models.CharField(blank=True, max_length=255, unique=False)
    age = models.PositiveIntegerField(null=False, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unspecified')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        """
        to set table name in database
        """
        db_table = "profile"
