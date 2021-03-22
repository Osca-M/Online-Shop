import uuid
from django.db import models
from oscar.apps.customer.abstract_models import AbstractProductAlert  # noqa isort:skip


class ProductAlert(AbstractProductAlert):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


from oscar.apps.customer.models import *  # noqa isort:skip
