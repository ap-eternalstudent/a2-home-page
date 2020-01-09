from django import forms
from django.core.mail import send_mail

from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaHiddenInput


class ContactsForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaHiddenInput())
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Name'}),
        max_length=50,
        min_length=2,
        required=True
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Email'}),
        max_length=50,
        required=True
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Subject'}),
        max_length=100,
        min_length=3,
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter Your Message...'}),
        max_length=500,
        min_length=20,
        required=True
    )

    def send_email(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        recipients = ['hello@wearea2.com']

        subject = '%s from %s' % (subject, name)
        send_mail(subject, message, email, recipients)
