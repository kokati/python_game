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
def init_screem():
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
#列表控制台输出函数
def print_screem(list01):
    for i in list01:
        for j in i:
            print("%5d"%j,end=" ")
        print()


screem01=init_screem()
screem01=add_num(screem01)
screem01=add_num(screem01)
print_screem(screem01)


while True:
    list_copy=copy.deepcopy(screem01)
    op_input=input("输入你的操作：")
    if op_input=="w":
        screem01=up_op(screem01)
        print_screem(screem01)
    elif op_input=="s":
        screem01=down_op(screem01)
        print_screem(screem01)
    elif op_input=="a":
        screem01=left_op(screem01)
        print_screem(screem01)
    elif op_input=="d":
        screem01=right_op(screem01)
        print_screem(screem01)
    else:
        continue
    print()
    if screem01==list_copy:
        continue
    screem01 = add_num(screem01)

    print_screem(screem01)



# list02=[[2,2,2,2],[0,4,32,0],[0,0,0,2],[0,0,8,4]]
# while True:
#     add01=input("请输入：")
#     if add01=="a":
#         list02=add_num(list02)
#         print(list02)
#     else:
#         break


# print_screem(list02)
# list02=down_op(list02)
# print()
#
# print_screem(list02)






