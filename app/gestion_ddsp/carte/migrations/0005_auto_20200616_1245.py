# Generated by Django 3.0.6 on 2020-06-16 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carte', '0004_deplacement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deplacement',
            name='direction',
        ),
        migrations.AddField(
            model_name='deplacement',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]