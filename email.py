import os
import smtplib
from email.message import EmailMessage
from token import email_host, token

def send_email():
    EMAIL_ADDRESS= email_host
    EMAIL_PASSWORD= token

    msg = EmailMessage()
    msg['Subject'] = 'Teste de email Script'
    msg['From']='gguedes10@gmail.com'
    msg['To']='gabriel.guedes@zerum.com'
    msg.set_content('Email teste, se vc está lendo essa msg o envio dela foi um sucesso!')

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

