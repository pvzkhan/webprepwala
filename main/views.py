from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 5}))

def home(request):
    return render(request, 'main/home.html')

def web_design(request):
    return render(request, 'main/web_design.html')

def web_hosting(request):
    return render(request, 'main/web_hosting.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f'Contact Form Submission from {name}'
            full_message = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
            try:
                send_mail(
                    subject,
                    full_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent!')
            except BadHeaderError:
                messages.error(request, 'Invalid header found. Message not sent.')
            except Exception:
                messages.error(request, 'There was an error sending your message. Please try again later.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

def about(request):
    return render(request, 'main/about.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def get_a_quote(request):
    return render(request, 'main/get_a_quote.html')
