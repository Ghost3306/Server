# Generated by Django 5.0 on 2024-02-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_placedorder_delstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='placedorder',
            name='productimage',
            field=models.ImageField(default='abc.jpg', upload_to=''),
        ),
    ]
