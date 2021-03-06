from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.
from martor.models import MartorField


class Tag(models.Model):
    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tag\'s')

    def __str__(self):
        return self.name

    name = models.CharField(max_length=16)


class Links(models.Model):
    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')

    def __str__(self):
        return self.name

    name = models.CharField(
        max_length=255,
        verbose_name=_('Name')
    )

    url = models.URLField(
        verbose_name=_('Url')
    )


class Services(models.Model):
    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.name

    def parents(self):
        return ServicesRelation.objects.get_or_create(children=self)[0].parents

    def children(self):
        return ServicesRelation.objects.filter(parents=self)

    def parents_count(self):
        return self.parents().count()

    def children_count(self):
        return self.children().count()

    service_status = (
        ('IDE', _('Idea')),
        ('IDV', _('In dev')),
        ('DEB', _('Debug')),
        ('COO', _('Сooked')),
    )

    name = models.CharField(
        max_length=255,
        verbose_name=_('Name')
    )

    about = models.TextField(
        max_length=50000,
        verbose_name=_('About')
    )

    authors = models.ManyToManyField(
        to=get_user_model(),
        verbose_name=_('Authors')
    )

    status = models.CharField(
        max_length=3,
        verbose_name=_('Status'),
        choices=service_status
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Date added')
    )

    stars = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Stars')
    )

    tags = models.ManyToManyField(
        to=Tag,
        verbose_name=_("Tag's")
    )


class ServiceAboutPreset(models.Model):
    class Meta:
        verbose_name = 'Preset'
        verbose_name_plural = 'Preset\'s'

    def __str__(self):
        return self.name

    name = models.CharField(
        max_length=255,
        verbose_name=_("Name")
    )
    preset = MartorField(
        max_length=50000,
        verbose_name=_("Preset")
    )


class ServicesRelation(models.Model):
    """
    Service relation parent
    """

    class Meta:
        verbose_name = _('Service relation')
        verbose_name_plural = _('Service relations')

    def __str__(self):
        return self.children.name

    children = models.OneToOneField(
        to=Services,
        on_delete=models.CASCADE,
        verbose_name=_('Children'),
        related_name='Children'
    )

    parents = models.ManyToManyField(
        to=Services,
        verbose_name=_('Parents'),
        related_name='Parents',
        blank=True
    )
