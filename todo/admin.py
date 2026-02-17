from django.contrib import admin
from .models import ToDo




class TodoAdmin(admin.ModelAdmin):
    list_display = ["id", "body", "duration", "duration_type", "status", "created_at", "duration_range"]

admin.site.register(ToDo, TodoAdmin)