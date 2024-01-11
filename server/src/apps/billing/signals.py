from dateutil.relativedelta import relativedelta
from django.db.models.signals import post_save
from django.dispatch import receiver

from src.apps.billing.models import Subscription


@receiver(post_save, sender=Subscription)
def make_expired_date_signal(sender, instance: Subscription, created: bool, **kwargs):
    if created:
        instance.expire_date = instance.created_at + relativedelta(months=instance.month_count)
        instance.save()
