# Generated by Django 4.2.7 on 2023-11-18 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_item_is_done'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='tag_id',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='user_id',
            new_name='user',
        ),
    ]
