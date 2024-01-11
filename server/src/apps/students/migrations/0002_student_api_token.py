# Generated by Django 4.2.4 on 2024-01-11 14:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="api_token",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                unique=True,
                verbose_name="API Токен",
            ),
        ),
    ]
