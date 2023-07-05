from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator


def validate_username(username):
    if len(username) >= 20 :
        raise ValidationError(
            _("%(value)s is bigger than 20 number"),
            params={"value": value},
        )
    if len(username) < 4 :
        raise ValidationError(
            _("%(value)s is lower than 4 number"),
            params={"value": value},
        )
