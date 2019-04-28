import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "269629907@qq.com"  # 用户名
mail_pass = "qfwdbfpzdkxkbhab"  # 口令
sender = '269629907@qq.com'
receivers = ['807008768@qq.com']
# ***************************************************************
msgRoot = MIMEMultipart()
msgRoot['From'] = Header('Ethan Hao', 'utf-8')
msgRoot['To'] = Header('CHING MOBILE', 'utf-8')
subject = 'New York Daily '
msgRoot['Subject'] = Header(subject, 'utf-8')

mail_msg = """
<p>New York Daily </p>
<p><a href="http://www.baidu.com">Just do it !</a></p>
<p>演示：</p>
<p><img src="cid:image1"></p>
"""

msgRoot.attach(MIMEText(mail_msg, 'html', 'utf-8'))
# 指定图片为当前目录
fp = open('C:/Users/86188/Desktop/PythonTest/t1/w4.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)
# ************************传送文件***************************************
# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('C:/Users/86188/Desktop/PythonTest/t1/foo.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="given.txt"'
msgRoot.attach(att1)
# ***************************************************************
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, msgRoot.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")