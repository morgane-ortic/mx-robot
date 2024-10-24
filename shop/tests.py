from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Product

class HomeTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='password1')
        self.product = Product.objects.create(name='Test Product', price=12.55)

    def test_home_view_logged_in_user(self):
        session = self.client.session
        session['user_id'] = self.user.id
        session.save()
        response = self.client.get(reverse('shop:home'))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Welcome, user1')
        self.assertContains(response, 'Test Product')
        self.assertContains(response, '12.55')

    def test_home_unregistered_user(self):
        response = self.client.get(reverse('shop:home'))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Welcome, ')
        self.assertNotContains(response, 'user1')
        self.assertContains(response, 'Test Product')
        self.assertContains(response, '12.55')


class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
        username='user1',
        password='password1',
        email='user1@gmail.com'
        )

    def test_user_registration_get_request(self):
        response = self.client.get(reverse('shop:register'))
        self.assertEqual(200, response.status_code)

    def test_registration_post_success(self):
        data = {'username': 'user2', 'password': 'password2', 'email': 'test2@gmail.com'}
        response = self.client.post(reverse('shop:register'), data)
        self.assertEqual(302, response.status_code)
        user_exists = User.objects.filter(username='user2').exists()
        self.assertTrue(user_exists)
        
    def test_login_success(self):
        data = {'username': 'user1', 'password': 'password1'}
        response = self.client.post(reverse('shop:login'), data)
        self.assertEqual(302, response.status_code)
        self.assertRedirects(response, reverse('shop:home'))
        session = self.client.session
        self.assertIn('user_id', session)
        self.assertEqual(session['user_id'], self.user.id)

    def test_logout_success(self):
        self.client.login(username='user1', password='password1')
        response = self.client.post(reverse('shop:log_out'))
        self.assertRedirects(response, reverse('shop:home'))
        session = self.client.session
        self.assertNotIn('user_id', session)