# Generated by Django 2.0.4 on 2018-06-05 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0024_auto_20180605_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
