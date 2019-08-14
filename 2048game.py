import pygame as py
from pygame.locals import*
import sys
py.init()
import random
import copy
#列表0置尾算法
def put_0_end(list01):
    list02=[]
    list03=[]
    list04=[]
    for item in list01:
        if item==0:
            list02.append(item)
        else:
            list03.append(item)
    list04 = list03 + list02
    return list04
#2048合成操作
def hecheng(list01):
    list01=put_0_end(list01)
    for i in range(len(list01)-1):
        if list01[i]==list01[i+1]:
            list01[i]=2*list01[i+1]
            list01[i+1]=0
            i+=1
    list02=put_0_end(list01)
    return list02
#屏幕中新出现（不包括叠加后出现的）的数字只可能是2或4，让它们出现的比例是4:1
tuple01=[2,2,2,2,4]
num_game=random.choice(tuple01)
#print(num_game)
#屏幕初始化列表
def init_screen():
    list_init=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    return list_init
#在屏幕的空白处出现一个2或者4
def add_num(list_screen):
    count_0=0
    for item in list_screen:
        num01=item.count(0)
        count_0+=num01
    if count_0==0:
        list_after=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        return list_after
    while True:
        i=random.randint(0,3)
        j=random.randint(0,3)
        if list_screen[i][j]==0:
            list_screen[i][j]=random.choice(tuple01)
            list_after=list_screen
            return list_after
#向左的操作
def left_op(list_left):
    left_op_list=[]
    for item in list_left:
        item01=hecheng(item)
        left_op_list.append(item01)

    return left_op_list
#向右的操作
def right_op(list_right):
    right_op_list=[]
    for item in list_right:
        item.reverse()
        item01=hecheng(item)
        item01.reverse()

        right_op_list.append(item01)

    return right_op_list
#向上的操作
def up_op(up_list):
    list_trun=[]#转换后的临时列表
    for j in range(4):
        list01=[]#临时列表，用来把列换成行
        for i in range(4):
            list01.append(up_list[i][j])
        list01=hecheng(list01)
        list_trun.append(list01)
    #还原列表
    list_trun_2=[]#最后结果列表
    for m in range(4):
        list02=[]#临时列表，用来把行换成列
        for n in range(4):
            list02.append(list_trun[n][m])
        list_trun_2.append(list02)
    return list_trun_2
#向下操作
def down_op(down_list):
    list_trun=[]#转换后的临时列表
    for j in range(4):
        list01=[]#临时列表，用来把列换成行
        for i in range(4):
            list01.append(down_list[i][j])
        list01.reverse()
        list02=hecheng(list01)
        list02.reverse()
        list_trun.append(list02)
    #还原列表
    list_trun_2=[]#最后结果列表
    for m in range(4):
        list02=[]#临时列表，用来把行换成列
        for n in range(4):
            list02.append(list_trun[n][m])
        list_trun_2.append(list02)
    return list_trun_2
#创建一个屏幕
screen=py.display.set_mode((500,500))
myfont = py.font.Font(None, 40)  # 创建一个字体对象
white=255,255,255
blue=0,0,255
screen.fill(white)
#屏幕输出函数，将列表在屏幕上排列
def print_screen(list01):
        pos_int_y=60
        for i in range(4):
            pos_int_x=60
            for item in list01[i]:
                if item==0:
                    str01=""
                else:
                    str01=str(item)

                textImage = myfont.render(str01, True,blue)
                screen.blit(textImage,(pos_int_x,pos_int_y))
                pos_int_x+=110
            pos_int_y+=110

screen01 = init_screen()
screen01 = add_num(screen01)
screen01 = add_num(screen01)

while True:
    for event in py.event.get():
        screen.fill(white)
        pos_rec_y = 20
        for i in range(4):
            pos_rec_x = 20
            for j in range(4):
                py.draw.rect(screen, (0, 0, 255), (pos_rec_x, pos_rec_y, 100, 100), 3)
                pos_rec_x += 110
            pos_rec_y += 110
        print_screen(screen01)
        list_copy = copy.deepcopy(screen01)
        if  event.type == py.QUIT:
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==py.K_UP:
                screen01 = up_op(screen01)
            elif event.key==py.K_DOWN:
                screen01 = down_op(screen01)
            elif event.key==py.K_LEFT:
                screen01 = left_op(screen01)
            elif event.key==py.K_RIGHT:
                screen01 = right_op(screen01)
            else:
                continue

        if screen01 == list_copy:
            continue
        screen01 = add_num(screen01)
    py.display.update()


