# Generated by Django 5.0 on 2024-01-31 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_products_height_alter_products_length_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='start',
            new_name='star',
        ),
    ]