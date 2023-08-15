# Generated by Django 4.1.3 on 2023-08-15 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_comment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='review',
            new_name='post',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
    ]
