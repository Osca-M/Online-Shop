import uuid
from django.db import models
from oscar.apps.partner.abstract_models import AbstractPartner, AbstractStockRecord, \
    AbstractStockAlert  # noqa isort:skip


class Partner(AbstractPartner):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class StockRecord(AbstractStockRecord):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class StockAlert(AbstractStockAlert):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


from oscar.apps.partner.models import *
