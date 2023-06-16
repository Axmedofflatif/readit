from django import forms

from .models import Cantact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Cantact
        fields = ['full_name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your name'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your emil'
        })
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Subject'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your message'
        })

    def clean(self):
        data = self.cleaned_data
        data['full_name'] = data['full_name'].title()
        data['subject'] = data['subject'].capitalize()
        return data
