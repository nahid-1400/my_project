from django.shortcuts import render
from django.views.generic import CreateView
from .models import ContactUs
from .forms import ContactForm
from django.urls import reverse_lazy
from account.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class Contact(CreateView):
    template_name = 'contact/contact.html'
    model = ContactUs
    form_class = ContactForm
    success_url = reverse_lazy('contact:success-contact')

    def form_valid(self, form_class):
        return form_class(initial={'user': self.request.user})


def success_send_message_contact(request):
    return render(request, 'contact/success_send_message_contact.html')