# Generated by Django 4.0.5 on 2022-10-05 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0003_report_belongs_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='assigned_to',
        ),
        migrations.AlterField(
            model_name='report',
            name='attachment',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='report',
            name='reported_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]