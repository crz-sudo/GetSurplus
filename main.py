from ECampusElectricity import ECampusElectricity
from QQemailSend import QQemailSend
config = {
    'shiroJID': '249c8c01-256d-4395-9816-86fefb754652',
    'ymId': '2309636210585927691'
}
email = '313057554@qq.com'
passwd = 'mrpusfmtwyiybhjc'
receiver = '313057554@qq.com'
ece = ECampusElectricity(config)
name,surplus = ece.get_room_and_surplus()
print(f'房间：{name} 当前余额：{surplus}')
email_sender = QQemailSend(email,passwd,receiver,surplus)
#email_sender.send_QQ_email_plain()

