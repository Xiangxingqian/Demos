# -*- coding: UTF-8 -*-
'''
发送txt文本邮件
小五义：http://www.cnblogs.com/xiaowuyi
'''
import smtplib  
from email.mime.text import MIMEText  
mailto_list=["1027068526@qq.com"] 
mail_host="smtp.qq.com"  #设置服务器
mail_user="412832527@qq.com"    #用户名
mail_pass="qxx1991070918lxh"   #口令 
mail_postfix="qq.com"  #发件箱的后缀
  
def send_mail(to_list,sub,content):  
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host) 
        server.login(mail_user,mail_pass) 
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except SMTPException:  
        return False  
if __name__ == '__main__':  
    if send_mail(mailto_list,"hello","hello world！"):  
        print "success"  
    else:  
        print "fail"  