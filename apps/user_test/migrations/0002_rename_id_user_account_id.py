# Generated by Django 4.1.7 on 2023-03-15 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_test', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='id_user',
            new_name='id',
        ),
    ]
