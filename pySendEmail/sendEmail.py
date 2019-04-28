import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "269629907@qq.com"  # 用户名
mail_pass = "qfwdbfpzdkxkbhab"  # 口令
sender = '269629907@qq.com'
receivers = ['807008768@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header('Like The Wind', 'utf-8')
message['To'] = Header('风', 'utf-8')
subject = 'New York Daily '
message['Subject'] = Header(subject, 'utf-8')
# 邮件正文内容
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
mail_msg ='New York Daily  '
message.attach(MIMEText(mail_msg, 'base64', 'utf-8'))
# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('C:/Users/86188/Desktop/PythonTest/t1/foo.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")