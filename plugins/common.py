import smtplib
from email.mime.text import MIMEText

# # Email details
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# username = 'fshi7418@gmail.com'  # Replace with your email
# app_password = 'icpurjpmfcdhskii'  # Replace with your app password
# to_email = 'fshi7419@gmail.com'  # Replace with the recipient's email
# subject = 'Test Email'
# body = 'This is a test email sent from Python.'


def send_email_smtp(host, user, pw, recipients, subject, body, cc=None, bcc=None):
    recipients = ['fshi7419@gmail.com', 'fshi7418@hotmail.com']
    ret = True
    # Create the email
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = recipients
    if cc is not None:
        msg['Cc'] = cc
    if bcc is not None:
        msg['Bcc'] = bcc

    try:
        with smtplib.SMTP(host, 587) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(user, pw)
            server.sendmail(user, recipients, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
        ret = False
    finally:
        return ret
