# Generated by Django 3.2.8 on 2021-11-10 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArrivalProbabilities',
            fields=[
                ('arrivalProbId', models.IntegerField(primary_key=True, serialize=False)),
                ('binEntry', models.FloatField(null=True)),
                ('binEdge', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='BackgroundSet',
            fields=[
                ('backgroundSetId', models.IntegerField(primary_key=True, serialize=False)),
                ('backgroundSetName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ChargingCurve',
            fields=[
                ('chargingCurveId', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.FloatField(default=None)),
                ('power', models.FloatField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='BackgroundPower',
            fields=[
                ('backgroundPowerId', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.FloatField(default=None)),
                ('power', models.FloatField(default=None)),
                ('backgroundSetId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='simulation.backgroundset')),
            ],
        ),
    ]
