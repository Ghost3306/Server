# Generated by Django 5.0 on 2024-02-13 03:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_cart_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveLater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=255)),
                ('productid', models.IntegerField()),
                ('price', models.IntegerField()),
                ('delivertcharge', models.IntegerField()),
                ('useruid', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantity', models.CharField(max_length=255)),
                ('sellerid', models.CharField(max_length=255)),
                ('sellername', models.CharField(max_length=255)),
                ('image', models.ImageField(default='default.png', upload_to='')),
            ],
        ),
    ]