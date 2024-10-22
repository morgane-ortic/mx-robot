from django.test import TestCase
from django.urls import reverse
from shop.models import Product

# Create your tests here.
class ItemTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name = 'test product',
            price = 10,
            description = 'test description',
            category = 'PC'
        )
    def test_items_list(self):
        response = self.client.get(reverse('shop:list_products'))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'test product')