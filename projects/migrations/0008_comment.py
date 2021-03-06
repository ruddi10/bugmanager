# Generated by Django 3.0.6 on 2020-05-07 12:57

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0007_auto_20200507_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created At')),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='your_comments', to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='projects.Issue')),
                ('mentions', models.ManyToManyField(blank=True, null=True, related_name='your_mentions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
