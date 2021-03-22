import uuid
from django.db import models
from oscar.apps.offer.abstract_models import AbstractConditionalOffer, AbstractBenefit, AbstractCondition, \
    AbstractRange, AbstractRangeProduct, AbstractRangeProductFileUpload  # noqa isort:skip


class ConditionalOffer(AbstractConditionalOffer):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class Benefit(AbstractBenefit):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class Condition(AbstractCondition):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class Range(AbstractRange):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class RangeProduct(AbstractRangeProduct):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class RangeProductFileUpload(AbstractRangeProductFileUpload):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


from oscar.apps.offer.models import *
