from flask_mail import Mail, Message
from flask import current_app, render_template

mail = Mail()

def configure_mail(app):
    mail.init_app(app)

def send_email(subject, recipient, template, **kwargs):
    msg = Message(subject, recipients=[recipient], 
                  html=render_template(template, **kwargs),
                  sender=current_app.config['MAIL_DEFAULT_SENDER'])
    mail.send(msg)
