# Generated by Django 3.0.6 on 2020-07-05 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_auto_20200705_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilepic',
            field=models.ImageField(blank=True, default='guest-user.jpg', null=True, upload_to=''),
        ),
    ]
