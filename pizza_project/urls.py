from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from pizza_app.views import CustomerViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, basename="orders")
router.register(r'customers', CustomerViewSet, basename="customers")

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'admin/', admin.site.urls),
]
