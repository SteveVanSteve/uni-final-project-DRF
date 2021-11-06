# Generated by Django 3.2.8 on 2021-11-06 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArrivalProbabilities',
            fields=[
                ('arrivalProbId', models.IntegerField(primary_key=True, serialize=False)),
                ('binEntry', models.FloatField(null=True)),
                ('binEdge', models.FloatField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='simulation', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['arrivalProbId'],
            },
        ),
    ]
