from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'is_staff',)
    list_filter = ('username', 'is_staff',)
    empty_value_display = '-пусто-'
