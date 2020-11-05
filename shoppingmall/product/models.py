from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.



class Product(models.Model):
    title = models.CharField(max_length=64, verbose_name ="상품명")
    price = models.IntegerField(verbose_name="가격")
    discount = models.IntegerField(verbose_name="할인")

    description = models.TextField(verbose_name="설명")


    created_at = models.DateTimeField('date published', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.CharField(max_length=128, default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "products"
        verbose_name="상품"

# 다수의 이미지 업로드
class Photo(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, null= True)
    image = models.ImageField(upload_to='images', blank=True)