# Generated by Django 3.2.2 on 2021-05-06 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_auto_20210506_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='duree',
            field=models.CharField(choices=[('~ 5 min.', '5'), ('~ 30 min.', '30'), ('~ 1h00', '60'), ('~ 1h30', '90'), ('~ 2h00', '120'), ('~ 2h +', '+120')], default='~ 30 min.', max_length=9),
        ),
    ]