import uuid
from django.db import models

from oscar.apps.payment.abstract_models import AbstractTransaction, AbstractSource, AbstractSourceType, \
    AbstractBankcard  # noqa isort:skip


class Transaction(AbstractTransaction):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class Source(AbstractSource):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class SourceType(AbstractSourceType):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class Bankcard(AbstractBankcard):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


from oscar.apps.payment.models import *
