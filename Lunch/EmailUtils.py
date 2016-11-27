'''
Created on Oct. 2016

@author: Jerry
'''
from django.core.mail import send_mail, EmailMessage
import datetime, time
from django.template import loader
from Food.settings import EMAIL_HOST_USER

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