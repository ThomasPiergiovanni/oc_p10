# Generated by Django 3.1.7 on 2021-04-13 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supersub', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='relation_user',
            new_name='relation_custom_user',
        ),
    ]