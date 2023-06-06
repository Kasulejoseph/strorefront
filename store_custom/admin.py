from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin
from store.models import Products
from tags.models import TagItem


class TagInline(GenericTabularInline):
    model = TagItem
    autocomplete_fields = ['tag']


class CustomProduct(ProductAdmin):
    inlines = [TagInline]

admin.site.unregister(Products)
admin.site.register(Products, CustomProduct)
