# Generated by Django 3.0.6 on 2020-06-10 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etatsite',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='hebergement',
            name='type',
            field=models.CharField(default=None, max_length=255, null=True, unique=True),
        ),
    ]
