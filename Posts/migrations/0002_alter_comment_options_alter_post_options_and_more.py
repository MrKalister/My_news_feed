# Generated by Django 4.1.3 on 2023-08-15 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created_date', 'id'), 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_date', '-id'), 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created',
            new_name='created_date',
        ),
    ]
