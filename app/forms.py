from django import forms
from app.models.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)