from django.test import TestCase

from pinax.cart.models import Product


class ProductTestCase(TestCase):

    def test_product_count(self):
        self.assertEqual(Product.objects.count(), 0)
