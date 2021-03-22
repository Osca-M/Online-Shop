import uuid
from django.db import models
from oscar.apps.analytics.abstract_models import AbstractProductRecord, AbstractUserRecord, AbstractUserProductView, \
    AbstractUserSearch  # noqa isort:skip


class ProductRecord(AbstractProductRecord):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class UserRecord(AbstractUserRecord):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class UserProductView(AbstractUserProductView):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class UserSearch(AbstractUserSearch):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


from oscar.apps.analytics.models import *
