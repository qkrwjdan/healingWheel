# Generated by Django 2.0.13 on 2019-07-30 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_merge_20190730_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivingtime',
            name='detail_menu',
            field=models.CharField(choices=[('10', '10분'), ('30', '30분'), ('60', '60분')], default='10', max_length=10),
        ),
    ]
