from enum import Enum, IntEnum


class AnswerType(str, Enum):
    PHOTO = "photo"
    TEXT = "text"


class SubscriptionType(str, Enum):
    MONTH = "MONTH"
    YEAR = "YEAR"
