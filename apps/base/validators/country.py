import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_name(value: str) -> None:
    # Matches any string that contains at least one either digit, non-wowrd
    # characters or uderscore
    pattern = r"(?:.*[\d\W_].*)"
    if re.fullmatch(pattern, value):
        message = _("name must contain only letters")
        raise ValidationError(message, code="invalid")
