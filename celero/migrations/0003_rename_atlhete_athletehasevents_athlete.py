# Generated by Django 4.0.3 on 2022-03-31 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celero', '0002_rename_atlheteid_id_athletehasevents_atlhete_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='athletehasevents',
            old_name='atlhete',
            new_name='athlete',
        ),
    ]