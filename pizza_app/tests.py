import unittest

from rest_framework.reverse import reverse


class TestOrderViewset(unittest.TestCase):
    def setUp(self):
        self._setUrl()
        # self.url = reverse("orders")

    def _setUrl(self):
        return reverse("orders")

    def _create_customer(self):
        
    def test_create_order(self):
        pass

