# Generated by Django 4.1.5 on 2023-03-11 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_rename_signup_table_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='name',
            new_name='username',
        ),
    ]