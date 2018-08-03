# Generated by Django 2.0.3 on 2018-04-17 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_R', models.DateTimeField(verbose_name='date published')),
                ('is_RDV', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_patient', models.CharField(max_length=25)),
                ('prenom_patient', models.CharField(max_length=25)),
                ('date_de_naissance_patient', models.DateTimeField(null=True)),
                ('sexe_patient', models.CharField(max_length=4)),
                ('adr_patient', models.CharField(max_length=250)),
                ('num_telephone_parent', models.CharField(max_length=10, null=True)),
                ('adr_mail_parent', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rendez_vous_externe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_pub', models.DateTimeField(blank=True, verbose_name='date published')),
                ('motif', models.CharField(blank=True, max_length=200)),
                ('nom', models.CharField(blank=True, max_length=25)),
                ('prenom', models.CharField(blank=True, max_length=25)),
                ('num_telephone', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rendez_vous_interne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_pub', models.DateTimeField(blank=True, verbose_name='date published')),
                ('motif', models.CharField(blank=True, max_length=200)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Patient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
