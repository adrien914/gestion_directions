# Generated by Django 3.0.6 on 2020-06-04 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carte', '0006_auto_20200604_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hebergeur',
            name='hebergement',
        ),
    ]
