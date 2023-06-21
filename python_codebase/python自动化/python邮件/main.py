import smtplib  # 发送邮件
from email.mime.text import MIMEText  # 邮件文本


class SendMail:
    def __init__(self, SMTP_server: str, port: int, Sender: str, Password: str):
        """

        :param SMTP_server: smtp服务器
        :param port: 端口
        :param Sender: 用户名
        :param Password: 密码（生成的授权密码）
        """
        self.SMTP_server = SMTP_server
        self.port = port
        self.Sender = Sender  # 发件人邮箱
        self.Password = Password  # 密码为授权码，在设置-SMTP-开启后会显示

    def send(self, Receiver: str, title: str, test: str):
        """

        :param Receiver: 收件人
        :param title: 标题
        :param test: 内容
        :return:
        """
        message = MIMEText(test)  # 邮件文本

        message['Subject'] = title  # 邮件标题
        message['From'] = self.Sender  # 发送者
        message['To'] = Receiver  # 接收者

        mail_server = smtplib.SMTP(self.SMTP_server, self.port)  # 连接端口
        mail_server.login(self.Sender, self.Password)  # 登录
        mail_server.sendmail(self.Sender, Receiver, message.as_string())  # 发送邮件
        mail_server.quit()
        print('发送成功')


my_send = SendMail('smtp.163.com', 25, 'xxx@163.com', 'JUBMSUDZGUxxxxxx')
my_send.send('xxx@qq.com', '标题测试', '内容测试')
