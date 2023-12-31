# Generated by Django 4.2.2 on 2023-06-27 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0004_personal_detail"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("age", models.IntegerField()),
                ("gender", models.CharField(max_length=10)),
                ("writing_content", models.TextField()),
                ("feedback", models.TextField()),
                ("errors", models.TextField()),
                ("score", models.DecimalField(decimal_places=1, max_digits=3)),
                ("recording", models.FileField(upload_to="recordings/")),
            ],
        ),
    ]
