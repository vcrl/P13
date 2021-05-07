# Generated by Django 3.2.2 on 2021-05-07 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_rdv_toiletteur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rdv',
            name='service',
        ),
        migrations.AddField(
            model_name='rdv',
            name='service',
            field=models.ManyToManyField(default='', null=True, to='management.Service'),
        ),
    ]
