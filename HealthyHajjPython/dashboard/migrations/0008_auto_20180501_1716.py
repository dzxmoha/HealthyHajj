# Generated by Django 2.0.3 on 2018-05-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20180430_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seuil',
            name='type',
            field=models.CharField(blank=True, choices=[('ponctuelle', 'p'), ('annuelle', 'a'), ('hebdomadaire', 'h')], max_length=1, null=True),
        ),
    ]
