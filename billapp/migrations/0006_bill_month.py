# Generated by Django 2.1.1 on 2018-10-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0005_expense'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='month',
            field=models.CharField(blank=True, default=0, max_length=20),
        ),
    ]
