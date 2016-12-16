'''
Created on Oct. 2016

@author: Jerry
'''
from django.core.mail import send_mail, EmailMessage
import datetime, time
from django.template import loader
from Food.settings import EMAIL_HOST_USER

from .emailgenerator import EMAILGENERATOR

def notify_superadmin(admin, message):
    '''
    send the message to super admin
    '''
    
    
def notify_admin(admin, message_dict):
    '''
    send the message to admin, generally is the daily summary of today's lunch
    '''
    subject = time.strftime('%Y-%m-%d',time.localtime(time.time())) + " Lunch Order Summary"
    
    message_dict['name'] = subject
    html_content = loader.render_to_string('email_template.html', message_dict)
    print admin
    print html_content
    
    msg = EmailMessage(subject, html_content, EMAIL_HOST_USER, [admin])
    msg.content_subtype = "html" # Main content is now text/html
    msg.send()
    #send_mail(subject, messages, 'zhaoyin0811@126.com',[admin])


def notify_order_state_to_user(mail_to, user, order_state):
    """
    Send an email to the user to notify the order state.
    """
    if not mail_to:
        return False

    subjuct = "Your order state is [%s]" % order_state
    
    content = "Dear %s,<br/><br/>" % user
    wel_str = """
            Our Happy Lunch Order System is coming.<br/>
            Welcome to visit the amazing website http://10.220.43.58:8000/lunch/ to enjoy.<br/>
            Have a try, and vote for us!<br/>
            Your future convenience is depending on your hands!<br/>
    """

    if order_state == "Submitted":
#         content = content + "Thanks for submitting the meal."
        content = content + wel_str
    elif order_state == "Canceled":
        content = content + "Your meal order has been canceled."
    elif order_state == "Confirmed":
        content = content + "Your meal has been delivered, please wait patiently."
    elif order_state == "Food Ready":
        content = content + "Your meal is ready, please come to bring."
    elif order_state == "Finished":
        content = content + "Your meal order is completed, welcome for your next use."
    else:
        content = None
    
    if content:
        content = content + "<br/><br/>Best regards,<br/>Happy Lunch Team"

    mail_obj = EMAILGENERATOR({"SmtpServer": "10.100.98.82", "FromAddr": "JuanZhang@infinera.com", "ToAddr": mail_to, "CcAddr": "", "Subject": subjuct})
    mail_obj.send_email(content)