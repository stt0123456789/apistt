import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from config import *
def send_email(report_file):
    with open(report_file,encoding='utf-8')as f:
        email_body=f.read()
    msg=MIMEMultipart()
    msg.attach(MIMEText(email_body,'html','utf-8'))
    att1=MIMEText(open(report_file,'rb').read(),'base64','utf-8')
    att1["Content-Type"]='application/actet-stream'
    att1["Content-Disposition"]='attachment;filename="report.html"'
    msg.attach(att1)
    try:
        smtp=smtplib.SMTP_SSL('smtp.qq.com')
        smtp.login('2889229108@qq.com','rvpipnavhrrrdced')
        smtp.sendmail('2889229108@qq.com','2889229108@qq.com',msg.as_string())
        logging.info("===============发送邮件成功============")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()
if __name__ == '__main__':
    send_email('../report/report.html')