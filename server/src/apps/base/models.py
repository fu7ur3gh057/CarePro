from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class PKIDMixin(models.Model):
    pk_id = models.BigAutoField(
        primary_key=True, editable=False, verbose_name=_("PK ID")
    )

    class Meta:
        abstract = True


class TelegramMixin(models.Model):
    tg_id = models.BigIntegerField(
        primary_key=True, unique=True, verbose_name=_("Телеграм ID")
    )


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Время создания")
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Последнее обновление")
    )

    class Meta:
        abstract = True
