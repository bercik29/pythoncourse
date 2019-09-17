#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText

sender = 'admin@example.com'
receiver = 'info@example.com'

msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'admin@example.com'
msg['To'] = 'info@example.com'

user = "0cbeeff8a16832"
password = "f8411eba6b2c6a"

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:

    server.login(user, password)
    server.sendmail(sender, receiver, msg.as_string())
    print("mail successfully sent")