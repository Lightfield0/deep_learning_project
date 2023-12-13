from django.shortcuts import render
from .models import TeamMember

# Create your views here.

def home(request):
    return render(request, 'home.html')

def introduction(request):
    return render(request,'introduction.html')

def types_of_nn(request):
    return render(request,'types-of-nn.html')

def about_us(request):
    members = TeamMember.objects.all()
    return render(request,'about_us.html', {'members': members})

def how_it_works(request):
    return render(request, 'how_it_works.html')