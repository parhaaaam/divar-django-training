from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView , UpdateView
from django.core.mail import send_mail
from .forms import ContactForm
from . import models


class Contact(CreateView) : 
    form_class = ContactForm
    contact = models.Contact

    # queryset = models.Contact.objects.all()

    template_name = 'contact.html'
    success_url = '/contact/success/'

    def form_valid(self, *args, **kwargs):
        res = super().form_valid(*args, **kwargs)

        contact = self.object

        send_mail(subject=contact.title, message=f"{contact.email}\n{contact.text}", from_email="parhamhohoho@gmail.com", recipient_list=['danial.erfanian@divar.ir'], fail_silently=False)

        return res
    
class Success(TemplateView) : 

    template_name = 'success.html'
    