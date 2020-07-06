from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from decouple import config


def seng_grid_go():

    to_emails = [
        ('kristapsk@gmail.com', 'Default Recipient'),
        ('kik369@live.com', 'Secondary Recipient'),
    ]

    message = Mail(
        from_email=('from@mail.com', 'From Name'),
        to_emails=to_emails,
        subject='Query from pieceofcake.solutions website',
        html_content='A new query has been received from',
        is_multiple=True)

    try:
        sendgrid_client = SendGridAPIClient(config('SENDGRID_API_KEY'))

        response = sendgrid_client.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

seng_grid_go()