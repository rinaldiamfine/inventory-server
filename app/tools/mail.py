from cmath import e
from email.message import EmailMessage
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import config
from app.order.models import OrderModel
from app.employee.models import EmployeeModel
from app.product.models import ProductModel
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
        from jinja2 import Environment, FileSystemLoader
        import os
        from datetime import date, datetime
        load_path = os.path.join(config.BASE_PATH, "app", "templates", "email")
        file_load_env = Environment(
            loader=FileSystemLoader(load_path)
        )
        email_template = file_load_env.get_template('email_notification.html')
        
        expired_status = config.EXPIRED_STATUS
        date_now = date.today()
        order_status, order_ids = OrderModel().get_order_expired(
            date=str(date_now),
            status=expired_status
        )
        if not order_status:
            return "Failed to get the order datas"
        
        datas = dict()
        for order_id in order_ids:
            employee_status, employee_ids = EmployeeModel().get_employee_by_id(
                id=order_id.get("employee_id")
            )
            product_status, product_ids = ProductModel().get_product_by_id(
                id=order_id.get("product_id")
            )
            if employee_status and product_status:
                employee_id = employee_ids[0]
                product_id = product_ids[0]
                emp_id = employee_id.get("id")
                order_data = {
                    'email': employee_id.get("email"),
                    'username': employee_id.get("name"),
                    'product_name': product_id.get("name"),
                    'qty': order_id.get('qty'),
                    'loan_date': order_id.get('start_date').strftime("%d-%m-%Y") if order_id.get('start_date') else "",
                    'due_date': order_id.get('end_date').strftime("%d-%m-%Y") if order_id.get('end_date') else ""
                }
                
                if datas.get(str(emp_id)) is not None:
                    datas[str(emp_id)].append(
                        order_data
                    )
                    
                else:
                    datas[str(emp_id)] = [order_data]
        
        for index, vals in datas.items():
            if len(vals) > 0:
                email = vals[0].get('email')
                username = vals[0].get('username').capitalize()
                template_render = email_template.render(
                    {
                        "username": username,
                        "date_returned": str(date.today().strftime("%d-%m-%Y")),
                        "current_year": str(datetime.now().year),
                        "order_ids": vals
                    } 
                )
                
                message = MIMEMultipart()
                message['To'] = email
                message['Subject'] = "Infineon - Expired Loan Notification"
                message['From'] = formataddr(("Inventory Loan", self.user))
                message.attach(MIMEText(template_render, "html"))
                self.server.send_message(message)
        
        return "Finish the notification scheduler"
            