# Generated by Django 4.2.5 on 2023-11-03 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_todos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Todos',
        ),
    ]