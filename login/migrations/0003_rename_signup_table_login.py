# Generated by Django 4.1.5 on 2023-03-10 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_rename_signup_signup_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='signup_table',
            new_name='login',
        ),
    ]