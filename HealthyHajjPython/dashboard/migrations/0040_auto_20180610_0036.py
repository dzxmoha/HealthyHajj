# Generated by Django 2.0.4 on 2018-06-09 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0039_auto_20180609_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='sexe_patient',
            field=models.CharField(choices=[('Garçon', 'garçon'), ('Fille', 'fille'), ('  Sexe non déterminé', 'sexe-non-déterminé')], max_length=25),
        ),
        migrations.AlterField(
            model_name='rendez_vous_externe',
            name='sexe',
            field=models.CharField(blank=True, choices=[('Garçon', 'garçon'), ('Fille', 'fille'), ('  Sexe non déterminé', 'sexe-non-déterminé')], max_length=250),
        ),
    ]
