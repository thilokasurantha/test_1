from django.shortcuts import render

# Create your views here.

def printname(request) :
    return render(request, "index.html")