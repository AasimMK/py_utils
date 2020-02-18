import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# Config emails
from_email = "SENDER"
to_email = "RECIPIENT"

# Compose email
msg = MIMEMultipart()  # instance of MIMEMultipart
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = 'EMAIL SUBJECT'
body = "Body_of_the_mail"
msg.attach(MIMEText(body, 'plain'))

# Attachment
file_name = '<FILENAME_WITH_EXTENSION>'
attachment = open(os.path.join(os.getcwd(), file_name), "rb")
mime_obj = MIMEBase('application', 'octet-stream')
mime_obj.set_payload(attachment.read())  # To change the payload into encoded form
encoders.encode_base64(mime_obj)
mime_obj.add_header('Content-Disposition', "attachment; filename= %s" % file_name)
msg.attach(mime_obj)

# Connection
connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()  # start TLS for security
connection.login(from_email, "<PASSWORD_OR_APP_TOKEN>")
text = msg.as_string()  # Converts the Multipart msg into a string
connection.sendmail(from_email, to_email, text)

# Bye
connection.quit()
