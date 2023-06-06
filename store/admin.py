from typing import Any, List, Optional, Tuple
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models import Count
from django.http.request import HttpRequest
from django.utils.html import format_html
from django.utils.http import urlencode
from django.urls import reverse
from . import models

class InventoryFilter(admin.SimpleListFilter):
    title = 'Inventory'
    parameter_name = 'Inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]
    
    def queryset(self, request: Any, queryset: QuerySet):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)
    
@admin.register(models.Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'inventory_status', 'collection_title']
    list_editable = ['price']
    list_select_related = ['collection']
    list_filter = ['collection', 'updated_at', InventoryFilter]

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory > 10:
            return 'Ok'
        return 'Low'


@admin.register(models.Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'order_count']
    list_editable = ['membership']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    @admin.display(ordering='order_count')
    def order_count(self, customer):
        url = (reverse('admin:store_order_changelist')
               + '?'
               + urlencode({
                   'customer_id': customer.id
               }))
        return format_html('<a href={}>{}</a>', url, customer.order_count)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            order_count=Count('order')
        )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['placed_at', 'payment_status', 'customer_name']
    list_select_related = ['customer']

    def customer_name(self, order):
        return order.customer.first_name + ' ' + order.customer.last_name


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count']

    @admin.display(ordering='product_count')
    def product_count(self, collection):
        url = (reverse('admin:store_products_changelist') + '?' + urlencode({
            'collection_id': collection.id
        }))
        return format_html('<a href="{}">{}</a>', url, collection.product_count)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            product_count=Count('products')
        )
