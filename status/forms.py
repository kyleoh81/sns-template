from django import forms
from django.utils.html import strip_tags

from .models import Status


class StatusForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(attrs={
            "placeholder": "Status",
            "class": "form-control",
            "rows": 5,
            "style": "resize: none;"}))

    class Meta:
        model = Status
        exclude = ("user", )

