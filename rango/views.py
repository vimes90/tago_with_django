from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello world! <br> <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango says: This is the about page!")