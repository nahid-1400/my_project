from pyexpat import model

from django import forms

from contact_us.models import ContactUs


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('user', 'subject', 'message_text')
        widgets = {
            'user': forms.HiddenInput()
                   }