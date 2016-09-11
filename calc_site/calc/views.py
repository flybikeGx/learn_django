from django.shortcuts import render
from django.http import HttpResponse

def add(request):
	return render(request, 'home.html')

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

# Create your views here.
