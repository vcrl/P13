# Generated by Django 3.2.2 on 2021-05-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_auto_20210507_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='chien',
        ),
        migrations.AddField(
            model_name='client',
            name='chien',
            field=models.ManyToManyField(default='', null=True, to='management.Chien'),
        ),
    ]