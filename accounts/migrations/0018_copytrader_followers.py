# Generated by Django 4.2.6 on 2024-03-30 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_remove_profile_ada_balance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='copytrader',
            name='followers',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
