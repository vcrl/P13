# Generated by Django 3.2.2 on 2021-05-06 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_alter_rdv_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='duree',
            field=models.CharField(choices=[('5', '~ 5 min.'), ('30', '~ 30 min.'), ('60', '~ 1h00'), ('90', '~ 1h30'), ('120', '~ 2h00'), ('+120', '~ 2h +')], default='60', max_length=9),
        ),
        migrations.AddField(
            model_name='service',
            name='race',
            field=models.CharField(choices=[('Petite', 'Petit'), ('Moyenne', 'Moyen'), ('Grande', 'Grand')], default='Moyenne', max_length=9),
        ),
    ]
