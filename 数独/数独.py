#检查数列中是否只有1-9的数字各一个
def num_check(list01):
    for i in range(1,10):
        if list01.count(i) !=1:
            return False
    return True
# list02=[1,3,2,5,4,6,7,8,9]
# print(num_check(list02))
#列表转换操作，把列表的列转换成行
def turn_list(list01):
	list_turn_2=[]#最后结果列表
	for m in range(9):
			list02=[]#临时列表，用来把行换成列
			for n in range(9):
				list02.append(list01[n][m])
			list_turn_2.append(list02)
	return list_turn_2
# list03=[[1,2,3,4,5,6,7,8,9],
#         [1,2,3,4,5,6,7,8,9],
#         [1,2,3,4,5,6,7,8,9],
#         [1,2,3,4,5,6,7,8,9],
#         [1,2,3,4,5,6,7,8,9],
#         [1,2,3,4,5,6,7,8,9],
#         [1,2,3,4,5,6,7,8,9],
#         [1,2,3,4,5,6,7,8,9],
#         [1,2,3,4,5,6,7,8,9]]
# list03=turn_list(list03)
# for item in list03:
#     print(item)
#把数独盘的9个3*3正方矩阵转换为列表
def turn_mat(list01):
    list02=[]
    m=0
    n=0
    for k in range(9):
        list03=[]
        i=n
        j=m

        for l in range(9):
            list03.append(list01[i][j])
            j+=1
            if j==m+3:
                j=m
                i+=1
        m+=3
        if m==9:
            m=0
            n+=3
        if n==9:
            n=0

        list02.append(list03)
    return list02
# list03=turn_mat(list03)
# for item in list03:
#     print(item)
def check_list(list01):
    for item01 in list01:
        if num_check(item01)==False:
            return False
    for item02 in (turn_mat(list01)):
        if num_check(item02)==False:
            return False
    for item03 in (turn_list(list01)):
        if num_check(item03)==False:
            return False
    return True



