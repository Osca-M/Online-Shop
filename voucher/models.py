import uuid
from django.db import models
from oscar.apps.voucher.abstract_models import AbstractVoucherSet, AbstractVoucher, \
    AbstractVoucherApplication  # noqa isort:skip


class VoucherSet(AbstractVoucherSet):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class Voucher(AbstractVoucher):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class VoucherApplication(AbstractVoucherApplication):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


from oscar.apps.voucher.models import *  # noqa isort:skip
