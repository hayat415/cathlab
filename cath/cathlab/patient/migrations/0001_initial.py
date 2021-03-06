# Generated by Django 4.0.5 on 2022-06-22 11:21

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Angio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_artery', tinymce.models.HTMLField()),
                ('second_artery', tinymce.models.HTMLField()),
                ('third_artery', tinymce.models.HTMLField()),
                ('fourth_atery', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('designation', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PCI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PCI_title', models.CharField(max_length=100)),
                ('PCI_desc', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedure_type', models.CharField(max_length=10)),
                ('Date', models.DateField()),
                ('discharge_date', models.DateField()),
                ('Cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=20)),
                ('cnic', models.IntegerField()),
                ('indication', models.CharField(max_length=40)),
                ('visit_number', models.IntegerField()),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.operator')),
                ('procedure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.procedure')),
            ],
        ),
    ]
