import uuid
from django.db import models
from oscar.apps.catalogue.reviews.abstract_models import AbstractProductReview, AbstractVote  # noqa isort:skip


class ProductReview(AbstractProductReview):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class Vote(AbstractVote):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


from oscar.apps.catalogue.reviews.models import *
