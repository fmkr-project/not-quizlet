from flask_mail import Mail, Message
from flask import render_template, current_app  
from os import getenv

def load_mail_config(app):
    app.config['MAIL_SERVER'] = getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = int(getenv('MAIL_PORT'))
    app.config['MAIL_USE_TLS'] = getenv('MAIL_USE_TLS') == '1'
    app.config['MAIL_USERNAME'] = getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = getenv('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = getenv('MAIL_DEFAULT_SENDER')    
def create_mail(app=None):
    mail = Mail()
    if app is not None:
        load_mail_config(app)
        mail.init_app(app)
    return mail

my_mail = create_mail()

def send_verification_email(to_email, token):
    with current_app.app_context():  # Use current_app to get the app context
        verification_link = f"https://learnwithpima.fr/verify?token={token}"
        msg = Message("Email Verification", recipients=[to_email])
        msg.html = render_template('mail_verification.html', verification_link=verification_link)
        my_mail.send(msg)
