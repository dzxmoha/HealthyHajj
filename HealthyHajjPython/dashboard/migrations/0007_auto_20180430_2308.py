# Generated by Django 2.0.3 on 2018-04-30 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20180430_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seuil',
            name='type',
            field=models.CharField(blank=True, choices=[('p', 'ponctuelle'), ('a', 'annuelle'), ('h', 'hebdomadaire')], max_length=1, null=True),
        ),
    ]