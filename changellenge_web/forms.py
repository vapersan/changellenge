from django import forms
from martor.fields import MartorFormField
from martor.widgets import MartorWidget

from changellenge_web.models import Services, ServicesRelation


class AddServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ('name', 'about', 'authors', 'tags')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['about'].widget = MartorWidget(self.fields['about'].widget.attrs)

    parents = forms.ModelMultipleChoiceField(
        queryset=ServicesRelation.objects.all()
    )
