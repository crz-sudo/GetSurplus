#邮件发送类
import smtplib
import time
from email.mime.text import MIMEText
class QQemailSend:
    def __init__(self,sender,passwd,receiver,surplus):
        self.sender = sender
        self.passwd = passwd
        self.surplus = surplus
        self.receiver = receiver
    def send_QQ_email_plain(self):
        sender = user = self.sender  
        receiver = self.receiver     
        msg = MIMEText(f'你的电费余额为 {self.surplus},请及时充值', 'plain', 'utf-8')
        msg['From'] = f'nickname <emailaddress@qq.com>' #emailaddress为发送邮箱
        msg['To'] = receiver
        msg['Subject'] = '电费余额低'         
        try:
            smtp = smtplib.SMTP_SSL('smtp.qq.com', 465)
            smtp.login(user, passwd)
            smtp.sendmail(sender, receiver, msg.as_string())
            print('邮件发送成功')
            smtp.quit()
        except Exception as e:
            print(e)
            print('发送邮件失败')