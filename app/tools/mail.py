from cmath import e
from email.message import EmailMessage
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config
from app.order.models import OrderModel
from app.employee.models import EmployeeModel
from datetime import date

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
                
    def order_notification_scheduler(self):
        expired_status = config.EXPIRED_STATUS
        date_now = date.today()
        order_status, order_ids = OrderModel().get_order_expired(
            date=str(date_now),
            status=expired_status
        )
        if not order_status:
            return "Failed to get the order datas"
        
        for order_id in order_ids:
            employee_status, employee_id = EmployeeModel().get_employee_by_id(
                id=order_id.get("employee_id")
            )
            if employee_status:
                emp_id = employee_id.get("id")
                print(f'Send the notification to employee = {emp_id}')
                message = self.msg
                message['To'] = employee_id.get("email")
                self.server.send_message(message)
            
        return "Finish the notification scheduler"
            