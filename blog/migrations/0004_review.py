# Generated by Django 4.2.1 on 2023-06-10 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_remove_teacher_student_name_alter_teacher_first_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="review",
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
                ("user_mail", models.CharField(max_length=100)),
                ("password", models.IntegerField()),
            ],
        ),
    ]