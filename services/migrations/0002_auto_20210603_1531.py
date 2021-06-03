# Generated by Django 3.2.3 on 2021-06-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='duree',
            field=models.CharField(choices=[('~ 5 min.', '5'), ('~ 30 min.', '30'), ('~ 1h00', '60'), ('~ 1h30', '90'), ('~ 2h00', '120'), ('~ 2h +', '+120')], default='~ 30 min.', max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='race',
            field=models.CharField(choices=[('Petite', 'Petit'), ('Moyenne', 'Moyen'), ('Grande', 'Grand')], default='Moyenne', max_length=9, null=True),
        ),
    ]
