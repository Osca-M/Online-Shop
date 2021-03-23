from oscar.apps.basket.abstract_models import AbstractBasket, AbstractLine, AbstractLineAttribute  # noqa isort:skip


class Basket(AbstractBasket):
    pass


class Line(AbstractLine):
    pass


class LineAttribute(AbstractLineAttribute):
    pass


from oscar.apps.basket.models import * # noqa isort:skip
