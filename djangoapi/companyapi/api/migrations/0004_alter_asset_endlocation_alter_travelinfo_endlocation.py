# Generated by Django 4.1.5 on 2023-01-13 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_asset_travelinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='endlocation',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='travelinfo',
            name='endlocation',
            field=models.CharField(max_length=20),
        ),
    ]
