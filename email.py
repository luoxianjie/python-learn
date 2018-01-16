import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '2860899420@qq.com'
receivers = 'jiexianluo@hotmail.com'


message = MIMEText('Python...', 'plain', 'utf-8')

message['From'] = Header("test", 'utf-8')
message['To'] =  Header("test", 'utf-8')
message['Subject'] = Header('Python SMTP Test', 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
    smtpObj.login('2860899420@qq.com','pgygvackxgzideih')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("Success")

except smtplib.SMTPException:
    print("Error: Failed")