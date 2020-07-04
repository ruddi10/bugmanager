# Generated by Django 3.0.6 on 2020-07-03 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_project_is_deployed'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('High', 'High'), ('Low', 'Low'), ('Moderate', 'Moderate')], default='Moderate', max_length=30),
        ),
    ]
