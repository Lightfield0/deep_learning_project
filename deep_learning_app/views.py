from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TeamMember, Contact
from .forms import ContactForm

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

def deep_learning_projects(request):
    return render(request, 'deep_learning_projects.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Form verilerini kaydet
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            # Kullanıcıya başarılı mesajı göster
            messages.success(request, 'Mesajınız başarıyla gönderildi!')
            # Formu sıfırla
            return redirect('contact')  # 'contact' burada URL adıdır
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})