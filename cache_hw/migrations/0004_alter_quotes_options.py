# Generated by Django 3.2.5 on 2021-07-16 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cache_hw', '0003_quotes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quotes',
            options={'ordering': ['id'], 'verbose_name': 'Quotes'},
        ),
    ]
