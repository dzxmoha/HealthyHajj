# Generated by Django 2.0.3 on 2018-05-03 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20180501_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendez_vous_externe',
            name='sexe',
            field=models.CharField(blank=True, choices=[('Homme', 'homme'), ('Famme', 'famme')], max_length=5),
        ),
    ]
