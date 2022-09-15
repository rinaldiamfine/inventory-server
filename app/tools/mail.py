from cmath import e
from email.message import EmailMessage
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

class MailManager:
    '''Mail Schedule Manager'''
    def __init__(self):
        self.server = smtplib.SMTP_SSL(config.MAIL_SMTP_SERVER, config.MAIL_SMTP_PORT)
        self.user = config.MAIL_USER
        self.password = config.MAIL_PASSWORD
        self.context = ssl.create_default_context()
        self.user_receive = config.MAIL_USER_RECEIVE

        self.msg = EmailMessage()

        self.is_login = False
        if not self.is_login:
            self.authenticate()
            
        self.setup_content()

    def setup_content(self):
        self.msg['Subject'] = ""
        self.msg['From'] = self.user
        # FOR RECEIVER SET PER SEND
        self.msg.set_content('See below')

    def authenticate(self):
        try:
            self.server.login(self.user, self.password)
            self.is_login = True
            
        except Exception as e:
            print('Something went wrong...', e)
    
    def send_email(self):
        for email in self.user_receive:
            try:
                message = self.msg
                message['To'] = email
                self.server.send_message(message)
            except Exception as e:
                print('Something went wrong...', e)