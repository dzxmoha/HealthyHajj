# Generated by Django 2.0.3 on 2018-04-28 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20180428_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendez_vous_externe',
            name='date_pub',
            field=models.DateField(blank=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='rendez_vous_interne',
            name='date_pub',
            field=models.DateField(blank=True, verbose_name='date published'),
        ),
    ]
