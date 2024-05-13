import smtplib
from email.mime.text import MIMEText
msg=MIMEText("我是测试邮件的正文",'plain','utf-8')
msg['From']='2889229108@qq.com'
msg['To']='2889229108@qq.com'
msg['Subject']='接口测试报告主题'
smtp=smtplib.SMTP_SSL('smtp.qq.com')
smtp.login('2889229108@qq.com','rvpipnavhrrrdced')
smtp.sendmail('2889229108@qq.com','2889229108@qq.com',msg.as_string())
smtp.quit()