# Generated by Django 2.0.3 on 2018-05-01 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20180501_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seuil',
            name='date',
            field=models.DateField(blank=True, null=True, unique=True),
        ),
    ]