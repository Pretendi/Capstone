# Generated by Django 2.1.2 on 2018-11-15 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='surveyed',
        ),
        migrations.DeleteModel(
            name='Survey',
        ),
    ]
