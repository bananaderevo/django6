# Generated by Django 3.2.5 on 2021-07-15 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cache_hw', '0002_auto_20210713_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotes', models.CharField(max_length=300)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cache_hw.author')),
            ],
        ),
    ]
