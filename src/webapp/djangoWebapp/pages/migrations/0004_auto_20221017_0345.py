# Generated by Django 3.1.14 on 2022-10-17 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20221012_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='ecg',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='sensordata',
            name='ecg_connected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ip',
            name='ts',
            field=models.IntegerField(default=1665978337),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='ts',
            field=models.IntegerField(default=1665978337),
        ),
    ]