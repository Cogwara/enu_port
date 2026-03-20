"""
Models for MRCHRYS ENT NIG LTD website.
"""
from django.db import models
from django.core.validators import EmailValidator


class ContactMessage(models.Model):
    """Model for storing contact form submissions."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"


class Service(models.Model):
    """Model for storing services."""
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True,
                            default='fas fa-service')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'category']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return f"{self.category} - {self.title}"


class Project(models.Model):
    """Model for storing portfolio projects."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-completion_date', '-order']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title
