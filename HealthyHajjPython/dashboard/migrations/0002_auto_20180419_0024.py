# Generated by Django 2.0.3 on 2018-04-18 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendez_vous_externe',
            name='adr',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='rendez_vous_externe',
            name='sexe',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
