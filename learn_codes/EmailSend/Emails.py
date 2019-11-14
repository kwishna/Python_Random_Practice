import smtplib

sender = "attidudek@gmail.com"
recipient = "dtmawani@yandex.com"
password = "" # Your SMTP password for Gmail
subject = "Test email from Python"
text = "Hello from Python"

smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

smtp_server.login(sender, password)
message = "Subject: {}\n\n{}".format(subject, text)
smtp_server.sendmail(sender, recipient, message)
smtp_server.close()