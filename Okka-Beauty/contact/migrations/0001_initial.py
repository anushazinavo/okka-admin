# Generated by Django 5.0.6 on 2024-06-20 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=255)),
                ('stores_name', models.CharField(max_length=255)),
                ('whatsapp_numbers', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('partnership_name', models.CharField(max_length=255)),
                ('email_another', models.CharField(max_length=500)),
                ('address_local', models.CharField(max_length=255)),
                ('address_country', models.CharField(default='Your Default Country', max_length=255)),
                ('see_more', models.CharField(default='see you more', max_length=255)),
            ],
        ),
    ]
