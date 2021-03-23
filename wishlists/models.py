from oscar.apps.wishlists.abstract_models import AbstractWishList, AbstractLine  # noqa isort:skip


class WishList(AbstractWishList):
    pass


class Line(AbstractLine):
    pass


from oscar.apps.wishlists.models import *  # noqa isort:skip
