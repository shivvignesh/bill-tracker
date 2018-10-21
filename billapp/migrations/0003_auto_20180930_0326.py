# Generated by Django 2.1.1 on 2018-09-30 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('billapp', '0002_auto_20180930_0225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='user',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='customer',
        ),
        migrations.AddField(
            model_name='bill',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserDetail',
        ),
    ]