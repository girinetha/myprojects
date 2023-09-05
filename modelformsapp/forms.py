from django import forms
from modelformsapp import models
class projectform(forms.ModelForm):
    class Meta:
        model=models.project
        fields='__all__'