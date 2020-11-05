import uuid as uuid
from django.db import models

# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    username = models.CharField(max_length=128, verbose_name="이름" )
    email = models.EmailField(verbose_name="이메일", blank=True)
    password = models.CharField(max_length=128, verbose_name="비밀번호")
    # user_type = models.CharField(max_length=8, verbose_name="등급",
    #     choices={
    #         ('admin', 'admin'),
    #         ('user', 'user')
    #     })
    user_type = models.CharField(max_length=8, default=False)

    created_at = models.DateTimeField('date published', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.CharField(max_length=128, default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)




    class Meta:
        db_table = 'users'
        verbose_name = "사용자"
        verbose_name_plural = "사용자"

    def __str__(self):
        return self.id
