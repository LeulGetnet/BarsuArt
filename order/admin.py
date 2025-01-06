from django.contrib import admin

# Register your models here.
from .models import Order, OrderFormDescription
admin.site.register(OrderFormDescription)
admin.site.register(Order)
