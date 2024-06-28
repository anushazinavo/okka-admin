# Generated by Django 5.0.6 on 2024-06-21 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banner", "0001_initial"),
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PriceBanner",
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
                ("image", models.ImageField(upload_to="price_banners/")),
                ("alt_text", models.CharField(blank=True, max_length=255, null=True)),
                ("slot_position", models.IntegerField(blank=True, null=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "Category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.parentcategory",
                    ),
                ),
            ],
        ),
    ]
