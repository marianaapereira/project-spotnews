from django.db import models
from django.core.exceptions import ValidationError


def validate_max_name_length(name):
    if len(name) > 200:
        error_message = (
            "Certifique-se de que o valor tenha no máximo "
            f"200 caracteres (ele possui {len(name)})."
        )

        raise ValidationError(error_message)


class Category(models.Model):
    name = models.CharField(
       max_length=200,
       blank=False,
       validators=[validate_max_name_length]
    )

    def __str__(self):
        return self.name
