from django import  forms
from django.db.models import fields
from apply.models import *
class helloforms(forms.ModelForm):
    class Meta:
        model=hello
        fields="__all__"