# Generated by Django 3.0.6 on 2020-06-04 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionnaire', '0002_remove_etatsite_direction'),
        ('carte', '0004_remove_direction_etat_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='direction',
            name='etat_site',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionnaire.EtatSite'),
        ),
    ]
