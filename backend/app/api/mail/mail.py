import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import render_template, current_app
from os import getenv
FLASK_URI = getenv("FLASK_HOST")+getenv("FLASK_PORT")
def load_mail_config():
    mail_config = {
        'MAIL_SERVER': getenv('MAIL_SERVER'),
        'MAIL_PORT': int(getenv('MAIL_PORT', 587)),
        'MAIL_USE_TLS': getenv('MAIL_USE_TLS') == '1',
        'MAIL_USERNAME': getenv('MAIL_USERNAME'),
        'MAIL_PASSWORD': getenv('MAIL_PASSWORD'),
        'MAIL_DEFAULT_SENDER': getenv('MAIL_DEFAULT_SENDER')
    }
    return mail_config

# Additional import for app context
from flask import current_app

def send_mail(to_email, subject, template, **kwargs):
    # Fetch the configuration inside the application context
    with current_app.app_context():
        config = load_mail_config()
        server = smtplib.SMTP(config['MAIL_SERVER'], config['MAIL_PORT'])
        server.starttls()
        server.login(config['MAIL_USERNAME'], config['MAIL_PASSWORD'])
        msg = MIMEMultipart()
        msg['From'] = config['MAIL_DEFAULT_SENDER']
        msg['To'] = to_email
        msg['Subject'] = subject
        # Render the template within the application context
        html_content = render_template(template, **kwargs)
        msg.attach(MIMEText(html_content, 'html'))
        server.send_message(msg)
        server.quit()

def send_verification_email(to_email, token):
    verification_link = f"{FLASK_URI}/verify?token={token}"
    send_mail(to_email, "Email Verification", 'mail_verification.html', verification_link=verification_link)

def send_reset_password_email(to_email, token):
    verification_link = f"{FLASK_URI}/reset_password?token={token}"
    send_mail(to_email, "Password Reset Request", 'password_reset.html', password_reset_link=verification_link)