from django import template
from martor.widgets import MartorWidget
from django.contrib.staticfiles.templatetags.staticfiles import static

register = template.Library()


@register.filter
def get_martor_css(dummy):
    return ''.join([f'<link rel="stylesheet" href="{static(x)}">' for x in MartorWidget().Media.css['all']])


@register.filter
def get_martor_js(dummy):
    return ''.join([f'<script src="{static(x)}"></script>' for x in MartorWidget().Media.js])
