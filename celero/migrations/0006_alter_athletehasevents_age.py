# Generated by Django 4.0.3 on 2022-03-31 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celero', '0005_alter_athletehasevents_medal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athletehasevents',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
