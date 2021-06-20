# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:33:13 2021

@author: KIM
"""
"""

! sdad
* saw
? kwon
//wqer
"""

import pygame
import numpy
import class_game
from resolution import *

#* global varialbe
if(True):
    #* global varialbe
    if(True):
        border=10
        mode=0;
        forpint=""
        jearn=0 #* spirng or V

    #* time
    if(True):
        clock = pygame.time.Clock()
        FPS=60
        time_count=0
        time_delta=1/FPS
        time_save=20
    
    #* resolution screen
    # if(True):
    #     size_screen_wide=1400
    #     size_screen_hight=800
    #     size_ui_x=250
    #     size_pic_x=size_screen_wide-size_ui_x
    #     size_pic_y=600
    #     size_pot_wide=200
    #     size_pot_hight=320

#* setup
if(True):
    #* setpic
    if(True):
        pygame.init()
        screen = pygame.display.set_mode((size_screen_wide,size_screen_hight))
        pygame.display.set_caption("hellp_world")
        background=pygame.image.load("4.jpg")
        background = pygame.transform.scale(background, (size_pic_x, size_pic_y))
        pot = pygame.image.load("pot_final-removebg-preview.png")
        pot = pygame.transform.scale(pot, (size_pot_wide, size_pot_hight))

    #* setup box
    if(True): 
        draw_list=[]
        check_list=[] #* click
        reset_list=[] #* reset when out
        new_word_list=[] #* that input
        box_setup_list=[]

        # box_bot=class_game.labbel(size_ui_x, size_pic_y, size_screen_wide-size_ui_x, size_pot_hight-size_pic_y)
        box_bot=class_game.labbel(size_ui_x, size_pic_y+border, size_screen_wide-size_ui_x, size_screen_hight-size_pic_y-border*2,"","antiquewhite")
        box_left=class_game.labbel(border,border,size_ui_x-border*2,size_screen_hight-border*2,"","antiquewhite");
        box_setup_list.append(box_bot)
        box_setup_list.append(box_left)
        size_y=20
        delta_y=50

        sx_box=class_game.Input_box(20, size_y, 210, 32,"2.00",0,"X = ", " M")
        draw_list.append(sx_box)
        check_list.append(sx_box)
        reset_list.append(sx_box)
        new_word_list.append(sx_box)
        size_y=size_y+delta_y

        sy_box=class_game.Input_box(20, size_y, 210, 32,"0.4",0,"Y = ", " M")
        draw_list.append(sy_box)
        check_list.append(sy_box)
        reset_list.append(sy_box)
        new_word_list.append(sy_box)
        size_y=size_y+delta_y

        set=class_game.Button(20, size_y, 210, 32,"set")
        draw_list.append(set)
        check_list.append(set)
        size_y=size_y+delta_y

        mass=class_game.Input_box(20, size_y, 210, 32,"1",0,"M = ", " KG")
        draw_list.append(mass)
        check_list.append(mass)
        reset_list.append(mass)
        new_word_list.append(mass)
        size_y=size_y+delta_y

        gravity=class_game.Input_box(20, size_y, 210, 32,"9.81",0,"G = ", " m/s^2")
        draw_list.append(gravity)
        check_list.append(gravity)
        reset_list.append(gravity)
        new_word_list.append(gravity)
        size_y=size_y+delta_y

        degree=class_game.Input_box(60, size_y, 170, 32,"45",1,"O = ","°")
        draw_list.append(degree)
        check_list.append(degree)
        reset_list.append(degree)
        new_word_list.append(degree)

        check_degree=class_game.Check_box(20, size_y, 32, 32)
        draw_list.append(check_degree)
        check_list.append(check_degree)
        size_y=size_y+delta_y

        instan_labbel=class_game.labbel(60, size_y, 170, 32 , "Instant speed")
        draw_list.append(instan_labbel)

        check_use_speed=class_game.Check_box(20, size_y, 32, 32)
        draw_list.append(check_use_speed)
        check_list.append(check_use_speed)
        size_y=size_y+delta_y

        speed=class_game.Input_box(60, size_y, 170, 32,"4.00",1,"V = "," m/s")
        draw_list.append(speed)
        check_list.append(speed)
        reset_list.append(speed)
        new_word_list.append(speed)

        check_speed=class_game.Check_box(20, size_y, 32, 32)
        draw_list.append(check_speed)
        check_list.append(check_speed)
        size_y=size_y+delta_y

        check_spring=class_game.Check_box(20, size_y, 32, 32)
        draw_list.append(check_spring)
        check_list.append(check_spring)

        spring_k=class_game.Input_box(60, size_y, 170, 32,"500",1,"K = "," N/m")
        draw_list.append(spring_k)
        check_list.append(spring_k)
        reset_list.append(spring_k)
        new_word_list.append(spring_k)
        size_y=size_y+delta_y

        spring_x=class_game.Input_box(40, size_y, 190, 32,"1",1,"lenght = "," m")
        draw_list.append(spring_x)
        check_list.append(spring_x)
        reset_list.append(spring_x)
        new_word_list.append(spring_x)
        size_y=size_y+delta_y

        cal=class_game.Button(20, size_y, 210, 32,"cal")
        draw_list.append(cal)
        check_list.append(cal)
        size_y=size_y+delta_y

        fight=class_game.Button(20, size_y, 210, 32,"fight")
        draw_list.append(fight)
        check_list.append(fight)
        size_y=size_y+delta_y

        cancel=class_game.Button(20, size_y, 210, 32,"Cancel","red","red")
        draw_list.append(cancel)
        check_list.append(cancel)
        active_1st=True
        size_y=size_y+delta_y

        time_box=class_game.labbel(20, size_y, 210, 32)
        draw_list.append(time_box)
        Text_time = "0.00         "

    #* setup ball
    ball=class_game.ball(5)
    ball.v.setspeed(4,45,9.81)
    tail = class_game.Tail()
    draw_list.append(tail)

while True:
    #* event
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #* all will False
            for i in reset_list:
                i.active=False

            for i in check_list:
                i.check(event.pos)
        
        if event.type == pygame.KEYDOWN:
            for i in new_word_list:
                i.new_word(event)


    #* draw_pic
    screen.fill("black")
    screen.blit(background,(size_ui_x,0))
    for i in box_setup_list:
        i.draw(screen)

    #* set_pic
    if(sx_box.Text !='' and sy_box.Text !=''):
        screen.blit(pot,(float(sx_box.Text)*100*scale+size_ui_x,size_pic_y-float(sy_box.Text)*100*scale-size_pot_hight))
        # screen.blit(pot,(800,size_screen_hight-int(speed.Text)-size_pot_hight))
        # print(size_screen_hight-int(speed.Text))
    elif(sy_box.Text !=''):
        screen.blit(pot,(size_ui_x,size_pic_y-float(sy_box.Text)*100*scale-size_pot_hight))
    elif(sx_box.Text !=''):
        screen.blit(pot,(float(sx_box.Text)*100*scale+size_ui_x,size_pic_y-size_pot_hight))
    else:
        screen.blit(pot,(size_ui_x,size_pic_y-size_pot_hight))

    #* cal
    if(True):
        #* boolean
        if(True):
            degree.off = not(check_degree.active)
            if(check_speed.active and check_spring.active):
                if(jearn):
                    check_speed.active=False
                    jearn=0
                else:
                    check_spring.active=False
                    jearn=1
            if(check_speed.active):
                jearn=1
            if(check_spring.active):
                jearn=0
                # print("activ above")

            if(check_use_speed.active):
                if(jearn):
                    check_speed.active = True
                else:
                    check_spring.active = True
                speed.off = not(check_speed.active)
                spring_k.off = not(check_spring.active)
                spring_x.off = not(check_spring.active)
            else:
                speed.off = True
                spring_k.off = True
                spring_x.off = True
                check_speed.active = False
                check_spring.active = False

            if(check_degree.active and check_use_speed.active and check_speed.active and not(check_spring.active)):
                #* free know
                mode=1

            elif(check_degree.active and check_use_speed.active and not(check_speed.active) and check_spring.active):
                #* free know v
                mode=2

            elif(check_degree.active and not(check_use_speed.active)):
                #* cal v.k
                mode=3
            elif(not(check_degree.active) and check_use_speed.active and check_speed.active and not(check_spring.active)):
                #* cal 0 from v
                mode=4
            elif(not(check_degree.active) and check_use_speed.active and not(check_speed.active) and check_spring.active):
                #* cal 0 from k
                mode=5
            else:
                #* error
                mode=0

        forpint=str(mode)
        #* calnumber
        if(cal.active):
            cal.active = False
            if(mode == 1):
                x=class_game.findxfromv(float(spring_k.Text),float(mass.Text),float(speed.Text))
                spring_x.Text=str(round(x,2));
                ball.v.setspeed(float(speed.Text),float(degree.Text),float(gravity.Text))
            elif(mode == 2):
                v=class_game.findVfromk(float(spring_k.Text),float(mass.Text),float(spring_x.Text))
                speed.Text=str(round(v,2));
                ball.v.setspeed(float(speed.Text),float(degree.Text),float(gravity.Text))

    #* fight
    if fight.active:
        #* fight 
        if active_1st:
            active_1st = False
        if(time_count % time_save):
            tail.add_position(ball.posi_x,ball.posi_y)
        # pygame.draw.circle(screen,'red', (v.get_position_x(time_count)+size_ui_x,size_pic_y-v.get_position_y(time_count)), 20)
        
        ball.setsize(float(mass.Text))
        ball.run(screen,time_count)
        time_count=time_count+time_delta
        Text_time=str(time_count)

    #* cancel
    if cancel.active:
        time_count=0
        fight.active=False
        cancel.active=False
        active_1st = True
        Text_time = "0.00         "

    #* fall
    if(ball.check_fall(time_count)):
        time_count=0
        fight.active = False
        active_1st = True

    #* update
    time_box.update_text(Text_time[0:5]+"   s"+forpint)
    clock.tick(FPS)

    #* display
    for i in draw_list:
        i.draw(screen)
    pygame.display.update()