from django.contrib import admin

from .models import StudentGroup


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ['name']}
    list_display_links = list_display
