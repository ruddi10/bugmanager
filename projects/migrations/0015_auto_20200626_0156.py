# Generated by Django 3.0.6 on 2020-06-25 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20200520_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('To Be Disscussed', 'To-Be-Disscussed'), ('Resolved', 'Resolved'), ('In Process', 'In Process')], default='Pending', max_length=30),
        ),
    ]
