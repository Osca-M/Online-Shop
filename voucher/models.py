from oscar.apps.voucher.abstract_models import AbstractVoucherSet, AbstractVoucher, \
    AbstractVoucherApplication  # noqa isort:skip


class VoucherSet(AbstractVoucherSet):
    pass


class Voucher(AbstractVoucher):
    pass


class VoucherApplication(AbstractVoucherApplication):
    pass


from oscar.apps.voucher.models import *  # noqa isort:skip
