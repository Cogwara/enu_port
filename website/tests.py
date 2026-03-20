"""
Tests for MRCHRYS ENT NIG LTD website.
"""
from django.test import TestCase, Client
from django.urls import reverse
from .models import ContactMessage, Service, Project


class WebsiteViewTests(TestCase):
    """Test cases for website views."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    def test_home_page_loads(self):
        """Test that home page loads successfully."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/home.html')

    def test_about_page_loads(self):
        """Test that about page loads successfully."""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/about.html')

    def test_services_page_loads(self):
        """Test that services page loads successfully."""
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/services.html')

    def test_projects_page_loads(self):
        """Test that projects page loads successfully."""
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/projects.html')

    def test_contact_page_loads(self):
        """Test that contact page loads successfully."""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/contact.html')


class ContactFormTests(TestCase):
    """Test cases for contact form functionality."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()
        self.contact_url = reverse('contact')

    def test_contact_form_submission(self):
        """Test valid contact form submission."""
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'phone': '1234567890',
            'message': 'This is a test message.'
        }
        response = self.client.post(self.contact_url, data)

        # Check if message was created
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(ContactMessage.objects.first().name, 'Test User')

    def test_contact_form_missing_required_fields(self):
        """Test contact form with missing required fields."""
        data = {
            'name': 'Test User',
            # Missing email and message
        }
        response = self.client.post(self.contact_url, data)

        # Check that no message was created
        self.assertEqual(ContactMessage.objects.count(), 0)


class ContactMessageModelTests(TestCase):
    """Test cases for ContactMessage model."""

    def test_create_contact_message(self):
        """Test creating a contact message."""
        message = ContactMessage.objects.create(
            name='Test User',
            email='test@example.com',
            phone='1234567890',
            message='Test message content'
        )

        self.assertEqual(message.name, 'Test User')
        self.assertEqual(message.email, 'test@example.com')
        self.assertFalse(message.is_read)

    def test_contact_message_string_representation(self):
        """Test string representation of contact message."""
        message = ContactMessage.objects.create(
            name='Test User',
            email='test@example.com',
            message='Test message'
        )

        self.assertIn('Test User', str(message))


class ServiceModelTests(TestCase):
    """Test cases for Service model."""

    def test_create_service(self):
        """Test creating a service."""
        service = Service.objects.create(
            category='Telecommunications',
            title='Fiber Optic Installation',
            description='Professional fiber optic installation services',
            icon='fas fa-tower-cell',
            order=1
        )

        self.assertEqual(service.category, 'Telecommunications')
        self.assertEqual(service.title, 'Fiber Optic Installation')


class ProjectModelTests(TestCase):
    """Test cases for Project model."""

    def test_create_project(self):
        """Test creating a project."""
        project = Project.objects.create(
            title='Telecom Site Installation',
            description='Installation of telecom infrastructure',
            category='Telecommunications',
            order=1
        )

        self.assertEqual(project.title, 'Telecom Site Installation')
        self.assertEqual(project.category, 'Telecommunications')
