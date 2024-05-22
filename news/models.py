from django import forms
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


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


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


def validate_title_word_count(field):
    if len(field.split()) < 2:
        error_message = (
            'O título deve conter pelo menos 2 palavras.'
        )

        raise ValidationError(error_message)


def validate_field_word_count(field):
    if len(field) < 1:
        error_message = ({
            field: [
                'Este campo não pode estar vazio.'
            ]
        })

        raise ValidationError(error_message)


class News(models.Model):
    title = models.CharField(
        max_length=200,
        blank=False,
        validators=[
            validate_max_length,
            validate_title_word_count,
            validate_field_word_count,
        ]
    )

    content = models.TextField(
        blank=False,
        validators=[validate_field_word_count]
    )

    author = models.ForeignKey(
      User,
      on_delete=models.CASCADE,
    )

    created_at = models.DateField(
        blank=False,
    )

    image = models.ImageField(
        blank=True,
        upload_to='img/'
    )

    categories = models.ManyToManyField(
        Category,
        blank=False,
    )

    def __str__(self):
        return self.title
