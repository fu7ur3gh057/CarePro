from src.apps.base.models import TimeStampedMixin, TelegramMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.base.regex import phone_regex
from src.apps.subjects.models import Subject


class Student(TelegramMixin, TimeStampedMixin):
    name = models.CharField(max_length=100, verbose_name=_("Имя"))
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        unique=True,
        verbose_name=_("Номер телефона"),
    )
    city = models.ForeignKey(
        to="locations.City",
        related_name="students",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Город"),
    )
    school = models.ForeignKey(
        to="locations.School",
        related_name="students",
        on_delete=models.SET_NULL,
        max_length=50,
        null=True,
        blank=True,
        verbose_name=_("Школа"),
    )
    grade = models.ForeignKey(
        to="subjects.Grade",
        related_name="students",
        verbose_name=_("Класс"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Студент")
        verbose_name_plural = _("Студенты")

    def get_subjects(self) -> list[Subject]:
        subscriptions = self.subscriptions.all().filter(is_active=True)
        if subscriptions is None:
            return []
        else:
            return [sub.subject for sub in subscriptions]

    def is_subscribed_to_subject(self, subject: Subject) -> bool:
        subjects = self.get_subjects()
        if subject in subjects:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"{self.name}"
