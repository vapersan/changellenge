from django.contrib import admin
from martor.widgets import AdminMartorWidget

from .models import Services, ServicesRelation, Links, ServiceAboutPreset
from django.db import models


# Register your models here.
@admin.register(ServicesRelation)
class ServicesRelationAdmin(admin.ModelAdmin):
    list_display = ('children',)
    list_display_links = ('children',)
    filter_horizontal = ('parents',)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
    list_display = ('name', 'status', 'date_created', 'stars', 'parents_count', 'children_count')
    list_display_links = ('name',)
    filter_vertical = ('authors',)
    list_filter = ('status',)
    search_fields = ('about', 'name')


@admin.register(ServiceAboutPreset)
class ServiceAboutPresetAdmin(admin.ModelAdmin):
    list_display = ('name', 'preset')
    list_display_links = ('name',)
