# Generated by Django 2.1.1 on 2018-10-20 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0006_bill_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='month',
        ),
    ]
