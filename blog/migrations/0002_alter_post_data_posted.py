# Generated by Django 4.2.4 on 2023-08-22 08:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
