# Generated by Django 3.1.4 on 2020-12-08 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitelist',
            name='location',
            field=models.CharField(default='Database', max_length=255),
        ),
    ]