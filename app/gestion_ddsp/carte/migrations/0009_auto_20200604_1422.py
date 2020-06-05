# Generated by Django 3.0.6 on 2020-06-04 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carte', '0008_direction_hebergement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='autres',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default=None, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='nom',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='prenom',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='telephone',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hebergeur',
            name='autres',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hebergeur',
            name='email',
            field=models.CharField(default=None, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='hebergeur',
            name='nom',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hebergeur',
            name='prenom',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hebergeur',
            name='telephone',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='stagiaire',
            name='divers',
            field=models.CharField(max_length=255),
        ),
    ]