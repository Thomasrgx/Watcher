# Generated by Django 3.1 on 2020-08-31 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_monitoring', '0021_site_misp_event_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='rtir',
            field=models.IntegerField(),
        ),
    ]