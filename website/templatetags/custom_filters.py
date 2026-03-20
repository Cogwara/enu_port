"""
Custom template tags for MRCHRYS website.
"""
from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """
    Get an item from a dictionary using a key.
    Usage: {{ mydict|get_item:key }}
    """
    if dictionary and key:
        return dictionary.get(key, '')
    return ''


@register.filter
def multiply(value, arg):
    """
    Multiply the value by the argument.
    Usage: {{ value|multiply:2 }}
    """
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return 0


@register.filter
def get_service_color(category):
    """
    Get a color for a service category.
    Usage: {{ category|get_service_color }}
    """
    colors = {
        'Telecommunications': 'primary',
        'Software & IT': 'info',
        'Cybersecurity': 'success',
        'Engineering & Construction': 'warning',
        'Electrical & Power': 'danger',
        'Logistics & Supply': 'secondary',
        'General Contracts': 'dark',
        'Entertainment & Media': 'purple',
        'Training & Consulting': 'primary',
        'Data & Smart Systems': 'info',
    }
    return colors.get(category, 'primary')
