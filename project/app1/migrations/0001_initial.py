# Generated by Django 5.0.7 on 2024-07-18 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_name', models.CharField(max_length=50)),
                ('fuel_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=50)),
                ('car_number', models.IntegerField()),
                ('company_name', models.CharField(max_length=50)),
                ('fuel_name', models.ManyToManyField(to='app1.fuel')),
            ],
        ),
    ]
