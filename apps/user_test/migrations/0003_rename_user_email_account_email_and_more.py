# Generated by Django 4.1.7 on 2023-03-15 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_test', '0002_rename_id_user_account_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_name',
        ),
    ]
