# Generated by Django 5.0.6 on 2024-06-22 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banner", "0004_whyus_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="whyus",
            name="slot_position",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
