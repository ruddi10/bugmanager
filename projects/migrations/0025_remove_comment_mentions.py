# Generated by Django 3.0.6 on 2020-07-17 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='mentions',
        ),
    ]