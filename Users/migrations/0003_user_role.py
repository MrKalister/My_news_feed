# Generated by Django 4.1.3 on 2023-08-14 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_user_options_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Администратор'), ('user', 'Пользователь')], default='user', max_length=50, verbose_name='Роль'),
        ),
    ]
