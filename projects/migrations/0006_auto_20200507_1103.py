# Generated by Django 3.0.6 on 2020-05-07 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0005_issueassign'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagname', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='assignedAt',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Assigned At'),
        ),
        migrations.AddField(
            model_name='issue',
            name='assigned_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issues_you_assigned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issue',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_issues', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='issue',
            name='tags',
        ),
        migrations.DeleteModel(
            name='IssueAssign',
        ),
        migrations.AddField(
            model_name='issue',
            name='tags',
            field=models.ManyToManyField(related_name='issues', to='projects.Tags'),
        ),
    ]
