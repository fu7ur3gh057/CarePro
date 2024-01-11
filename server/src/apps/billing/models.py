from django.db import models

from src.apps.base.models import PKIDMixin, TimeStampedMixin
from src.apps.students.models import Student


class Subscription(PKIDMixin, TimeStampedMixin):
    student = models.ForeignKey(
        to="students.Student",
        related_name="subscriptions",
        on_delete=models.CASCADE,
        verbose_name=_("Студент"),
    )
    subject = models.ForeignKey(
        to="subjects.Subject",
        related_name="subscriptions",
        on_delete=models.CASCADE,
        verbose_name=_("Предмет"),
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Сумма")
    )
    transaction = models.CharField(
        max_length=512, verbose_name=_("Транзакция"), unique=True
    )
    month_count = models.IntegerField(default=3, verbose_name=_("Количество месяцев"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активна"))
    expire_date = models.DateTimeField(
        null=True, blank=True, verbose_name=_("Дата окончания")
    )
