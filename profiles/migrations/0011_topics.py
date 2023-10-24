# Generated by Django 4.2.2 on 2023-07-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0010_alter_create_room_room_ide"),
    ]

    operations = [
        migrations.CreateModel(
            name="topics",
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
                ("part1", models.CharField(max_length=500)),
                ("part2", models.CharField(max_length=600)),
                ("part3", models.CharField(max_length=500)),
            ],
        ),
    ]
