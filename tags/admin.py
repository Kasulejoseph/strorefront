from django.contrib import admin

from .models import TagItem, Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ['label']
    search_fields = ['label']

