from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Pizza(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return "%s: %scm" % (self.name, self.size)


class Order(models.Model):
    PIZZA_SIZES = (
        ('small', '30cm'),
        ('large', "50cm")
    )
    size = models.CharField(max_length=5, choices=PIZZA_SIZES)
    pizza = models.ForeignKey(Pizza, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.pizza.title + self.address

    def get_cost(self):
        return self.price * self.quantity
