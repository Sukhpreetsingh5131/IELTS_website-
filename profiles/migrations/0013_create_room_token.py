# Generated by Django 4.2.3 on 2023-07-24 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0012_question"),
    ]

    operations = [
        migrations.AddField(
            model_name="create_room",
            name="token",
            field=models.CharField(default=0, max_length=100),
        ),
    ]
