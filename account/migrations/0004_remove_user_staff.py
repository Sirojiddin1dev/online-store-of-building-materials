# Generated by Django 5.0.3 on 2024-03-27 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_staff_alter_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='staff',
        ),
    ]