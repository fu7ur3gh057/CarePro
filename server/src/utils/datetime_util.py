from django.utils import timezone


def is_datetime_in_range(start_time, end_time):
    current_datetime = timezone.localtime(timezone.now())
    start_time = timezone.localtime(start_time)
    end_time = timezone.localtime(end_time)
    return start_time <= current_datetime <= end_time


def is_datetime_bigger(start_time):
    current_datetime = timezone.localtime(timezone.now())
    start_time = timezone.localtime(start_time)
    return start_time > current_datetime


def is_date_expired(end_time: timezone) -> bool:
    current_datetime = timezone.localtime(timezone.now())
    end_time = timezone.localtime(end_time)
    return end_time <= current_datetime
