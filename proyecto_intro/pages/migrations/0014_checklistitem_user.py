# Generated by Django 4.2.5 on 2023-11-27 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_rename_item_name_checklistitem_elementos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistitem',
            name='user',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
