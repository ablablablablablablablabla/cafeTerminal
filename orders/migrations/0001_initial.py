# Generated by Django 5.1.7 on 2025-04-01 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField()),
                ('items', models.JSONField(default=list)),
                ('status', models.CharField(default='В ожидании', max_length=20)),
            ],
        ),
    ]
