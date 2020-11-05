import uuid as uuid
from django.db import models

# 제출시에 수정
# from product.models import Product
from product.models import Product

from user.models import User


class Pick(models.Model):
    pick_id = models.CharField(max_length=128, blank=True)
    # user_pick = models.ForeignKey(User, on_delete=models.CASCADE, default=True)

    user_type = models.CharField(max_length=8, default=False)
    created_at = models.DateTimeField('date published', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.CharField(max_length=128, default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        db_table = 'Pick'
        ordering = ['created_at']

    def __str__(self):
        return self.pick_id

class PickItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pick = models.ForeignKey(Pick, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    class Meta:
        db_table = 'PickItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product

