# Generated by Django 2.2.10 on 2020-05-16 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_auto_20200503_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
