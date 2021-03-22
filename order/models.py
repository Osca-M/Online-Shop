import uuid
from django.db import models
from oscar.apps.order.abstract_models import AbstractOrder, AbstractOrderNote, AbstractOrderStatusChange, \
    AbstractCommunicationEvent, AbstractLine, AbstractLineAttribute, AbstractLinePrice, AbstractPaymentEventType, \
    AbstractPaymentEvent, AbstractShippingEvent, AbstractShippingEventType, AbstractOrderDiscount, AbstractSurcharge  # noqa isort:skip


class Order(AbstractOrder):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class OrderNote(AbstractOrderNote):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class OrderStatusChange(AbstractOrderStatusChange):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class CommunicationEvent(AbstractCommunicationEvent):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class Line(AbstractLine):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class LineAttribute(AbstractLineAttribute):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class LinePrice(AbstractLinePrice):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class PaymentEventType(AbstractPaymentEventType):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class PaymentEvent(AbstractPaymentEvent):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class ShippingEvent(AbstractShippingEvent):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class ShippingEventType(AbstractShippingEventType):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class OrderDiscount(AbstractOrderDiscount):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class Surcharge(AbstractSurcharge):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


from oscar.apps.order.models import *
