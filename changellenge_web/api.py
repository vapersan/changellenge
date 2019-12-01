from django.db.models import Q
from django.http import JsonResponse, Http404, HttpResponse
from django.template.defaultfilters import truncatechars_html
from martor.templatetags.martortags import safe_markdown

from . import models


def get_services(request):
    q = request.GET.get('q', '')
    return JsonResponse(
        [
            {
                'id': x.id,
                'name': x.name,
                'about': x.about,
                'about_html': truncatechars_html(safe_markdown(x.about), 100),
                'authors': [{'first_name': y.first_name, 'last_name': y.last_name} for y in x.authors.all()],
                'status': x.status,
                'status_name': [d for d in models.Services.service_status if d[0] == x.status][0][1],
                'date_created': x.date_created,
                'stars': x.stars,
                'parents': [y.id for y in x.parents().all()],
            } for x in models.Services.objects.filter(Q(about__contains=q) | Q(name__contains=q))],
        safe=False,
        json_dumps_params={'ensure_ascii': False}
    )


def get_service(request, id_):
    try:
        x = models.Services.objects.get(id=id_)
    except models.Services.DoesNotExist:
        raise Http404
    return JsonResponse({
        'id': x.id,
        'name': x.name,
        'about': x.about,
        'about_html': safe_markdown(x.about),
        'authors': [{'first_name': y.first_name, 'last_name': y.last_name} for y in x.authors.all()],
        'status': x.status,
        'status_name': [d for d in models.Services.service_status if d[0] == x.status][0][1],
        'date_created': x.date_created,
        'stars': x.stars,
        'parents': [y.id for y in x.parents().all()],
    }, safe=False, json_dumps_params={'ensure_ascii': False})


def get_service_count(request):
    return HttpResponse(str(models.Services.objects.count()))
