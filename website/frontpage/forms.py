from django import forms
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from decouple import config
from datetime import datetime, timedelta


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

    def seng_grid_go(self):

        daysUntil = self.cleaned_data["startDate"] - datetime.now().date()

        if daysUntil.days < 3:
            label = 'urgent'
        else:
            label = 'normal'

        customer_email = self.cleaned_data["email"]
        customer_name = self.cleaned_data["name"]

        to_emails = [
            ('kristapsk@gmail.com', 'Default Recipient'),
            (f'{customer_email}', f'{customer_name}'),
        ]

        message = Mail(
            from_email=(
                'service@pieceofcake.solutions', 'Piece of Cake Solutions'),
            to_emails=to_emails,
            subject='Query from pieceofcake.solutions website',
            html_content=f'A new query has been received from <a href="https://pieceofcake.solutions/">pieceofcake.solutions</a><br>' +
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
            is_multiple=True)

        sendgrid_client = SendGridAPIClient(config('SENDGRID_API_KEY'))
        response = sendgrid_client.send(message)
