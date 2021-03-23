from oscar.apps.catalogue.reviews.abstract_models import AbstractProductReview, AbstractVote  # noqa isort:skip


class ProductReview(AbstractProductReview):
    pass


class Vote(AbstractVote):
    pass


from oscar.apps.catalogue.reviews.models import * # noqa isort:skip
