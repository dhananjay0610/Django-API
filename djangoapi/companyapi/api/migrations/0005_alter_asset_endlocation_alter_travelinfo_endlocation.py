# Generated by Django 4.1.5 on 2023-01-14 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_asset_endlocation_alter_travelinfo_endlocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='endlocation',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='travelinfo',
            name='endlocation',
            field=models.CharField(max_length=50),
        ),
    ]
