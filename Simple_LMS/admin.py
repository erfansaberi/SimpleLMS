from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Course)
admin.site.register(models.Notes)
admin.site.register(models.Videos)
admin.site.register(models.Solutions)
admin.site.register(models.Homeworks)
admin.site.register(models.Notifications)
