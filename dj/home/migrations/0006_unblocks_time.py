# Generated by Django 4.0.1 on 2022-11-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_unblocks'),
    ]

    operations = [
        migrations.AddField(
            model_name='unblocks',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]
