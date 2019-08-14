import pygame as py
import sys
import time
from pygame.locals import*
import  random
py.init()
#画出主屏幕
screen=py.display.set_mode((500,700))
myfont = py.font.Font(None, 40)  # 创建一个字体对象
white=255,255,255
blue=0,0,255
screen.fill(white)
list_op=[[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],]
def list_generate(int01, int02):


    list_all_rect = [[[(int01 + 1, int02 - 2), (int01 + 1, int02 - 1), (int01, int02), (int01 + 1, int02)],
                      [(int01 - 1, int02), (int01, int02), (int01 + 1, int02), (int01 + 1, int02 + 1)],
                      [(int01, int02 - 1), (int01 + 1, int02 - 1), (int01, int02), (int01, int02 + 1)],
                      [(int01 - 1, int02 - 1), (int01 - 1, int02), (int01, int02), (int01 + 1, int02)]],

                     [[(int01 + 1, int02 - 1), (int01, int02), (int01 + 1, int02), (int01, int02 + 1)],
                      [(int01 - 1, int02 - 1), (int01, int02 - 1), (int01, int02), (int01 + 1, int02)],
                      [(int01 + 1, int02 - 1), (int01, int02), (int01 + 1, int02), (int01, int02 + 1)],
                      [(int01 - 1, int02 - 1), (int01, int02 - 1), (int01, int02), (int01 + 1, int02)]],
                     [[(int01 + 1, int02 - 1), (int01, int02), (int01 + 1, int02), (int01 + 1, int02 + 1)],
                      [(int01, int02), (int01 + 1, int02), (int01 + 2, int02), (int01 + 1, int02 + 1)],
                      [(int01 + 1, int02 - 1), (int01 + 1, int02), (int01 + 2, int02), (int01 + 1, int02 + 1)],
                      [(int01 + 1, int02 - 1), (int01, int02), (int01 + 1, int02), (int01 + 2, int02)]],


                     [[(int01, int02 - 1), (int01, int02), (int01 + 1, int02), (int01 + 1, int02 + 1)],
                      [(int01, int02 - 1), (int01 + 1, int02 - 1), (int01 - 1, int02), (int01, int02)],
                      [(int01, int02 - 1), (int01, int02), (int01 + 1, int02), (int01 + 1, int02 + 1)],
                      [(int01, int02 - 1), (int01 + 1, int02 - 1), (int01 - 1, int02), (int01, int02)]],
                     [[(int01, int02 - 1), (int01 + 1, int02 - 1), (int01, int02), (int01 + 1, int02)],
                      [(int01, int02 - 1), (int01 + 1, int02 - 1), (int01, int02), (int01 + 1, int02)],
                      [(int01, int02 - 1), (int01 + 1, int02 - 1), (int01, int02), (int01 + 1, int02)],
                      [(int01, int02 - 1), (int01 + 1, int02 - 1), (int01, int02), (int01 + 1, int02)]],
                     [[(int01, int02), (int01 + 1, int02), (int01 + 1, int02 + 1), (int01 + 1, int02 + 2)],
                      [(int01, int02), (int01 + 1, int02), (int01 + 2, int02), (int01, int02 + 1)],
                      [(int01 + 1, int02 - 1), (int01 + 1, int02), (int01 + 1, int02 + 1), (int01 + 2, int02 + 1)],
                      [(int01 + 2, int02 - 1), (int01, int02), (int01 + 1, int02), (int01 + 2, int02)]],
                     [[(int01, int02 - 2), (int01, int02 - 1), (int01, int02), (int01, int02 + 1)],
                      [(int01 - 2, int02), (int01 - 1, int02), (int01, int02), (int01 + 1, int02)],
                      [(int01, int02 - 2), (int01, int02 - 1), (int01, int02), (int01, int02 + 1)],
                      [(int01 - 2, int02), (int01 - 1, int02), (int01, int02), (int01 + 1, int02)]]]
    return list_all_rect





def apperr_rect(a, list):
    '''

    :param a: 检查上一个元素是否到底
    :param list: 被操作的列表，主列表
    :return: 如果返回0，表示游戏可以结束了
    '''
    global rect_type
    rect_type = random.choice((1, 2, 3, 4, 5, 6, 7))

    if a == 0:
        pass
    if a == 1 and list[0][5] == 0:
        if rect_type == 1:
            if list[1][5] == 0 and list[1][4] == 0 and list[1][3] == 0:
                list[1][5] = 1
                list[1][4] = 1
                list[1][3] = 1
                list[0][5] = 1
            else:
                return 0
        if rect_type == 2:
            if list[0][6] == 0 and list[1][4] == 0 and list[1][5] == 0:
                list[0][6] = 1
                list[1][4] = 1
                list[1][5] = 1
                list[0][5] = 1
            else:
                return 0

        if rect_type == 3:
            if list[1][5] == 0 and list[1][4] == 0 and list[1][6] == 0:
                list[1][5] = 1
                list[1][4] = 1
                list[1][6] = 1
                list[0][5] = 1
            else:
                return 0

        if rect_type == 4:
            if list[0][4] == 0 and list[1][5] == 0 and list[1][6] == 0:
                list[0][4] = 1
                list[1][5] = 1
                list[1][6] = 1
                list[0][5] = 1
            else:
                return 0

        if rect_type == 5:
            if list[0][4] == 0 and list[1][4] == 0 and list[1][5] == 0:
                list[0][4] = 1
                list[1][4] = 1
                list[1][5] = 1
                list[0][5] = 1
            else:
                return 0

        if rect_type == 6:
            if list[1][5] == 0 and list[1][6] == 0 and list[1][7] == 0:
                list[1][5] = 1
                list[1][6] = 1
                list[1][7] = 1
                list[0][5] = 1
            else:
                return 0

        if rect_type == 7:
            if list[0][3] == 0 and list[0][4] == 0 and list[0][6] == 0:
                list[0][3] = 1
                list[0][4] = 1
                list[0][6] = 1
                list[0][5] = 1
            else:
                return 0


def remove_rect(list, score):
    list01 = []  # 一个临时储存数据的列表
    remove_num = 0  # 被消除的行数
    '''

    :param list: 被操作的列表
    :param score: 总的得分
    :param check_lowest: 检查元素是否已经到底
    :return: 
    '''

    for item in list:
        if item.count(1) != 10:
            list01.append(item)
        else:
            list01.insert(0, [0] * 10)
            remove_num += 1
    if remove_num == 1:
        score += 100
    if remove_num == 2:
        score += 300
    if remove_num == 3:
        score += 500
    if remove_num == 4:
        score += 800
    return list01

# 元素下降的操作，注意下落的速度，不然会造成操作的不协调
def rect_set(x_value,y_value,list001):
    list=list_generate(x_value,y_value)
    for item in list[rect_type - 1][rect_trun_num - 1]:
        # print(item)
        if list001[item[0]][item[1]] == 1:
            return 0
    for item in list[rect_type - 1][rect_trun_num - 1]:

        list001[item[0]][item[1]] = 1
    # print_list(list001)
    show_screen()
    return 1


def clear_rect(x_value,y_value,list001):
    # print(x_value)
    list = list_generate(x_value, y_value)
    # print_list(list)
    for item in list[rect_type - 1][rect_trun_num - 1]:
        # print(item)
        list001[item[0]][item[1]] = 0

    # print_list(list001)


def show_screen():
    '''
    显示屏幕
    :return:

    '''
    pos_rec_y = 80

    for j in range(20):
        pos_rec_x = 20
        for i in range(10):
            py.draw.rect(screen, (128, 128, 128), (pos_rec_x, pos_rec_y, 30, 30), 1)
            if list_op[j][i] == 1:
                py.draw.rect(screen, (255, 140, 0), (pos_rec_x + 5, pos_rec_y + 5, 20, 20))

            pos_rec_x += 30
        pos_rec_y += 30




# print(list_op)
x,y=0,5
a=1
score=0#得分出始值设为0
lowest_value=0#检查是否到底的标识，1位到底

#测试￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥

clock_num=0
clock=py.time.Clock()
rect_trun_num=1
# rect_type = 1
def print_list(list):
    for i in list:
        for j in i:
            print(j,end=' ')
        print("")
    print("------------------------------")
if __name__=='__main__':
    while True:

        if lowest_value==1 and clock_num==0:
            list_op=remove_rect(list_op,score)
        screen.fill(white)
        clock.tick(30)
        if x==0 and clock_num==0:
            y=5
            rect_trun_num = 1
            apperr_rect(a,list_op)
        a=0

        show_screen()

        if clock_num==60:

            clock_num=0

            try:
                clear_rect(x,y,list_op)
            except IndexError:
                x = 0
                lowest_value=1
                continue

            # print_list(list_generate(x, y))
            if x < 19:
                x += 1
                try:
                    if rect_set(x,y,list_op)==0:
                        x -= 1
                        rect_set(x, y, list_op)
                        x=0
                        lowest_value = 1
                        continue
                except IndexError:
                    x -= 1
                    rect_set(x, y, list_op)
                    x = 0
                    lowest_value = 1
                    continue

                try:
                    rect_set(x,y,list_op)
                except IndexError:
                    x-=1
                    rect_set(x, y, list_op)
                    x=0
                    lowest_value = 1
                    continue




            if x==19:
                rect_set(x, y, list_op)
                x=0
                continue

        for event in py.event.get():
            if  event.type == py.QUIT:
                sys.exit()

            if event.type==KEYDOWN:

                if event.key==py.K_UP:
                        clear_rect(x, y, list_op)
                        rect_trun_num += 1
                        if rect_trun_num == 5:
                            rect_trun_num = 1
                        try:
                            if rect_set(x, y, list_op) == 0:
                                rect_trun_num -= 1
                                rect_set(x, y, list_op)
                            else:
                                rect_set(x, y, list_op)
                        except IndexError:
                            rect_trun_num -=1
                            if rect_trun_num ==0:
                                rect_num=4
                            rect_set(x, y, list_op)




                elif event.key==py.K_DOWN:
                    if x<19:
                        clear_rect(x, y, list_op)
                        x += 1

                        try:
                            if rect_set(x, y, list_op) == 0:
                                x -= 1
                                rect_set(x, y, list_op)
                            else:
                                rect_set(x, y, list_op)
                        except IndexError:
                            x -= 1
                            rect_set(x, y, list_op)



                elif event.key==py.K_LEFT:
                    if y>0 and not (y==1 and rect_type==6 and (rect_trun_num==3 or rect_trun_num==4))\
                            and not(y==2 and rect_type==1 and rect_trun_num==1)\
                            and not(y==1 and rect_type==1 and (rect_trun_num==3 or rect_trun_num==4))\
                            and not (y==1 and rect_type==2 and(rect_trun_num==1 or rect_trun_num==2 or rect_trun_num==3 or rect_trun_num==4))\
                            and not (y==1 and rect_type==3 and (rect_trun_num==1 or rect_trun_num==3 or rect_trun_num==4))\
                            and not(y==1 and rect_type==4 and (rect_trun_num==1 or rect_trun_num==2 or rect_trun_num==3 or rect_trun_num==4))\
                            and not (y==1 and rect_type==5  and (rect_trun_num==1 or rect_trun_num==2 or rect_trun_num==3 or rect_trun_num==4))\
                            and not (y==2 and rect_type==7 and (rect_trun_num==1 or rect_trun_num==3)):



                        clear_rect(x, y, list_op)
                        y-=1
                        try:
                            if rect_set(x,y,list_op)==0:
                                y+=1
                                rect_set(x, y, list_op)
                            else:
                                rect_set(x, y, list_op)
                        except IndexError:
                            y += 1
                            rect_set(x, y, list_op)



                elif event.key==py.K_RIGHT:
                    if y<9:
                       clear_rect(x, y, list_op)
                       y+=1
                       try:
                           if rect_set(x, y, list_op) == 0:
                               y -= 1
                               rect_set(x, y, list_op)
                           else:
                               rect_set(x, y, list_op)
                       except IndexError:
                           y -= 1
                           rect_set(x, y, list_op)

                       # time.sleep(1)
                else:
                    continue

        clock_num += 1


        py.display.update()