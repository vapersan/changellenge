from django.contrib import admin
from martor.widgets import AdminMartorWidget

from .models import Services, ServicesRelation
from django.db import models


# Register your models here.

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
    list_display = ('name', 'status', 'date_created', 'date_release', 'stars', 'parents_count', 'children_count')
    list_display_links = ('name',)
    list_filter = ('status',)
    search_fields = ('about', 'name')

    def parents_count(self, obj):
        return ServicesRelation.objects.get_or_create(children=obj)[0].parents.count()

    def children_count(self, obj):
        return ServicesRelation.objects.filter(parents=obj).count()

    parents_count.__name__ = 'Parents count'
    children_count.__name__ = 'Children\'s count'
