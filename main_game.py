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

from numpy.core.numeric import count_nonzero
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
        bool_start=0
        kim = 5 #* what degree for display
        position_ball=[[192,184],[199,174],[198,174],[195,180],[193,183],[192,184], [190,193],[187,196],[186,198],[182,200]]
        do_again = 0 #mode4
        do_again2 = 0 #mode5
        do_again3 = 0 #mode3
        tar = 0
    #* time
    if(True):
        clock = pygame.time.Clock()
        FPS=120
        time_count=0
        time_delta=1/FPS
        time_save=1 #xframe tosave
    
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
        pot = pygame.image.load("pot3.png")
        pot = pygame.transform.scale(pot, (size_pot_wide, size_pot_hight))
        
        #* lilac
        lilac_list=[]
        if(True):

            buf=0
            buf2=-2
            buf=buf+buf2
            lilac_35 = pygame.image.load("35_u.png")
            image_w, image_h = lilac_35.get_size()
            lilac_35 = pygame.transform.scale(lilac_35, (lilac_x+buf, int(image_h/2)))
            lilac_list.append(lilac_35)
            lilac_list.append(lilac_35)
            buf=buf+buf2
            
            lilac_37 = pygame.image.load("37_u.png")
            lilac_37 = pygame.transform.scale(lilac_37, (lilac_x+buf, lilac_y))
            lilac_list.append(lilac_37)
            buf=buf+buf2
            
            lilac_40 = pygame.image.load("40_u.png")
            lilac_40 = pygame.transform.scale(lilac_40, (lilac_x+buf, lilac_y))
            lilac_list.append(lilac_40)
            buf=buf+buf2
            
            lilac_42 = pygame.image.load("42_u.png")
            lilac_42 = pygame.transform.scale(lilac_42, (lilac_x+buf, lilac_y))
            lilac_list.append(lilac_42)
            buf=buf+buf2
            
            lilac_45 = pygame.image.load("45_u.png")
            lilac_45 = pygame.transform.scale(lilac_45, (lilac_x+buf, lilac_y))
            lilac_list.append(lilac_45)
            buf=buf+buf2
            
            lilac_47 = pygame.image.load("47_u.png")
            lilac_47 = pygame.transform.scale(lilac_47, (lilac_x+buf, lilac_y))
            lilac_list.append(lilac_47)
            buf=buf+buf2
            
            lilac_50 = pygame.image.load("50_u.png")
            lilac_50 = pygame.transform.scale(lilac_50, (lilac_x+buf, lilac_y))
            lilac_list.append(lilac_50)
            
            lilac_52 = pygame.image.load("52_u.png")
            lilac_52 = pygame.transform.scale(lilac_52, (lilac_x+buf, lilac_y))
            lilac_list.append(lilac_52)
            buf=buf+buf2*2
            
            lilac_55 = pygame.image.load("55_u.png")
            lilac_55 = pygame.transform.scale(lilac_55, (lilac_x+buf, lilac_y))
            lilac_list.append(lilac_55)

    lilac_list[0]=lilac_list[5]

    #* setup box
    if(True):
        #* part1
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
            delta_y=40
            delta_y_mini=20

            text_box_sx=class_game.labbel(20,size_y, 170, 32 , "Distance X","gray",False,"","")
            draw_list.append(text_box_sx)
            size_y=size_y+delta_y_mini

            sx_box=class_game.Input_box(20, size_y, 210, 32,"200",0,"X = ", " CM")
            draw_list.append(sx_box)
            check_list.append(sx_box)
            reset_list.append(sx_box)
            new_word_list.append(sx_box)
            size_y=size_y+delta_y

            text_box_sy=class_game.labbel(20,size_y, 170, 32 , "Distance Y","gray",False,"","")
            draw_list.append(text_box_sy)
            size_y=size_y+delta_y_mini

            sy_box=class_game.Input_box(20, size_y, 210, 32,"40",0,"Y = ", " CM")
            draw_list.append(sy_box)
            check_list.append(sy_box)
            reset_list.append(sy_box)
            new_word_list.append(sy_box)
            size_y=size_y+delta_y

            # set=class_game.Button(20, size_y, 210, 32,"set")
            # draw_list.append(set)
            # check_list.append(set)
            # size_y=size_y+delta_y

            text_box_mass=class_game.labbel(20,size_y, 170, 32 , "Mass","gray",False,"","")
            draw_list.append(text_box_mass)
            size_y=size_y+delta_y_mini

            mass=class_game.Input_box(20, size_y, 210, 32,"0.1",0,"M = ", " KG")
            draw_list.append(mass)
            check_list.append(mass)
            reset_list.append(mass)
            new_word_list.append(mass)
            size_y=size_y+delta_y

            text_box_gravity=class_game.labbel(20,size_y, 170, 32 , "gravity","gray",False,"","")
            draw_list.append(text_box_gravity)
            size_y=size_y+delta_y_mini

            gravity=class_game.Input_box(20, size_y, 210, 32,"9.81",0,"G = ", " m/s^2")
            draw_list.append(gravity)
            check_list.append(gravity)
            reset_list.append(gravity)
            new_word_list.append(gravity)
            size_y=size_y+delta_y

            size_y=size_y+delta_y_mini

        #* part2 mass_bot
        if(True):
            text_box_degree=class_game.labbel(20,size_y, 170, 32 , "degree","gray",False,"","")
            draw_list.append(text_box_degree)
            size_y=size_y+delta_y_mini

            degree=class_game.Input_box(60, size_y, 170, 32,"45.0",1,"O = ","??")
            draw_list.append(degree)
            check_list.append(degree)
            reset_list.append(degree)
            new_word_list.append(degree)

            check_degree=class_game.Check_box(20, size_y, 32, 32)
            draw_list.append(check_degree)
            check_list.append(check_degree)
            size_y=size_y+delta_y

            size_y=size_y+delta_y_mini

            instan_labbel=class_game.labbel(60, size_y+5, 170, 32 , "Instant speed","gray",False,"","",28)
            draw_list.append(instan_labbel)

            check_use_speed=class_game.Check_box(20, size_y, 32, 32)
            draw_list.append(check_use_speed)
            check_list.append(check_use_speed)
            size_y=size_y+delta_y

            speed=class_game.Input_box(60, size_y, 170, 32,"5.00",1,"V = "," m/s")
            draw_list.append(speed)
            check_list.append(speed)
            reset_list.append(speed)
            new_word_list.append(speed)

            check_speed=class_game.Check_box(20, size_y, 32, 32)
            draw_list.append(check_speed)
            check_list.append(check_speed)
            size_y=size_y+delta_y

            text_box_spring=class_game.labbel(60,size_y, 170, 32 , "spring detail","gray",False,"","")
            draw_list.append(text_box_spring)
            size_y=size_y+delta_y_mini

            check_spring=class_game.Check_box(20, size_y, 32, 32)
            draw_list.append(check_spring)
            check_list.append(check_spring)

            spring_k=class_game.Input_box(60, size_y, 170, 32,"500",1,"K = "," N/m")
            draw_list.append(spring_k)
            check_list.append(spring_k)
            reset_list.append(spring_k)
            new_word_list.append(spring_k)
            size_y=size_y+delta_y

            spring_x=class_game.Input_box(40, size_y, 190, 32,"7.5",1,"lenght = "," cm")
            draw_list.append(spring_x)
            check_list.append(spring_x)
            reset_list.append(spring_x)
            new_word_list.append(spring_x)
            size_y=size_y+delta_y

            cal=class_game.Button(20, size_y, 210, 32,"cal")
            draw_list.append(cal)
            check_list.append(cal)
            size_y=size_y+delta_y

            fight=class_game.Button(1200, 630, 170, 32,"start")
            draw_list.append(fight)
            check_list.append(fight)

            save=class_game.Button(1200, 680, 170, 32,"save")
            draw_list.append(save)
            check_list.append(save)

            cancel=class_game.Button(1200, 730, 170, 32,"Cancel","red","red")
            draw_list.append(cancel)
            check_list.append(cancel)
            active_1st=True
            
            text_box_time=class_game.labbel(300,670, 170, 32 , "Time","gray",False,"","",28)
            draw_list.append(text_box_time)

            time_box=class_game.labbel(300, 700, 150, 32,"0.00","gray",True,"T = "," s",28)
            draw_list.append(time_box)
            time_count_var = "0.00"

            debug1=class_game.Input_box(20, 680, 200, 32,"200",0,"debug1 : ","")
            # draw_list.append(debug1)
            # check_list.append(debug1)
            # reset_list.append(debug1)
            # new_word_list.append(debug1)

            debug2=class_game.Input_box(20, 730, 200, 32,"40",0,"debug2 : ","")
            # draw_list.append(debug2)
            # check_list.append(debug2)
            # reset_list.append(debug2)
            # new_word_list.append(debug2)

            error_massage=class_game.labbel(20, size_y, 200, 32 , "","gray",False,"","",24)
            draw_list.append(error_massage)
            size_y=size_y+delta_y

            error_massage2=class_game.labbel(20, size_y, 200, 32 , "","gray",False,"","",24)
            draw_list.append(error_massage2)
            size_y=size_y+delta_y
    #* setup ball
    ball=class_game.ball(5)
    ball.setspeed(4,45,9.81)
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
    if(True):
        screen.fill("black")
        screen.blit(background,(size_ui_x,0))
        for i in box_setup_list:
            i.draw(screen)

        #* set_pic
        if(sx_box.Text !='' and sy_box.Text !=''):
            pot_position_x=float(sx_box.Text)*scale+size_ui_x+position_ball[kim][0]
            pot_position_y=size_pic_y-float(sy_box.Text)*scale-size_pot_hight
            
            # screen.blit(pot,(800,size_screen_hight-int(speed.Text)-size_pot_hight))
            # print(size_screen_hight-int(speed.Text))
        elif(sy_box.Text !=''):
            pot_position_x=size_ui_x+position_ball[kim][0]
            pot_position_y=size_pic_y-float(sy_box.Text)*scale-size_pot_hight

        elif(sx_box.Text !=''):
            pot_position_x=float(sx_box.Text)*scale+size_ui_x+position_ball[kim][0]
            pot_position_y=size_pic_y-size_pot_hight
        else:
            pot_position_x=size_ui_x+position_ball[kim][0]
            pot_position_y=size_pic_y-size_pot_hight
        
        goal_x=pot_position_x+size_pot_wide/2
        goal_y=pot_position_y+size_pot_hight/4
        
        screen.blit(pot,(pot_position_x,pot_position_y))
        pygame.draw.circle(screen,'yellow', (goal_x,goal_y), 5)
        screen.blit(lilac_list[kim],(size_ui_x,size_pic_y-lilac_y))
        # pygame.draw.circle(screen,'yellow', (size_ui_x,goal_y), 5)

    #* calboolean
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

        # forpint=str(mode)

    #* calnumber
    if(cal.active or do_again or do_again2 or do_again3):
        cal.active = False
        for i in new_word_list:
            if(i.Text == ""):
                i.Text = i.default_value
        #* setpic_degree
        """
        kim=kim+1
        if(kim==10):
            kim=0
        
        """
        if(True):
            if(float(degree.Text)>=35 and float(degree.Text) <=55):
                if(float(degree.Text)<37):
                    kim=1  #35
                elif(float(degree.Text)<40):
                    kim=2  #37
                elif(float(degree.Text)<42):
                    kim=3  #40
                elif(float(degree.Text)<45):
                    kim=4  #42
                elif(float(degree.Text)<47):
                    kim=5  #45
                elif(float(degree.Text)<50):
                    kim=6  #47
                elif(float(degree.Text)<52):
                    kim=7  #50
                elif(float(degree.Text)<55):
                    kim=8  #52
                else:
                    kim=9  #55
            else:
                kim=0
        
        forpint=str(kim)

        #* setmode
        if(mode == 1):
            x=class_game.findxfromv(float(spring_k.Text),float(mass.Text),float(degree.Text),float(gravity.Text),float(speed.Text))
            spring_x.Text=str(round(x*100,2))
            ball.setspeed(float(speed.Text),float(degree.Text),float(gravity.Text))
        elif(mode == 2):
            v=class_game.findVfromk(float(spring_k.Text),float(mass.Text),float(degree.Text),float(gravity.Text),float(spring_x.Text)/100)
            speed.Text=str(round(v,2));
            ball.setspeed(float(speed.Text),float(degree.Text),float(gravity.Text))
        elif(mode == 3 or do_again3):
            if(do_again3>0):
                do_again3 = do_again3-1
            elif(do_again3 ==0):
                do_again3 = 4
            sx=(goal_x-size_ui_x-position_ball[kim][0])/(100*scale)
            sy=((size_pic_y-goal_y)-position_ball[kim][1])/(100*scale)
            # print("sx : %.2f\tsx_box : %.2f\tsize_pot : %.2f"%(sx,float(sx_box.Text)/100,size_pot_wide/2))
            # print("sy : %.2f\tsize_pic_y : %.2f\tgoal_y : %.2f\tpostionball : %.2f"%(sy,size_pic_y,goal_y,position_ball[kim][1]))

            v=class_game.findvfromo(sx,sy,float(gravity.Text),float(degree.Text))
            speed.Text=str(round(v,2));
            x=class_game.findxfromv(float(spring_k.Text),float(mass.Text),float(degree.Text),float(gravity.Text),float(speed.Text))
            spring_x.Text=str(round(x*100,2));
            ball.setspeed(float(speed.Text),float(degree.Text),float(gravity.Text))
        elif(mode == 4 or do_again):
            if(do_again>0):
                do_again = do_again-1
            elif(do_again ==0):
                do_again = 4
            sx=(goal_x-size_ui_x-position_ball[kim][0])/(100*scale)
            sy=((size_pic_y-goal_y)-position_ball[kim][1])/(100*scale)
            ga=float(gravity.Text)
            spe=float(speed.Text)
            # print("sx : %.2f\tsx_box : %.2f\tsize_pot : %.2f"%(sx,float(sx_box.Text)/100,size_pot_wide/2))
            # print("sy : %.2f\tsize_pic_y : %.2f\tgoal_y : %.2f\tpostionball : %.2f"%(sy,size_pic_y,goal_y,position_ball[kim][1]))
            # print("sx : %.2f\tsy : %.2f\tG : %.2f\tspeed : %.2f" %(sx,sy,ga,spe))
            o=class_game.findofromv(sx,sy,ga,spe)
            if(o==-5):

                error_massage2.Text="cannot shoot"
                continue
            error_massage2.Text=""
            degree.Text=str(round(o,2))
            x=class_game.findxfromv(float(spring_k.Text),float(mass.Text),float(degree.Text),float(gravity.Text),float(speed.Text))
            spring_x.Text=str(round(x*100,2));

            ball.setspeed(float(speed.Text),float(degree.Text),float(gravity.Text))
        elif(mode == 5 or do_again2):
            if(do_again2>0):
                do_again2 = do_again2-1
            elif(do_again2 ==0):
                do_again2 = 4
            

            sx=(goal_x-size_ui_x-position_ball[kim][0])/(100*scale)
            sy=((size_pic_y-goal_y)-position_ball[kim][1])/(100*scale)
            ga=float(gravity.Text)
            spr=float(spring_k.Text)
            ma=float(mass.Text)
            xx=float(spring_x.Text)/100
            # print("sx : %.2f\tsx_box : %.2f\tsize_pot : %.2f"%(sx,float(sx_box.Text)/100,size_pot_wide/2))
            # print("sy : %.2f\tsize_pic_y : %.2f\tgoal_y : %.2f\tpostionball : %.2f"%(sy,size_pic_y,goal_y,position_ball[kim][1]))
            # print("sx : %.2f\tsy : %.2f\tG : %.2f\tspeed : %.2f" %(sx,sy,ga,spe))
            o=class_game.findofromk(sx,sy,ga,spr,ma,xx)

            if(o[0]==0):
                error_massage2.Text="cannot shoot"
                continue
            error_massage2.Text=""
            degree.Text=str(round(o[1],2))
            speed.Text=str(round(o[0],2))
            ball.setspeed(float(speed.Text),float(degree.Text),float(gravity.Text))
    #* degeree_for_start

    if(debug1.Text !='' and debug2.Text !=''):
        ball.setposion_start(position_ball[kim][0],position_ball[kim][1])
        pygame.draw.circle(screen,'yellow', (float(debug1.Text)*scale+size_ui_x,size_pic_y-float(debug2.Text)*scale), 5)
        # print([float(debug1.Text)*scale+size_ui_x,size_pic_y-float(debug2.Text)*scale])
        pygame.draw.circle(screen,'yellow', (position_ball[kim][0]*1+size_ui_x,size_pic_y-position_ball[kim][1]*1), 5)

    #* check error
    if(kim==0):
        error_massage.Text="no found image"
    #* fight
    if fight.active:
        #* fight 
        if active_1st:
            # tail.reset()
            active_1st = False
        # print(time_count*100)

        if(time_count >0):
            # print("add : %.2f\t%.2f"%(ball.posi_x,ball.posi_y))
            tail.add_position(ball.posi_x,ball.posi_y,time_count)
        # pygame.draw.circle(screen,'red', (v.get_position_x(time_count)+size_ui_x,size_pic_y-v.get_position_y(time_count)), 20)
        
        ball.setsize(float(mass.Text))
        ball.run(screen,time_count)
        time_count=time_count+time_delta
        time_count_var=str(time_count)

    #* cancel
    if cancel.active:
        time_count=0
        fight.active=False
        cancel.active=False
        active_1st = True
        time_count_var = "0.00         "
        tail.reset()

    if(save.active):
        save.active=False
        print("print_data")
        file1 = open("output.csv","a")
        file1.write("input,sx(cm),sy(cm),mass(KG),gravity(m/s^2),degree(??),speed(m/s),spring_k(n/m),lenght(cm),mode,pic_number,sx_real(cm),sy_real(cm),positionstart_x(cm),positionstart_y(cm)\n")
        buf=""
        # print(tail.detail_shoot)
        for i in range(len(tail.detail_shoot)):
            buf=str(i+1)+","

            tail.detail_shoot[i][12]=tail.detail_shoot[i][12]*100
            tail.detail_shoot[i][13]=tail.detail_shoot[i][13]*100
            for j in tail.detail_shoot[i]:

                buf=buf+str(j)+","
            buf=buf+"\n"
            file1.write(buf)

            buf="t(ms),"
            for j in tail.postionball[i][2]:
                buf=buf+str(j)+","
            buf=buf+"\n"
            file1.write(buf)

            buf="x(cm_global),"
            for j in tail.postionball[i][0]:
                buf=buf+str(j)+","
            buf=buf+"\n"
            file1.write(buf)

            buf="y(cm_global),"
            for j in tail.postionball[i][1]:
                buf=buf+str(j)+","
            buf=buf+"\n"
            file1.write(buf)

            buf="sx(cm),"
            for j in tail.postionball[i][0]:
                buf=buf+str(round(j-tail.detail_shoot[i][12],2))+","
            buf=buf+"\n"
            file1.write(buf)

            buf="sy(cm),"
            for j in tail.postionball[i][1]:
                buf=buf+str(round(j-tail.detail_shoot[i][13],2))+","
            buf=buf+"\n"
            file1.write(buf)

            tail.detail_shoot[i][12]=tail.detail_shoot[i][12]/100
            tail.detail_shoot[i][13]=tail.detail_shoot[i][13]/100
        file1.write("\n\n")
        file1.close()

    #* fall
    if(ball.check_fall(time_count)):
        
        sx=(goal_x-size_ui_x)/(100*scale)
        sy=((size_pic_y-goal_y))/(100*scale)
        ballposiotion_x=position_ball[kim][0]/(100*scale)
        ballposiotion_y=position_ball[kim][1]/(100*scale)
        buf2=[]
        buf1=[mode,kim,sx,sy,ballposiotion_x,ballposiotion_y]

        for i in new_word_list:
            buf2.append(float(i.Text))
        for i in buf1:
            buf2.append(i)
        buf2=[round(num, 2) for num in buf2]
        tail.detail_shoot.append(buf2)

        time_count=0
        fight.active = False
        active_1st = True
        tail.next()
        # print(tail.detail_shoot)
        # print(tail.postionball)

    #* update
    time_box.update_text(time_count_var[0:5])
    clock.tick(FPS)

    #* display
    for i in draw_list:
        i.draw(screen)
    pygame.display.update()

    #* debug
    debug1.word_end=forpint