from oscar.apps.payment.abstract_models import AbstractTransaction, AbstractSource, AbstractSourceType, \
    AbstractBankcard  # noqa isort:skip


class Transaction(AbstractTransaction):
    pass


class Source(AbstractSource):
    pass


class SourceType(AbstractSourceType):
    pass


class Bankcard(AbstractBankcard):
    pass


from oscar.apps.payment.models import * # noqa isort:skip
