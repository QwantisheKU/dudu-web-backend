# Generated by Django 4.2.7 on 2023-11-27 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_rename_tag_id_item_tag_rename_user_id_item_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='todo.tag'),
        ),
    ]