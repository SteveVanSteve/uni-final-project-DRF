# Generated by Django 3.2.8 on 2021-11-07 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargingCurve',
            fields=[
                ('chargingCurveId', models.IntegerField(primary_key=True, serialize=False)),
                ('Time', models.FloatField()),
                ('Power', models.FloatField()),
            ],
            options={
                'ordering': ['chargingCurveId'],
            },
        ),
    ]