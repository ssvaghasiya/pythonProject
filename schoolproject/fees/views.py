from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_python(request):
    return HttpResponse('<h1>Hello Django Fees</h1>')