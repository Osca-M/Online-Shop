from oscar.apps.partner.abstract_models import AbstractPartner, AbstractStockRecord, \
    AbstractStockAlert  # noqa isort:skip


class Partner(AbstractPartner):
    pass


class StockRecord(AbstractStockRecord):
    pass


class StockAlert(AbstractStockAlert):
    pass


from oscar.apps.partner.models import *  # noqa isort:skip
