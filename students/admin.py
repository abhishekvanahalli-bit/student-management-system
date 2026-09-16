from django.contrib import admin

from .models import Achievement, Category, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'register_number',
        'email',
        'course',
        'department',
        'status')
    search_fields = ('name', 'register_number', 'email')
    list_filter = ('status', 'department', 'course')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'student', 'category', 'date', 'status')
    search_fields = ('title', 'student__name', 'student__register_number')
    list_filter = ('status', 'category', 'date')
