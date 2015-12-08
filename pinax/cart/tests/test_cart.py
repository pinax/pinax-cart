from django.test import TestCase

from pinax.cart.models import Cart


class CartTestCase(TestCase):

    def test_cart(self):
        self.assertEqual(Cart.objects.count(), 0)
