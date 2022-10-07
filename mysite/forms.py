from .models import message
from django.forms import ModelForm


class messageFrom(ModelForm):
    class Meta:
        model = message
        fields = ['sender', 'recipient', 'title', 'full_text']