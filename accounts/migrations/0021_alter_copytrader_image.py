# Generated by Django 4.2.6 on 2024-08-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_profile_otp_profile_preferred_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copytrader',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='copy-traders'),
        ),
    ]
