# Generated by Django 5.0 on 2024-02-22 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_products_color_products_country_products_payondel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='uid',
        ),
    ]