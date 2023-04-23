import re
from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_first_name(value: str) -> None:
    # Matches any string that contains at least one either digit, non-wowrd
    # characters or uderscore
    pattern = r"(?:.*[\d\W_].*)"
    if re.fullmatch(pattern, value):
        message = _("first_name must contain only letters")
        raise ValidationError(message, code="invalid")


def validate_last_name(value: str) -> None:
    # Matches any string that contains at least one either digit, non-wowrd
    # characters or uderscore
    pattern = r"(?:.*[\d\W_].*)"
    if re.fullmatch(pattern, value):
        message = _("first_name must contain only letters")
        raise ValidationError(message, code="invalid")


def validate_phone(value: str) -> None:
    # Matches any string that contains only digits and + character
    if value is None:
        return
    pattern = r"^\+?\d+$"
    if not re.fullmatch(pattern, value):
        message = _(
            "phone must contain only numbers and + characters at the begining"
        )
        raise ValidationError(message, code="invalid")


def validate_nid(value: str) -> None:
    if value is None:
        return
    # Matches any string that contains only letters, digits and - character
    pattern = r"^[a-zA-Z0-9-]+$"
    if not re.fullmatch(pattern, value):
        message = _("nid must contain only numbers, letters and - character")
        raise ValidationError(message, code="invalid")


def validate_birth(value: datetime) -> None:
    if value is None:
        return
    if value > datetime.now():
        message = _("birth date must be lesser than {date}").format(
            date=datetime.now()
        )
        raise ValidationError(message, code="invalid")
