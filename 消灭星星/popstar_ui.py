import pygame as py
import sys
from pygame.locals import *
import time
import random
from popstar import *

py.init()
#颜色列表
list_clor = [(0, 19, 255), (148, 2, 211), (0, 128, 0), (255, 140, 0), (255, 0, 0)]  # 深天蓝，紫色，绿色，深橙色，纯红

global score
level_num = 1
clock=py.time.Clock()

def count_list(a_fun,list_fun):
    a_fun_total=0
    for item in list_fun:
        a_fun_total+=item.count(a_fun)
    return  a_fun_total




def screen_play(screen_fun, list_fun,score_fun):
    pos_rec_y = 50

    for j in range(10):
        pos_rec_x = 20
        for i in range(10):
            py.draw.rect(screen_fun, (128, 128, 128), (pos_rec_x, pos_rec_y, 50, 50), 1)
            if list_fun[j][i] in (1,2,3,4,5):
                py.draw.rect(screen_fun, list_clor[list_fun[j][i]-1], (pos_rec_x + 5, pos_rec_y + 5, 40, 40))

            pos_rec_x += 50
        pos_rec_y += 50

    score_image=py.image.load("other/score.png")
    score_rect=score_image.get_rect()
    score_rect.x,score_rect.y=550,50
    screen_fun.blit(score_image,score_rect)



    # 定义字体
    font01 = py.font.Font(None, 60)
    text_score = font01.render(str(score_fun), True, (0, 0, 0))  # 得分文本，用来显示得分
    text_score_rect = text_score.get_rect()
    text_score_rect.x, text_score_rect.y = 700, 50
    screen_fun.blit(text_score,text_score_rect)

    #显示重新开始按钮
    restart_image=py.image.load("other/restart.png")
    restart_rect = restart_image.get_rect()
    restart_rect.x, restart_rect.y = 550, 220
    screen_fun.blit(restart_image,restart_rect)

#游戏不能继续就显示gameover
    if check_list_fun(list_fun)==0:
        over_image = py.image.load("other/gameover.png")
        over_rect = over_image.get_rect()
        over_rect.x, over_rect.y = 180, 220
        screen_fun.blit(over_image, over_rect)


def play_game():

    # 生成一个随机列表，用来显示初始界面
    list_random = init_list_fun()
    # global score#定义得分，初始值设为0
    score=0
    # global level_num#定义关卡数，初始设为1
    # level_num=1

    screen = py.display.set_mode((900, 600))
    back_clor = 238, 232, 170
    screen.fill(back_clor)
    score_num = 0
    count_num_best=0
    while True:
        clock.tick(30)
        screen.fill(back_clor)


        best_image = py.image.load("other/best.png")
        best_rect = best_image.get_rect()
        best_rect.x, best_rect.y = 550, 300
        if score_num >= 4 and count_num_best<61:

                screen.fill(back_clor)
                screen_play(screen, list_random, score)


                screen.blit(best_image, best_rect)
                count_num_best +=1
                if count_num_best==60:
                    count_num_best=0
                    score_num=0



        screen_play(screen, list_random,score)
        for event in py.event.get():
            if event.type == py.QUIT:
                sys.exit()
            pos_rec_y = 50

            for j in range(10):
                pos_rec_x = 20
                for i in range(10):
                    if event.type == py.MOUSEBUTTONDOWN:
                        if pos_rec_x < event.pos[0] < pos_rec_x + 50 and \
                                pos_rec_y < event.pos[1] < pos_rec_y + 50:
                            what_int=list_random[j][i]
                            a_int=count_list(what_int,list_random)

                            list_random=main_fun(j,i,list_random)
                            b_int=count_list(what_int,list_random)

                            score_num=a_int-b_int

                            score += score_num ** 2 * 5







                    pos_rec_x += 50
                pos_rec_y += 50
            if event.type == py.MOUSEBUTTONDOWN:
                if 550 <event.pos[0]<700 and 220 < event.pos[1]<290:
                    list_random = init_list_fun()
                    score=0

        py.display.update()
# play_game()


