# Generated by Django 2.0.4 on 2018-06-05 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_auto_20180605_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='pic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]