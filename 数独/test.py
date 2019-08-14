# -*- coding:utf-8 -*-
import wx
import copy
import 数独
import 数独数据
data_all_op=copy.deepcopy(数独数据.data_all)
#主窗口类
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent,id, title="数独游戏",size=(600,600))
        #创建面板
        panel = wx.Panel(self)

        #创建“确定”和“取消”按钮
        self.bt_easy = wx.Button(panel,label='简单等级',pos=(105,130),size=(200,60))
        self.bt_normal  = wx.Button(panel,label='普通等级',pos=(105,200),size=(200,60))
        self.bt_hard = wx.Button(panel, label='困难等级', pos=(105, 270), size=(200, 60))

        but_tuple=(self.bt_easy,self.bt_normal,self.bt_hard)
        for item in range(len(but_tuple)-1):

            but_tuple[item].Bind(wx.EVT_BUTTON,self.Onclick(list_fram=data_all_op[item]))
            # but_tuple[item].Bind(wx.EVT_BUTTON,self.Onclick)
#传参list_frame,是否成功有待考证
    def Onclick(self,list_fram):
        if __name__ == '__main__':
            app = wx.App()  # 初始化
            frame_sle = slect_frame(parent=None, id=-1,data02=list_fram)  # 实例MyFrame类，并传递参数
            # frame_sle.data02=list_fram
            frame_sle.Show()  # 显示窗口
            app.MainLoop()  # 调用主循环方法


#选择关卡界面类
class slect_frame(wx.Frame):
    def __init__(self, parent, id,data02):
        self.data02=data02
        wx.Frame.__init__(self, parent, id, title="数独游戏", size=(600, 600))
        # 创建面板
        panel = wx.Panel(self)
        # 创建文本和密码输入框
        self.title = wx.StaticText(panel, label="请选择关卡", pos=(140, 50))
        font = wx.Font(20, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        self.title.SetFont(font)

        # 创建“选择关卡”按钮
        init_x = 105
        init_y = 130  # 第一个按钮的位置
        list_button_num = []
        for num01 in range(1, 10):
            self.button_num = wx.Button(panel, label=str(num01), pos=(init_x, init_y), size=(70, 70))
            # self.bt_2  = wx.Button(panel,label='2',pos=(205,130),size=(70,70))
            list_button_num.append(self.button_num)
            init_x += 100
            if init_x == 405:
                init_x = 105
                init_y += 105
        for item in range(len(list_button_num)-1):
            list_button_num[item].Bind(wx.EVT_BUTTON,self.onclick_level(list_level=data02[item]))
    def onclick_level(self, list_level):
        if __name__ == '__main__':
            app = wx.App()  # 初始化
            frame_sle = slect_level_frame(parent=None, id=-1,data01=list_level)  # 实例MyFrame类，并传递参数
            frame_sle.Show()  # 显示窗口
            app.MainLoop()  # 调用主循环方法

#数独游戏界面
class slect_level_frame(wx.Frame):
    def __init__(self,parent,id,data01):
        self.data01=data01
        wx.Frame.__init__(self, parent,id, title="数独游戏",size=(600, 600))
        #创建面板
        panel = wx.Panel(self)

        self.con_data = wx.Button(panel, label=str("提交结果"), pos=(495, 200), size=(80, 40))

        #创建数列排列的按钮
        init_x=50
        init_y=50#第一个按钮的位置
        list_l=[]
        list_m=[]
        list_text=[]
        for num02 in range(9):
            list_l = []
            for num01 in range(9):


                if data01[num02][num01]!=0:

                    rec_num=data01[num02][num01]
                    self.button_num = wx.Button(panel, label=str(rec_num), pos=(init_x, init_y), size=(40, 40))
                    self.button_num.SetBackgroundColour("#FFCC66")  # 设置按钮背景颜色
                    list_l.append(rec_num)
                else:
                    self.text_put_num = wx.TextCtrl(panel, pos=(init_x, init_y), size=(40, 40))
                    # put_num_value = self.text_put_num.GetValue()
                    list_text.append(self.text_put_num)
                    list_l.append(0)



                init_x+=45
                if init_x==185:
                    init_x=190
                if init_x==325:
                    init_x=330
                if init_x==465:
                    init_x=50
                    init_y+=45
                if init_y == 185:
                    init_y = 190
                if init_y == 325:
                    init_y = 330
            list_m.append(list_l)
        # self.con_data.Bind(wx.EVT_BUTTON, self.on_click)
        def on_click(self):
            list_k=copy.deepcopy(list_m)
            num_list=0
            for i in range(9):
                if list_text[num_list].GetValue() not in("1","2","3","4","5","6","7","8","9"):
                    break
                for j in range(9):
                    if  list_k[i][j]==0:
                        list_k[i][j]=int(list_text[num_list].GetValue())
                        num_list+=1
            if 数独.check_list(list_k)==True:
                message="恭喜你过关了"
            else:
                message="有错误，请仔细检查"
            wx.MessageBox(message)

                # print(list_k)

        self.con_data.Bind(wx.EVT_BUTTON,on_click )

if __name__ == '__main__':
    app = wx.App()                      # 初始化
    frame_init = MyFrame(parent=None,id=-1)  # 实例MyFrame类，并传递参数
    # frame_sle = slect_frame(parent=None, id=-1)
    frame_init.Show()                        # 显示窗口
    app.MainLoop()                      # 调用主循环方法

