from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "main/index.html")

def about(request):
    return HttpResponse("Тут будет страница о приюте")

def help(request):
    return HttpResponse("Тут будет страница как помочь приюту")