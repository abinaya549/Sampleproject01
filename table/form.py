from django import forms
from .models import MyProject


class EmpForm(forms.ModelForm):
    class Meta:
        model = MyProject
        fields = "__all__"
