# Generated by Django 3.2.8 on 2021-10-14 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0003_auto_20211014_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arrivalprobabilities',
            old_name='ArrivalProbId',
            new_name='arrivalProbId',
        ),
        migrations.RenameField(
            model_name='arrivalprobabilities',
            old_name='BinEdge',
            new_name='binEdge',
        ),
        migrations.RenameField(
            model_name='arrivalprobabilities',
            old_name='BinEntry',
            new_name='binEntry',
        ),
    ]