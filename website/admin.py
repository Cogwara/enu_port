"""
Django admin configuration for website app.
"""
from django.contrib import admin
from .models import ContactMessage, Service, Project


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Admin interface for contact messages."""
    list_display = ['name', 'email', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at']

    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} message(s) marked as read.')
    mark_as_read.short_description = 'Mark selected as read'

    actions = [mark_as_read]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Admin interface for services."""
    list_display = ['category', 'title', 'order']
    list_filter = ['category']
    search_fields = ['title', 'description']
    ordering = ['order', 'category']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin interface for projects."""
    list_display = ['title', 'category', 'completion_date', 'order']
    list_filter = ['category', 'completion_date']
    search_fields = ['title', 'description']
    ordering = ['-completion_date', 'order']
