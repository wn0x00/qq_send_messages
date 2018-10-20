# 原理是先将需要发送的文本放到剪贴板中，然后将剪贴板内容发送到qq窗口
# 之后模拟按键发送enter键发送消息

import win32gui
import win32con
import win32clipboard as w
import time
import threading

class SendMessage:
    to_who =''
    msg=''

    def __init__(self,t,m):
        self.to_who = t
        self.msg = m

    def getText(self):
        """获取剪贴板文本"""
        w.OpenClipboard()
        d = w.GetClipboardData(win32con.CF_UNICODETEXT)
        w.CloseClipboard()
        return d

    def setText(self):
        """设置剪贴板文本"""
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT,self.msg)
        w.CloseClipboard()

    def send_qq(self):
        """发送qq消息
        to_who：qq消息接收人
        msg：需要发送的消息
        """
        # 将消息写到剪贴板
        self.setText()
        # 获取qq窗口句柄
        qq = win32gui.FindWindow(None, self.to_who)
        # 投递剪贴板消息到QQ窗体
        win32gui.SendMessage(qq, 258, 22, 2080193)
        win32gui.SendMessage(qq, 770, 0, 0)
        # 模拟按下回车键
        win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    # def display(self):
    #     print(self.to_who)
        
if __name__ =='__main__':
    num=0
    #msg：你想输入的消息
    msg=''
    #to_who_x: 用于qq的消息窗口
    to_who_1 = ""
    to_who_2 =""
    m1 = SendMessage(to_who_1,msg)
    m2 = SendMessage(to_who_2,msg)

    while True:
        t1= threading.Thread(target= m1.send_qq())
        t2= threading.Thread(target= m2.send_qq())

        t1.start
        t1.join
        t2.start
        t2.join
        print(num)
        num=num+1
        time.sleep(30)