# Generated by Django 3.2.8 on 2021-11-12 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimulationResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.FloatField(default=None)),
                ('power', models.FloatField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='SimulationConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('houseId', models.IntegerField()),
                ('numberOfCars', models.IntegerField()),
                ('backgroundSetId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='simulation.backgroundset')),
            ],
        ),
    ]
