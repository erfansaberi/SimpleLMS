from typing import Any
from django.contrib import admin
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.urls import reverse

from . import models

# Register your models here.
@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'enrolls_count']
    search_fields = ['name']
    
    @admin.display(ordering='enrolls_count')
    def enrolls_count(self, course):
        return course.enrolls_count


    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            enrolls_count=Count('enrolls')
        )
    
@admin.register(models.Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'student', 'score']
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request)\
            .prefetch_related("course")\
            .prefetch_related("student")

@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'course', 'upload_date']

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).prefetch_related("course")

@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'subject']
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).prefetch_related("course")

@admin.register(models.Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'home_work', 'student', 'score']
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request)\
            .prefetch_related("home_work")\
            .prefetch_related("student")\
            .prefetch_related("course")

@admin.register(models.Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'deadline', 'max_score']
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).prefetch_related("course")

@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'title', 'timestamp']
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).prefetch_related("course")
