#!/usr/bin/python
#coding=UTF-8
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import utils, encoders

class FILEMISSERROR(StandardError):
    pass

class EMAILGENERATOR(object):
    '''

    '''
    def __init__(self, emailsettings = {"SmtpServer": "10.100.98.82", "FromAddr": "", "ToAddr": "", "CcAddr": "", "Subject": ""}):

        self.smtp_server = emailsettings["SmtpServer"]
        self.from_addr = emailsettings["FromAddr"]
        self.to_addr = emailsettings["ToAddr"]
        self.cc_addr = emailsettings["CcAddr"]
        self.subject = emailsettings["Subject"]

        self.msg = MIMEMultipart()
        self.msg['To'] = self.to_addr.replace(' ', '')
        self.msg['From'] = "<" + self.from_addr + ">"
        self.msg['Cc'] = self.cc_addr.replace(' ', '')
        self.msg['Subject'] = self.subject
        self.msg['Date'] = utils.formatdate(localtime=1)
        self.msg['Message-ID'] = utils.make_msgid()

    def send_email(self, email_body, all_result_files = None):
        '''

        '''
        body = MIMEText(email_body, _subtype='html', _charset='utf-8')
        self.msg.attach(body)

        #files = ['mime_get_basic.py']
        if all_result_files is not None:
            for filename in all_result_files:
                self.msg.attach(self._attachment(filename))

        self.s = smtplib.SMTP(self.smtp_server)
        """
        self.s = smtplib.SMTP()
        self.s.connect(self.smtp_server)
        self.s.login("hanyulong8888", "wshylwshyl")
        """
        sent_list=[]
        to_addr_list = self.msg['To'].split(';')

        # currently, we should send one by one, batch send will failed
        self.s.sendmail(self.msg['From'], to_addr_list, self.msg.as_string())
        sent_list.extend(to_addr_list)

        if self.msg['Cc'] not in ['',' ']:
            cc_addr_list = self.msg['Cc'].split(';')
            for cc_addr in cc_addr_list:
                if cc_addr not in sent_list:
                    self.s.sendmail(self.msg['From'], cc_addr, self.msg.as_string())
                    sent_list.append(cc_addr)

        print "sent to %s" %str(sent_list)
        self.s.close()

    def _attachment(self, filename):
        '''
        build attachment object
        '''
        fd = open(filename, 'rb')

        mimetype, mimeencoding = mimetypes.guess_type(filename)
        if mimeencoding or (mimetype is None):
            mimetype = 'application/octet-stream'

        maintype, subtype = mimetype.split('/')

        if maintype == 'text':
            retval = MIMEText(fd.read(), _subtype=subtype)
        else:
            retval = MIMEBase(maintype, subtype)
            retval.set_payload(fd.read())
            encoders.encode_base64(retval)

        retval.add_header('Content-Disposition', 'attachment',
                          filename=filename.split('/')[-1])
        fd.close()

        return retval


if __name__ == "__main__":

    f = "Hello,world"
    email = EMAILGENERATOR({"SmtpServer": "10.100.98.82", "FromAddr": "jizhong@infinera.com", "ToAddr": "jizhong@infinera.com", "CcAddr": "", "Subject": "Test Driver"})
    email.send_email(f)


