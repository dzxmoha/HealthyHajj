# Generated by Django 2.0.4 on 2018-06-08 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0033_auto_20180606_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='examan',
            name='ALSO',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='CPK',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='CRP',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='HbAlc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='NFS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='TCK_INR',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='TP',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='UCB',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='VS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='acide_urique',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='autre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='examan',
            name='bilan_lipidique',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='bilirubinemie',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='calcemie',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='chimiz_urines',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='creatininemie',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='electrophorese',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='febrinogene',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='fer_serique',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='glycémie_a_jeun',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='groupage_sanguin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='ionogramme_sanguin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='latex',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='mahnesemie',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='phosphatases',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='phosphorémie',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='proteinurie',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='serologie',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='toxoplasmose',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='examan',
            name='waaler_rose',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='examan',
            name='consultation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Consultation'),
        ),
        migrations.AlterField(
            model_name='lettre',
            name='consultation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Consultation'),
        ),
    ]
