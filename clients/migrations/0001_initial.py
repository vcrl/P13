# Generated by Django 3.2.3 on 2021-05-29 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='', max_length=155, null=True)),
                ('age', models.CharField(default='', max_length=155, null=True)),
                ('comment', models.CharField(default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(default='', max_length=155, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=155, null=True)),
                ('nom', models.CharField(default='', max_length=155, null=True)),
                ('adresse', models.CharField(default='', max_length=155, null=True)),
                ('num', models.CharField(default='', max_length=255, null=True)),
                ('mail', models.CharField(default='', max_length=255, null=True)),
                ('profession', models.CharField(max_length=155, null=True)),
                ('comment', models.CharField(max_length=155, null=True)),
                ('chien', models.ManyToManyField(default='', null=True, to='clients.Chien')),
                ('toiletteur', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='employes.employee')),
            ],
        ),
        migrations.AddField(
            model_name='chien',
            name='race',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.race'),
        ),
    ]