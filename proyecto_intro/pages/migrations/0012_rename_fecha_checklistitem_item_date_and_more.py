# Generated by Django 4.2.5 on 2023-11-27 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_rename_read_news_userprofile_read_news_titles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklistitem',
            old_name='fecha',
            new_name='item_date',
        ),
        migrations.RenameField(
            model_name='checklistitem',
            old_name='elementos',
            new_name='item_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='checklist_items',
            field=models.ManyToManyField(to='pages.checklistitem'),
        ),
    ]