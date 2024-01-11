from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from src.apps.base.models import TimeStampedMixin, TelegramMixin, PKIDMixin
from src.apps.base.regex import phone_regex


class Teacher(TelegramMixin, TimeStampedMixin):
    full_name = models.CharField(max_length=255, verbose_name=_("ФИО"))
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        unique=True,
        verbose_name=_("Номер телефона"),
    )
    api_token = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, verbose_name=_("API Токен")
    )
    subjects = models.ManyToManyField(
        to="subjects.Subject", related_name="teachers", verbose_name=_("Предметы")
    )

    class Meta:
        verbose_name = _("Учитель")
        verbose_name_plural = _("Учителя")

    def __str__(self) -> str:
        return f"{self.full_name}"
