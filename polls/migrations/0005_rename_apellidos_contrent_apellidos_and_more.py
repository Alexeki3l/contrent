# Generated by Django 4.2.1 on 2023-05-09 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_rename_last_name_contrent_apellidos_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contrent',
            old_name='apellidos',
            new_name='Apellidos',
        ),
        migrations.RenameField(
            model_name='contrent',
            old_name='nombre',
            new_name='Nombre',
        ),
    ]
