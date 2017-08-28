# coding=utf-8
import smtplib
import time
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import Config
from log import logger

CONFIG = Config()
SMTP = CONFIG.get('mail', 'smtp')
PASSWORD = CONFIG.get('mail', 'password')
SENDER = CONFIG.get('mail', 'sender')
RECEIVER = CONFIG.get('mail', 'receiver')
SUBJECT = CONFIG.get('mail', 'subject')
MESSAGE = CONFIG.get('mail', 'message')
ATTACH = CONFIG.get('mail', 'attach')


class Mail:
    """
    邮件类，提供发送邮件的方法
    """
    def __init__(self, smtp=SMTP, sender=SENDER, password=PASSWORD, receiver=RECEIVER, subject=SUBJECT, message=MESSAGE, attach=ATTACH):
        self.msg = MIMEMultipart('related')
        self.smtp = smtp
        self.sender = sender
        self.receiver = receiver
        self.password = password
        self.subject = subject
        self.message = message
        self.attach = attach

    def _attach_file(self, att_file):
        """将单个文件添加到附件列表中"""
        att = MIMEText(open('%s' % att_file, 'rb').read(), 'html', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]
        self.msg.attach(att)
        logger.info('attach file {}'.format(att_file))

    def send(self):
        self.msg['from'] = self.sender
        self.msg['to'] = self.receiver
        self.msg['Subject'] = self.subject
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        # 邮件正文
        # if self.message:
        #     self.msg.attach(MIMEText(self.message, 'plain', 'utf-8'))
        if self.attach:
            with open(self.attach, 'rb') as f:
                self.msg.attach(MIMEText(f.read(), 'html', 'utf-8'))

        # 添加附件，支持多个附件（传入list），或者单个附件（传入str）
        if self.attach:
            if isinstance(self.attach, list):
                for f in self.attach:
                    self._attach_file(f)
            elif isinstance(self.attach, str):
                self._attach_file(self.attach)

        logger.debug(self.msg.as_string())

        # 连接服务器，发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp)
        smtp.login(self.sender, self.password)
        smtp.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())
        smtp.quit()
        logger.info('email has send to %s successfully!', self.receiver)


if __name__ == '__main__':
    Mail().send()
