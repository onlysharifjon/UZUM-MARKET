# Generated by Django 4.2.8 on 2024-01-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalerRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=18, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('phone', models.IntegerField(unique=True)),
                ('PasportSeria', models.CharField(max_length=2)),
                ('PasportNumber', models.IntegerField(unique=True)),
            ],
        ),
    ]