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
#! global varialbe
size_ui=200
size_screen_wide=1286+size_ui
size_screen_hight=720

#*time
clock = pygame.time.Clock()
FPS=120
time_count=0
time_delta=1/FPS

#*enviroment setup

#*setup
pygame.init()
screen = pygame.display.set_mode((size_screen_wide,size_screen_hight))
pygame.display.set_caption("hellp_world")
background=pygame.image.load("4.jpg")

draw_list=[]
check_list=[]

fight=class_game.Button(20, 250, 160, 32,"fight")
draw_list.append(fight)
check_list.append(fight)

cancel=class_game.Button(20, 200, 160, 32,"Cancel","red","red")
draw_list.append(cancel)
check_list.append(cancel)
active_1st=True

speed=class_game.Input_box(60, 350, 120, 32,"400")
draw_list.append(speed)
check_list.append(speed)

degree=class_game.Input_box(60, 300, 120, 32,"45")
draw_list.append(degree)
check_list.append(degree)

time=class_game.labbel(20, 150, 160, 32)
draw_list.append(time)
Text_time = "0.00         "

check_speed=class_game.Check_box(20, 350, 32, 32)
draw_list.append(check_speed)
check_list.append(check_speed)

check_degree=class_game.Check_box(20, 300, 32, 32)
draw_list.append(check_degree)
check_list.append(check_degree)

ball=class_game.ball(10)
#*start
while True:
    #exit
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # * all will False
            speed.active = False
            degree.active = False

            for i in check_list:
                i.check(event.pos)
        
        if event.type == pygame.KEYDOWN:
            speed.new_word(event)
            degree.new_word(event)


    time.update_text(Text_time[0:5]+"   s")
    #*compute
    screen.fill("black")
    screen.blit(background,(200,0))

    for i in draw_list:
        i.draw(screen)

    if fight.active:
        if active_1st:
            active_1st = False
            ball.v.setspeed(int(speed.Text),int(degree.Text))
        # pygame.draw.circle(screen,'red', (v.get_position_x(time_count)+size_ui,size_screen_hight-v.get_position_y(time_count)), 20)
        
        ball.run(screen,time_count)
        time_count=time_count+time_delta
        Text_time=str(time_count)

    if cancel.active:
        time_count=0
        ball.v.resetpositon()
        fight.active=False
        cancel.active=False
        active_1st = True
        Text_time = "0.00         "

    #wait
    clock.tick(FPS)

    #display
    pygame.display.update()

    if(ball.check_fall(time_count)):
        time_count=0
        fight.active = False
        active_1st = True