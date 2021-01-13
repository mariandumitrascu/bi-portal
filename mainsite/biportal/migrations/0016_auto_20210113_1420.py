# Generated by Django 3.1.5 on 2021-01-13 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biportal', '0015_auto_20210112_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='bipage',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='bipage',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Internal name'),
        ),
    ]
