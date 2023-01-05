# coding=utf-8
# -----------------------------------------------------------------
# ProjectName:      PycharmProjects
# FileName:         send_email.py
# Author:           袁骏翼
# Email:            
# Datetime:         2022/10/13 11:42
# Description:      邮件发送
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，常量大写
# -----------------------------------------------------------------
import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from tools.get_log import GetLog
from config import *

log = GetLog().get_logger()


# 纯文本邮件内容
def send_email():
    # 设置email信息
    text = "第一次发送邮件 hello world!"  # 配置邮件内容
    message = MIMEText(text, "plain", "utf-8")
    message["Subject"] = 'frist send email...'  # 邮件主题
    message['from'] = sender  # 发送方信息
    message['to'] = ",".join(receivers)  # 接收方信息
    # 构造附件
    message = MIMEMultipart()
    message["Subject"] = 'frist send email...'  # 邮件主题
    message['from'] = sender  # 发送方信息
    message['to'] = ",".join(receivers)  # 接收方信息
    text = "本轮测试报告详情请见附件！"
    message.attach(MIMEText(text, "plain", "utf-8"))  # 纯文本邮件内容定义通过MIMEText操作

    filepath = DIR_PATH + os.sep + 'report' + os.sep + 'report.html'
    with open(filepath, "r", encoding="utf-8") as f:  # 读取文件
        content = f.read()
    att1 = MIMEText(content, "plain", "utf-8")  # 构造附件，读取文件
    att1["Content-Type"] = 'application/octet-stream'  # 设置格式
    att1["Content-Disposition"] = 'attachment; filename="report.html"'
    message.attach(att1)
    # 发送邮件
    try:
        smtp = smtplib.SMTP()  # 登录并发送邮件
        smtp.connect(mail_host, port=25)  # 连接服务器
        smtp.login(mail_user, mail_pwd)  # 登录服务器
        smtp.sendmail(sender, receivers, message.as_string())  # 发送
        smtp.quit()  # 退出
        log.info("发送成功，请到邮箱查看邮件！")
        print("发送成功，请到邮箱查看邮件！")
    except smtplib.SMTPException as e:
        log.info("发送失败：", e)
        print("发送失败：", e)


if __name__ == '__main__':
    send_email()
