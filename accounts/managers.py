from django.contrib.auth.base_user import BaseUserManager
from django.db.models import Q
from django.utils.translation import ugettext as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and
        password.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
            email,
            password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def get_from_username_or_email_or_phone(self, identifier):
        users = self.filter(Q(username__iexact=identifier) | Q(
            email__iexact=identifier) | Q(phone=identifier))
        users_count = len(users)

        if users_count == 1:
            return users[0]

        if users_count == 0:
            error = _(
                "User with username or email or phone {} does not exist"
            ).format(identifier)
            raise self.model.DoesNotExist(error)
        else:
            error = _(
                "More than one user found for username or email or phone {}"
            ).format(identifier)
            raise self.model.MultipleObjectsReturned(error)
