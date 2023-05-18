from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from . import models

# Register your models here.
@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    ...

@admin.register(models.Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request)\
            .prefetch_related("course")\
            .prefetch_related("student")

@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).prefetch_related("course")

@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).prefetch_related("course")

@admin.register(models.Solution)
class SolutionAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request)\
            .prefetch_related("home_work")\
            .prefetch_related("student")\
            .prefetch_related("course")

@admin.register(models.Homework)
class HomeworkAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).prefetch_related("course")

@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).prefetch_related("course")
