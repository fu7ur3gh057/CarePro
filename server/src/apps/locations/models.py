from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.base.models import PKIDMixin


class City(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name=_("VK ID"), unique=True)
    title = models.CharField(max_length=100, verbose_name=_("Имя"))
    area = models.CharField(
        max_length=100, null=True, blank=True, db_index=True, verbose_name=_("Район")
    )
    region = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Регион")
    )

    class Meta:
        verbose_name = _("Город")
        verbose_name_plural = _("Города")

    def __str__(self) -> str:
        return f"{self.title}, {self.region}"


class School(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name=_("VK ID"), unique=True)
    city = models.ForeignKey(
        to="locations.City",
        related_name="schools",
        on_delete=models.CASCADE,
        verbose_name=_("Город"),
    )
    title = models.CharField(max_length=100, verbose_name=_("Название"))

    class Meta:
        verbose_name = _("Школа")
        verbose_name_plural = _("Школы")

    def __str__(self) -> str:
        return f"{self.title}"
