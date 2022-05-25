from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    now=datetime.now()
    return render(request,"newyear/index.html",{
     "check": True
    })

