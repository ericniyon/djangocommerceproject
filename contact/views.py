from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.
def contact(request):
    title = 'Contact'
    form = ContactForm(request.POST or None)
    confrm_message = None
    if form.is_valid():
        name = form.cleaned_data['name']
        comments = form.cleaned_data['comments']
        subject = 'Message from MYSITE.com'
        message = '%s %s' %(comments, name)
        email_from = form.cleaned_data['email']
        email_to = [settings.EMAIL_HOST_USER]
        send_mail(subject,message,email_from, email_to, fail_silently=False,)
        title = 'Thanks'
        confrm_message= 'Thanks for mailing me .'
        form = None
    context = {'title': title, 'form': form, 'confrm_message':confrm_message}

   
    template = 'contact.html'
    return render(request, template, context)