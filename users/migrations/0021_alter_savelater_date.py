# Generated by Django 5.0 on 2024-02-13 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_savelater'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savelater',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
