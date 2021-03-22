import uuid

from django.db import models
from oscar.apps.communication.abstract_models import AbstractEmail, AbstractCommunicationEventType, \
    AbstractNotification  # noqa isort:skip


class Email(AbstractEmail):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class CommunicationEventType(AbstractCommunicationEventType):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class Notification(AbstractNotification):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


from oscar.apps.communication.models import *
