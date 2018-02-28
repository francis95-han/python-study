#coding:utf-8
#不知道为什么啊  python用qq邮箱发送邮箱不行啊
# smtplib.SMTPSenderRefused: (503, 'Error: need EHLO and AUTH first !', '352049215@qq.com')
# 提示要获取权限什么的
__author__ = 'ZhangBohan'

from smtplib import  SMTP
from poplib import  POP3
from time import sleep

SMTPSVR ='smtp.qq.com'
POP3SVR = 'pop.qq.com'

origHdrs=['From:352049215@qq.com','To: 352049215@qq.com','Subject:test mail']
origBody = ['xxx','yyy','zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs),'\r\n'.join(origBody)])

sendSvr = SMTP(SMTPSVR)
errs = sendSvr.sendmail('352049215@qq.com',('352049215@qq.com'),origMsg)
sendSvr.quit()
assert len(errs)==0,errs
sleep(10)

recvSVR = POP3(POP3SVR)
recvSVR.user('352049215')
recvSVR.pass_('')    # ''内的事你的email的密码
rsp,msg,siz= recvSVR.retr(recvSVR.stat()[0])
sep = msg.index('')
recvBody = msg[sep+1:]
assert origBody==recvBody

