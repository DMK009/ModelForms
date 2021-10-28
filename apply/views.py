from django.forms.forms import Form
from django.shortcuts import render
from apply.forms import *


# Create your views here.
def homeviews(request):
    con={}
    form=helloforms(request.POST)
    # if form.is_valid():
    form.save()
    con['form']=form
    return render(request,'home1.html',con)
