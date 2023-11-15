from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def introduction(request):
    return render(request,'introduction.html')

def types_of_nn(request):
    return render(request,'types-of-nn.html')