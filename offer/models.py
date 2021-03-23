from oscar.apps.offer.abstract_models import AbstractConditionalOffer, AbstractBenefit, AbstractCondition, \
    AbstractRange, AbstractRangeProduct, AbstractRangeProductFileUpload  # noqa isort:skip


class ConditionalOffer(AbstractConditionalOffer):
    pass


class Benefit(AbstractBenefit):
    pass


class Condition(AbstractCondition):
    pass


class Range(AbstractRange):
    pass


class RangeProduct(AbstractRangeProduct):
    pass


class RangeProductFileUpload(AbstractRangeProductFileUpload):
    pass


from oscar.apps.offer.models import * # noqa isort:skip
