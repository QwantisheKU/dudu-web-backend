# Generated by Django 4.2.7 on 2023-11-17 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_item_tag_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='is_done',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
