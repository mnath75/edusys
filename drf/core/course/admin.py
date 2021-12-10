from django.contrib import admin
from django.db import models
from .models import Category, Course, Lesson, Comment

class LessonCommentInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['cm_lesson']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['ls_title', 'ls_course', 'ls_status', 'ls_type']
    list_filter = ['ls_status']
    search_fields = ['ls_title', 'ls_short']

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Comment)