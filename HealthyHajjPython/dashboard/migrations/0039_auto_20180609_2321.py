# Generated by Django 2.0.4 on 2018-06-09 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0038_auto_20180609_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendez_vous_externe',
            name='sexe',
            field=models.CharField(blank=True, choices=[('Fille', 'fille'), ('Garçon', 'garçon'), ('Sexe non  déterminé', 'sexe-non-déterminé')], max_length=250),
        ),
    ]
