# Generated by Django 3.0.6 on 2020-06-25 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20200626_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Updated At'),
        ),
    ]
