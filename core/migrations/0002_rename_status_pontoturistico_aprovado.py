# Generated by Django 3.2.8 on 2021-10-06 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pontoturistico',
            old_name='status',
            new_name='aprovado',
        ),
    ]
