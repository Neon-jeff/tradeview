# Generated by Django 4.2.6 on 2024-03-05 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_profile_country_profile_phone_profile_phone_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]