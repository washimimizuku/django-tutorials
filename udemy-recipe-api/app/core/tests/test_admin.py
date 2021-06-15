from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from faker import Faker

faker = Faker()


class AdminSiteTests(TestCase):

    def setUp(self):
        admin_email = faker.email()
        admin_password = faker.password(length=12)

        user_email = faker.email()
        user_password = faker.password(length=12)

        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email=admin_email,
            password=admin_password
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email=user_email,
            password=user_password,
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
