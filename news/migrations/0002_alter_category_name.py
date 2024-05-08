# Generated by Django 4.2.3 on 2024-05-08 00:39

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                max_length=200,
                validators=[news.models.validate_max_name_length],
            ),
        ),
    ]
