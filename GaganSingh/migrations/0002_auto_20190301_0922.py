# Generated by Django 2.1.3 on 2019-03-01 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GaganSingh', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsgagan',
            name='Glink',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='projectsgagan',
            name='Llink',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
