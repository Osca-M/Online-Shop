import math
import random
import uuid

from django.db import models
from django.contrib.auth import get_user_model

# from products.models import Product

User = get_user_model()


# Create your models here.

def generate_reference_number():
    digits_in_otp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    reference_number = ""
    length = len(digits_in_otp)
    # for a 8 digit OTP we are using 8 in range
    for i in range(8):
        reference_number += digits_in_otp[math.floor(random.random() * length)]
    exists = Order.objects.filter(reference_number=reference_number)
    if exists:
        generate_reference_number()
    return reference_number


class Order(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    reference_number = models.CharField(max_length=15, default=generate_reference_number, editable=False)
    # cart = models.ForeignKey(Cart, blank=True, null=True)
    # items = models.ManyToManyField(Product)
    user = models.ForeignKey(User, related_name="user_orders", on_delete=models.CASCADE)
    destination = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.reference_number)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


def generate_reference_number_order_item():
    digits_in_otp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    reference_number = ""
    length = len(digits_in_otp)
    # for a 8 digit OTP we are using 8 in range
    for i in range(8):
        reference_number += digits_in_otp[math.floor(random.random() * length)]
    exists = OrderItem.objects.filter(reference_number=reference_number)
    if exists:
        generate_reference_number()
    return reference_number


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    reference_number = models.CharField(max_length=15, default=generate_reference_number_order_item, editable=False)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.reference_number)

    def get_cost(self):
        return self.price * self.quantity
