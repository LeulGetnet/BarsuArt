from django.urls import path
from .views import order, orderView

urlpatterns = [
    path('', order, name='order'),
    path('order_list/', orderView, name='order_list')
]