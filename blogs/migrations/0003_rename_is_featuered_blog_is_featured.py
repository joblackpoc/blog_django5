# Generated by Django 5.0.6 on 2024-06-02 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_category_options_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='is_featuered',
            new_name='is_featured',
        ),
    ]