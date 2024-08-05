from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('role', 'first_name', 'last_name', 'email', 'description', 'student_groups')
    list_display_links = list_display

