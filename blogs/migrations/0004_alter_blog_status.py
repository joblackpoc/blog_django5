# Generated by Django 5.0.6 on 2024-06-02 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_rename_is_featuered_blog_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default='Draft'),
        ),
    ]
