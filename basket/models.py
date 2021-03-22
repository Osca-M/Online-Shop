import uuid
from django.db import models
from oscar.apps.basket.abstract_models import AbstractBasket, AbstractLine, AbstractLineAttribute  # noqa isort:skip


class Basket(AbstractBasket):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class Line(AbstractLine):
    pass


class LineAttribute(AbstractLineAttribute):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


from oscar.apps.basket.models import *
