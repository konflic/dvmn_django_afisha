# Generated by Django 3.0 on 2021-11-28 09:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20211128_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='image_file',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
