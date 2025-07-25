import smtplib
from email.mime.text import MIMEText

msg = MIMEText('This is a test email sent via Gmail SMTP.')
msg['Subject'] = 'Test Email'
msg['From'] = 'davudazizov637@gmail.com'
msg['To'] = 'davudazizov637@gmail.com'

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('', '')
    server.send_message(msg)
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send: {e}")

