from django.db import models
from django.core.exceptions import ValidationError


def validate_max_length(field):
    if len(field) > 200:
        error_message = (
            "Certifique-se de que o valor tenha no máximo "
            f"200 caracteres (ele possui {len(field)})."
        )

        raise ValidationError(error_message)


class Category(models.Model):
    name = models.CharField(
       max_length=200,
       blank=False,
       validators=[validate_max_length]
    )

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(
       max_length=200,
       blank=False,
       validators=[validate_max_length]
    )

    email = models.EmailField(
       max_length=200,
       blank=False,
       validators=[validate_max_length]
    )

    password = models.CharField(
       max_length=200,
       blank=False,
       validators=[validate_max_length]
    )

    role = models.CharField(
       max_length=200,
       blank=False,
       validators=[validate_max_length]
    )

    def __str__(self):
        return self.name
