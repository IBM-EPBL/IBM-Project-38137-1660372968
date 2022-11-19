import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('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'))
from_email = Email("rajierajie465@gmail.com.com")
to_email = To("rajierajie465@gmail.ocm.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)

