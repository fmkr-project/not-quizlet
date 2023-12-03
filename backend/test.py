import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP server configuration
smtp_server = 'send.one.com'  # e.g., smtp.gmail.com for Gmail
smtp_port = 587  # For TLS
smtp_username = 'noreply@learnwithpima.fr'
smtp_password = 'pimapassword123'

# Sender's and Receiver's email address
from_email = 'noreply@learnwithpima.fr'
to_email = 'skoukou007@gmail.com'

# Create message
message = MIMEMultipart('alternative')
message['Subject'] = 'Test SMTP Email'
message['From'] = from_email
message['To'] = to_email

# Email body
text = "Hello, this is a test email sent using SMTP."
html = """\
<html>
  <head></head>
  <body>
    <p>Hello, this is a test email sent using SMTP.</p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
message.attach(part1)
message.attach(part2)

# Send email
try:
    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(smtp_username, smtp_password)  # Log in to the server
    server.sendmail(from_email, to_email, message.as_string())  # Send the email
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()  