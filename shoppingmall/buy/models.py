import uuid as uuid
from django.db import models

# Create your models here.
from pick.models import PickItem


class Buy(models.Model):
    product_buy = models.ForeignKey(PickItem, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    expected_delivery_time= models.DateField(auto_now=True)
    delivery_state = models.CharField(max_length=128, default=True)


    created_at = models.DateTimeField('date published', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.CharField(max_length=128, default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)


    class Meta:
        db_table = 'buys'