from rest_framework import viewsets, mixins

from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Order, Customer

from .serializers import OrderSerializer, CustomerSerializer, CustomerOrderSerializer


class OrderViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    @action(detail=True, methods=["get"])
    def orders(self, request, pk=None):
        queryset = Order.objects.filter(customer=pk)
        serializer = CustomerOrderSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
