from django.contrib import admin
from .models import Services, ServicesRelation
from django.utils.translation import gettext_lazy as _


# Register your models here.

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
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
