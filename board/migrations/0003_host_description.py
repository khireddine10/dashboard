# Generated by Django 4.0.4 on 2022-05-25 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_rename_hosts_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
