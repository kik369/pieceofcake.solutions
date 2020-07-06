from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from decouple import config


message = Mail(
    from_email='Piece Of Cake Solutions <someone@pieceofcake.solutions>',
    to_emails='kristapsk@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong><br>New line content 😏')
try:
    sg = SendGridAPIClient(config('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
