# Generated by Django 2.1.5 on 2019-03-12 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author_id',
            field=models.IntegerField(),
        ),
    ]
