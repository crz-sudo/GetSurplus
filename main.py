from ECampusElectricity import ECampusElectricity
from QQemailSend import QQemailSend
config = {
    'shiroJID': '',
    'ymId': ''
}
email = '' #发送邮箱
passwd = ''#邮箱授权码
receiver = ''#接收邮箱
ece = ECampusElectricity(config)
name,surplus = ece.get_room_and_surplus()
print(f'房间：{name} 当前余额：{surplus}')
if surplus <= 50:
    email_sender = QQemailSend(email,passwd,receiver,surplus)
    email_sender.send_QQ_email_plain()

