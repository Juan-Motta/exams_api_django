# Generated by Django 4.2 on 2023-04-26 22:02

import apps.users.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.DateField(
                blank=True,
                null=True,
                validators=[apps.users.validators.validate_birth],
            ),
        ),
        migrations.AlterField(
            model_name='user',
            name='nid',
            field=models.CharField(
                blank=True,
                max_length=16,
                null=True,
                validators=[apps.users.validators.validate_nid],
            ),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(
                blank=True,
                max_length=16,
                null=True,
                validators=[apps.users.validators.validate_phone],
            ),
        ),
    ]
