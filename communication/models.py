from oscar.apps.communication.abstract_models import AbstractEmail, AbstractCommunicationEventType, \
    AbstractNotification  # noqa isort:skip


class Email(AbstractEmail):
    pass


class CommunicationEventType(AbstractCommunicationEventType):
    pass


class Notification(AbstractNotification):
    pass


from oscar.apps.communication.models import * # noqa isort:skip
