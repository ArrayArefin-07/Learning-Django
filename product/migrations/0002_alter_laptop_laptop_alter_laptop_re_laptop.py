# Generated by Django 4.2.5 on 2023-12-21 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='laptop',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='re_laptop',
            field=models.CharField(max_length=100),
        ),
    ]
