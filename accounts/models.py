from django.contrib.auth.models import AbstractBaseUser
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone

from .managers import UserManager
import uuid
from django.core.validators import RegexValidator

from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name='email address', blank=False, max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(
        _('Active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.

    objects = UserManager()

    def __str__(self):
        return self.email

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
        return True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return self.profile.full_name.strip()

    def get_short_name(self):
        """
        Return the short name for the user.
        """
        return self.profile.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Send an email to this user.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def _migrate_alerts_to_user(self):
        """
        Transfer any active alerts linked to a user's email address to the
        newly registered user.
        """
        ProductAlert = self.alerts.model
        alerts = ProductAlert.objects.filter(
            email=self.email, status=ProductAlert.ACTIVE)
        alerts.update(user=self, key='', email='')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Migrate any "anonymous" product alerts to the registered user
        # Ideally, this would be done via a post-save signal. But we can't
        # use get_user_model to wire up signals to custom user models
        # see Oscar ticket #1127, Django ticket #19218
        self._migrate_alerts_to_user()

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
    full_name = models.CharField(max_length=255, unique=False)
    # last_name = models.CharField(max_length=50, unique=False)
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
