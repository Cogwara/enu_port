"""
Management command to load initial data for MRCHRYS website.
Usage: python manage.py load_initial_data
"""
from django.core.management.base import BaseCommand
from website.models import Service, Project


class Command(BaseCommand):
    help = 'Load initial data for MRCHRYS website'

    def handle(self, *args, **options):
        # Define initial services
        services_data = [
            {
                'category': 'Telecommunications',
                'items': [
                    'Telecom site installation and maintenance',
                    'Fiber optic installation',
                    'Network optimization',
                    'Equipment installation',
                ]
            },
            {
                'category': 'Software & IT',
                'items': [
                    'Web development',
                    'Mobile apps',
                    'Enterprise software',
                    'Cloud services',
                ]
            },
            {
                'category': 'Cybersecurity',
                'items': [
                    'Network security',
                    'Penetration testing',
                    'Security audits',
                    'Threat monitoring',
                ]
            },
            {
                'category': 'Engineering & Construction',
                'items': [
                    'Building construction',
                    'Civil engineering',
                    'Facility maintenance',
                ]
            },
            {
                'category': 'Electrical & Power',
                'items': [
                    'Solar installation',
                    'Inverter systems',
                    'Electrical wiring',
                ]
            },
            {
                'category': 'Logistics & Supply',
                'items': [
                    'Procurement',
                    'Import/export',
                    'Transportation',
                ]
            },
            {
                'category': 'General Contracts',
                'items': [
                    'Corporate contracts',
                    'Office equipment supply',
                    'Industrial materials',
                ]
            },
            {
                'category': 'Entertainment & Media',
                'items': [
                    'Event management',
                    'Media production',
                    'Content creation',
                ]
            },
            {
                'category': 'Training & Consulting',
                'items': [
                    'ICT training',
                    'Cybersecurity awareness',
                    'Business consulting',
                ]
            },
            {
                'category': 'Data & Smart Systems',
                'items': [
                    'Data analytics',
                    'Smart systems',
                    'Digital transformation',
                ]
            },
        ]

        # Icons mapping
        icons = {
            'Telecommunications': 'fas fa-tower-cell',
            'Software & IT': 'fas fa-code',
            'Cybersecurity': 'fas fa-shield-alt',
            'Engineering & Construction': 'fas fa-hard-hat',
            'Electrical & Power': 'fas fa-bolt',
            'Logistics & Supply': 'fas fa-truck',
            'General Contracts': 'fas fa-handshake',
            'Entertainment & Media': 'fas fa-film',
            'Training & Consulting': 'fas fa-chalkboard-user',
            'Data & Smart Systems': 'fas fa-chart-bar',
        }

        # Create services
        created_count = 0
        for service in services_data:
            for idx, item in enumerate(service['items']):
                obj, created = Service.objects.get_or_create(
                    category=service['category'],
                    title=item,
                    defaults={
                        'description': f"{item} for professional use",
                        'icon': icons.get(service['category'], 'fas fa-star'),
                        'order': idx,
                    }
                )
                if created:
                    created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {created_count} services'
            )
        )
