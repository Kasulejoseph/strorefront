from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models import Count
from django.http.request import HttpRequest
from . import models

# Register your models here.

@admin.register(models.Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'inventory_status', 'collection_title']
    list_editable = [ 'price']
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory > 10:
            return 'Ok'
        return 'Low'

@admin.register(models.Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['placed_at', 'payment_status', 'customer_name']
    list_select_related = ['customer']

    def customer_name(self, order):
        return order.customer.first_name  + ' ' + order.customer.last_name
    


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count']

    @admin.display(ordering='product_count')
    def product_count(self, collection):
        return collection.product_count

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            product_count=Count('products')
        )