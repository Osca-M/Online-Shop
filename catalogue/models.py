import uuid
from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProductClass, AbstractCategory, AbstractProductCategory, \
    AbstractProduct, AbstractProductRecommendation, AbstractProductAttribute, AbstractProductAttributeValue, \
    AbstractAttributeOptionGroup, AbstractAttributeOption, AbstractOption  # noqa isort:skip


class ProductClass(AbstractProductClass):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class Category(AbstractCategory):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class ProductCategory(AbstractProductCategory):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class Product(AbstractProduct):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    video_url = models.URLField(null=True)


class ProductRecommendation(AbstractProductRecommendation):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class ProductAttribute(AbstractProductAttribute):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class ProductAttributeValue(AbstractProductAttributeValue):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class AttributeOptionGroup(AbstractAttributeOptionGroup):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class AttributeOption(AbstractAttributeOption):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


class Option(AbstractOption):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)


from oscar.apps.catalogue.models import *  # noqa isort:skip
