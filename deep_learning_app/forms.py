from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Adınız')
    email = forms.EmailField(label='E-posta Adresiniz')
    message = forms.CharField(widget=forms.Textarea, label='Mesajınız')
