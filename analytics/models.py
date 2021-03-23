from oscar.apps.analytics.abstract_models import AbstractProductRecord, AbstractUserRecord, AbstractUserProductView, \
    AbstractUserSearch  # noqa isort:skip


class ProductRecord(AbstractProductRecord):
    pass


class UserRecord(AbstractUserRecord):
    pass


class UserProductView(AbstractUserProductView):
    pass


class UserSearch(AbstractUserSearch):
    pass


from oscar.apps.analytics.models import * # noqa isort:skip
