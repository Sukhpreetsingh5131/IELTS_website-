# Generated by Django 4.2.1 on 2023-06-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0002_writing"),
    ]

    operations = [
        migrations.CreateModel(
            name="param",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment", models.TextField()),
            ],
        ),
    ]
