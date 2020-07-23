from django import forms
from django.core.mail import send_mail
from decouple import config
from datetime import datetime, timedelta
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    phone = forms.CharField(max_length=30, required=True)
    collectionPostcode = forms.CharField(max_length=10, required=True)
    deliveryPostcode = collectionPostcode = forms.CharField(
        max_length=10, required=False)
    startDate = forms.DateField(required=False)
    jobType = forms.ChoiceField(choices=([('Home move', 'Home move'), (
        'Office move', 'Office move'), ('Handyman services', 'Handyman services')]), required=True)
    details = forms.CharField(widget=forms.Textarea, required=False)
    captcha = ReCaptchaField(widget=ReCaptchaV3(attrs={'data-badge': 'bottomleft'}))

    def seng_grid_go(self):

        daysUntil = self.cleaned_data["startDate"] - datetime.now().date()

        if daysUntil.days < 14:
            label = 'urgent'
        else:
            label = 'normal'

        send_mail(
            # subject
            'Query from pieceofcake.solutions website',

            # message
            f'',

            # from
            f'peter@pieceofcake.solutions.com',

            # to
            [config('DEFAULT_TO_EMAIL'), f'{self.cleaned_data["email"]}'],

            html_message=f'A new query from <a href="https://pieceofcake.solutions/">pieceofcake.solutions</a> has been received<br>' +
            f'These are the details:<br><br>' +
            f'<strong>Name:</strong> {self.cleaned_data["name"]}<br>' +
            f'<strong>Email:</strong> {self.cleaned_data["email"]}<br>' +
            f'<strong>Phone:</strong> {self.cleaned_data["phone"]}<br>' +
            f'<strong>Collection post code:</strong> {self.cleaned_data["collectionPostcode"]}<br>' +
            f'<strong>Delivery post code:</strong> {self.cleaned_data["deliveryPostcode"]}<br>' +
            f'<strong>Would like to commence the job on:</strong> {self.cleaned_data["startDate"].strftime("%A, %d %B, %Y")} (in {daysUntil.days} days)<br>' +
            f'<strong>Job type:</strong> {self.cleaned_data["jobType"]}<br>' +
            f'<strong>Label:</strong> {label}<br>' +
            f'<strong>Optional details:</strong> {self.cleaned_data["details"]}',
            fail_silently=False,
        )
