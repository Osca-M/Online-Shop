import uuid
from django.db import models
from oscar.apps.wishlists.abstract_models import AbstractWishList, AbstractLine  # noqa isort:skip


class WishList(AbstractWishList):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class Line(AbstractLine):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


from oscar.apps.wishlists.models import *  # noqa isort:skip
