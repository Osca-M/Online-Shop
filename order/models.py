from oscar.apps.order.abstract_models import AbstractOrder, AbstractOrderNote, AbstractOrderStatusChange, \
    AbstractCommunicationEvent, AbstractLine, AbstractLineAttribute, AbstractLinePrice, AbstractPaymentEventType, \
    AbstractPaymentEvent, AbstractShippingEvent, AbstractShippingEventType, AbstractOrderDiscount, AbstractSurcharge  # noqa isort:skip


class Order(AbstractOrder):
    pass


class OrderNote(AbstractOrderNote):
    pass


class OrderStatusChange(AbstractOrderStatusChange):
    pass


class CommunicationEvent(AbstractCommunicationEvent):
    pass


class Line(AbstractLine):
    pass


class LineAttribute(AbstractLineAttribute):
    pass


class LinePrice(AbstractLinePrice):
    pass


class PaymentEventType(AbstractPaymentEventType):
    pass


class PaymentEvent(AbstractPaymentEvent):
    pass


class ShippingEvent(AbstractShippingEvent):
    pass


class ShippingEventType(AbstractShippingEventType):
    pass


class OrderDiscount(AbstractOrderDiscount):
    pass


class Surcharge(AbstractSurcharge):
    pass


from oscar.apps.order.models import * # noqa isort:skip
