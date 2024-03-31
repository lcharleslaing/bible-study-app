from django import forms
from .models import BibleStudy


class BibleStudyForm(forms.ModelForm):
    class Meta:
        model = BibleStudy
        fields = ["title"]  # Exclude the 'user' field; it will be set in the view
