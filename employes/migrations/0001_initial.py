# Generated by Django 3.2.3 on 2021-05-29 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=155, null=True)),
                ('nom', models.CharField(default='', max_length=155, null=True)),
                ('adresse', models.CharField(default='', max_length=155, null=True)),
                ('num', models.CharField(default='', max_length=255, null=True)),
                ('rdv_number', models.IntegerField(default=0, null=True)),
                ('joined', models.DateTimeField(null=True)),
                ('fired', models.DateTimeField(null=True)),
            ],
        ),
    ]
