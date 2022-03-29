from django.contrib import admin

from.models import Product, Type, Subtype, Order, Client

admin.site.register(Product)
admin.site.register(Type)
admin.site.register(Subtype)
admin.site.register(Order)
admin.site.register(Client)
