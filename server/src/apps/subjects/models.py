from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.base.models import PKIDMixin, TimeStampedMixin


class Grade(PKIDMixin):
    number = models.PositiveIntegerField(unique=True)

    class Meta:
        verbose_name = _("Класс")
        verbose_name_plural = _("Классы")

    def __str__(self) -> str:
        return f"№{self.number}"


class Subject(PKIDMixin, TimeStampedMixin):
    title = models.CharField(max_length=100, verbose_name=_("Название"))
    grade = models.ForeignKey(
        to="subjects.Grade",
        related_name="subjects",
        verbose_name=_("Класс"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Предмет")
        verbose_name_plural = _("Предметы")

    def __str__(self) -> str:
        return f"{self.title} {self.grade.number}"
