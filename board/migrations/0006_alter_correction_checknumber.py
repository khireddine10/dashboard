# Generated by Django 4.0.4 on 2022-06-15 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_correction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correction',
            name='checknumber',
            field=models.CharField(max_length=200),
        ),
    ]
