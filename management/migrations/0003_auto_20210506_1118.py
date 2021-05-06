# Generated by Django 3.2.2 on 2021-05-06 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20210506_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chien',
            name='owner',
        ),
        migrations.AddField(
            model_name='client',
            name='chien',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.chien'),
        ),
    ]
