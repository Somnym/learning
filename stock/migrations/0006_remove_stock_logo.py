# Generated by Django 4.2.7 on 2023-11-28 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_stock_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='logo',
        ),
    ]
