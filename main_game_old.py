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
v=class_game.Velocity(500,500)


#*setup
pygame.init()
screen = pygame.display.set_mode((size_screen_wide,size_screen_hight))
pygame.display.set_caption("test")
background=pygame.image.load("background.jpg")

base_font = pygame.font.Font(None, 32)

rect_fight = pygame.Rect(20, size_screen_hight-250, 160, 32)
color_active_fight = pygame.Color('lightskyblue3')
color_passive_fight = pygame.Color('chartreuse4')
color_fight = color_passive_fight
active_fight = False
Text_fight = "Fight"

rect_cancel = pygame.Rect(20, size_screen_hight-200, 160, 32)
color_cancel = pygame.Color('red')
active_cancel = False
Text_cancel = "Cancel"

rect_time = pygame.Rect(20, size_screen_hight-150, 160, 32)
color_time = pygame.Color('lightskyblue3')
Text_time = "0.00         "

rect_speed = pygame.Rect(20, size_screen_hight-350, 100, 32)
color_active_speed = pygame.Color('lightskyblue3')
color_passive_speed = pygame.Color('chartreuse4')
color_speed = color_passive_speed
active_speed = False
Text_speed = "500"

rect_degree = pygame.Rect(20, size_screen_hight-300, 100, 32)
color_active_degree = pygame.Color('lightskyblue3')
color_passive_degree = pygame.Color('chartreuse4')
color_degree = color_passive_degree
active_degree = False
Text_degree = "45"

rect_degree_check = pygame.Rect(20, size_screen_hight-300, 100, 32)
color_active_degree = pygame.Color('lightskyblue3')
color_passive_degree = pygame.Color('chartreuse4')
color_degree = color_passive_degree
active_degree = False
Text_degree = "45"

rect_degree = pygame.Rect(20, size_screen_hight-300, 100, 32)
color_active_degree = pygame.Color('lightskyblue3')
color_passive_degree = pygame.Color('chartreuse4')
color_degree = color_passive_degree
active_degree = False
Text_degree = "45"

mode=0

active_1st=True
#*start
while True:
    #exit
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # * all will False
            active_speed = False
            active_degree = False

            if rect_fight.collidepoint(event.pos):
                active_fight = True
            elif rect_cancel.collidepoint(event.pos):
                active_cancel = True
            elif rect_speed.collidepoint(event.pos):
                active_speed = True
            elif rect_degree.collidepoint(event.pos):
                active_degree = True
        if event.type == pygame.KEYDOWN:
            if active_speed:
                if event.key == pygame.K_BACKSPACE:
                    Text_speed = Text_speed[:-1]
                elif (event.unicode >= "0" and event.unicode <="9") or event.unicode <=".":
                    Text_speed += event.unicode
            if active_degree:
                if event.key == pygame.K_BACKSPACE:
                    Text_degree = Text_degree[:-1]
                elif (event.unicode >= "0" and event.unicode <="9") or event.unicode <=".":
                    Text_degree += event.unicode


    if active_fight:
        color_fight = color_active_fight
    else:
        color_fight = color_passive_fight

    if active_speed:
        color_speed = color_active_speed
    else:
        color_speed = color_passive_speed

    if active_degree:
        color_degree = color_active_degree
    else:
        color_degree = color_passive_degree
    
    #*compute
    screen.fill("black")
    screen.blit(background,(200,0))

    pygame.draw.rect(screen, color_fight, rect_fight)
    pygame.draw.rect(screen, color_speed, rect_speed)
    pygame.draw.rect(screen, color_degree, rect_degree)
    pygame.draw.rect(screen, color_cancel, rect_cancel)

    if active_fight:
        if active_1st:
            v.setspeed(int(Text_speed),int(Text_degree))
            active_1st = False
        pygame.draw.circle(screen,'red', (v.get_position_x(time_count)+size_ui,size_screen_hight-v.get_position_y(time_count)), 20)
        time_count=time_count+time_delta
        Text_time=str(time_count)

    if active_cancel:
        time_count=0
        v.resetpositon()
        active_fight=False
        active_cancel=False
        active_1st = True
        Text_time = "0.00         "

    Text_time=Text_time[0:5]+"   s"
    text_surface_time = base_font.render(Text_time, True, (255, 255, 255))
    screen.blit(text_surface_time, (rect_time.x+40, rect_time.y+5))

    text_surface_fight = base_font.render(Text_fight, True, (255, 255, 255))
    screen.blit(text_surface_fight, (rect_fight.x+40, rect_fight.y+5))

    text_surface_speed = base_font.render(Text_speed, True, (255, 255, 255))
    screen.blit(text_surface_speed, (rect_speed.x+20, rect_speed.y+5))

    text_surface_degree = base_font.render(Text_degree, True, (255, 255, 255))
    screen.blit(text_surface_degree, (rect_degree.x+20, rect_degree.y+5))

    text_surface_cancel = base_font.render(Text_cancel, True, (255, 255, 255))
    screen.blit(text_surface_cancel, (rect_cancel.x+40, rect_cancel.y+5))
    #wait
    clock.tick(FPS)


    #display
    pygame.display.update()

    
    # print("x={:.2f},y={:.2f}".format(v.get_position_x(time_count),v.get_position_y(time_count)))
    if(v.get_position_y(time_count) < -1):
        time_count=0
        v.resetpositon()
        active_fight=False
        active_1st = True