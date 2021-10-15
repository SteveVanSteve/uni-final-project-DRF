# Generated by Django 3.2.8 on 2021-10-15 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0004_auto_20211014_1825'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BackgroundPower',
            new_name='ChargingPowers',
        ),
        migrations.RenameField(
            model_name='chargingpowers',
            old_name='BackgroundPowerId',
            new_name='Id',
        ),
        migrations.AlterField(
            model_name='backgroundprofiles',
            name='BackgroundName',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='BackgroundPowers',
            fields=[
                ('BackgroundPowerId', models.IntegerField(primary_key=True, serialize=False)),
                ('Time', models.FloatField()),
                ('Power', models.FloatField()),
                ('BackgroundId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='simulation.backgroundprofiles')),
            ],
        ),
    ]