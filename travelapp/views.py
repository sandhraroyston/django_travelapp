from django.shortcuts import render
from django.http import HttpResponse
from . models import Place,Team

# Create your views here.
def home(request):
    obj1=Place.objects.all()
    obj2=Team.objects.all()
    return render(request,'index.html',{"result":obj1,"team":obj2})