

import copy
import random
# gone_num=0



#初始化界面，随机生成一个10*10的列表，每个元素为（1,2,3,4,5,6)中的一个
def init_list_fun():
    list09=[]#最后返回的列表，设初始值为空
    for i in range(10):
        list10=[]
        for j in range(10):
            num01=random.choice((1,2,3,4,5))
            list10.append(num01)
        list09.append(list10)
    return  list09
list_random=init_list_fun()



# 消灭星星核心算法，点击一个方块，
# 和它相邻且相同的元素一起消失
def to_zero(a, list_op):
    '''
    :param a: 要被消灭的元素的标识
    :param list_op: 被操作的主列表
    :return: 返回操作后的主列表
    '''

    while True:

        list_copy = copy.deepcopy(list_op)
        for i in range(10):
            for j in range(10):
                if list_op[i][j] == 0:
                    if i != 0 and list_op[i - 1][j] == a:
                        list_op[i - 1][j] = 0


                    if i != 9 and list_op[i + 1][j] == a:
                        list_op[i + 1][j] = 0

                    if j != 0 and list_op[i][j - 1] == a:
                        list_op[i][j - 1] = 0


                    if j != 9 and list_op[i][j + 1] == a:
                        list_op[i][j + 1] = 0


        if list_op == list_copy:
            break
    return list_op
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
# 列表置换的方法，把列表的行换成列
def trun_list_fun(list03):
    list_trun = []  # 转换后的临时列表
    for j in range(10):
        list04 = []  # 临时列表，用来把列换成行
        for i in range(10):
            list04.append(list03[i][j])
        list_trun.append(list04)
    return  list_trun



# 有些元素消除后，其它元素因为地心引力向下移动
def rect_down(down_list):
    down_list=trun_list_fun(down_list)
    list07=[]
    for item in down_list:
        list06=[]
        item.reverse()
        item=put_0_end(item)
        item.reverse()
        list06=item
        list07.append(list06)
    down_list=trun_list_fun(list07)
    return down_list
# a=9
#把列表里的0变成9
def zero_to_nine(list08):
    global a
    # a+=2
    for i in range(10):
        for j in range(10):
            if list08[i][j]==0:
                list08[i][j]=9
    return list08
#如果垂直的某一列元素全部是0和9，把它们移除，并让其它列向左靠拢，
#差的列用全部是9的列补齐
def list_left_fun(list10):
    num_fun=0
    list11=[]
    list10=trun_list_fun(list10)
    for item in list10:
        if item.count(9)!=10:
            list11.append(item)
        else:
            num_fun+=1
    if num_fun>0:
        for item in range(num_fun):
            list11.append([9,9,9,9,9,9,9,9,9,9])
    list10=trun_list_fun(list11)
    return  list10

#检查主列表是否还有能够操作的元素，如果没有，返回一个0，表示游戏可以结束
def check_list_fun(list12):

    for i in range(10):
        for j in range(10):
            num_fun=list12[i][j]
            if num_fun!=9:
                if i != 0 and list12[i - 1][j] == num_fun:

                    return 1

                if i != 9 and list12[i + 1][j] == num_fun:
                    return 1

                if j != 0 and list12[i][j - 1] == num_fun:
                    return 1

                if j != 9 and list12[i][j + 1] == num_fun:
                    return 1
    return  0
#点击一个元素，然后进行操作，这个是操作列表的最终程序
def main_fun(x_fun,y_fun,list_fun):
    if list_fun[x_fun][y_fun]==9:
        return list_fun

    num_fun=list_fun[x_fun][y_fun]
    list_fun[x_fun][y_fun]=0
    list_fun_copy=copy.deepcopy(list_fun)
    list_fun=to_zero(num_fun,list_fun)
    if list_fun==list_fun_copy:
        list_fun[x_fun][y_fun]=num_fun
        return  list_fun
    list_fun=rect_down(list_fun)

    list_fun=zero_to_nine(list_fun)

    list_fun=list_left_fun(list_fun)
    return list_fun











