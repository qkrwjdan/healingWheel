# Generated by Django 2.2.1 on 2019-07-30 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190730_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivingtime',
            name='detail_menu',
            field=models.CharField(choices=[('10', '10분'), ('30', '30분'), ('60', '60분')], default='10', max_length=10),
        ),
    ]