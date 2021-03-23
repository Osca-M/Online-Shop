from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProductClass, AbstractCategory, AbstractProductCategory, \
    AbstractProduct, AbstractProductRecommendation, AbstractProductAttribute, AbstractProductAttributeValue, \
    AbstractAttributeOptionGroup, AbstractAttributeOption, AbstractOption  # noqa isort:skip


class ProductClass(AbstractProductClass):
    pass


class Category(AbstractCategory):
    pass


class ProductCategory(AbstractProductCategory):
    pass


class Product(AbstractProduct):
    video_url = models.URLField(null=True)


class ProductRecommendation(AbstractProductRecommendation):
    pass


class ProductAttribute(AbstractProductAttribute):
    pass


class ProductAttributeValue(AbstractProductAttributeValue):
    pass


class AttributeOptionGroup(AbstractAttributeOptionGroup):
    pass


class AttributeOption(AbstractAttributeOption):
    pass


class Option(AbstractOption):
    pass


from oscar.apps.catalogue.models import *  # noqa isort:skip
