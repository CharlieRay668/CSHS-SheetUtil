import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "attendanceinformation@gmail.com"
receiver_email = "ebnewson01@bvsd.org"
password = "makeSureToRememberthePassword1256801.?.?.?1!"

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email
message["BCC"] = receiver_email
text = """\
This is an email to test my program for auto emails
"""

part1 = MIMEText(text, "plain")

message.attach(part1)
filename = 'percentageattended.csv'
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)
text = message.as_string()
message.attach(part)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
