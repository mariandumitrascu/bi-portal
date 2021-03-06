# Generated by Django 3.1.5 on 2021-01-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biportal', '0006_auto_20210106_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='image_cropped',
            field=models.ImageField(blank=True, null=True, upload_to='image_cropped/', verbose_name='Report Snippet'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='image_rendered',
            field=models.ImageField(blank=True, null=True, upload_to='image_rendered/', verbose_name='Rendered Report'),
        ),
    ]
