from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from pizza_app.models import Pizza, Customer, Order


class CustomerTests(APITestCase):
    def setUp(self):
        self.pizza_name = 'Pepperoni'
        self.customer_first_name = 'Gianluigi'
        self.customer_last_name = 'Buffon'
        self.customer_email = 'gbuffon@gmail.com'

    def test_create_customer(self):
        url = reverse('customers-list')
        data = {
            'first_name': self.customer_first_name,
            'last_name': self.customer_last_name,
            'email': self.customer_email,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().first_name, self.customer_first_name)

    def test_customer_order(self):
        pizza = Pizza.objects.create(name=self.pizza_name)
        customer = Customer.objects.create(
            first_name=self.customer_first_name,
            last_name=self.customer_last_name,
            email=self.customer_email
        )
        url = reverse('orders-list')

        data = {
            'customer': customer.id,
            'pizza': pizza.id,
            'size': 'small',
            "address": "Baker street"
        }
        response = self.client.post(url, data, format='json')

        url = reverse('customers-detail', args=[customer.id]) + 'orders/'

        response = self.client.get(url)
        print(response.json())
        self.assertEqual(response.data[0]['customer']['email'], self.customer_email)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['pizza']['name'], self.pizza_name)


class OrderTests(APITestCase):
    def setUp(self):
        self.pizza_name = 'Pulled pork'
        self.customer_first_name = 'Gianluigi'
        self.customer_last_name = 'Buffon'
        self.customer_email = 'gbuffon@gmail.com'

    def test_create_order(self):
        pizza = Pizza.objects.create(name=self.pizza_name)
        customer = Customer.objects.create(
            first_name=self.customer_first_name,
            last_name=self.customer_last_name,
            email=self.customer_email
        )
        url = reverse('orders-list')
        data = {
            'customer': customer.id,
            'pizza': pizza.id,
            'size': 'small',
            "address": "Baker street"
        }
        response = self.client.post(url, data, format='json')
        print(response.json())
        order_id = response.data['id']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get(id=order_id).pizza.name, self.pizza_name)
