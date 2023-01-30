from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Course)
admin.site.register(models.Note)
admin.site.register(models.Video)
admin.site.register(models.Solution)
admin.site.register(models.Homework)
admin.site.register(models.Notification)
