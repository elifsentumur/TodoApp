from django.forms import ModelForm
from app.models import ProviderModel


class ProviderForm(ModelForm):
    class Meta:
        model = ProviderModel
        fields = ['name']