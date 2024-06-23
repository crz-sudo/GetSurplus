from ECampusElectricity import ECampusElectricity
from QQemailSend import QQemailSend
config = {
    'shiroJID': '',
    'ymId': ''
}
email = ''
passwd = ''
receiver = ''
ece = ECampusElectricity(config)
name,surplus = ece.get_room_and_surplus()
print(f'房间：{name} 当前余额：{surplus}')
email_sender = QQemailSend(email,passwd,receiver,surplus)
email_sender.send_QQ_email_plain()

