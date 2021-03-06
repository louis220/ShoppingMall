# Generated by Django 2.2.16 on 2020-10-26 16:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=128, verbose_name='이름')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='이메일')),
                ('password', models.CharField(max_length=128, verbose_name='비밀번호')),
                ('user_type', models.CharField(default=False, max_length=8)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.CharField(default=False, max_length=128)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'users',
            },
        ),
    ]
